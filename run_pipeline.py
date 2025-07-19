from mcp_context import MCPContext
from agents import SummariserAgent, ChartAgent

def main():
    user_query = "Summarise the document and show word frequency chart"
    context = MCPContext(user_input=user_query)

    summariser = SummariserAgent()
    chart_gen = ChartAgent()

    summariser.run(context)
    chart_gen.run(context)

    print("\nFinal Context State:")
    print(context)

if __name__ == "__main__":
    main()
python run_pipeline.py
[SummariserAgent] Summarising text...
[ChartAgent] Generating word frequency chart...
[ChartAgent] Chart generated and saved.

# Final Context State:
# Context(user_input=Summarise the document and show word frequency chart, summary=The Model Context Protocol (MCP) is an emerging open standard designed to connect AI assistants to the systems where data lives, enabling them to access and utilize information more effectively.  It aims to create a more standardized and open ecosystem for AI applications by providing a universal way to connect AI systems with various data sources and tools, chart_data=[('to', 5), ('ai', 3), ('and', 3), ('the', 2), ('open', 2)])
