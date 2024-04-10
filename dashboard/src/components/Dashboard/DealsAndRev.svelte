<script>
  import { onMount } from 'svelte';
  import Chart from 'chart.js/auto';

  const NUMBER_SALES = [2,6,5,8,9,1,6,5,8,9,1,6,5,8,9,1,6,5,8,9,1,6,5,8,9,1,6,5,8,9,1,6,5,8,9,1];
  const NUMBER_REVENUE = [200, 250, 500, 450, 300, 250, 500, 450, 300, 250, 500, 450, 300, 250, 500, 450, 300];
  const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

  const maxLength = Math.max(NUMBER_REVENUE.length, NUMBER_SALES.length);

  // Dynamically generate labels by looping through the length of data arrays
  const labels = Array.from({ length: maxLength }, (_, index) => months[index % 12]);

  const data = {
    labels: labels,
    datasets: [
      {
        label: 'Sales',
        data: NUMBER_SALES,
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
        yAxisID: 'y-axis-1'
      },
      {
        label: 'Revenue',
        data: NUMBER_REVENUE,
        borderColor: 'rgb(54, 162, 235)',
        backgroundColor: 'rgba(54, 162, 235, 0.5)',
        yAxisID: 'y-axis-2'
      }
    ]
  };

  let chart;

  onMount(() => {
    const ctx = document.getElementById('myChart').getContext('2d');
    chart = new Chart(ctx, {
      type: 'line',
      data: data,
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
            labels:{
              color:'#fff'
            }
          },
          title: {
            display: true,
            text: 'Deals and Revenue',
            color: '#fff'
          }
        },
        scales: {
          yAxes: [
            {
              type: 'linear',
              display: true,
              position: 'left',
              id: 'y-axis-1',
              ticks: {
                stepSize: 2,
                beginAtZero: true,
                font: {
                  color: '#fff'
                }
              }
            },
            {
              type: 'linear',
              display: true,
              position: 'right',
              id: 'y-axis-2',
              ticks: {
                callback: function(value, index, values) {
                  return '$' + value;
                },
                stepSize: 200,
                beginAtZero: true,
                font: {
                  color:'#fff'
                }
              },
              grid: {
                drawOnChartArea: false
              }
            }
          ],
          xAxes: [{
            ticks: {
              font: {
                color: '#fff'
              }
            }
          }]
        },
        plugins: {
          tooltip: {
            callbacks: {
              labelColor: function(context) {
                return {
                  borderColor: 'white',
                  backgroundColor: 'white'
                };
              }
            }
          },
          legend: {
            labels: {
              color: 'white'
            }
          },
          title: {
            color: 'white'
          }
        }
      }
    });
  });
</script>

<style>
  canvas {
    width: 100%;
    height: 400px; 
  }
</style>

<canvas id="myChart"></canvas>
