<script>
  export let caseDetail;

  function upload() {
    window.alert("Upload button clicked");
  }

  function analyse() {
    window.alert("Analyse button clicked");
  }
</script>

<div class="case-card">
  <div class="row">
    <h3>{caseDetail.title}</h3>
    <button class="new">New</button>
  </div>
  <hr />
  <b><p>Total files: {caseDetail.totalFiles}</p></b>
  <b><p>Total Document: {caseDetail.totalDocuments}</p></b>
  <p>Last Uploaded date: {caseDetail.lastUploadedDate}</p>
  <p>Last Uploaded Time: {caseDetail.lastUploadedTime}</p>
  <hr />
  <div class="row">
    <button class="upload" on:click={upload}>
      Upload
    </button>
    <button class="analyse" on:click={analyse}>Analyse</button>
  </div>
</div>

<style>
  .case-card {
    border: 1px solid #b9b8b8;
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
  .case-card button.new {
    background-color: green;
    color: white;
    border: none;
    padding: 0.5em;
    border-radius: 5px;
    cursor: pointer;
    text-align: right;
    width: 25%;
    flex-grow: 0;
  }
  .case-card button {
    margin-top: 1em;
    padding: 0.5em 1em;
    border-radius: 5px;
    border: none;
    cursor: pointer;
  }
  .case-card button.upload {
    background: transparent;
    border: 1px solid #ccc;
    width: 30%;
    flex-grow: 0;
  }
  .case-card button.analyse {
    margin-left: 100px;
    background: rgb(253, 255, 134);
    color: rgb(0, 0, 0);
    width: 30%;
    flex-grow: 0;
  }
</style>
