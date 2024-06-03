<script>
    import { onMount, tick } from 'svelte';
    import { marked } from 'marked';

    let display_messages = [];
    let query_messages = [];
    let messageContainer;

    // Convert Markdown to HTML
    function convertMarkdownToHtml(markdownText) {
        return marked(markdownText);
    }

    async function sendMessage() {
        const messageText = document.querySelector('.input-textbox').textContent.trim();
        if (!messageText) return;

        document.querySelector('.input-textbox').textContent = '';

        // Add user message to display and query arrays
        let userMessage = { content: messageText, role: 'user' };
        display_messages = [...display_messages, userMessage];
        query_messages = [...query_messages, userMessage];

        // Scroll to the bottom when the user message is added
        await tick();
        scrollToBottom();

        // Request a response from the server
        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ messages: query_messages, user_input: messageText  })
        });

        const data = await response.json();

        // Add AI response to the messages array
        if (data.response) {
            let aiMessage = { content: data.response, role: 'system' };
            display_messages = [...display_messages, aiMessage];
            query_messages = [...query_messages, aiMessage];
        }

        // Wait for UI to update and then scroll to the bottom
        await tick();
        scrollToBottom();
    }

    function scrollToBottom() {
        if (messageContainer) {
            messageContainer.scrollTop = messageContainer.scrollHeight;
        }
    }

    onMount(() => {
        let systemMessage = { content: "Hi! How are you feeling today?", role: 'system' };
        display_messages = [systemMessage];
        query_messages = [systemMessage];
        scrollToBottom();
    });
</script>

<div class="chat-container">
    <div bind:this={messageContainer} class="messages">
        {#each display_messages as message}
        <div class={`message ${message.role === 'user' ? 'user-message' : 'ai-message'}`}>
            {#if message.role === 'system'}
                <img src='robot.svg' alt="robot" />
            {/if}
            <p>{@html convertMarkdownToHtml(message.content)}</p>
            {#if message.role === 'user'}
                <img src='user.svg' alt="user" />
            {/if}
        </div>
        {/each}
    </div>
    <div class="input-area">
        <div
            role="textbox"
            tabindex="0"
            contenteditable="true"
            class="input-textbox"
            placeholder="Send a new message"
            on:keyup={(e) => {
                if (e.key === 'Enter') {
                    sendMessage();
                    e.preventDefault(); // Prevents form submission and page reload
                }
            }}
        ></div>
        <button on:click={sendMessage}>Send</button>
    </div>
</div>

<style lang='postcss'>
    .input-area {
        font-family: 'Comic Sans MS', cursive;
        padding: 18px;
        display: flex;
        border-top: 1px solid #b2a5a5;
        column-gap: 1rem;
    }

    .input-textbox[placeholder]:empty::before {
        content: attr(placeholder);
        color: #555; 
    }

    .input-textbox[placeholder]:empty:focus::before {
        content: "";
    }

    .chat-container {
        font-family: 'Comic Sans MS', cursive;
        display: flex;
        flex-direction: column;
        height: 98%;
        background-color: #d8e4f6;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        overflow: hidden;
        overflow-y: auto;
        max-height: 100%;
    }

    .messages {
        font-size: 14px;
        flex-grow: 1;
        overflow-y: auto;
        padding: 20px;
        display: flex;
        flex-direction: column;
    }

    .message {
        padding: 8px;
        border-radius: 16px;
        margin-bottom: 12px;
        display: flex;
        gap: 0.5rem;
    }

    .user-message {
        background-color: #fff;
        color: black;
        margin-left: auto;
    }

    .ai-message {
        text-align: left;
        background-color: #fff;
        color: black;
        margin-right: auto;
    }

    .input-textbox {
        font-family: 'Comic Sans MS', cursive;
        border-radius: 0.35rem;
        padding: 0.5rem;
        flex-grow: 1;
        background-color: white;
        border: 2px solid black;
        text-align: left;
        height: 28px;
        overflow-y: auto;
    }

    button {
    font-family: 'Comic Sans MS', cursive;
    padding: 10px 20px; 
    background-color: #fff;
    cursor: pointer;
    border: 2px solid rgb(25, 23, 23);
    border-radius: 4px;
    }
    
    button:hover {
    background-color: #F0F0F0; /* Gray for hover effect */
    }
</style>




<!-- <script>
    import { onMount, tick } from 'svelte';

    let messages = [];
    let messageContainer;

    async function sendMessage() {
        const messageText = document.querySelector('.input-textbox').textContent.trim();
        if (!messageText) return;

        document.querySelector('.input-textbox').textContent = '';

        // Add user message to the array and immediately try to update UI
        messages = [...messages, { text: messageText, from: 'user' }];

        // Request a response from the server
        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ messages })
        });

        const data = await response.json();

        // Add AI response to the messages array
        messages = [...messages, { text: data.response, from: 'ai' }];

        // Wait for UI to update and then scroll to the bottom
        await tick();
        scrollToBottom();
    }

    function scrollToBottom() {
        messageContainer.scrollTop = messageContainer.scrollHeight;
    }

    onMount(() => {
        messages = [{ text: "Hi! How are you feeling today?", from: 'ai' }];
    });
