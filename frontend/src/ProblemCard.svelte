<script lang="ts">
  export let item;
</script>

<div class="prob-card">
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
  /* cursor: pointer; */
}
.problem-title, .solution-title {
  color: #4474a4;
  font-family: 'Comic Sans MS', cursive;
}
.solution-list {
  margin-top: 25px;
}
.solution-item {
  margin-bottom: 5px;
  color: #2a2828;
  font-family: 'Comic Sans MS', cursive;
}
</style>


