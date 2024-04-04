<script>
    let visitors = 12345;
    let contacts = 6789;
    let deals = 4321;
    let revenue = 987654;
  
    let visitorsChange = 10; 
    let contactsChange = -5;
    let dealsChange = 15; 
    let revenueChange = 20; 
  </script>
  
  <style>
    .dashboard {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1rem; 
    }
  
    .kpi {
      padding: 1rem;
      border: 1px solid #ccc;
    }
  </style>
  
  <div class="dashboard">
    <div class="kpi">
      <h2>Visitors</h2>
      <p>{visitors}</p>
      <span>
        +{visitorsChange}%
      </span>
    </div>
  
    <div class="kpi">
      <h2>Contacts</h2>
      <p>{contacts}</p>
      <span>
        +{contactsChange}%
      </span>
    </div>
  
    <div class="kpi">
      <h2>Attributable Deals</h2>
      <p>{deals}</p>
      <span>
        +{dealsChange}%
      </span>
    </div>
  
    <div class="kpi">
      <h2>Revenue</h2>
      <p>${revenue.toLocaleString()}</p>
      <span class={revenueChange > 0 ? 'positive' : 'negative'}>
        {revenueChange > 0 ? '+' : ''}{revenueChange}%
      </span>
    </div>
  </div>
  