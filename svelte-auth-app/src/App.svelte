<script>
  export let name;
  /** IMPORTS */
  import Login from "./Login.svelte";
  import Signup from "./Signup.svelte";
  import Home from "./Home.svelte";
  import PrivateRoute from "./routes/PrivateRoutes.svelte";
  import { Router, Route } from "svelte-navigator";
  /** VARIABLES */
  const sdkoptions = {
	"apiKey": __myapp["env"].API_CLIENT_KEY,
	"appName":__myapp["env"].APP_NAME,
    "apiSecret":__myapp["env"].API_SECRET
  };
//   const endpoint = `${BASE_URL}?apikey=${sdkoptions.apiKey}&apisecret=${sdkoptions.apiSecret}`
</script>

<main>
	<Router>
	  <div>
		<Route path="signup">
		  <Signup {sdkoptions} />
		</Route>
		<Route path="login">
		  <Login {sdkoptions} />
		</Route>
		<Route path="/">
		  <Home />
		</Route>
	  </div>
	</Router>
  </main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
