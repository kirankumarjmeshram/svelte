<script>
  import { createEventDispatcher } from 'svelte';

  // Create an event dispatcher
  const dispatch = createEventDispatcher();

  // Emit the selected component name
  function selectComponent(component) {
    event.preventDefault();
    dispatch('selectComponent', component);
  }
</script>
  
<div class="sidebar">
  <h2>UNIFYDATA</h2>
  <ul>
    <li class="sidebar_el"><a on:click={selectComponent.bind(this, 'Dashboard')}>Dashboard</a></li>
    <li class="sidebar_el"><a on:click={selectComponent.bind(this, 'RevenueAnalytics')}>Revenue Analytics</a></li>
    <li class="sidebar_el"><a on:click={selectComponent.bind(this, 'Journeys')}>Journeys</a></li>
    <li class="sidebar_el"><a on:click={selectComponent.bind(this, 'Performance')}>Performance</a></li>
    <li class="sidebar_el"><a on:click={selectComponent.bind(this, 'DataPlatform')}>Data Platform</a></li>
    <hr class="divider">
    <li class="sidebar_el"><a on:click={selectComponent.bind(this, 'Settings')}>Settings</a></li>
    <li class="sidebar_el"><a on:click={selectComponent.bind(this, 'Help')}>Help</a></li>
    <hr class="divider2">
    <li class="sidebar_el"><a on:click={selectComponent.bind(this, 'Profile')}>Profile</a></li>
  </ul>
</div>

<style>
  .sidebar {
    width: 15%;
    background-color: #333;
    color: #fff;
    padding: 1rem;
    height: 100vh; 
    display: flex; 
    flex-direction: column; 
  }

  .sidebar_el {
    padding: 10%;
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

  a {
    text-decoration: none;
    color: #fff;
    font-weight: bold;
  }

  a:hover {
    color: #ffcc00;
  }
</style>
