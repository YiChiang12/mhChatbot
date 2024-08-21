import json
import os
import openai

def read_api():
    with open("openai_api_key", "r") as file:
        api_key = file.read().strip()
    openai.api_key = api_key

def request_gpt(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            # max_tokens=1000
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Extract problems and solutions from the conversation
def extract_prob_sol(transcript):
    transcript_str = ""
    for index, message in enumerate(transcript):
        role = message['from']
        text = message['text']
        transcript_str += f'{index}. {role}: {text}\n'
    
    prompt = """You are an assistant skilled in analyzing conversations for problem-solving.
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

    messages = [
        {'role': 'system', 'content': prompt + transcript_str},
        {'role': 'user', 'content': "Please analyze the transcript and extract problems and solutions."}
    ]

    extracted_data = request_gpt(messages)
    # Parse JSON data
    problems_solutions = json.loads(extracted_data)
    # print("Problems and Solutions:", problems_solutions)
    return problems_solutions

    # return request_gpt(messages, format = 'json')

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, indent=4)

def main():
    read_api()
    script_path = os.path.join('scripts', 'scriptc.json')
    output_path = os.path.join('data', 'outputc.json')

    # Conversation from the script file
    with open(script_path, 'r') as file:
        conversation_json = json.load(file)

  
    problems_solutions = extract_prob_sol(conversation_json)

    # Save the extracted prob/sol to a JSON file
    if problems_solutions:
        save_json(problems_solutions, output_path)
        # print(f"Successfully extracted")

if __name__ == '__main__':
    main()

