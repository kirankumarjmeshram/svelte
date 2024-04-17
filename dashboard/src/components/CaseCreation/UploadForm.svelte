<!-- <script>
    import { formOpen, caseId } from './store.js';

    let isOpen = false;
    let files = [];

    let currCaseId;
    caseId.subscribe(value => currCaseId = value);
    // console.log("currCaseId",currCaseId)

    formOpen.subscribe(value => {
        isOpen = value;
    });

    function openForm() {
        console.log("Clicked on upload");
        formOpen.set(true);
    }


    function closeForm() {
        formOpen.set(false);
        // isOpen = false;
        files = []; // Clear the selected files
    }

    function handleFileChange(event) {
        files = Array.from(event.target.files);
    }

    function handleUpload() {
        console.log(files);
        closeForm();
    }
</script> -->
<script>
    import { formOpen, caseId } from './store.js';
    export let title;

    let isOpen = false;
    let files = [];

    let currCaseId;
    caseId.subscribe(value => currCaseId = value);

    formOpen.subscribe(value => {
        isOpen = value;
    });

    function openForm() {
        // console.log("Clicked on upload");
        formOpen.set(true);
    }

    function closeForm() {
        formOpen.set(false);
        files = []; 
    }

    function handleFileChange(event) {
        files = Array.from(event.target.files);
    }

    async function handleUpload() {
        const data = new FormData();
        files.forEach(file => data.append('file', file));

        const response = await fetch(`http://127.0.0.1:5323/data/${currCaseId}`, {
            method: 'PUT',
            body: data
        });

        if (response.ok) {
            console.log('Files uploaded successfully');
        } else {
            console.error('Error uploading files');
        }

        closeForm();
    }


</script>
{#if isOpen}
  <div class="backdrop"></div>
  <div class="upload-form">
    <!-- <p>Case id {currCaseId}</p> -->
    <p>Upload File in {title}</p>
    <input type="file" multiple on:change={handleFileChange} />
    <button on:click={handleUpload}>Upload</button>
    <button on:click={closeForm}>Cancel</button>
  </div>
{/if}

<style>
  .backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(194, 192, 192, 0);
    backdrop-filter: blur(5px);
    z-index: 9998;
  }

  .upload-form {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 1em;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    z-index: 9999;
  }
</style>