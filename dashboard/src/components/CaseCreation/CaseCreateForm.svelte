<script>
  import axios from 'axios';

  let title = ''; 

  async function postData() {
    try {
      const response = await axios.post('http://127.0.0.1:5323/data', { title });

      title = '';
      
      alert('Data posted successfully'); 
    } catch (error) {
      console.error(error);
      alert('Failed to post data'); 
    }
  }
</script>

<div class='container'>
  <h2>Case Title</h2>
  <form on:submit|preventDefault={postData}>
    <label>
      Title:
      <input type="text" bind:value={title} />
    </label>
    <button type="submit">Submit</button>
  </form>
</div>

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
    margin: 1em;
    background-color: green;
    color: white;
    border: none;
    cursor: pointer;
  }
</style>