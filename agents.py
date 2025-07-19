from collections import Counter
import matplotlib.pyplot as plt
import string

class SummariserAgent:
    def run(self, context):
        print("[SummariserAgent] Summarising text...")
        with open("sample.txt", "r") as f:
            text = f.read()
        sentences = text.split(".")
        summary = ". ".join(sentences[:2])
        context.update("summary", summary)
        print("[SummariserAgent] Summary done.")

class ChartAgent:
    def run(self, context):
        print("[ChartAgent] Generating word frequency chart...")
        text = context.summary.lower().translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        word_freq = Counter(words)
        common = word_freq.most_common(5)

        words, counts = zip(*common)
        plt.bar(words, counts)
        plt.title("Top 5 Words in Summary")
        plt.savefig("word_freq_chart.png")
        context.update("chart_data", common)
        print("[ChartAgent] Chart generated and saved.")
