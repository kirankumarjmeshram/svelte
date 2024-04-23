<!-- SignIn.svelte -->
<script>
    let username = '';
    let password = '';
  
    const signIn = async () => {
      const response = await fetch('http://192.168.108.80:5000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      });
      const data = await response.json();
      if (data.message === 'User login is successful') {
        // Handle successful login
      } else {
        // Handle login error
      }
    };
  </script>
  
  <form on:submit|preventDefault={signIn}>
    <input bind:value={username} placeholder="Username" required />
    <input bind:value={password} type="password" placeholder="Password" required />
    <button type="submit">Sign In</button>
  </form>
  