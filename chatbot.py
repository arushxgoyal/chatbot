from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)
chatbot = SimpleChatbot()

class SimpleChatbot:
    def __init__(self):
        self.greetings = ["Hi there!", "Hello!", "Hey!"]
        self.responses = {
            "hello": ["Hi!", "Hello!", "Hey there!", "Hi! How can I help you today?"],
            "how are you": ["I'm doing well, thanks!", "I'm great! How about you?"]
        }
        self.default_response = "I'm not sure how to respond to that."

    def get_response(self, user_input):
        # Convert input to lowercase for easier matching
        user_input = user_input.lower()
        
        # Check for greetings
        if any(greeting in user_input for greeting in ["hi", "hello", "hey"]):
            return random.choice(self.greetings)
            
        # Check for specific responses
        for keyword, responses in self.responses.items():
            if keyword in user_input:
                return random.choice(responses)
                
        # Default response if no match found
        return self.default_response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    response = chatbot.get_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
