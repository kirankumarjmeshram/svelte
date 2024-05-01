<!-- SignUp.svelte -->
<script>
    import { goto } from '$app/navigation';
  
    let username = '';
    let password = '';
    let passcode = '';
    let errorMessage = '';
    const signUp = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5124/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password, passcode })
        });
        const data = await response.json();
        if (data.message === 'User registered, contact admin for approval') {
          goto('/signIn'); 
        } else {
          errorMessage = data.message;
        }
      } catch (error) {
        errorMessage = 'An error occurred while registering.';
      }
    };
  </script>
  
  <form on:submit|preventDefault={signUp}>
    <input bind:value={username} placeholder="Username" required />
    <input bind:value={password} type="password" placeholder="Password" required />
    <input bind:value={passcode} placeholder="Passcode" required />
    <button type="submit">Sign Up</button>
    {#if errorMessage}
      <p>{errorMessage}</p>
    {/if}
  </form>
  