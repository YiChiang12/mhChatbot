import json
import openai

def read_api():
    with open("openai_api_key", "r") as file:
        api_key = file.read().strip()
    openai.api_key = api_key

def request_gpt(messages):
    # try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message['content']
    # except Exception as e:
    #     print(f"Error: {e}")
    #     return None

# Extract problems and solutions from the conversation
def extract_prob_sol(transcript):
    # transcript_str = "\n".join([f"{msg['from']}: {msg['text']}" for msg in transcript])
    transcript_str = ""
    for msg in transcript:
        role = msg['role']
        content = msg['content'].replace('\n', ' ')
        transcript_str += f'{role}: {content}\n'
    
    prompt = """
    You are an assistant skilled in analyzing conversations for problem-solving.
    Given a transcript of a conversation between a user and an AI, identify the main problems discussed and the solutions provided.
    Respond in the following JSON format:
    [
        {
            "problem": "description",
            "solution": "action taken"
        }
    ].
    Here is the transcript:
    """

    messages = [{'role': 'system', 'content': prompt + transcript_str}]

    extracted_data = request_gpt(messages)

    # try:
    problems_solutions = json.loads(extracted_data)
    # except json.JSONDecodeError:
    #     problems_solutions = {"error"}
    return problems_solutions

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, indent=4)

def main():
    read_api()
    conversation_path = 'scripts/conversation.json'
    output_path = 'data/extracted_prob_sol.json'

    # Conversation from the file
    with open(conversation_path, 'r') as file:
        conversation_json = json.load(file)

    problems_solutions = extract_prob_sol(conversation_json)

    # Save the extracted problems and solutions to a JSON file
    if problems_solutions:
        save_json(problems_solutions, output_path)
        print(f"Successfully extracted and saved to {output_path}")

if __name__ == '__main__':
    main()







# import json
# import os
# import openai

# def read_api():
#     with open("openai_api_key", "r") as file:
#         api_key = file.read().strip()
#     openai.api_key = api_key

# def request_gpt(messages):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=messages,
#             # max_tokens=1000
#         )
#         return response.choices[0].message['content']
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None

# # Extract problems and solutions from the conversation
# def extract_prob_sol(transcript):
#     transcript_str = ""
#     for index, message in enumerate(transcript):
#         role = message['from']
#         text = message['text']
#         transcript_str += f'{index}. {role}: {text}\n'
    
#     prompt = """You are an assistant skilled in analyzing conversations for problem-solving.
#     Given a transcript of a conversation between a user and an AI, identify the main problems discussed and the solutions provided.
#     Respond in the following JSON format:
#     [
#         {
#             "problem": "description",
#             "solution": "action taken"
#         }
#     ].
#     Here is the transcript:
#     """

#     messages = [
#         {'role': 'system', 'content': prompt + transcript_str},
#         {'role': 'user', 'content': "Please analyze the transcript and extract problems and solutions."}
#     ]

#     extracted_data = request_gpt(messages)
#     # Parse JSON data
#     problems_solutions = json.loads(extracted_data)
#     # print("Problems and Solutions:", problems_solutions)
#     return problems_solutions

#     # return request_gpt(messages, format = 'json')

# def save_json(data, filepath):
#     with open(filepath, 'w', encoding='utf-8') as fp:
#         json.dump(data, fp, indent=4)

# def main():
#     read_api()
#     script_path = os.path.join('scripts', 'scriptc.json')
#     output_path = os.path.join('data', 'outputc.json')

#     # Conversation from the script file
#     with open(script_path, 'r') as file:
#         conversation_json = json.load(file)

  
#     problems_solutions = extract_prob_sol(conversation_json)

#     # Save the extracted prob/sol to a JSON file
#     if problems_solutions:
#         save_json(problems_solutions, output_path)
#         # print(f"Successfully extracted")

# if __name__ == '__main__':
#     main()





# import json
# import os
# import openai
# # import re

# def initialize_client():
#     with open("openai_api_key", "r") as file:
#         api_key = file.read().strip()
#     openai.api_key = api_key

# def request_gpt(messages):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=messages,
#         )
#         if response.choices:
#             content = response.choices[0].message['content']
#             print("API Response:", content)  # Logging the raw API response
#             return content
#         else:
#             print("No content in response.")
#             return '{}'
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return '{}'

# # def clean_response(response):
# #     # Remove the triple quotes and any other non-JSON compliant parts
# #     response = re.sub(r"```json", "", response)
# #     response = re.sub(r"```", "", response)
# #     response = response.strip()
# #     return response

# def extract_prob_sol(transcript):
#     transcript_str = ""
#     for index, message in enumerate(transcript):
#         role = message['from']
#         text = message['text']
#         transcript_str += f'{index}. {role}: {text}\n'
    
#     prompt = """You are an assistant skilled in analyzing conversations for problem-solving.
#     Given a transcript of a conversation between a user and an AI, identify the main problems discussed and the solutions provided.
#     Respond in the following JSON format:
#     [
#         {
#             "problem": "description",
#             "solution": "action taken"
#         }
#     ].
#     Here is the transcript:
#     """

