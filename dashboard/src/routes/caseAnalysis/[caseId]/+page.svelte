<script>
  import { onMount } from "svelte";
  import { page } from "$app/stores";
  import axios from "axios";

  let caseId = $page.params.caseId;
  // console.log("caseId",caseId)
  let caseDetail = null;
  

  onMount(async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5124/data/${caseId}`);
      caseDetail = response.data;
      // console.log("caseDetail",caseDetail)
    } catch (error) {
      console.error("Error fetching case data:", error);
    }
  });
  function goback(){
    console.log("Clicked on go back")
    window.history.back()
  }
</script>

  <button on:click={goback}>back</button>
  <div class="analysis-modal">
    <div class="analysis-content">
      {#if caseDetail !== null}
        <h2>{caseDetail.title} Analysis</h2>
        {#if caseDetail.totalFiles.length}
          <div>
            <table>
              <thead>
                <tr>
                  <th>File Name</th>
                  <th>File Path</th>
                  <th>Size</th>
                  <th>Type</th>
                </tr>
              </thead>
              <tbody>
                {#each caseDetail.totalFiles as file}
                  <tr>
                    <td>{file.filename}</td>
                    <td>{file.filepath}</td>
                    <td>{(file.size / 1000).toFixed(2)} kb</td>
                    <td>{file.type}</td>
                  </tr>
                {/each}
              </tbody>
            </table>
          </div>
        {/if}
      {/if}
      
    </div>
  </div>
  
  
  <style>
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }
  
    th,
    td {
      padding: 8px;
      border-bottom: 1px solid #ddd;
      text-align: left;
    }
  
    th {
      background-color: #f2f2f2;
    }
  
    button {
      padding: 10px 20px;
      border: none;
      background-color: #007bff;
      color: white;
      border-radius: 5px;
      cursor: pointer;
    }
  
    button:hover {
      background-color: #0056b3;
    }
  </style>
  