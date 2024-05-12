<template>
    <div class="situation-chart">
      <echart :options="situationChartOptions" height="400px" />
    </div>
  </template>
  
  <script>
  import Echart from '@/common/echart/index.vue'; // 引入通用组件
  
  export default {
    name: 'Situation',
    components: {
      Echart
    },
    data() {
      const ROOT_PATH = ''; // 有需要再设置 ROOT_PATH，这里先不用
      const weatherIcons = {
        TheErrors: ROOT_PATH + '/data/asset/image/situation/errorimage.jpg',
        Fish: ROOT_PATH + '/data/asset/image/situation/fish.jpg',
        Hardware: ROOT_PATH + '/data/asset/image/situation/hardware.jpg'
      };
      const seriesLabel = {
        show: true
      };
      return {
        situationChartOptions: {
          title: {
            text: '海洋牧场状态'
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            }
          },
          legend: {
            data: ['区域 A', '区域 B', '区域 C']
          },
          grid: {
            left: 100
          },
          toolbox: {
            show: true,
            feature: {
              saveAsImage: {}
            }
          },
          xAxis: {
            type: 'value',
            name: 'Days',
            axisLabel: {
              formatter: '{value}'
            }
          },
          yAxis: {
            type: 'category',
            inverse: true,
            data: ['TheErrors', 'Fish', 'Hardware'],
            axisLabel: {
              formatter: function (value) {
                return '{' + value + '| }\n{value|' + value + '}';
              },
              margin: 20,
              rich: {
                value: {
                  lineHeight: 30,
                  align: 'center'
                },
                TheErrors: {
                  height: 40,
                  align: 'center',
                  backgroundColor: {
                    image: weatherIcons.TheErrors
                  }
                },
                Fish: {
                  height: 40,
                  align: 'center',
                  backgroundColor: {
                    image: weatherIcons.Fish
                  }
                },
                Hardware: {
                  height: 40,
                  align: 'center',
                  backgroundColor: {
                    image: weatherIcons.Hardware
                  }
                }
              }
            }
          },
          series: [
            {
              name: '区域 A',
              type: 'bar',
              data: [165, 170, 30],
              label: seriesLabel,
              markPoint: {
                symbolSize: 1,
                symbolOffset: [0, '50%'],
                label: {
                  formatter: '{a|{a}\n}{b|{b} }{c|{c}}',
                  backgroundColor: 'rgb(242,242,242)',
                  borderColor: '#aaa',
                  borderWidth: 1,
                  borderRadius: 4,
                  padding: [4, 10],
                  lineHeight: 26,
                  position: 'right',
                  distance: 20,
                  rich: {
                    a: {
                      align: 'center',
                      color: '#fff',
                      fontSize: 18,
                      textShadowBlur: 2,
                      textShadowColor: '#000',
                      textShadowOffsetX: 0,
                      textShadowOffsetY: 1,
                      textBorderColor: '#333',
                      textBorderWidth: 2
                    },
                    b: {
                      color: '#333'
                    },
                    c: {
                      color: '#ff8811',
                      textBorderColor: '#000',
                      textBorderWidth: 1,
                      fontSize: 22
                    }
                  }
                },
                data: [
                  { type: 'max', name: '最大值: ' },
                  { type: 'min', name: '最小值: ' }
                ]
              }
            },
            {
              name: '区域 B',
              type: 'bar',
              label: seriesLabel,
              data: [150, 105, 110]
            },
            {
              name: '区域 C',
              type: 'bar',
              label: seriesLabel,
              data: [220, 82, 63]
            }
          ]
        }
      };
    }
  };
  </script>
  
  <style scoped>
  .situation-chart {
    width: 100%;
    height: 400px;
  }
  </style>
  