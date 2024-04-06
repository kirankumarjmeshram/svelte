<script>
    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto'; // Import Chart.js library

    // Define chart_colors object
    const chart_colors = {
            direct: '#A1FED4',
            paid : '#009999',
            social: '#0066cc',
            other: '#00ffff',
            // Add more colors as needed
        };

    let chart; // Initialize the chart variable

    // Function to create the chart
    function createChart() {
      const ctx = document.getElementById('doughnutChart');
      chart = new Chart(ctx, config);
    }

    function destroyChart() {
      if (chart) {
        chart.destroy();
      }
    }

    onMount(() => {
      createChart();
      return () => {
        destroyChart();
      };
    });

    const data = {
      labels: ['Direct', 'Paid', 'Social', 'Other'],
      datasets: [
        {
          label: 'Dataset 1',
          data: [110, 100, 120, 60], 
          backgroundColor: Object.values(chart_colors),
        }
      ]
    };

    const config = {
      type: 'doughnut',
      data: data,
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'bottom',
          },
          title: {
            display: true,
            text: 'Top Revenue Channels'
          }
        }
      },
    };
</script>

<!-- HTML structure for the chart with background color -->
<div class='doughnutChart'>
  <canvas id="doughnutChart"></canvas>
</div>

<style>
    /* .doughnutChart {
        background-color: #002300;
    } */
    #doughnutChart {
      width: 100%;
      height: 100%;
    }


</style>
