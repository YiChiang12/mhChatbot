from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Get the OpenAI API key
    try:
        with open("openai_api_key", "r") as file:
            openai_api_key = file.read().strip()
        openai.api_key = openai_api_key
    except Exception as e:
        print(f"Cannot load API key: {e}")

    # Define the chat route to handle POST request
    @app.route("/chat", methods=["POST"])
    def chat():
        # print("asdfghj")
        user_input = request.json['input']
        messages = [{"role": "user", "content": user_input}]
        response_content = request_chatgpt(messages)
        # print(response_content)
        if response_content:
            return jsonify({"response": response_content}) # Return the response in JSON format
        else:
            return jsonify({"response": "No response generated."})
    return app

def request_chatgpt(messages):
    try:
        chat_messages = [
            {
                "role": "system",
                "content": """You are a professional therapist, exceptionally skilled in listening and genuinely empathetic towards others. 
                            You adeptly guide people towards solutions for their challenges and provide steadfast support during their difficult times."""
            },
            {
                "role": "user", 
                "content": messages[0]["content"]
            }
        ]

        response = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = chat_messages,
            # max_tokens = 100
        )

        # Chat response
        return response.choices[0].message.content if response.choices else "No response generated."
    except Exception as e:
        return f"Error: {str(e)}"
    
