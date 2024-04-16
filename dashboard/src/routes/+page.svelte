<script>
  import CaseCreation from "./caseInfo/+page.svelte";
  import { onMount } from "svelte";
  import SidebarMenu from "../components/SidebarMenu.svelte";
  import Dashboard from "../components/Dashboard.svelte"
  import RevenueAnalytics from "../components/RevenueAnalytics.svelte";
  import Journeys from "../components/Journeys.svelte";
  import Performance from "../components/Performance.svelte";
  import DataPlatform from "../components/DataPlatform.svelte";
  import Settings from "../components/Settings.svelte";
  import Help from "../components/Help.svelte";
  import Profile from "../components/Profile.svelte";

  let selectedComponent = CaseCreation;

  function selectComponent(component) {
    // console.log(component.detail)
    switch (component.detail) {
      case "Dashboard":
        selectedComponent = Dashboard;
        break;

      case "RevenueAnalytics":
        selectedComponent = RevenueAnalytics;
        break;

      case "Journeys":
        selectedComponent = Journeys;
        break;

      case "Performance":
        selectedComponent = Performance;
        break;

      case "DataPlatform":
        selectedComponent = DataPlatform;
        break;

      case "Settings":
        selectedComponent = Settings;
        break;

      case "Help":
        selectedComponent = Help;
        break;

      case "Profile":
        selectedComponent = Profile;
        break;

      case "CaseCreation":
        selectedComponent = CaseCreation;
        break;

      default:
        selectedComponent = CaseCreation;
    }
  }

  onMount(() => {
    // Your initialization logic here
  });
</script>

<div class="app-container">
  <SidebarMenu on:selectComponent={selectComponent} />

  <div class="main-content">
    <svelte:component this={selectedComponent} />
  </div>
</div>

<style>
  .app-container {
    display: flex;
    height: 100vh;

    /* padding: 2%; */
    /* background-color: #cdfeff; */
  }

  .main-content {
    flex: 1;
    /* padding: 1rem; */
    background-color: #121b1b;
    color: white;
    /* border-radius: 0px 30px 30px 0px; */
  }
</style>
