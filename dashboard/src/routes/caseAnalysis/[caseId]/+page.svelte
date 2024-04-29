<script>
  import { onMount } from "svelte";
  import { page } from "$app/stores";
  import axios from "axios";

  // export async function load({ params }) {
  //   return {
  //     props: {
  //       caseId: params.caseId
  //     }
  //   };
  // }

  let caseId = $page.params.caseId;
  let caseDetail = null;
  let selectedFile = null;

  onMount(async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5124/data/${caseId}`);
      caseDetail = response.data;
      if (caseDetail.totalFiles.length > 0) {
        // set first file as default
        selectedFile = caseDetail.totalFiles[0];
      }
    } catch (error) {
      console.error("Error fetching case data:", error);
    }
  });

  function selectFile(file) {
    selectedFile = file;
  }

  function goback() {
    window.history.back();
  }
</script>
<button on:click={goback}>back</button>
<div class="container">
  <div class="sidebar">
    {#if caseDetail !== null}
      {#each caseDetail.totalFiles as file, index}
        <div class="tab {selectedFile === file ? 'active' : ''}" on:click={() => selectFile(file)}>
          {file.filename}
        </div>
      {/each}
    {/if}
  </div>

  <div class="details">
    {#if selectedFile !== null}
      <h2>{selectedFile.filename} Details</h2>
      <p><strong>File Path:</strong> {selectedFile.filepath}</p>
      <p><strong>Size:</strong> {(selectedFile.size / 1000).toFixed(2)} kb</p>
      <p><strong>Type:</strong> {selectedFile.type}</p>
    {/if}
  </div>
</div>

<style>
  .container {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
  }

  .sidebar {
    width: 200px;
    background-color: #f2f2f2;
    border-right: 1px solid #ddd; /* Added border to the right */
  }

  .tab {
    padding: 8px;
    cursor: pointer;
    border-bottom: 1px solid #ddd;
  }

  .tab.active {
    background-color: #ddd;
  }

  .details {
    flex: 1;
    padding: 0 20px;
  }

  .details h2 {
    margin-top: 0;
  }

  .details {
    border-left: 1px solid #ddd;
  }

  .details {
    border-top: 1px solid #ddd;
    border-bottom: 1px solid #ddd;
  }
</style>



<!-- <script>
  import { onMount } from "svelte";
  import { page } from "$app/stores";
  import axios from "axios";

  export async function load({ params }) {
    return {
      props: {
        caseId: params.caseId
      }
    };
  }

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
  
 
  </style>
   -->