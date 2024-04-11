<script>
	import { page } from '$app/stores';
  let visitors = 12345;
  let contacts = 6789;
  let deals = 4321;
  let revenue = 987654;
  let visitorsChange = 10;
  let contactsChange = 5;
  let dealsChange = 15;
  let revenueChange = 20;
</script>

<div class="dashboard">
  <div class="kpi">
    <p>Visitors</p>
    <h4>{visitors}</h4>
    <span class='change'>
      +{visitorsChange}%
    </span>
  </div>

  <div class="kpi">
    <p>Contacts</p>
    <h4>{contacts}</h4>
    <span class='change'>
      +{contactsChange}%
    </span>
  </div>

  <div class="kpi">
    <p>Attributable Deals</p>
    <h4>{deals}</h4>
    <span class='change'>
      +{dealsChange}%
    </span>
  </div>

  <div class="kpi">
    <p>Revenue</p>
    <h4>${revenue.toLocaleString()}</h4>
    <span class='change'>
      +{revenueChange}%
    </span>
  </div>
</div>

<style>
  .dashboard {
    padding: 10px;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    background-color: #0a1515;
    margin-bottom: 20px;
  }

  .kpi {
    padding: 12%;
    border: 1px solid #1a2b2b;
  }

  .change{
    background-color: rgb(229, 255, 172);
    border-radius: 10px;
    padding: 2px;
    color: black;
  }

  .kpi:hover{
    background-color: rgb(166, 245, 211);
    transform: scale(1.1); 
    box-shadow: 0 0 20px rgba(242, 236, 236, 0.3); 
    border-radius: 10px;
    color: black;
  }
</style>
