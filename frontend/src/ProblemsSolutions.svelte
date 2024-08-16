<script>
  import { onMount } from 'svelte';
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



