<template>
  <div class="content">
    <div>
      <dv-border-box-8 :reverse="true">
        <div class="head">
          <div class="head_content">  
          <h2>鱼类数量</h2>
          <dv-digital-flop :config="config1" style="width:150px;height:50px;" />
          </div>
          <div class="head_content">  
          <h2>鱼类数量</h2>
          <dv-digital-flop :config="config2" style="width:150px;height:50px;" />
          </div>
          <div class="head_content">  
          <h2>鱼类数量</h2>
          <dv-digital-flop :config="config3" style="width:150px;height:50px;" />
          </div>
        </div>
      </dv-border-box-8>
    </div>

    <div class="body">
      <dv-border-box-6
        ><Echart :options="options1" height="350px"
      /></dv-border-box-6>
      <dv-border-box-10>
        <Echart :options="options2" height="400px"/>
      </dv-border-box-10>
    </div>
  </div>
</template>



<script>
import Echart from "@/common/echart/index.vue";
// import * as echarts from "echarts";

function formatter (number) {
  const numbers = number.toString().split('').reverse()
  const segs = []

  while (numbers.length) segs.push(numbers.splice(0, 3).join(''))

  return segs.join(',').split('').reverse().join('')
}

const config1 = {
  number: [123456],
  content: '{nt}个',
  formatter
}

const config2 = {
  number: [3],
  content: '{nt}个',
  formatter
}
const config3 = {
  number: [7],
  content: '{nt}个',
  formatter
}

let base = +new Date(1988, 9, 3);
let oneDay = 24 * 3600 * 1000;
let data = [[base, Math.random() * 300]];
for (let i = 1; i < 20000; i++) {
  let now = new Date((base += oneDay));
  data.push([+now, Math.round((Math.random() - 0.5) * 20 + data[i - 1][1])]);
}

export default {
  components: { Echart },
  data() {
    return {
      config1,
      config2,
      config3,
      options1: {
        color: ["#80FFA5"],
        title: {
          text: "环境得分计算",
        },
        tooltip: {
            formatter: '{a} <br/>{b} : {c}%'
        },
        series: [
            {
            name: 'Pressure',
            type: 'gauge',
            progress: {
                show: true
            },
            detail: {
                valueAnimation: true,
                formatter: '{value}'
            },
            data: [
                {
                value: 50,
                name: 'SCORE'
                }
            ]
            }
        ],
        toolbox: {
          feature: {
            saveAsImage: {},
          },
        },
      },
    options2: {
        tooltip: {
            trigger: 'axis',
            position: function (pt) {
            return [pt[0], '10%'];
            }
        },
        title: {
            left: 'center',
            text: '鱼群个体数量历史曲线'
        },
        toolbox: {
            feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
            }
        },
        xAxis: {
            type: 'time',
            boundaryGap: false
        },
        yAxis: {
            type: 'value',
            name: "条",
            boundaryGap: [0, '100%']
        },
        dataZoom: [
            {
            type: 'inside',
            start: 0,
            end: 20
            },
            {
            start: 0,
            end: 20
            }
        ],
        series: [
            {
            type: 'line',
            smooth: true,
            symbol: 'none',
            areaStyle: {},
            data: data,
            tooltip: {
              valueFormatter: function (value) {
                return value + " 条";
              },
            },
            }
        ]
    },
    };
  },
};
</script>

<style scoped>
.content {
  width: 30%;
}
.head {
  padding: 5px;
  height: 150px;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-around;
}
.head_content {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
.body {
  margin-top: 10px;
  justify-content: space-between;
  align-items: center;
}
</style>
