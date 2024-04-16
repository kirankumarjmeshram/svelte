<script>
  import { onMount } from "svelte";
  import { page } from "$app/stores";
  import axios from "axios";

  let caseId = $page.params.caseId;
  let caseDetail = null;

  onMount(async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5123/data/${caseId}`);
      caseDetail = response.data;
    } catch (error) {
      console.error("Error fetching case data:", error);
    }
  });
  function goback(){
    window.history.back()
  }
</script>

<button on:click={goback}>Back</button>
<div class="case-card">
  {#if caseDetail}
    <div class="row">
      <h3>{caseDetail.title}</h3>
    </div>
    <hr />
    <b><p>Total files: {caseDetail.totalFiles.length}</p></b>
    <b><p>Total Document: {caseDetail.totalDocuments.length}</p></b>
    <p>Last Uploaded date: {caseDetail.lastUploadedDate}</p>
    <p>Last Uploaded Time: {caseDetail.lastUploadedTime}</p>
    <hr />
  {:else}
    <p>Loading...</p>
  {/if}
</div>

<style>
  .case-card {
    border: 1px solid #e6e4e4;
    padding: 1em;
    margin: 1em;
    border-radius: 10px;
    box-shadow: 7px 7px 8px rgba(0, 0, 0, 0.1);
  }
  .case-card .row {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .case-card .row h3 {
    flex: 1;
  }
</style>
