<script>
  import BasicStacts from "./Dashboard/BasicStacts.svelte";
  import DealsAndRev from "./Dashboard/DealsAndRev.svelte";
  import CampaignPerfo from "./Dashboard/CampaignPerfo.svelte";
  import TopRevCh from "./Dashboard/TopRevCh.svelte";
</script>

<div class="dashboard">
  <div class="header">
    <h1>Dashboard</h1>
    <input type="text" placeholder="&#x1F50D; Search..." class="search-bar" />
  </div>

  <div class="content">
    <div class="basicStacts">
      <BasicStacts />
    </div>
    <div class="DealsAndRev">
      <DealsAndRev />
    </div>
    <div class="CampaignPerfo">
      <CampaignPerfo />
    </div>
    <div class="TopRevCh">
      <TopRevCh />
    </div>
  </div>
</div>

<style>
  html,
  body,
  .dashboard {
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;
    
  }

  .dashboard {
    border-radius: 0px 40px 40px 0px;
    display: flex;
    flex-direction: column;
    width: 85%;
    height: 100%;
    padding: 1rem;
    overflow: hidden; 
    border-radius: 40px 0px 0px 40px
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }

  h1 {
    font-size: 1.5rem;
  }

  .search-bar {
    background-color: #0d1515;
    width: 200px;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  .content {
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    grid-template-rows: repeat(9, 1fr);
    gap: 1rem;
    height: 100%; /* Ensure content takes up full height */
    overflow: hidden; /* Prevent content from overflowing */
  }

  .basicStacts {
    grid-column: span 3;
    grid-row: span 4;
  }

  .DealsAndRev {
    grid-column: span 5;
    grid-row: span 4;
    border: 1px solid rgb(77, 77, 77);
  }

  .CampaignPerfo {
    grid-column: span 5;
    grid-row: span 5;
    border: 1px solid rgb(77, 77, 77);
  }

  .TopRevCh {
    grid-column: span 3;
    grid-row: span 5;
    border: 1px solid rgb(77, 77, 77);
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
