# Coltex V1 — `.ctex` Workspaces

**Tagline:** The AI Knowledge Platform for Modern Organizations

**Goal:** Turn scattered business knowledge into AI-ready intelligence in under 10 minutes.

Coltex V1 is a **local CLI**. The primary unit of work is a **Coltex Workspace (`.ctex`)** — the official project file, similar to `.uproject` or `.blend`.

---

## Create a workspace

```bash
coltex new MyWorkspace
```

Generates:

```
MyWorkspace/
├── MyWorkspace.ctex
├── knowledge/
├── documents/
├── embeddings/
├── graph/
├── metadata/
├── cache/
├── indexes/
├── logs/
├── backups/
├── settings/
└── runtime/
```

---

## Workspace commands

| Command | Purpose |
|---------|---------|
| `coltex new <name>` | Create workspace |
| `coltex open <file.ctex>` | Open workspace |
| `coltex build` | Process, chunk, embed, index, validate |
| `coltex status` | Workspace stats and health |
| `coltex validate` | Integrity checks |
| `coltex export` | Portable archive |
| `coltex import <archive>` | Restore workspace |

Opening a workspace:

```
Opening Workspace...

Workspace: MyWorkspace
Coltex Version: 1.0
Knowledge Health: 97%
Documents: 482
Embeddings: 19,304
Graph Nodes: 52,101
Last Build: 2 minutes ago

Workspace Ready.
```

---

## `.ctex` manifest

The manifest stores workspace metadata — never large data:

- Workspace name, UUID, Coltex version
- Created / modified dates
- Knowledge source locations
- AI provider, embedding model, retrieval settings
- Graph and search configuration
- Statistics and health
- User settings

Updated automatically on upload, build, sync, and other operations.

---

## Knowledge commands

```bash
coltex upload path/to/document.pdf
coltex search "authentication"
coltex ask "How do we handle refunds?"
coltex sources
coltex knowledge
coltex settings
```

---

## License

MIT — see [LICENSE](../../LICENSE).