</script>

<div class="chat-container">
    <div bind:this={messageContainer} class="messages">
        {#each messages as message (message.text)}
        <div class={`message ${message.from === 'user' ? 'user-message' : 'ai-message'}`}>
            {#if message.from === 'ai'}
                <img src='robot.svg' alt="robot" />
            {/if}
            <p>{message.text}</p>
            {#if message.from === 'user'}
                <img src='user.svg' alt="user" />
            {/if}
        </div>
        {/each}
    </div>
    <div class="input-area">
        <div
            role="textbox"
            tabindex="0"
            contenteditable="true"
            class="input-textbox"
            placeholder="Send a new message"
            on:keyup={(e) => {
                if (e.key === 'Enter') {
                    sendMessage();
                    e.preventDefault(); // Prevents form submission and page reload
                }
            }}
        ></div>
        <button on:click={sendMessage}>Send</button>
    </div>
</div> -->




<!-- <script>
    import { onMount, afterUpdate, tick } from 'svelte';

    let messages = [];
    let messageContainer;

    async function sendMessage() {
        const messageText = document.querySelector('.input-textbox').textContent.trim();
        if (!messageText) return;

        // Clear the input box
        document.querySelector('.input-textbox').textContent = '';

        // Append user message to the messages array
        messages = [...messages, { text: messageText, from: 'user' }];

        // Send the updated messages array to the server
        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ messages })
        });

        const data = await response.json();

        // Append AI response to the messages array
        messages = [...messages, { text: data.response, from: 'ai' }];
    }

    // This function is called after every DOM update
    afterUpdate(async () => {
        await tick();
        scrollToBottom();
    });

    function scrollToBottom() {
        messageContainer.scrollTop = messageContainer.scrollHeight;
    }

    onMount(() => {
        // Initialize with a greeting message from AI
        messages = [{ text: "Hi! How are you feeling today?", from: 'ai' }];
    });
</script> -->

