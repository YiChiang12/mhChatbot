from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import json

def create_app():
    app = Flask(__name__)
    CORS(app)

    try:
        with open("openai_api_key", "r") as file:
            openai.api_key = file.read().strip()
    except FileNotFoundError:
        print("API key file not found.")
        raise
    except Exception as e:
        print(f"Error reading API key: {e}")
        raise

    @app.route("/chat", methods=["POST"])
    def chat():
        conversation = request.json.get('messages', [])
        if not conversation:
            return jsonify({"error": "No conversation provided"}), 400
        print("Received conversation:", conversation)  # Log received data
        try:
            response = request_chatgpt(conversation)
            if response:
                print("Sending response:", response)  # Log sent data
                return jsonify({"response": response})
            else:
                return jsonify({"error": "No response from model"}), 500
        except Exception as e:
            print(f"Error handling request: {str(e)}")
            return jsonify({"error": str(e)}), 500


    return app

def request_chatgpt(conversation):
    # Convert the incoming message format to what OpenAI expects
    formatted_messages = [
        {"role": "assistant" if msg["from"] == "ai" else "user", "content": msg["text"]} for msg in conversation
    ]

    # System prompt for the therapist context
    system_prompt = {
        "role": "system",
        "content": """You are a professional therapist, exceptionally skilled in listening and genuinely empathetic towards others.
                      You adeptly guide people towards solutions for their challenges and provide steadfast support during their difficult times.
                      Sometimes, you could be a bit hilarious and funny, but always professional.
                      Make sure you provide a response that is concise and conversational, advice should be clear and helpful."""
    }

    # Add the system message at the start of the conversation
    messages = [system_prompt] + formatted_messages

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message['content'] if response.choices else "No content returned from API"
    except Exception as e:
        print(f"OpenAI API request failed: {e}")
        return f"Error in connecting with OpenAI API: {str(e)}"


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)  # Ensure it's listening on the correct interface










# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import openai

# def create_app():
#     app = Flask(__name__)
#     CORS(app)

#     try:
#         with open("openai_api_key", "r") as file:
#             openai.api_key = file.read().strip()
#     except Exception as e:
#         print(f"Cannot load API key: {e}")

#     @app.route("/chat", methods=["POST"])
#     def chat():
#         user_input = request.json.get('input', '')
#         try:
#             response = request_chatgpt(user_input)
#             return jsonify({"response": response})
#         except Exception as e:
#             return jsonify({"error": str(e)})
#     return app

# def request_chatgpt(user_input):
#     chat_messages = [
#         {
#             "role": "system",
#             "content": """You are a professional therapist, exceptionally skilled in listening and genuinely empathetic towards others. 
#                           You adeptly guide people towards solutions for their challenges and provide steadfast support during their difficult times. 
#                           Somtimes, you could be a bit hilarious and funny, but always professional.
#                           Make sure you provide a response that is concise and conversational, advices should be clear and helpful."""
#         },
#         {
#             "role": "user", 
#             "content": user_input
#         }
#     ]

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=chat_messages
#         )
#         return response.choices[0].message['content']
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         raise