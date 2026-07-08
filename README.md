# Coltex

**The AI Knowledge Platform for Modern Organizations**

Turn scattered business knowledge into AI-ready intelligence in under 10 minutes — from your terminal.

```bash
pip install -r requirements.txt
coltex new MyWorkspace
coltex upload document.pdf
coltex ask "What is our policy?"
```

Coltex is a **local CLI**. Your project is a **`.ctex` workspace** — like `.uproject` for Unreal or `.blend` for Blender.

---

## Workspace commands

| Command | Purpose |
|---------|---------|
| `coltex new <name>` | Create a new `.ctex` workspace |
| `coltex open <workspace>.ctex` | Open a workspace |
| `coltex build` | Process documents, embed, index, update manifest |
| `coltex status` | Workspace info, health, document counts |
| `coltex validate` | Check workspace integrity |
| `coltex export` | Portable workspace archive |
| `coltex import <archive>` | Restore a workspace |

## Knowledge commands

| Command | Purpose |
|---------|---------|
| `coltex upload file.pdf` | Upload and process a source |
| `coltex search "query"` | Universal search |
| `coltex ask "question"` | Ask Knowledge — answer with sources |
| `coltex sources` | List uploaded sources |
| `coltex knowledge` | Browse knowledge objects |
| `coltex settings` | View or update workspace settings |
| `coltex health` | Knowledge Health score |
| `coltex curator` | Proactive knowledge alerts |

Supported uploads: **PDF · DOCX · Markdown · TXT · HTML · JSON**

Also available: `./coltex` or `python3 -m runtime`

---

## Workspace layout

```
MyWorkspace/
├── MyWorkspace.ctex      ← workspace manifest (auto-managed)
├── knowledge/
├── documents/
├── embeddings/
├── graph/
├── metadata/
├── settings/
└── runtime/
```

The `.ctex` file stores metadata only — never embeddings or documents. The CLI updates it automatically.

---

## License

MIT — see [LICENSE](LICENSE).