<!-- <div class="chat-container" bind:this={messageContainer}>
    <div class="messages">
        {#each messages as message (message.text)}
        <div class={`message ${message.from === 'user' ? 'user-message' : 'ai-message'}`}>
            {#if message.from === 'ai'}
                <img src='robot.svg' alt="robot" />
            {/if}
            <p>{message.text}</p>
            {#if message.from === 'user'}
                <img src='user.svg' alt="user" />
            {/if}
        </div>
        {/each}
    </div>
    <div class="input-area">
        <div
            role="textbox"
            tabindex="0"
            contenteditable="true"
            class="input-textbox"
            placeholder="Send a new message"
            on:keyup={(e) => {
                if (e.key === 'Enter') {
                    sendMessage();
                    e.preventDefault(); // Prevent form submission and page reload
                }
            }}
        ></div>
        <button on:click={sendMessage}>Send</button>
    </div>
</div> -->







<!-- <script>
    import { onMount } from 'svelte';

    let messages = [];

    async function sendMessage() {
        // const messageText = document.querySelector('.input-textbox').innerText.trim();
        const messageText = document.querySelector('.input-textbox').textContent.trim();
        if (!messageText) return;

        // Clear the input box
        document.querySelector('.input-textbox').textContent = '';

        // Update messages array 
        messages = [...messages, { text: messageText, from: 'user' }];

        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            // body: JSON.stringify({ input: messageText })
            body: JSON.stringify({ messages })
        });

        const data = await response.json();
        messages = [...messages, { text: data.response, from: 'ai' }]; // Update and trigger reactivity
    }


    onMount(() => {
        // Initialize with first message
        messages = [{ text: "Hi! How are you feeling today?", from: 'ai' }]; 
    });
    </script>

    <div class="chat-container">
    <div class="messages">
        {#each messages as message (message.text)}
        <div class={`message ${message.from === 'user' ? 'user-message' : 'ai-message'}`}>
            {#if message.from === 'ai'}
            <img src='robot.svg' alt="robot" />
            {/if}
            <p>{message.text}</p>
            {#if message.from === 'user'}
            <img src='user.svg' alt="user" />
            {/if}
        </div>
        {/each}
    </div>
    <div class="input-area">
        <div
        role="textbox"
        tabindex="0"
        contenteditable="true"
        class="input-textbox"
        placeholder="Send a new message"
        on:keyup={(e) => {
            if (e.key === 'Enter') {
            sendMessage();
            e.preventDefault(); // Stop the default behavior of Enter key in contenteditable
            }
        }}
        ></div>
        <button on:click={sendMessage}>Send</button>
    </div>
</div>

<style lang='postcss'>
    /* .input-textbox {
        border-radius: 0.35rem;
        padding: 0.5rem;
        flex: 1;
        flex-grow: 1;
        background-color: white;
        outline: 1px solid black;
        min-height: 20px; 
        max-height: 150px;
        overflow-y: auto; 
    } */
    .input-area {
      font-family: 'Comic Sans MS', cursive;
      padding: 18px;
      display: flex;
      border-top: 1px solid #b2a5a5;
      column-gap: 1rem;
      }
    .input-textbox[placeholder]:empty::before {
        content: attr(placeholder);
        color: #555; 
    }
    
    .input-textbox[placeholder]:empty:focus::before {
        content: "";
    }
    .chat-container {
    font-family: 'Comic Sans MS', cursive;
    display: flex;
    flex-direction: column;
    height: 98vh;
    width: 47%;
    /* max-width: 650px; */
    /* left: 50%;
    top: 50px; */
    background-color: #d8e4f6;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    overflow: hidden;
    left: 0;
    }
    .messages { /* Message container */
    font-size: 12px;
    flex-grow: 1;
    overflow-y: auto;
    padding: 20px;
    display: flex;
    flex-direction: column;
    }
    .message { /* Individual message */
    padding: 10px;
    border-radius: 16px;
    margin-bottom: 12px;
    /* max-width: 60%; */
    align-items: center;
    word-wrap: break-word;
    display: flex;
    gap: 0.5rem;
    }
    .user-message {
    /* text-align: right; */
    background-color: #fff;
    color: black;
    margin-left: auto;
    }
    .ai-message {
    text-align: left;
    background-color: #fff;
    color: black;
    margin-right: auto;
    }

    /* .input-area {
    padding: 18px;
    display: flex;
    justify-content: space-between; 
    align-items: center; 
    border-top: 1px solid #b2a5a5;
    width: 100%; 
    box-sizing: border-box; 
    } */

    .input-textbox {
    font-family: 'Comic Sans MS', cursive;
    border-radius: 0.35rem;
    padding: 0.5rem;
    flex-grow: 1; 
    padding: 10px;
    margin-right: 8px;
    background-color: white;
    border: 2px solid black;
    border-radius: 4px;
    text-align: left;
    height: 28px; 
    overflow-y: auto; 
    }

    button {
    font-family: 'Comic Sans MS', cursive;
    padding: 10px 20px; 
    background-color: #fff;
    cursor: pointer;
    border: 2px solid rgb(25, 23, 23);
    border-radius: 4px;
    }
    button:hover {
    background-color: #F0F0F0; /* Gray for hover effect */
    }
    </style> -->
    