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
              'Administator',
              'Farmer',
              'Food Buyer',
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
                { value: 12, name: 'Administator' },
                { value: 75, name: 'Farmer' },
                { value: 279, name: 'Food Buyer', selected: true }
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
                { value: 48, name: 'Zhu' },
                { value: 35, name: 'Farmer' },
                { value: 10, name: 'Emma' },
                { value: 51, name: 'Gao' },
                { value: 34, name: 'Zhou' },
                { value: 17, name: 'Feng' },
                { value: 15, name: 'Yang' },
                { value: 12, name: 'Others' }
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
  