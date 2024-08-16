<script>
    import { onMount, tick } from 'svelte';
    import { marked } from 'marked';

    let display_messages = [];
    let query_messages = [];
    let messageContainer;
    let showModal = false;

    function clearChat() {
        showModal = true;
    }

    function cancelClear() {
        showModal = false;
    }

    async function confirmClear() {
        try {
            // Clear the chat on the backend
            const response = await fetch('http://127.0.0.1:5000/clear_chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' }
            });

            const data = await response.json();
            if (data.status === 'success') {
                // Clear the chat in the frontend
                display_messages = [{
                    role: "system",
                    content: "I know you’ve been having a tough time recently. <br>Can you share what has been going on?"
                }];
                query_messages = [];
                showModal = false;
                scrollToBottom();
            } else {
                console.error('Fail to clear chat:', data.message);
            }
        } catch (error) {
            console.error('Fail to clear chat:', error);
        }
    }

    // function confirmClear() {
    //     display_messages = [{
    //         role: "system",
    //         content: "I know you’ve been having a tough time recently. <br>Can you share what has been going on?"
    //     }];
    //     query_messages = [];
    //     showModal = false;
    //     // display_messages.push({content: "I know you’ve been having a tough time recently. <br>Can you share what has been going on?", role: "system"});
    //     scrollToBottom();
    // }

    const renderer = new marked.Renderer();
    const originalLinkRenderer = renderer.link;
    renderer.link = (href, title, text) => {
        const html = originalLinkRenderer.call(renderer, href, title, text);
        return html.replace(/^<a /, '<a target="_blank" ');
    };

    // Convert Markdown to HTML
    function convertMarkdownToHtml(markdownText) {
        return marked(markdownText, { renderer });
    }

    async function sendMessage() {
        try {
            const messageText = document.querySelector('.input-textbox').textContent.trim();
            if (!messageText) return;
            document.querySelector('.input-textbox').textContent = '';
            let userMessage = { content: messageText, role: 'user' };
            display_messages = [...display_messages, userMessage];
            query_messages = [...query_messages, userMessage];

            // Scroll to the bottom when the user message is added
            await tick();
            scrollToBottom();
            
            const response = await fetch('http://127.0.0.1:5000/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ messages: query_messages, user_input: messageText  })
            });

            const data = await response.json();

            // Add AI response
            // if (data.response) {
            //     let aiMessage = { content: data.response, role: 'system' };
            //     display_messages = [...display_messages, aiMessage];
            //     query_messages = [...query_messages, aiMessage];
            // }
            if (data.response) {
                await displayResponseTypingEffect(data.response);
            }
            // After AI response, scroll to the bottom
            await tick();
            scrollToBottom();
        } catch (error) {
            console.error('Failed to send message:', error);
        }
    }

    async function displayResponseTypingEffect(response) {
        let aiMessage = { content: '', role: 'system' };
        display_messages = [...display_messages, aiMessage];

        for (let i = 0; i < response.length; i++) {
            aiMessage.content += response[i];
            display_messages = [...display_messages];
            await tick();
            scrollToBottom();
            await new Promise(resolve => setTimeout(resolve, 13));
        }

        query_messages = [...query_messages, aiMessage];
    }

    function scrollToBottom() {
        if (messageContainer) {
            messageContainer.scrollTop = messageContainer.scrollHeight;
        }
    }

    onMount(() => {
        let systemMessage = { content: "I know you’ve been having a tough time recently. <br>Can you share what has been going on?", role: 'system' };
        display_messages = [systemMessage];
        query_messages = [systemMessage];
        scrollToBottom();
    });
</script>

