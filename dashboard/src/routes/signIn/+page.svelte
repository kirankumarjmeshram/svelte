<script>
  import { goto } from "$app/navigation";

  let username = "";
  let password = "";
  let errorMessage = "";

  const signIn = async () => {
  try {
    const response = await fetch("http://127.0.0.1:5124/login", {
      method: "POST",
      headers: { 
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });
    const data = await response.json();
    if (response.ok) {
      // Set the JWT token in localStorage
      localStorage.setItem("token", data.access_token);
      goto("/caseInfo");
    } else {
      errorMessage = data.message || "An error occurred while signing in.";
    }
  } catch (error) {
    errorMessage = "An error occurred while signing in.";
  }
};
</script>

<form on:submit|preventDefault={signIn}>
  <input bind:value={username} placeholder="Username" required />
  <input
    bind:value={password}
    type="password"
    placeholder="Password"
    required
  />
  <button type="submit">Sign In</button>
  {#if errorMessage}
    <p>{errorMessage}</p>
  {/if}
</form>
