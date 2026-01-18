# Gemini Beads Extension

This is a [Gemini CLI](https://github.com/google/gemini-cli) extension for **Beads (`bd`)**, a graph-based issue tracker that provides persistent memory for multi-session work, backed by Git.

## Description

The Gemini Beads extension allows you to manage tasks, issues, and project context directly from your Gemini CLI session. It wraps the `bd` command-line tool, enabling an AI-native workflow for managing complex, multi-session development tasks.

**Features:**
- **Persistent Memory:** Track work across multiple AI sessions.
- **Dependency Management:** Handle blocked tasks and prerequisites.
- **Git Integration:** Issues and state are stored in your git repository.
- **Context Awareness:** Provides AI-optimized context about the project and current tasks.

## Prerequisites

This extension requires the **Beads (`bd`)** CLI tool to be installed and available in your system's PATH.

*(Note: Ensure you have the `bd` executable installed on your machine.)*

## Installation

To install this extension with Gemini CLI:

```bash
gemini extension install https://github.com/thoreinstein/gemini-beads
```

## Usage

Once installed, the `bd` commands are available within Gemini. The extension also provides the `GEMINI.md` context file, which instructs Gemini on how to effectively use Beads to manage your project.

### Common Commands

- `/beads:prime`: Load project context (run this when starting a session).
- `/beads:ready`: Find unblocked work to do.
- `/beads:create`: Create a new issue/bead.
- `/beads:list`: List issues.
- `/beads:show`: Show details of a specific issue.
- `/beads:update`: Update an issue's status or properties.
- `/beads:close`: Close an issue.
- `/beads:sync`: Sync changes to git.

### Full Command List

The extension maps the following `bd` commands:

- `audit`
- `blocked`
- `close`
- `comments`
- `compact`
- `create`
- `daemon` / `daemons`
- `delete`
- `dep` (dependencies)
- `epic`
- `export` / `import`
- `init`
- `label`
- `list`
- `prime`
- `quickstart`
- `ready`
- `rename-prefix`
- `reopen`
- `restore`
- `search`
- `show`
- `stats`
- `sync`
- `template`
- `update`
- `version`
- `workflow`

## AI Context

This extension includes a `GEMINI.md` file that provides specific instructions to the Gemini agent on how to:
1.  **Start** a session (check for unblocked work).
2.  **Contextualize** (read task details).
3.  **Work** (update status).
4.  **Finish** (close tasks).
5.  **Save** (sync to git).

## License

MIT
