<template>
  <div class="content">
    <div>
      <dv-border-box-8 :reverse="true" style="padding: 10px">
        <div class="grade">
          <h2>海洋牧场环境感知得分</h2>
          <Echart :options="options1" height="350px" />
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
          <h2>水温过高</h2>
        </div>
      </div>
    </dv-border-box-8>
    </div>
    <div class="body">
      <dv-border-box-6  style="padding: 10px">
        <Echart :options="options2" height="380px"
      /></dv-border-box-6>
    </div>
  </div>
</template>

<script>
import Echart from "@/common/echart/index.vue";
export default {
  components: { Echart },
  data() {
    return {
      options1: {
        series: [
          {
            type: 'gauge',
            startAngle: 180,
            endAngle: 0,
            center: ['50%', '75%'],
            radius: '90%',
            min: 0,
            max: 1,
            splitNumber: 8,
            axisLine: {
              lineStyle: {
                width: 6,
                color: [
                  [0.25, '#FF6E76'],
                  [0.5, '#FDDD60'],
                  [0.75, '#58D9F9'],
                  [1, '#7CFFB2']
                ]
              }
            },
            pointer: {
              icon: 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
              length: '12%',
              width: 20,
              offsetCenter: [0, '-60%'],
              itemStyle: {
                color: 'auto'
              }
            },
            axisTick: {
              length: 12,
              lineStyle: {
                color: 'auto',
                width: 2
              }
            },
            splitLine: {
              length: 20,
              lineStyle: {
                color: 'auto',
                width: 5
              }
            },
            axisLabel: {
              color: '#464646',
              fontSize: 20,
              distance: -60,
              rotate: 'tangential',
              formatter: function (value) {
                if (value === 0.875) {
                  return '舒适';
                } else if (value === 0.625) {
                  return '正常';
                } else if (value === 0.375) {
                  return '隐患';
                } else if (value === 0.125) {
                  return '危险';
                }
                return '';
              }
            },
            title: {
              offsetCenter: [0, '-10%'],
              fontSize: 20
            },
            detail: {
              fontSize: 30,
              offsetCenter: [0, '-35%'],
              valueAnimation: true,
              formatter: function (value) {
                return Math.round(value * 100) + '';
              },
              color: 'inherit'
            },
            data: [
              {
                value: 0.7,
                name: '评估得分'
              }
            ]
          }
        ],
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
  height:80px;
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
}
.body {
  margin-top: 10px;
}
h2 {
  text-align: center;
}
</style>
