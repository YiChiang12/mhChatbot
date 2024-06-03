<script lang="ts">
    export let item;

    let buttonText = 'Copy';

    function copyText() {
      const textToCopy = `Problem: ${item.problem}\nSolution: ${item.solution.join('; ')}`;
      navigator.clipboard.writeText(textToCopy).then(() => {
        buttonText = 'Copied!';
        setTimeout(() => buttonText = 'Copy', 2000); // Reset button text after 2 seconds
      }, err => {
        console.error('Error in copying text: ', err);
      });
    }

    function handleKeypress(event) {
      if (event.key === 'Enter' || event.key === ' ') {
        copyText();
      }
    }
</script>

<div class="prob-card" role="button" tabindex="0" on:click={copyText} on:keypress={handleKeypress}>
  <button class="copy-button">{buttonText}</button>
  <h3 class="problem-title">Problem: {item.problem}</h3>
  <div class="solution-section">
    <h4 class="solution-title">Solution:</h4>
    <ul class="solution-list">
      {#each item.solution as solution}
        <li class="solution-item">{solution}</li>
      {/each}
    </ul>
  </div>
</div>

<style>
  .prob-card {
    background: #ffecd1;
    padding: 20px;
    margin: 10px 0;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    position: relative;
    transition: transform 0.2s;
    cursor: pointer;
  }
  .problem-title, .solution-title {
    color: #4474a4;
    font-family: 'Comic Sans MS', cursive;
  }
  .solution-list {
    margin-top: 5px;
  }
  .solution-item {
    margin-bottom: 3px;
    color: #2a2828;
    font-family: 'Comic Sans MS', cursive;
  }
  .copy-button {
    background-color: #535453; 
    font-family: 'Comic Sans MS', cursive;
    border: none;
    color: white;
    padding: 5px 10px;
    font-size: 12px;
    position: absolute;
    top: 10px;
    right: 10px;
    cursor: pointer;
    border-radius: 4px;
  }
</style>






<!-- <script lang="ts">
    export let item;

    let buttonText = 'Copy';

    function copyText() {
      const textToCopy = `Problem: ${item.problem}\nSolution: ${item.solution}`;
      navigator.clipboard.writeText(textToCopy).then(() => {
        buttonText = 'Copied!';
        setTimeout(() => buttonText = 'Copy', 2000); // Reset button text after 2 seconds
      }, err => {
        console.error('Error in copying text: ', err);
      });
    }

    function handleKeypress(event) {
      if (event.key === 'Enter' || event.key === ' ') {
        copyText();
      }
    }
</script>

<div class="prob-card" role="button" tabindex="0" on:click={copyText} on:keypress={handleKeypress}>
  <button class="copy-button" on:click={copyText}>{buttonText}</button>
  <h3 class="problem-title">Problem: {item.problem}</h3>
  <div class="solution-section">
    <h4 class="solution-title">Solution:</h4>
    <ul class="solution-list">
      {#each item.solution.split(';') as solution}
        <li class="solution-item">{solution.trim()}</li>
      {/each}
    </ul>
  </div>
</div>

<style>
  .prob-card {
    background: #ffecd1; 
    padding: 20px;
    margin: 10px 0;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    position: relative;
    transition: transform 0.2s;
    cursor: pointer;
  }
  .prob-card:hover {
    transform: translateY(-5px);
  }
  .problem-title, .solution-title {
    color: #4474a4;
    font-family: 'Comic Sans MS', cursive;
  }
  .solution-list {
    margin-top: 5px;
  }
  .solution-item {
    margin-bottom: 3px;
    color: #2a2828;
    font-family: 'Comic Sans MS', cursive;
  }
  .copy-button {
    background-color: #535453; 
    font-family: 'Comic Sans MS', cursive;
    border: none;
    color: white;
    padding: 5px 10px;
    font-size: 12px;
    position: absolute;
    top: 10px;
    right: 10px;
    cursor: pointer;
    border-radius: 4px;
  }
</style> -->






<!-- <script lang="ts">
    export let item; // This will contain a problem and its solution
  </script>
  
  <div class="prob-card">
    <h3>Problem: {item.problem}</h3>
    <p>Solution: {item.solution}</p>
  </div>
  
  <style>
    .prob-card {
      background: #f0f0f0;
      padding: 10px;
      margin: 10px 0;
      border-radius: 5px;
    }
  </style> -->
  




<!-- <script>
    export let problem;
    export let solution;
  </script>
  
  <div class="card">
    <h3 class="problem-title">Problem: {problem}</h3>
    <p class="solution-description">Solution: {solution}</p>
  </div>
  
  <style>
    .card {
      background-color: #f0f8ff;
      border: 1px solid #ddd;
      padding: 16px;
      margin-bottom: 8px;
      border-radius: 8px;
    }
    .problem-title {
      color: #333;
      font-weight: bold;
    }
    .solution-description {
      color: #666;
    }
  </style> -->
  
  