#     messages = [
#         {'role': 'system', 'content': prompt + transcript_str},
#         {'role': 'user', 'content': "Analyze the transcript and extract problems and solutions."}
#     ]

#     extracted_data = request_gpt(messages)
#     cleaned_data = clean_response(extracted_data)
#     try:
#         problems_solutions = json.loads(extracted_data)
#         return problems_solutions
#     except json.JSONDecodeError:
#         print("Failed to decode JSON from GPT response.")
#         return []

# def save_json(data, filepath):
#     with open(filepath, 'w', encoding='utf-8') as fp:
#         json.dump(data, fp, indent=4)

# def main():
#     initialize_client()
#     script_path = os.path.join('scripts', 'script.json')
#     output_path = os.path.join('data', 'output.json')

#     with open(script_path, 'r') as file:
#         conversation_json = json.load(file)

#     problems_solutions = extract_prob_sol(conversation_json)
#     if problems_solutions:
#         save_json(problems_solutions, output_path)
#         print(f"Problems and solutions saved to {output_path}")

# if __name__ == '__main__':
#     main()








# import json
# import os
# import openai

# def initialize_client():
#     with open("openai_api_key", "r") as file:
#         api_key = file.read().strip()
#     openai.api_key = api_key

# def request_gpt(messages):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=messages,
#             max_tokens=1000
#         )
#         return response['choices'][0]['message']['content']
#     except openai.error.OpenAIError as e:
#         print(f"An error occurred: {e}")
#         return None

# def extract_prob_sol(transcript):
#     transcript_str = ""
#     for index, message in enumerate(transcript):
#         role = message['from']
#         text = message['text']
#         transcript_str += f'{index}. {role}: {text}\n'
    
#     prompt = """You are an assistant skilled in analyzing conversations for problem-solving.
#     Given a transcript of a conversation between a user and an AI, identify the main problems discussed and the solutions provided.
#     Respond in the following JSON format:
#     [
#         {
#             "problem": "description", 
#             "solution": "action taken"
#         },
#         ...
#     ]
#     Here is the transcript:
#     """

#     messages = [
#         {'role': 'system', 'content': prompt + transcript_str},
#         {'role': 'user', 'content': "Please analyze the transcript and extract problems and solutions."}
#     ]

#     extracted_data = request_gpt(messages)
#     print("Extracted Text:", extracted_data)
#     problems_solutions = json.loads(extracted_data)
#     print("Problems and Solutions:", problems_solutions)
#     return problems_solutions
#     # return extracted_data

# def save_json(data, filepath):
#     with open(filepath, 'w', encoding='utf-8') as fp:
#         json.dump(data, fp, indent=4)

# def main():
#     initialize_client()
#     script_path = os.path.join('scripts', 'scripta.json')
#     output_path = os.path.join('data', 'output.json')

#     # Load the conversation from the script JSON file
#     with open(script_path, 'r') as file:
#         conversation_json = json.load(file)

#     # Extract problems and solutions
#     problems_solutions = extract_prob_sol(conversation_json)

#     # Save the extracted data to an output JSON file
#     if problems_solutions:
#         save_json(problems_solutions, output_path)
#         print(f"Problems and solutions extracted and saved to {output_path}")

# if __name__ == '__main__':
#     main()







# import openai
# import json
# import os

# def request_gpt(messages):
#     with open("openai_api_key", "r") as file:
#         openai.api_key = file.read().strip()

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages,
#         max_tokens=1000
#     )
#     return response.choices[0].message['content']

# def extract_prob_sol(transcript):
#     transcript_str = ""
#     for index, message in enumerate(transcript):
#         role = message['from']
#         text = message['text']
#         transcript_str += f'{index}. {role}: {text}\n'
    
#     prompt = """You are an assistant skilled in analyzing conversations for problem-solving.
#     Given a transcript of a conversation between a user and an AI, identify the main problems discussed and the solutions provided.
#     The problems are the challenges faced by the user, and the solutions are the responses or actions taken by the AI to address those challenges.
#     Respond in the following JSON format:
#                 [
#                     {
#                         "problem": " ",
#                         "solution": " "
#                     },
#                     {
#                         "problem": " ",
#                         "solution": " "
#                     }
#                 ].
#     Here is the transcript:
#     """

#     messages = [
#         {
#             'role': 'system',
#             'content': prompt + transcript_str
#         },
#         {
#             'role': 'user',
#             'content': "Please analyze the transcript and extract problems and solutions."
#         }
#     ]

#     extracted_data = request_gpt(messages)
#     return extracted_data

# # Adjust the path to the scripta.json file in the scripts folder
# script_path = os.path.join('scripts', 'scripta.json')
# output_path = os.path.join('data', 'output.json')

# # Load conversation from scripta.json
# with open(script_path, 'r') as file:
#     conversation_json = json.load(file)

# # Extract problems and solutions from the conversation
# problems_solutions = extract_prob_sol(conversation_json)

# # Save the extracted problems and solutions to output.json in the data folder
# with open(output_path, 'w') as file:
#     json.dump(problems_solutions, file, indent=4)

# print(f"Problems and solutions extracted and saved to {output_path}")
