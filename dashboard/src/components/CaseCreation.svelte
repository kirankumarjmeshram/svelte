<script>
  import Case from "./CaseCreation/Case.svelte";
  import CaseCreateForm from "./CaseCreation/CaseCreateForm.svelte";
  let showForm = false;
  let cases = [
    {
      title: "Area 1",
      totalFiles: 4,
      totalDocuments: 600,
      lastUploadedDate: "04/02/24",
      lastUploadedTime: "14:02:19",
    },
    {
      title: "Area 2",
      totalFiles: 8,
      totalDocuments: 782,
      lastUploadedDate: "03/28/24",
      lastUploadedTime: "09:45:32",
    },
    {
      title: "Area 3",
      totalFiles: 2,
      totalDocuments: 345,
      lastUploadedDate: "04/01/24",
      lastUploadedTime: "17:30:59",
    },
    {
      title: "Area 4",
      totalFiles: 6,
      totalDocuments: 912,
      lastUploadedDate: "04/05/24",
      lastUploadedTime: "08:12:07",
    },
    {
      title: "Area 5",
      totalFiles: 3,
      totalDocuments: 507,
      lastUploadedDate: "03/30/24",
      lastUploadedTime: "11:20:44",
    },
    {
      title: "Area 6",
      totalFiles: 5,
      totalDocuments: 684,
      lastUploadedDate: "04/07/24",
      lastUploadedTime: "15:55:21",
    },
    {
      title: "Area 7",
      totalFiles: 9,
      totalDocuments: 1123,
      lastUploadedDate: "04/08/24",
      lastUploadedTime: "10:18:36",
    },
    {
      title: "Area 8",
      totalFiles: 1,
      totalDocuments: 213,
      lastUploadedDate: "04/06/24",
      lastUploadedTime: "13:40:15",
    },
    {
      title: "Area 9",
      totalFiles: 7,
      totalDocuments: 875,
      lastUploadedDate: "04/09/24",
      lastUploadedTime: "16:25:03",
    },
    {
      title: "Area 10",
      totalFiles: 4,
      totalDocuments: 642,
      lastUploadedDate: "04/02/24",
      lastUploadedTime: "19:08:50",
    },
    {
      title: "Area 11",
      totalFiles: 2,
      totalDocuments: 489,
      lastUploadedDate: "04/04/24",
      lastUploadedTime: "14:58:28",
    },
    {
      title: "Area 12",
      totalFiles: 6,
      totalDocuments: 745,
      lastUploadedDate: "04/11/24",
      lastUploadedTime: "09:35:17",
    },
    {
      title: "Area 13",
      totalFiles: 3,
      totalDocuments: 560,
      lastUploadedDate: "03/29/24",
      lastUploadedTime: "12:48:03",
    },
    {
      title: "Area 14",
      totalFiles: 5,
      totalDocuments: 821,
      lastUploadedDate: "04/10/24",
      lastUploadedTime: "08:07:42",
    },
    {
      title: "Area 15",
      totalFiles: 8,
      totalDocuments: 987,
      lastUploadedDate: "04/03/24",
      lastUploadedTime: "17:15:59",
    },
    {
      title: "Area 16",
      totalFiles: 1,
      totalDocuments: 376,
      lastUploadedDate: "04/12/24",
      lastUploadedTime: "11:50:28",
    },
    {
      title: "Area 17",
      totalFiles: 7,
      totalDocuments: 1054,
      lastUploadedDate: "04/07/24",
      lastUploadedTime: "14:22:07",
    },
    {
      title: "Area 18",
      totalFiles: 4,
      totalDocuments: 719,
      lastUploadedDate: "04/05/24",
      lastUploadedTime: "10:30:45",
    },
    {
      title: "Area 19",
      totalFiles: 9,
      totalDocuments: 1236,
      lastUploadedDate: "04/01/24",
      lastUploadedTime: "13:40:29",
    },
    {
      title: "Area 20",
      totalFiles: 3,
      totalDocuments: 593,
      lastUploadedDate: "04/09/24",
      lastUploadedTime: "18:05:53",
    },
  ];

  function addNewCase(e){
    cases = [e.detail,...cases]
  }
</script>

<div class="container">
    <div class="header">
      <h1>Case Creation</h1>
      <button on:click={() => (showForm = !showForm)}>{showForm ? "Show All Cases":"+Add New Case"}</button>
    </div>
    {#if showForm}
      <CaseCreateForm on:add = {addNewCase} />
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
  .case_container{
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
    margin-right:2em;

  }
</style>
