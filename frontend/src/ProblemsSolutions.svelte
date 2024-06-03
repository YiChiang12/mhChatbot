<script>
  import { onMount, tick } from 'svelte';
  import ProblemCard from './ProblemCard.svelte';
  
  let problemsSolutions = [];

  async function loadProblemsSolutions() {
    try {
      const response = await fetch('http://127.0.0.1:5000/data/extracted_prob_sol.json');
      if (!response.ok) throw new Error('Failed to fetch');
      problemsSolutions = await response.json();
    } catch (error) {
      console.error('Fetch error:', error);
    }
  }

  onMount(() => {
    loadProblemsSolutions();
    const interval = setInterval(loadProblemsSolutions, 5000);  // Poll every 5 seconds
    return () => clearInterval(interval);  // Cleanup on component destruction
  });
</script>

<style>
  .problems-solutions-container {
    width: 50%;
    padding: 20px;
    overflow-y: auto;
    max-height: 100%;
  }
</style>

<div class="problems-solutions-container">
  {#each problemsSolutions as item}
    <ProblemCard {item} />
  {/each}
</div>




<!-- <script>
  import { onMount } from 'svelte';
  import ProblemCard from './ProblemCard.svelte';
  
  let problemsSolutions = [];

  async function loadProblemsSolutions() {
    
  try {
    const response = await fetch('http://127.0.0.1:5000/data/extracted_prob_sol.json');
    if (!response.ok) throw new Error('Network response was not okay');
    problemsSolutions = await response.json();
  } catch (error) {
    console.error('Failed to fetch problems and solutions:', error);
  }
  }

  onMount(() => {
    loadProblemsSolutions();
  });
</script>

<style>
  .problems-solutions-container {
    width: 50%;
    padding: 20px;
    overflow-y: auto;
    max-height: 100%;
  }
</style>

<div class="problems-solutions-container">
  {#each problemsSolutions as item}
    <ProblemCard {item} />
  {/each}
</div> -->








<!-- <script>
  import { onMount } from 'svelte';
  import { Card } from 'flowbite-svelte';

  let problemsSolutions = [];

  onMount(async () => {
    try {
      const response = await fetch('../../server/data/extracted_prob_sol.json');  
      if (response.ok) {
        problemsSolutions = await response.json();
      } else {
        console.error('Failed to fetch:', response.status);
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  });
</script> -->

<!-- <script>
  import { Card } from 'flowbite-svelte';
  import { onMount } from 'svelte';

  let problemsSolutions = [];

  onMount(async () => {
    try {
      // 'http://localhost:5000/data/extracted_prob_sol.json'
      // '../../server/data/extracted_prob_sol.json'
      const response = await fetch('http://localhost:5000/data/extracted_prob_sol.json', {
        method: 'GET', // Explicitly state the method
        headers: {
          'Accept': 'application/json' // Correct header for accepting JSON
        }
      });
      if (response.ok) {
        problemsSolutions = await response.json();
      } else {
        throw new Error(`Failed to load data: ${response.status}`);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  });
</script>

  
  <div class="problems-solutions-container">
    {#each problemsSolutions as item}
      <Card>
        <div class="card-content">
          <h5 class="problem-title">Problem:</h5>
          <p>{item.problem}</p>
          <h5 class="solution-title">Solution:</h5>
          <p>{item.solution}</p>
        </div>
      </Card>
    {/each}
  </div>
  
  <style>
    .problems-solutions-container {
      width: 50%; 
      padding: 20px; /* Padding for aesthetic spacing */
    }
  </style> -->
  





<!-- <script>
    import { Card } from 'flowbite-svelte';
    import { onMount } from 'svelte';
  
    let problemsSolutions = [];
  
    // onMount(async () => {
    //   const response = await fetch('/server/data/extracted_prob_sol.json');
    //   problemsSolutions = await response.json();
    // });
    onMount(async () => {
    try {
        const response = await fetch('../../server/data/extracted_prob_sol.json');
        if (response.ok) {
            problemsSolutions = await response.json();
            console.log("Data loaded successfully:", problemsSolutions);
        } else {
            throw new Error('Failed to load data: ' + response.status);
        }
    } catch (error) {
        console.error("Error fetching data:", error);
    }
});
  </script>
  
  <div class="problems-solutions-container">
    {#each problemsSolutions as item}
      <Card>
        <div class="card-content">
          <h5 class="problem-title">Problem:</h5>
          <p>{item.problem}</p>
          <h5 class="solution-title">Solution:</h5>
          <p>{item.solution}</p>
        </div>
      </Card>
    {/each}
  </div>
  
  <style>
    .problems-solutions-container {
      margin: 0 20px;
      max-width: 300px;
    }
    .problem-title, .solution-title {
      font-weight: bold;
    }
  </style> -->
  