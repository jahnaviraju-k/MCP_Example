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
