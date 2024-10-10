# Mental Health Chatbot with Visualization Feedback

Welcome to the AI-Driven Mental Health Chatbot with Crisis Intervention project! This project leverages conversational AI to support mental well-being through crisis intervention with interaction and personalized advice. It utilizes OpenAI's GPT models to understand and respond to user emotions, providing a tailored conversational experience, the ultimately goal is to enhance the user's willingness to seek professional help.

<!-- Welcome to the AI-Driven Mental Health Chatbot with Visualization Feedback project! This project leverages conversational AI to support mental well-being through dynamic interaction and personalized advice. It utilizes OpenAI's GPT models to understand and respond to user emotions, providing a tailored conversational experience. This project is still under development! -->

## 🚧 Project Status
This project is currently **in progress**:
- The chatbot interface using Svelte, CSS, and HTML is operational.
- Backend integration using OpenAI's GPT model for generating dynamic conversations based on user input.
<!-- - Figma designs for the conversational flow map are complete, but the implementation into the chatbot is pending. -->

## 📌 Current Implementation
- **Chatbot Interface**: Allows users to interact through a prototype interface where they can express their suicidal thoughts, any feelings, ask questions, or seek help.
- **Backend Logic**: Utilizes OpenAI's GPT models to analyze the user's current stage (with suicidal tendencies) and using the corresponding prompt for each stage to provide user the response.


https://github.com/YiChiang12/mhChatbot/assets/146417836/2e9d2adb-6366-4e32-a5a5-268284010282



## 🛠 Technologies Used
- **Svelte**: for building the interactive frontend.
- **CSS/HTML**: for styling and markup.
- **Flask**: for backend API to handle requests.
- **OpenAI's GPT**: for generating AI-based responses and analyzing users' conversations.

## 📈 Future Plans
- **Conversational Flow Map**: To visually represent user emotional journeys through their interactions. This will enhance user engagement and understanding.
- **Expansion of Chat Features**: Including starting new chats and accessing recent chats.

## 🏁 Getting Started
To set up the project locally, you can clone this repository and follow the setup instructions:

```bash
git clone https://github.com/YiChiang12/mhChatbot.git
cd mhChatbot
```
1. To Launch the Server:
```shell
cd server/
export FLASK_APP=chatbot_api.py
flask run
```

2. To Launch the Front-end:
```shell
cd frontend/src/
npm run dev
```

3. Open `localhost:5173` in the browser

## ✉️ Contact
Feel free to reach out to me at [yichiang@ucdavis.edu](mailto:yichiang@ucdavis.edu) or drop a message in the project's issues section on GitHub.
