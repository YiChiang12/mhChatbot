<script>
  import Chatbot from './Chatbot.svelte';
  import ProblemsSolutions from './ProblemsSolutions.svelte';
</script>

<div id="app" class="root">
  <Chatbot />
  <ProblemsSolutions />
</div>

<!-- <style>
  .app-container {
    display: flex;
    width: 100%;
    height: 100vh;
  }
</style> -->








<!-- <script>
  import Chatbot from './Chatbot.svelte';
</script>

<div id="app">
  <Chatbot />
</div> -->








<!-- <script>
  import { onMount } from 'svelte';

  let messages = [];

  async function sendMessage() {
    const messageText = document.querySelector('.input-textbox').innerText.trim();
    if (!messageText) return;

    // Manually clear the input box
    document.querySelector('.input-textbox').innerText = '';

    // Update messages array and trigger reactivity
    messages = [...messages, { text: messageText, from: 'user' }];

    try {
      const response = await fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ input: messageText })
      });

      const data = await response.json();
      messages = [...messages, { text: data.response, from: 'ai' }]; // Update and trigger reactivity
    } catch (error) {
      console.error('Failed to send message:', error);
    }
  }
  
  onMount(() => {
    messages = [{ text: "Hi! How are you feeling today?", from: 'ai' }]; // Initialize with first message
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
  </style> -->
  















<!-- 
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
</script>

<main>
  <div>
    <a href="https://vitejs.dev" target="_blank" rel="noreferrer">
      <img src={viteLogo} class="logo" alt="Vite Logo" />
    </a>
    <a href="https://svelte.dev" target="_blank" rel="noreferrer">
      <img src={svelteLogo} class="logo svelte" alt="Svelte Logo" />
    </a>
  </div>
  <h1>Vite + Svelte</h1>

  <div class="card">
    <Counter />
  </div>

  <p>
    Check out <a href="https://github.com/sveltejs/kit#readme" target="_blank" rel="noreferrer">SvelteKit</a>, the official Svelte app framework powered by Vite!
  </p>

  <p class="read-the-docs">
    Click on the Vite and Svelte logos to learn more
  </p>
</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
</style> -->
