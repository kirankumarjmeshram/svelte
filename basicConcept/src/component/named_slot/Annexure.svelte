<script>
    import data from './data.json';
  
    const columns = [
      'source_number',
      'destination_number',
      'call_type',
      'date',
      'time',
      'first_cgid',
      'Provider'
    ];
  </script>
  
<div>
    <table>
        <thead>
          <tr>
            {#each columns as column} <th>{column} </th> {/each}
          </tr>
        </thead>
        <tbody>
          {#each data as row}
            <tr>
              <td>{row.source_number}</td>
              <td>{row.destination_number}</td>
              <td>{row.call_type}</td>
              <td>{row.date}</td>
              <td>{row.time}</td>
              <td>{row.first_cgid}</td>
              <td>{row.Provider}</td>
            </tr>
          {/each}
        </tbody>
      </table>
</div>
  
  <style>
    table, th, td {
      border: 1px solid;
      border-collapse: collapse;
      padding: 5px;
    }
  </style>




  