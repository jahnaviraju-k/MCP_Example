# MCP - Model Context Protocol Project

A Python simulation of MCP (Model Context Protocol) using a shared context and two agents:

- `SummariserAgent`: Summarises a sample text
- `ChartAgent`: Generates a word frequency chart from the summary
# Overview
- Built a Python-based simulation of Model Context Protocol (MCP) using a two-agent system that collaborates via shared context. Demonstrated summarisation and data visualisation in a modular AI pipeline that mimics assistant tool routing workflows.
- This project is a Python-based simulation of the Model Context Protocol (MCP) an emerging standard for connecting AI assistants to live data sources and enabling modular, multi-agent workflows. The goal was to model how different AI agents can collaborate using a shared memory context to complete a larger task.

# Agent Pipeline Building 
Developed a minimal yet functional multi-agent pipeline that:
- Accepts raw input text from a file
- Passes it to a SummariserAgent which generates a condensed version of the content
- Sends the summary to a ChartAgent which creates a word frequency bar chart
- Uses a shared MCP Context object that mimics how agents communicate via context in a real MCP system

# Agent Workflow (MCP-style Routing)
- The program starts with an input text file (sample.txt)
- The "SummariserAgent" reads the text and extracts a short summary
- It updates the shared context with that summary
- The "ChartAgent" retrieves the summary from the context
- It analyses the frequency of words in the summary and generates a visual bar chart
- The chart is saved locally as word_freq_chart.png

# Real-World Relevance
- This project mirrors foundational design patterns used in LangChain agent chains, OpenAI Assistants API, Microsoft AutoGen tool routing and RAG systems using vector stores and summarisation agents
- It shows how large-scale assistants could Summarise long documents, Generate dashboards or insights and Interact with multiple tools (summariser, chart, DB) in a memory-aware, sequential workflow



