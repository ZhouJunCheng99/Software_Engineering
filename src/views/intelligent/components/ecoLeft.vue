<template>
  <div class="content">
    <div>
      <dv-border-box-8 :reverse="true" style="padding: 10px">
        <div class="grade">
          <h2>海洋牧场环境温度感知</h2>
          <Echart :options="options1" ref="myChart" height="350px" />
        </div>
      </dv-border-box-8>
    </div>
    <div>
      <dv-border-box-8 :reverse="true">
        <div class="alarm">
          <div class="top">
            <h1>预警</h1>
          </div>
          <div class="bottom">
            <div class="info">
              <p>当前温度: {{ currentTemperature }}℃</p>
              <p>当前湿度: {{ currentHumidity }}%</p>
              <p>最近警告</p>
              <div class="warnings">
                <ul>
                  <li v-for="warning in warnings" :key="warning.time" class="warning-message">
                    {{ warning.time }} - {{ warning.message }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </dv-border-box-8>
    </div>
    <div class="body">
      <dv-border-box-6 style="padding: 10px">
        <Echart :options="options2" height="380px" class="echart"/>
      </dv-border-box-6>
    </div>
  </div>
</template>





<script>
import Echart from "@/common/echart/index.vue";
import axios from "axios";
export default {
  components: { Echart },
  data() {
    return {
      allWaterData:[],
      index:0,
      options1: {
        series: [
          {
            type: 'gauge',
            center: ['50%', '60%'],
            startAngle: 200,
            endAngle: -20,
            min: 0,
            max: 60,
            splitNumber: 12,
            itemStyle: {
              color: '#FFAB91'
            },
            progress: {
              show: true,
              width: 30
            },
            pointer: {
              show: false
            },
            axisLine: {
              lineStyle: {
                width: 30
              }
            },
            axisTick: {
              distance: -45,
              splitNumber: 5,
              lineStyle: {
                width: 2,
                color: '#999'
              }
            },
            splitLine: {
              distance: -52,
              length: 14,
              lineStyle: {
                width: 3,
                color: '#999'
              }
            },
            axisLabel: {
              distance: -20,
              color: '#999',
              fontSize: 20
            },
            anchor: {
              show: false
            },
            title: {
              show: false
            },
            detail: {
              valueAnimation: true,
              width: '60%',
              lineHeight: 40,
              borderRadius: 8,
              offsetCenter: [0, '-15%'],
              fontSize: 30, // 改小显示温度的字体大小
              fontWeight: 'bolder',
              formatter: '{value} °C',
              color: 'inherit'
            },
            data: [
              {
                value: 20
              }
            ]
          },
          {
            type: 'gauge',
            center: ['50%', '60%'],
            startAngle: 200,
            endAngle: -20,
            min: 0,
            max: 60,
            itemStyle: {
              color: '#FD7347'
            },
            progress: {
              show: true,
              width: 8
            },
            pointer: {
              show: false
            },
            axisLine: {
              show: false
            },
            axisTick: {
              show: false
            },
            splitLine: {
              show: false
            },
            axisLabel: {
              show: false
            },
            detail: {
              show: false
            },
            data: [
              {
                value: 20
              }
            ]
          }
        ]
      },
      options2: {
        title: {
          text: "网衣/鱼群检测",
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            axisTick: {
              alignWithLabel: true
            }
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'Direct',
            type: 'bar',
            barWidth: '60%',
            data: [10, 52, 200, 334, 390, 330, 220]
          }
        ]
      }
    };
  },
  mounted() {
    // this.updateChart();
    // setInterval(this.updateChart, 10000);
  },
  created() {
    this.fetchWaterData();
    this.startDataUpdateInterval();
  },
  methods: {
    async fetchWaterData(){
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/water-data/');
        if (response.data.length > 0) {
          // this.waterData = response.data[0];  // 获取第一条数据
          this.allWaterData = response.data; // 保存所有数据
          this.updateChart(); // 初始化第一次数据
        }
      } catch (error) {
        console.error('Error fetching water data:', error);
      }
    },
    startDataUpdateInterval() {
      setInterval(this.updateChart, 10000);
    },
    updateChart() {
      const random = this.allWaterData[this.index].water_temperature? this.allWaterData[this.index].water_temperature.toFixed(2):'';
      this.index=(this.index+1)%this.allWaterData.length;
      const color = random > 25 ? 'red' : '#FFC0CB'; // 浅粉色
      this.$refs.myChart.chart.setOption({
        series: [
          {
            data: [
              {
                value: random,
                detail: {
                  color: color
                }
              }
            ]
          },
          {
            data: [
              {
                value: random
              }
            ]
          }
        ]
      });
      if (random > 25) {
        alert(`水温过高！已达到 ${random}℃，请尽快处理！`);
      }
    }
  }
};
</script>








<style scoped>
.content {
  width: 23%;
}
.head {
  padding: 10px;
  height: 80px;
  display: flex;
  justify-content: space-around;
}
.head_content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
.grade {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}
.alarm {
  height: 200px; /* 调整高度，适应滚动条 */
  display: flex;
  flex-direction: column;
  margin-top: 10px;
}
.top {
  align-self: flex-start;
}
.bottom {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-grow: 1;
  overflow: hidden; /* 确保内容不溢出 */
}
.info {
  text-align: left;
  font-size: 18px; /* 增加字体大小 */
  line-height: 1.5; /* 增加行高 */
  font-family: Arial, sans-serif; /* 更改字体 */
}
.warnings {
  max-height: 100px; /* 限制警告区域的最大高度，调整为适合的大小 */
  overflow-y: auto; /* 增加垂直滚动条 */
}
.warning-message {
  color: red; /* 设置警告消息的颜色为红色 */
}
h2 {
  text-align: center;
}

.body {
  margin-top: 10px;
  height: 300px; /* 设置高度为自动，以便根据内容调整 */
  overflow-y: auto; /* 增加垂直滚动条，以防内容溢出 */
}
.dv-border-box-6 {
  height: 100%; /* 确保容器高度为100% */
  padding: 10px;
}
.echart {
  height: 100%; /* 确保图表高度为100% */
}

</style>



