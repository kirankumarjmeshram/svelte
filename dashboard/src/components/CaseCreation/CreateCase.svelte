<script>
    import axios from 'axios';
  
    let title = ''; 
  
    async function postData() {
      try {
        const response = await axios.post('http://localhost:5323/post', { title });
  
        title = '';
        
        alert('Data posted successfully'); 
      } catch (error) {
        console.error(error);
        alert('Failed to post data'); 
      }
    }
  </script>
  
  <div>
    <h2>Post Data</h2>
    <form on:submit|preventDefault={postData}>
      <label>
        Title:
        <input type="text" bind:value={title} />
      </label>
      <button type="submit">Submit</button>
    </form>
  </div>
  