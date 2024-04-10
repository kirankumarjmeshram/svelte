<script>
    let selectedCols = ["id", "campaign", "visitors", "contacts", "companies", "leads", "value"];
    let data = [
      { id: 1, campaign: "Campaign A", visitors: 500, contacts: 200, companies: 100, leads: 50, value: "$5000.00" },
      { id: 2, campaign: "Campaign B", visitors: 700, contacts: 250, companies: 120, leads: 70, value: "$7000.00" },
      { id: 3, campaign: "Campaign C", visitors: 800, contacts: 300, companies: 150, leads: 80, value: "$8000.00" },
      { id: 4, campaign: "Campaign D", visitors: 600, contacts: 220, companies: 110, leads: 60, value: "$6000.00" },
      { id: 5, campaign: "Campaign E", visitors: 900, contacts: 350, companies: 180, leads: 90, value: "$9000.00" }
    ];
  
    const COLUMNS = {
      id: {
        key: "id",
        title: "Sr.NO",
        value: v => v.id,
        sortable: true,
      },
      campaign: {
        key: "campaign",
        title: "CAMPAIGN",
        value: v => v.campaign,
        sortable: true,
      },
      visitors: {
        key: "visitors",
        title: "VISITORS",
        value: v => v.visitors,
        sortable: true,
      },
      contacts: {
        key: "contacts",
        title: "CONTACTS",
        value: v => v.contacts,
        sortable: true,
      },
      companies: {
        key: "companies",
        title: "COMPANIES",
        value: v => v.companies,
        sortable: true,
      },
      leads: {
        key: "leads",
        title: "LEADS",
        value: v => v.leads,
        sortable: true,
      },
      value: {
        key: "value",
        title: "VALUE",
        value: v => v.value,
        sortable: true,
      }
    };
  
    $: cols = selectedCols.map(key => COLUMNS[key]);
  </script>
  
  <div class="container">
    <div class="header">
      <h1 class="title">Campaign Performance</h1>
      <div class="channels">
        <span>Channels:</span>
        <select class="dropdown">
          <option>All</option>
          <option>All</option>
          <option>All</option>
        </select>
      </div>
    </div>
    <div class="table-responsive">
      <table class="table">
        <thead>
          <tr>
            {#each cols as col}
              <th class="border-top border-bottom">{col.title}</th>
            {/each}
          </tr>
        </thead>
        <tbody>
          {#each data as row}
            <tr>
              {#each selectedCols as col}
                <td class="border-bottom">{row[col]}</td>
              {/each}
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  </div>
  
  <style>
    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      background-color: #151b21;
    }
  
    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }
  
    .title {
      margin: 0;
    }
  
    .channels {
      display: flex;
      align-items: center;
    }
  
    .channels span {
      margin-right: 10px;
    }
  
    .dropdown {
      width: 150px;
    }
  
    .table {
      width: 100%;
      border-collapse: collapse;
      border-spacing: 0;
    }
  
    .table th,
    .table td {
      padding: 0.75rem;
      text-align: left;
      vertical-align: top;
      border-top: 1px solid #dee2e6;
    }
  
    .table th {
      border-top: none;
    }
  
    .border-top {
      border-top: 1px solid #dee2e6;
    }
  
    .border-bottom {
      border-bottom: 1px solid #dee2e6;
    }
  </style>
  