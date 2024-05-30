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
    except Exception as e:
        print(f"Error reading the api key")
        raise

    @app.route("/chat", methods=["POST"])
    def chat():
        conversation = request.json.get('messages', [])
        if not conversation:
            return jsonify({"No conversation"})
        # print(conversation)  
        response = request_chatgpt(conversation)
        if response:
            conversation.append({"from": "ai", "text": response})
            # Save new conversation to a file
            save_conversation(conversation)
            # print("response:", response)  
            return jsonify({"response": response})
        else:
            return jsonify({"No response"})
        #     if response:
        #         print("response:", response)
        #         return jsonify({"response": response})
        #     else:
        #         return jsonify({"No response"})
        # except Exception as e:
        #     print(f"Error request: {str(e)}")
        #     return jsonify({"error": str(e)})
    return app

def save_conversation(conversation):
    # Format the conversation
    cleaned_conversation = []
    for msg in conversation:
        cleaned_msg = {
            "from": msg["from"],
            "text": msg["text"].replace('\u00a0', ' ')
        }
        cleaned_msg_ordered = dict([("from", cleaned_msg["from"]), ("text", cleaned_msg["text"])])
        cleaned_conversation.append(cleaned_msg_ordered)
    
    # Save the conversation to a JSON file
    with open('./scripts/conversation.json', 'w') as fp:
        json.dump(cleaned_conversation, fp, indent=4)

def request_chatgpt(conversation):
    transcript_str = ""
    for msg in conversation:
        role = "assistant" if msg["from"] == "ai" else "user"
        content = msg["text"]
        transcript_str += f'{role}: {content}\n'

    # Stll need to modify the prompt (adding emoji and formatting to be readable)
    system_prompt = """
    You are a professional therapist, exceptionally skilled in listening and genuinely empathetic towards others.
    You adeptly guide people towards solutions for their challenges and provide steadfast support during their difficult times.
    Sometimes, you could be a bit hilarious and funny, but always professional.
    Make sure you provide a response that is concise and conversational, advice should be clear and helpful.
    """

    # Combine the prompt with the conversation history
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": transcript_str
        }
    ]
    # formatted_messages = []
    # for msg in conversation:
    #     role = "assistant" if msg["from"] == "ai" else "user"
    #     content = msg["text"]
    #     formatted_messages.append({"role": role, "content": content})

    # # Stll need to modify the prompt (adding emoji and formatting)
    # prompt = {
    #     "role": "system",
    #     "content": """You are a professional therapist, exceptionally skilled in listening and genuinely empathetic towards others.
    #                   You adeptly guide people towards solutions for their challenges and provide steadfast support during their difficult times.
    #                   Sometimes, you could be a bit hilarious and funny, but always professional.
    #                   Make sure you provide a response that is concise and conversational, advice should be clear and helpful."""
    # }

    # # Combine the prompt at with the conversation history
    # messages = [prompt] + formatted_messages

    # try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message['content']   # if response.choices else "No content"
    # except Exception as e:
    #     # print(f"API request failed: {e}")
    #     return f"Error api"

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