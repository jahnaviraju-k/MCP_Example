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
