MCP Agentic Application – Day 4 Exercise

This folder contains a minimal example for the MCP + Agents mini-project (Parts 1+2).

Files:
- app.py: Streamlit UI to run the agent.
- config.py: Loads LLM and MCP server configuration from environment variables.
- llm_client.py: Wrapper around an OpenAI-compatible client for planning.
- mcp_multi_client.py: Connects to multiple MCP servers and exposes tools to the LLM.
- my_mcp_server.py: Example local MCP server (`local_insights`) with two tools.
- orchestrator.py: Agentic orchestrator that composes tools using an LLM.
- requirements.txt: minimal dependencies.

Quick run (after configuring env vars):

1. Create a virtualenv and install deps:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Set environment variables (example):

- `LLM_BACKEND` = "ollama" or "groq"
- If `ollama`, set `LLM_MODEL` and ensure Ollama is running locally.
- `MCP_LOCAL_CMD` = python
- `MCP_LOCAL_ARGS` = my_mcp_server.py
- Configure two external MCP servers via `MCP_FILES_ARGS` and `MCP_WEB_ARGS` if available.

3. Run the Streamlit UI:

```powershell
streamlit run app.py
```

Notes:
- This example expects MCP servers compatible with the `mcp` Python SDK.
- For testing without external MCP servers, set `MCP_FILES_ARGS` and `MCP_WEB_ARGS` to usable commands or adapt `load_mcp_server_configs`.
