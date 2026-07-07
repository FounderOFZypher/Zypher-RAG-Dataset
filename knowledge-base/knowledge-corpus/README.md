# Coltex Knowledge Architecture

Enterprise RAG knowledge corpus with **6 processing layers**, **10 functional clusters**, **4 memory tiers**, **18 knowledge hubs**, and **millions of graph edges**.

## Structure

```
knowledge-corpus/
├── cortex/L1-sensory … L6-meta    # Processing layers
├── lobes/                           # Functional clusters
├── domains/                         # 62+ technology domains
├── hubs/                            # 18 knowledge clusters
├── synapses/                        # Hub-to-hub graph links
├── pathways/                        # Inter-cluster routes
├── memory/                          # Tiered retention stores
└── reflexes/                        # Quick-reference FAQs
```

## Build

```bash
make corpus-advanced              # Full architecture bootstrap
make corpus-grow COUNT=1000       # Add domain documents
make corpus-mega                  # 10,000 documents
```

## Query

```bash
make index
python3 -m brain report
python3 -m brain retrieve "Explain domain pathway routing" --context
```
