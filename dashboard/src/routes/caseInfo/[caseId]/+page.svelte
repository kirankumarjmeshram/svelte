<script>
  import { onMount } from "svelte";
  import { page } from "$app/stores";
  import axios from "axios";

  let caseId = $page.params.caseId;
  let caseDetail = null;
  // const url = import.meta.env.API_URI;
  // console.log(url)

  onMount(async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5124/data/${caseId}`);
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
    <p>created_by : {caseDetail.created_by ?caseDetail.created_by :'admin'}</p>
    <hr />
    {#if caseDetail.totalFiles.length}
      <div>
        <table>
          <thead>
            <th>File Name</th>
            <th>File Path</th>
            <th>Size</th>
            <th>Type</th>
          </thead>
          <tbody>
            {#each caseDetail.totalFiles as data }
              <tr>
                <td>{data.filename}</td>
                <td>{data.filepath}</td>
                <td>{data.size/1000} kb</td>
                <td>{data.type}</td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    {/if}
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
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }

  th, td {
    padding: 8px;
    border-bottom: 1px solid #ddd;
    text-align: left;
  }

  th {
    background-color: #f2f2f2;
  }

  tr:hover {
    background-color: #f2f2f2;
  }
</style>
