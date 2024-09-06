from textblob import TextBlob

class SentimentChatbot:
    def __init__(self):
        self.bot_name = "SentimentBot"

    def analyze_sentiment(self, message):
        analysis = TextBlob(message)
        sentiment = analysis.sentiment.polarity
        if sentiment > 0:
            return "positive"
        elif sentiment < 0:
            return "negative"
        else:
            return "neutral"

    def chat(self):
        print(f"{self.bot_name}: Hello! I'm {self.bot_name}. Type 'exit' to end our conversation.")

        while True:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                print(f"{self.bot_name}: Goodbye! Have a nice day.")
                break

            sentiment = self.analyze_sentiment(user_input)
            print(f"{self.bot_name}: You seem to be feeling {sentiment} about that.")

if __name__ == "__main__":
    chatbot = SentimentChatbot()
    chatbot.chat()