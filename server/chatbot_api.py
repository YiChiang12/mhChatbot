from flask import Flask, request, jsonify, send_from_directory  
from flask_cors import CORS
import openai
import json
import os


def create_app():
    app = Flask(__name__)
    # CORS(app)
    CORS(app)

    try:
        with open("openai_api_key", "r") as file:
            openai.api_key = file.read().strip()
    except Exception as e:
        print(f"Error reading the api key")
        raise e

    @app.route("/chat", methods=["POST"])
    def chat():
        conversation = request.json.get('messages', [])
        if not conversation:
            return jsonify({"No conversation"}), 400
        # print(conversation)  
        user_input = request.json.get('user_input', '')
        if user_input:
            conversation.append({"role": "user", "content": user_input})
        if not conversation:
            return jsonify({"error": "No conversation provided"}), 400
        
        response = request_chatgpt(conversation)
        if response:
            conversation.append({"role": "system", "content": response})
            # Save new conversation to a file
            save_conversation(conversation)
            # print("response:", response)  
            return jsonify({"response": response})
        else:
            return jsonify({"No response from model"}), 500
   
    @app.route("/data/extracted_prob_sol.json", methods=["GET"])
    def send_json():
        directory = os.path.join(app.root_path, 'data')
        try:
            return send_from_directory(directory, 'extracted_prob_sol.json')
        except FileNotFoundError:
            return jsonify({"error": "File not found"}), 404
    # @app.route("/data/extracted_prob_sol.json", methods=["GET"])
    # def send_json():
    #     try:
    #         return send_from_directory(
    #             os.path.join(app.root_path, 'data'),
    #             'extracted_prob_sol.json',
    #             as_attachment=False
    #         )
    #     except FileNotFoundError:
    #         return jsonify({"error": "File not found"}), 404

    
    return app

def save_conversation(conversation):
    # Format the conversation
    cleaned_conversation = []
    for msg in conversation:
        cleaned_msg = {
            "role": msg["role"],
            "content": msg["content"].replace('\u00a0', ' ')
        }
        cleaned_msg_ordered = dict([("role", cleaned_msg["role"]), ("content", cleaned_msg["content"])])
        cleaned_conversation.append(cleaned_msg_ordered)
    
    # Save the conversation to a JSON file
    with open('./scripts/conversation.json', 'w') as fp:
        json.dump(cleaned_conversation, fp, indent=4)

def request_chatgpt(conversation):
    # transcript_str = ""
    # for msg in conversation:
    #     role = "assistant" if msg["from"] == "ai" else "user"
    #     content = msg["text"]
    #     transcript_str += f'{role}: {content}\n'

    # Stll need to modify the prompt (adding emoji and formatting to be readable)
    system_prompt = """
    You are a professional therapist, exceptionally skilled in listening.
    You adeptly guide people towards solutions for their challenges and provide support during their difficult times.
    Sometimes, you could be a bit hilarious and funny, but always professional.
    Make sure you provide a response that is concise and conversational, advice should be clear and helpful.
    Add emoji to make the conversation more engaging sometimes. 
    Make your response in a format that is easy to read. For example, make the response into different paragraphs with space between 
    and if your response suggestions are a lot, list them 1, 2, 3....
    """

    # Prepend system prompt to the messages
    formatted_messages = [{"role": "system", "content": system_prompt}] + conversation

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=formatted_messages
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"API request failed: {e}")
        return f"Error: {str(e)}"

app = create_app()










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