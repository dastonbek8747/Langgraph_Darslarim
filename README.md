# LangGraph Tutorials

> Hands-on LangGraph notebooks and scripts that build up from a first graph to routing, tools, evaluation and orchestration flows.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)


## What Is Inside

| File | Topic |
|---|---|
| `first_graph.ipynb` | The smallest possible StateGraph. |
| `messages.ipynb` | Message state and reducers. |
| `routing_graph.ipynb` | Conditional edges and routing. |
| `tools_graph.ipynb` | Tool calling inside a graph. |
| `evalutor_graph.ipynb` | An evaluator node and feedback loop. |
| `orchestrater_flow.ipynb` | Multi-agent orchestration. |
| `workflow.ipynb` | A full workflow end to end. |
| `day1.py` … `day4.py` | Daily practice scripts. |

## Quick Start

```bash
git clone https://github.com/dastonbek8747/langgraph-tutorials.git
cd langgraph-tutorials
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Each notebook is self-contained. Run them in order to follow the learning path.

## Tech Stack

- LangGraph
- LangChain
- Jupyter Notebook

## Why This Repo Exists

These are my study notes while learning LangGraph. They show the progression from a single node to a routed multi-agent graph, which is the design used in my larger project, [tech-ai-teacher-assistant](https://github.com/dastonbek8747/tech-ai-teacher-assistant).

## License

MIT © 2026 Doston Sultonov.
