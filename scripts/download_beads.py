#!/usr/bin/env python3
import os
import shutil
import zipfile
import urllib.request
import io
from pathlib import Path

# Configuration
REPO_ZIP_URL = "https://github.com/steveyegge/beads/archive/refs/heads/main.zip"
# The folder structure in the zip usually follows "repo-branch" naming
ZIP_SUBFOLDER = "beads-main/claude-plugin/skills/beads"
DEST_DIR = "skills/beads"

REPLACEMENTS = [
    ("Claude code", "Gemini CLI"),
    ("Claude", "Gemini"),
    ("TodoWrite", "Session Todos (write_todos)"),
]


def main():
    # Determine the project root relative to this script
    # Assuming script is in scripts/ folder, root is one level up
    # If run from root, we should handle that.
    # Let's use current working directory if it contains 'skills', otherwise try to locate root

    current_dir = Path.cwd()
    dest_path = current_dir / DEST_DIR

    print(f"Target destination: {dest_path}")

    # Clean existing destination if it exists
    if dest_path.exists():
        print(f"Cleaning existing directory: {dest_path}")
        shutil.rmtree(dest_path)

    # Create destination directory
    dest_path.mkdir(parents=True, exist_ok=True)

    print(f"Downloading {REPO_ZIP_URL}...")
    try:
        with urllib.request.urlopen(REPO_ZIP_URL) as response:
            zip_data = response.read()
    except Exception as e:
        print(f"Failed to download zip: {e}")
        return

    print("Extracting and processing files...")
    try:
        with zipfile.ZipFile(io.BytesIO(zip_data)) as z:
            # Filter files in the specific subfolder
            # We look for files starting with ZIP_SUBFOLDER
            target_files = [
                f
                for f in z.namelist()
                if f.startswith(ZIP_SUBFOLDER) and not f.endswith("/")
            ]

            if not target_files:
                print(
                    f"Error: Could not find folder '{ZIP_SUBFOLDER}' in the zip archive."
                )
                print("Dumping top-level folders in zip for debugging:")
                top_levels = set(f.split("/")[0] for f in z.namelist())
                print(top_levels)
                return

            for file_path in target_files:
                # Determine relative path for destination
                # Remove the ZIP_SUBFOLDER prefix to get the relative path inside skills/beads
                rel_path = file_path[len(ZIP_SUBFOLDER) :].lstrip("/")
                final_path = dest_path / rel_path

                # Create parent directories for the file
                final_path.parent.mkdir(parents=True, exist_ok=True)

                # Read content from zip
                try:
                    content_bytes = z.read(file_path)
                    try:
                        content = content_bytes.decode("utf-8")
                        is_text = True
                    except UnicodeDecodeError:
                        is_text = False
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
                    continue

                # Apply replacements only to Markdown files
                if is_text and final_path.suffix.lower() == ".md":
                    original_content = content
                    for old, new in REPLACEMENTS:
                        content = content.replace(old, new)

                    if content != original_content:
                        print(f"Updated: {rel_path}")
                    else:
                        print(f"Copied: {rel_path}")

                    # Write modified content
                    with open(final_path, "w", encoding="utf-8") as f:
                        f.write(content)
                else:
                    # Write binary/other content as is
                    print(f"Copied: {rel_path}")
                    with open(final_path, "wb") as f:
                        f.write(content_bytes)

        print("Done!")

    except zipfile.BadZipFile:
        print("Error: The downloaded file is not a valid zip archive.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
