class MCPContext:
    def __init__(self, user_input):
        self.user_input = user_input
        self.summary = None
        self.chart_data = None
        self.history = []

    def update(self, key, value):
        setattr(self, key, value)
        self.history.append((key, value))

    def __str__(self):
        return f"Context(user_input={self.user_input}, summary={self.summary}, chart_data={self.chart_data})"

# python run_pipeline.py
[SummariserAgent] Summarising text...
[ChartAgent] Generating word frequency chart...
[ChartAgent] Chart generated and saved.

# Final Context State:
# Context(user_input=Summarise the document and show word frequency chart, summary=The Model Context Protocol (MCP) is an emerging open standard designed to connect AI assistants to the systems where data lives, enabling them to access and utilize information more effectively.  It aims to create a more standardized and open ecosystem for AI applications by providing a universal way to connect AI systems with various data sources and tools, chart_data=[('to', 5), ('ai', 3), ('and', 3), ('the', 2), ('open', 2)])
