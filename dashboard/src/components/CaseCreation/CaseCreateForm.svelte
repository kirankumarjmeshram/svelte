<!-- CaseForm.svelte -->
<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  let caseDetail = {
    title: "",
    totalFiles: 0,
    totalDocuments: 0,
    lastUploadedDate: "",
    lastUploadedTime: "",
  };

  function addCase() {
    dispatch('add', caseDetail);
    caseDetail = {
      title: "",
      totalFiles: 0,
      totalDocuments: 0,
      lastUploadedDate: "",
      lastUploadedTime: "",
    };
  }

</script>

<style>
  .container{
    border: 1px solid #b9b8b8;
    padding: 1em;
    border-radius: 10px;
    box-shadow: 7px 7px 8px rgba(0, 0, 0, 0.1); 
  }
  div {
    display: flex;
    flex-direction: column;
    gap: 1em;
    width: 300px;
    margin: auto;
  }
  label {
    display: flex;
    flex-direction: column;
    gap: 0.5em;
  }
  button {
    padding: 0.5em;
    background-color: green;
    color: white;
    border: none;
    cursor: pointer;
  }
</style>

<div class='container'>
  <label>
    Title:
    <input bind:value={caseDetail.title} type="text" />
  </label>
  <label>
    Total Files:
    <input bind:value={caseDetail.totalFiles} type="number" />
  </label>
  <label>
    Total Documents:
    <input bind:value={caseDetail.totalDocuments} type="number" />
  </label>
  <label>
    Last Uploaded Date:
    <input bind:value={caseDetail.lastUploadedDate} type="date" />
  </label>
  <label>
    Last Uploaded Time:
    <input bind:value={caseDetail.lastUploadedTime} type="time" />
  </label>
  <button on:click={addCase}>Add</button>
</div>
