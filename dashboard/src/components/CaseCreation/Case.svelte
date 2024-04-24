<script>
  import { goto } from "$app/navigation";
  import { formOpen, caseId, title, analysisOpen } from './store.js';
  import UploadForm from './UploadForm.svelte';
  export let caseDetail;

  function openAnalyse() {
      const caseId = caseDetail._id;
      goto(`/caseAnalysis/${caseId}`);

  }

  function getCaseInfo() {
      const caseId = caseDetail._id;
      goto(`/caseInfo/${caseId}`);
  }

  function openUploadForm() {
      caseId.set(caseDetail._id)
      title.set(caseDetail.title)
      formOpen.set(true);
  }
</script>

<div class="case-card">
<div class="row">
  <h3>{caseDetail.title}</h3>
  <button class="new" on:click={getCaseInfo}>Info</button>
</div>
<hr />
<p>Case id {caseDetail._id}</p>
<b><p>Total files: {caseDetail.totalFiles.length}</p></b>
<b><p>Total Document: {caseDetail.totalDocuments.length}</p></b>
<p>Last Uploaded date: {caseDetail.lastUploadedDate}</p>
<p>Last Uploaded Time: {caseDetail.lastUploadedTime}</p>
<hr />
<div class="row">
  <button class="upload" on:click={openUploadForm}> Upload </button>
  <button class="analyse" on:click={openAnalyse}>Analyse</button>
</div>
</div>
<UploadForm/>
<!-- <CaseAnalysis/> -->

<style>
.case-card {
  border: 1px solid #e6e4e4;
  padding: 1em;
  margin: 1em;
  border-radius: 10px;
  box-shadow: 7px 7px 8px rgba(228, 227, 193, 0.1);
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
