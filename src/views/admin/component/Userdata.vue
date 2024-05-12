<template>
    <div class="userdata-chart">
      <echart :options="userdataChartOptions" height="400px" />
    </div>
  </template>
  
  <script>
  import Echart from '@/common/echart/index.vue'; // 引入通用组件
  
  export default {
    name: 'Userdata',
    components: {
      Echart
    },
    data() {
      return {
        userdataChartOptions: {
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b}: {c} ({d}%)'
          },
          legend: {
            data: [
              'Farmer',
              'Researcher',
              'Economist',
              'Emma',
              'Zhou',
              'Yang',
              'Zhu',
              'Gao',
              'Feng',
              'Others'
            ]
          },
          series: [
            {
              name: 'Access From',
              type: 'pie',
              selectedMode: 'single',
              radius: [0, '30%'],
              label: {
                position: 'inner',
                fontSize: 14
              },
              labelLine: {
                show: false
              },
              data: [
                { value: 1548, name: 'Economist' },
                { value: 775, name: 'Farmer' },
                { value: 679, name: 'Researcher', selected: true }
              ]
            },
            {
              name: 'Access From',
              type: 'pie',
              radius: ['45%', '60%'],
              labelLine: {
                length: 30
              },
              label: {
                formatter:
                  '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                backgroundColor: '#F6F8FC',
                borderColor: '#8C8D8E',
                borderWidth: 1,
                borderRadius: 4,
                rich: {
                  a: {
                    color: '#6E7079',
                    lineHeight: 22,
                    align: 'center'
                  },
                  hr: {
                    borderColor: '#8C8D8E',
                    width: '100%',
                    borderWidth: 1,
                    height: 0
                  },
                  b: {
                    color: '#4C5058',
                    fontSize: 14,
                    fontWeight: 'bold',
                    lineHeight: 33
                  },
                  per: {
                    color: '#fff',
                    backgroundColor: '#4C5058',
                    padding: [3, 4],
                    borderRadius: 4
                  }
                }
              },
              data: [
                { value: 1048, name: 'Zhu' },
                { value: 335, name: 'Farmer' },
                { value: 310, name: 'Emma' },
                { value: 251, name: 'Gao' },
                { value: 234, name: 'Zhou' },
                { value: 147, name: 'Feng' },
                { value: 135, name: 'Yang' },
                { value: 102, name: 'Others' }
              ]
            }
          ]
        }
      };
    }
  };
  </script>
  
  <style scoped>
  .userdata-chart {
    width: 100%;
    height: 400px;
  }
  </style>
  