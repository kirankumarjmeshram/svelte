<script>
  import { createEventDispatcher } from "svelte";

  // Create an event dispatcher
  const dispatch = createEventDispatcher();

  // Emit the selected component name
  function selectComponent(component) {
    event.preventDefault();
    dispatch("selectComponent", component);
  }
</script>

<div class="sidebar">
  <h2>
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="1.2em"
      height="1.2em"
      viewBox="0 0 24 24"
      ><path
        fill="none"
        stroke="white"
        stroke-width="2"
        d="M12 15a3 3 0 1 0 0-6a3 3 0 0 0 0 6Zm3-3c4 3 5 7 5 7m-8 4c6.075 0 11-4.925 11-11S18.075 1 12 1S1 5.925 1 12s4.925 11 11 11Zm0-14c3-5 7-6 7-6m-7 12c-3 4-7 5-7 5m4-8C5 9 4 5 4 5"
      /></svg
    >
    &nbsp; UNIFYDATA
  </h2>
  <ul class="sidebar_main">
    <li class="sidebar_el">
      <a on:click={selectComponent.bind(this, "Dashboard")} class="custom-link">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="1.2em"
          height="1.2em"
          viewBox="0 0 24 24"
          ><path
            fill="white"
            d="M4 13h6a1 1 0 0 0 1-1V4a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1m-1 7a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-4a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1zm10 0a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-7a1 1 0 0 0-1-1h-6a1 1 0 0 0-1 1zm1-10h6a1 1 0 0 0 1-1V4a1 1 0 0 0-1-1h-6a1 1 0 0 0-1 1v5a1 1 0 0 0 1 1"
          /></svg
        >
        &nbsp; Dashboard
      </a>
    </li>
    <li class="sidebar_el">
      <a
        on:click={selectComponent.bind(this, "RevenueAnalytics")}
        class="custom-link"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="1.2em"
          height="1.2em"
          viewBox="0 0 16 16"
          ><path
            fill="currentColor"
            d="M12 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2m-2 11.5v-6a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5m-2.5.5a.5.5 0 0 1-.5-.5v-4a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-.5.5zm-3 0a.5.5 0 0 1-.5-.5v-2a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.5.5z"
          /></svg
        >
        &nbsp; Revenue Analytics</a
      >
    </li>
    <li class="sidebar_el">
      <a on:click={selectComponent.bind(this, "Journeys")} class="custom-link">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="1.2em"
          height="1.2em"
          viewBox="0 0 48 48"
          ><g fill="none" stroke="white" stroke-linecap="round" stroke-width="4"
            ><path
              stroke-linejoin="round"
              d="M24 40C32.2843 40 39 33.2843 39 25C39 16.7157 32.2843 10 24 10C15.7157 10 9 16.7157 9 25C9 33.2843 15.7157 40 24 40Z"
            /><path
              d="M20.0002 11C21.8049 12.0083 23.5002 13.5 23.3581 15.4454C23.2445 17 21.915 17.3469 21.6369 18.4711C21.359 19.5953 22.9674 20.8217 20.2464 22.636C18.4324 23.8455 12.971 26.1447 9 24"
            /><path
              stroke-linejoin="round"
              d="M9.50011 24.5C6.50011 26.3883 2.06824 31.521 4.00056 35C6.5 39.5 16.0004 35.6906 27.0001 27C37.9999 18.3094 42.2291 5.60642 42.2291 5.60642L37.0005 7"
            /><path
              d="M26.0006 40C26.0006 40 26.5003 35 30 32C33.4997 29 38.0007 29 38.0007 29"
            /></g
          ></svg
        >Journeys
      </a>
    </li>
    <li class="sidebar_el">
      <a
        on:click={selectComponent.bind(this, "Performance")}
        class="custom-link"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="1.2em"
          height="1.2em"
          viewBox="0 0 20 20"
          ><path
            fill="white"
            d="M3.76 17.01h12.48A7.991 7.991 0 0 0 18 12c0-4.41-3.58-8-8-8s-8 3.59-8 8c0 1.9.66 3.63 1.76 5.01M9 6c0-.55.45-1 1-1s1 .45 1 1c0 .56-.45 1-1 1s-1-.44-1-1M4 8c0-.55.45-1 1-1s1 .45 1 1c0 .56-.45 1-1 1s-1-.44-1-1m4.52 3.4c.84-.83 6.51-3.5 6.51-3.5s-2.66 5.68-3.49 6.51c-.84.84-2.18.84-3.02 0a2.13 2.13 0 0 1 0-3.01M3 13c0-.55.45-1 1-1s1 .45 1 1c0 .56-.45 1-1 1s-1-.44-1-1m6 0c0-.55.45-1 1-1s1 .45 1 1c0 .56-.45 1-1 1s-1-.44-1-1m6 0c0-.55.45-1 1-1s1 .45 1 1c0 .56-.45 1-1 1s-1-.44-1-1"
          /></svg
        >
        &nbsp; Performance
      </a>
    </li>
    <li class="sidebar_el">
      <a
        on:click={selectComponent.bind(this, "DataPlatform")}
        class="custom-link"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="1.2em"
          height="1.2em"
          viewBox="0 0 16 16"
          ><path
            fill="currentColor"
            d="M4.318 2.687C5.234 2.271 6.536 2 8 2s2.766.27 3.682.687C12.644 3.125 13 3.627 13 4c0 .374-.356.875-1.318 1.313C10.766 5.729 9.464 6 8 6s-2.766-.27-3.682-.687C3.356 4.875 3 4.373 3 4c0-.374.356-.875 1.318-1.313M13 5.698V7c0 .374-.356.875-1.318 1.313C10.766 8.729 9.464 9 8 9s-2.766-.27-3.682-.687C3.356 7.875 3 7.373 3 7V5.698c.271.202.58.378.904.525C4.978 6.711 6.427 7 8 7s3.022-.289 4.096-.777A5 5 0 0 0 13 5.698M14 4c0-1.007-.875-1.755-1.904-2.223C11.022 1.289 9.573 1 8 1s-3.022.289-4.096.777C2.875 2.245 2 2.993 2 4v9c0 1.007.875 1.755 1.904 2.223C4.978 15.71 6.427 16 8 16s3.022-.289 4.096-.777C13.125 14.755 14 14.007 14 13zm-1 4.698V10c0 .374-.356.875-1.318 1.313C10.766 11.729 9.464 12 8 12s-2.766-.27-3.682-.687C3.356 10.875 3 10.373 3 10V8.698c.271.202.58.378.904.525C4.978 9.71 6.427 10 8 10s3.022-.289 4.096-.777A5 5 0 0 0 13 8.698m0 3V13c0 .374-.356.875-1.318 1.313C10.766 14.729 9.464 15 8 15s-2.766-.27-3.682-.687C3.356 13.875 3 13.373 3 13v-1.302c.271.202.58.378.904.525C4.978 12.71 6.427 13 8 13s3.022-.289 4.096-.777c.324-.147.633-.323.904-.525"
          /></svg
        >
        &nbsp; Data Platform</a
      >
    </li>
    <hr class="divider" />
    <li class="sidebar_el">
      <a on:click={selectComponent.bind(this, "Settings")} class="custom-link">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="1.2em"
          height="1.2em"
          viewBox="0 0 24 24"
          ><path
            fill="white"
            d="m12 .845l9.66 5.578v11.154L12 23.155l-9.66-5.578V6.423zm0 2.31L4.34 7.577v8.846L12 20.845l7.66-4.422V7.577zM12 9a3 3 0 1 0 0 6a3 3 0 0 0 0-6m-5 3a5 5 0 1 1 10 0a5 5 0 0 1-10 0"
          /></svg
        >
        &nbsp; Settings</a
      >
    </li>
    <li class="sidebar_el">
      <a on:click={selectComponent.bind(this, "Help")} class="custom-link">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="1.2em"
          height="1.2em"
          viewBox="0 0 24 24"
          ><path
            fill="white"
            d="M20 16V4H8v12zm2 0c0 1.1-.9 2-2 2H8c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h12c1.1 0 2 .9 2 2zm-6 4v2H4c-1.1 0-2-.9-2-2V7h2v13zM14.2 5q-1.35 0-2.1.6c-.5.4-.8 1-.8 1.8h1.9c0-.3.1-.5.3-.7c.2-.1.4-.2.7-.2s.6.1.8.3s.3.4.3.8c0 .3-.1.6-.2.8s-.4.4-.6.6c-.5.3-.9.6-1 .9c-.4.2-.5.6-.5 1.1h2c0-.3 0-.6.1-.7c.1-.2.3-.4.5-.5c.4-.2.8-.5 1.1-.9c.3-.5.5-.9.5-1.4c0-.8-.3-1.4-.8-1.8c-.5-.5-1.3-.7-2.2-.7M13 12v2h2v-2z"
          /></svg
        >
        &nbsp; Help</a
      >
    </li>
    <hr class="divider2" />
    <li class="sidebar_el">
      <a on:click={selectComponent.bind(this, "Profile")} class="custom-link">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="1.2em"
          height="1.2em"
          viewBox="0 0 16 16"
          ><path
            fill="white"
            fill-rule="evenodd"
            d="M8 14.5a6.47 6.47 0 0 0 3.25-.87V11.5A2.25 2.25 0 0 0 9 9.25H7a2.25 2.25 0 0 0-2.25 2.25v2.13A6.47 6.47 0 0 0 8 14.5m4.75-3v.937a6.5 6.5 0 1 0-9.5 0V11.5a3.75 3.75 0 0 1 2.486-3.532a3 3 0 1 1 4.528 0A3.75 3.75 0 0 1 12.75 11.5M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16M9.5 6a1.5 1.5 0 1 1-3 0a1.5 1.5 0 0 1 3 0"
            clip-rule="evenodd"
          /></svg
        >
        &nbsp;Profile</a
      >
    </li>
  </ul>
</div>

<style>
  .sidebar_main {
    padding-top: 2rem;
  }
  .sidebar {
    width: 15%; /* Width of the outer component */
    background-color: #413f3f;
    color: #fff;
    padding: 1rem;
    height: 100vh;
    display: flex;
    flex-direction: column;
  }

  .sidebar_el {
    margin: 5%;
    font-size: large;
  }

  .divider {
    width: 80%;
    border-top: 1px solid white;
    margin: 0 auto;
    margin: 1rem auto 0;
  }

  .divider2 {
    width: 80%;
    border-top: 1px solid white;
    margin: 10rem auto 0;
  }

  ul {
    list-style: none;
    padding: 0;
    margin: 0;
    flex: 1;
  }

  li {
    margin-bottom: 1rem;
  }

  /* Custom styles for the link */
  .custom-link {
    display: block;
    color: #fff;
    padding: 0.5rem 1rem;
    text-decoration: none;
    border-radius: 0.25rem;
  }

  .custom-link:hover,
  .custom-link:focus {
    background-color: rgb(
      180,
      241,
      214
    ); /* Change background color on hover or focus */
    color: #000; /* Change text color to black */
  }
</style>
