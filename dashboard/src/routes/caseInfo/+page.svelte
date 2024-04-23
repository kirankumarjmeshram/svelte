<script>
  import axios from 'axios';
  import Case from "../../components/CaseCreation/Case.svelte";
  import CaseCreateForm from "../../components/CaseCreation/CaseCreateForm.svelte";
  import { onMount } from 'svelte';

  let showForm = false;
  let cases = [];

  async function fetchData() {
    try {
      const response = await axios.get('http://127.0.0.1:5124/data');
      cases = response.data;
    } catch (error) {
      console.error(error);
    }
  }

  onMount(fetchData);
  
  function addNewCase(e) {
    cases = [e.detail, ...cases]
  }
</script>

<div class="container">
  <div class="header">
    <h1>Case Creation</h1>
    <button on:click={() => (showForm = !showForm)}>{showForm ? "Show All Cases" : "+Add New Case"}</button>
  </div>
  {#if showForm}
    <CaseCreateForm on:add={addNewCase} />
  {:else}
    <div class="case_container">
      {#each cases as caseDetail (caseDetail.title)}
        <Case {caseDetail} />
      {/each}
    </div>
  {/if}
</div>

<style>
  .container {
    background-color: white;
    height: 100%;
    color: black;
  }
  .case_container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(20%, 1fr));
    gap: 1rem;
    overflow-y: scroll;
    height: 100%;
  }
  .header {
    display: flex;
    flex-direction: column;
    align-items: flex-start
  }

  .header button {
    align-self: flex-end;
    background-color: rgb(241, 246, 241);
    color: rgb(0, 0, 0);
    border: none;
    padding: 0.5em;
    border-radius: 5px;
    cursor: pointer;
    margin-right: 2em;
  }
</style>
