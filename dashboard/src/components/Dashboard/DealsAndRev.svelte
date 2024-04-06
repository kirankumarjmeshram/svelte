<!-- <script>
    import { onMount } from 'svelte';
    import { Chart } from 'chart.js/auto'; // Import Chart.js library
    
    // Define the chart configuration
    const dealsData = [20, 4, 6, 2, 4, 7];
    const revenueData = [2,5,4,7,9,10];
    const labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'];
    const data = {
      labels: labels,
      datasets: [
        {
          label: 'Deals',
          data: dealsData,
          borderColor: 'red',
          backgroundColor: 'rgba(255, 99, 132, 0.5)'
        },
        {
          label: 'Revenue',
          data: revenueData,
          borderColor: 'blue',
          backgroundColor: 'rgba(54, 162, 235, 0.5)'
        }
      ]
    };
    
    // Define chart actions
    const actions = [
      {
        name: 'Randomize',
        handler(chart) {
          // This function can be implemented to randomize the data if needed
        }
      },
      // Define other actions similarly
    ];
  
    // Define chart configuration
    let chart;
    const config = {
      type: 'line',
      data: data,
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: 'Deals and Revenue'
          }
        },
        scales: {
          x: {
            display: true,
            position: 'bottom',
            grid: {
              display: false
            },
            ticks: {
              // Custom ticks for months
              callback: (value, index, values) => value,
            }
          },
          y: {
            display: true,
            position: 'left',
            grid: {
              display: false
            },
            title: {
              display: true,
              text: 'Deals'
            },
            ticks: {
              // Custom ticks for deals
              stepSize: 1,
              min: 0
            }
          },
          y1: {
            display: true,
            position: 'right',
            grid: {
              display: false
            },
            title: {
              display: true,
              text: 'Revenue'
            },
            ticks: {
              // Custom ticks for revenue
              stepSize: 200,
              callback: (value, index, values) => ('$' + value)
            }
          }
        }
      }
    };
  
    // Function to create the chart on component mount
    onMount(() => {
      const ctx = document.getElementById('line-chart');
      chart = new Chart(ctx, config);
    });
  </script>
  
  <style>
    canvas {
      width: 100%;
      height: 400px; /* Adjust height as needed */
    }
  </style>
-->
  <!-- <canvas id="line-chart"></canvas>  -->

  
  <script>
    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto';
  
    const Utils = {
      months: ({ count }) => {
        const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
        return months.slice(0, count);
      },
      numbers: ({ count, min, max }) => {
        const result = [];
        for (let i = 0; i < count; i++) {
          result.push(Math.floor(Math.random() * (max - min + 1)) + min);
        }
        return result;
      },
      transparentize: (color, opacity) => {
        const alpha = Math.round(opacity * 255);
        return `${color}${alpha.toString(16).toUpperCase()}`;
      },
    };
  
    const DATA_COUNT = 7;
    const NUMBER_CFG = { count: DATA_COUNT, min: -100, max: 100 };
  
    const labels = Utils.months({ count: 7 });
    const data = {
      labels: labels,
      datasets: [
        {
          label: 'Sales',
          data: Utils.numbers(NUMBER_CFG),
          borderColor: 'rgb(255, 99, 132)',
          backgroundColor: 'rgba(255, 99, 132, 0.5)',
          yAxisID: 'y-axis-1'
        },
        {
          label: 'Revenue',
          data: Utils.numbers(NUMBER_CFG),
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
            },
            title: {
              display: true,
              text: 'Deals and Revenue'
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
                  beginAtZero: true
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
                  beginAtZero: true
                },
                grid: {
                  drawOnChartArea: false
                }
              }
            ]
          }
        }
      });
    });
  </script>
  
  <canvas id="myChart" ></canvas>
  