<div class="chat-container">
    <div class="chat-title">
        Eunoia Chatbot
        <button class="clear-chat-btn" on:click={clearChat} aria-label="Clear Chat">
            <img src="delete.svg" alt="Clear Chat Icon" />
        </button>
    </div>
    {#if showModal}
        <div class="modal">
            <div class="modal-content">
                <p>Do you want to clear the chat?</p>
                <div class="modal-buttons">
                    <button on:click={cancelClear} class="cancel-btn">Cancel</button>
                    <button on:click={confirmClear} class="confirm-btn">Confirm Delete</button>
                </div>
            </div>
        </div>
    {/if}
    
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
    <div class="chat-disclaimer">
        This is a chatbot, not a licensed professional. If you need to talk to someone, please contact the 24/7 crisis lifeline at <a href='tel:988'>988</a>.
    </div>
</div>

<style lang='postcss'>
    .modal {
        display: flex;
        justify-content: center;
        align-items: center;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
    }

    .modal-content {
        background-color: white;
        padding: 22px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .modal-buttons {
        display: flex;
        justify-content: center;
        gap: 15px;
        border-top: 1px solid #ccc;
        padding-top: 20px;
    }

    .clear-chat-btn {
        width: 24px;
        height: 24px;
        cursor: pointer;
        position: absolute;
        top: 50%; 
        right: 40px;
        transform: translateY(-50%); 
        background: none;
        border: none;
        padding: 0; 
        display: flex;
        align-items: center; 
        justify-content: center; 
    }

    .clear-chat-btn：hover {
        background-color: rgba(0, 0, 0, 0.1);
        /* background-color: #d73a3a; */
        border-radius: 50%;
    }

    .cancel-btn {
        background-color: rgb(231, 226, 226);
        color: rgb(92, 84, 84);
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .cancel-btn:hover {
        background-color: #cbc4c4;
    }

    .confirm-btn{
        background-color: #d72a2a;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .confirm-btn:hover {
        background-color: #af1105;
    }

    .chat-title {
        font-family: 'Comic Sans MS', cursive;
        padding: 15px 30px;
        text-align: left;
        background-color: #fcfdfe;
        border-bottom: 2px solid #bed0ed;
        text-align: left;
        font-size: 19px;
        color: #747578;
        position: relative;
    }
    .input-area {
        font-family: 'Comic Sans MS', cursive;
        padding: 25px;
        display: flex;
        border-top: 1px solid #b2a5a5;
        column-gap: 1rem;

        padding: 25px 35px 1px 25px;
        /* margin-bottom: 20px; */
    }

    .chat-disclaimer {
    font-family: 'Comic Sans MS', cursive;
    /* background-color: #fcfdfe; */
    padding: 10px;
    text-align: center;
    font-size: 14px;
    color: #84878c;
    width: 100%;
    padding: 25px;
    }

    .chat-disclaimer a {
        color: #d72a2a;
        text-decoration: none;
    }

    .chat-disclaimer a:hover {
        text-decoration: underline;
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
        /* height: 80vh; */
        height: 100%;
        background-color: #d8e4f6;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        overflow: hidden;
        overflow-y: auto;
        max-height: 100%;
        width: 75%;    
        margin-left: 25%;
        padding-bottom: 80px;
        position: relative;

        margin: 0 auto;
    }
    .messages {
        font-size: 14px;
        flex-grow: 1;
        overflow-y: auto;
        padding: 30px;
        display: flex;
        flex-direction: column;
    }
    .message {
        padding: 8px;
        border-radius: 16px;
        margin-bottom: 22px;
        display: flex;
        gap: 0.8rem;
        /* max-width: 90%; */
    }
    .user-message {
        /* text-align: middle; */
        background-color: #fff;
        color: black;
        margin-left: auto;
        /* border: 1px solid #ccc; */
        padding-left: 20px;
        padding-right: 15px;
        max-width: 65%;
    }

    .ai-message {
        text-align: left;
        background-color: #fff;
        color: black;
        margin-right: auto;
        border: 1.5px solid #c3c1c1;
        padding-right: 20px;
        padding-left: 15px;
        max-width: 73%;
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
        padding-left: 15px;
        font-size: 16px;
    }

    button {
    font-family: 'Comic Sans MS', cursive;
    padding: 10px 20px; 
    background-color: #fff;
    cursor: pointer;
    border: 2px solid rgb(25, 23, 23);
    border-radius: 4px;
    font-size: 16px;
    }
    
    button:hover {
    background-color: #F0F0F0; /* Gray for hover effect */
    }
</style>


