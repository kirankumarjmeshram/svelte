<script>
    import { analysisOpen } from './store.js'; 
  
    export let caseDetail;
  
    function closeAnalysis() {
      analysisOpen.set(false);
    }
  </script>
  
  <div class="analysis-modal">
    <div class="analysis-content">
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
      <div class="action-buttons">
        <button on:click={closeAnalysis}>Close</button> 
      </div>
    </div>
  </div>
  
  
  <style>
    .analysis-modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(238, 234, 234, 0.1);
      z-index: 10000;
      display: flex;
      justify-content: center;
      align-items: center;
    }
  
    .analysis-content {
      background-color: white;
      color: black;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(127, 124, 124, 0.5);
      max-width: 80%;
      max-height: 80%;
      overflow-y: auto;
    }
  
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
  
    .action-buttons {
      margin-top: 20px;
      text-align: center;
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
  