<script>
  import BasicStacts from './Dashboard/BasicStacts.svelte';
  import DealsAndRev from './Dashboard/DealsAndRev.svelte';
  import CampaignPerfo from './Dashboard/CampaignPerfo.svelte';
  import TopRevCh from './Dashboard/TopRevCh.svelte';
</script>

<div class="dashboard">
  <div class="header">
    <h1>Dashboard</h1>
    <input type="text" placeholder="Search..." class="search-bar" />
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
  .dashboard {
    display: flex;
    flex-direction: column;
    width: 85%;
    padding: 1rem;
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
  }


  .basicStacts {
    grid-column: span 4; /* Width 50% */
    grid-row: span 4;    /* Height 40% */
    height: 40%;
    width: 50%;
    border: 2px solid red; /* Red border */
  }

  .DealsAndRev {
    grid-column: span 4; /* Width 50% */
    grid-row: span 4;    /* Height 40% */
    height: 40%;
    width: 50%;
    border: 2px solid red; /* Red border */
  }

  .CampaignPerfo {
    grid-column: span 4; /* Width 60% */
    grid-row: span 5;    /* Height 50% */
    height: 50%;
    width: 60%;
    border: 2px solid red; /* Red border */
  }

  .TopRevCh {
    grid-column: span 4; /* Width 40% */
    grid-row: span 3;    /* Height 50% */
    height: 50%;
    width: 40%;
    border: 2px solid red; /* Red border */
  }
</style>
