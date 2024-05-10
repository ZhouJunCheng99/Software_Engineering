<template>
  <div class="content">
    <!-- <heat-map-echarts height="580px" width="680px" /> -->
    <div class="center_contetn">
        <div class="col_text_content">
          <div class="air"  style="padding: 30px">
            <h1>设备信息</h1>
          </div>
          <div class="air"  style="padding: 30px">
            <h1>设备信息</h1>
          </div>
        </div>
        <!-- <Echart :options="options1" height="500px" width="500px"/> -->
        <!-- <div class="col_text_content">
            <dv-border-box-12 style="padding: 30px">
            <div class="air">
                <h1>设备信息</h1>
                <h1>设备信息</h1>
            </div>
            </dv-border-box-12>        
            <dv-border-box-12 style="padding: 30px">
            <div class="air">
                <h1>设备信息</h1>
                <h1>设备信息</h1>
            </div>
            </dv-border-box-12>        -->
        <!-- </div> -->
        <div class="col_text_content">
          <div class="air"  style="padding: 30px">
            <h1>设备信息</h1>
          </div>
          <div class="air"  style="padding: 30px">
            <h1>设备信息</h1>
          </div>
        </div>
    </div>
    <Echart :options="options1" height="400px" width="500px"/>
    <div>
      <dv-border-box-7>
        <h2 class="title">鱼类重量</h2>
        <Echart :options="options2" height="350px" width="680px" />
      </dv-border-box-7>
    </div>
  </div>
</template>

<script>
import Echart from "@/common/echart/index.vue";
// import heatMapEcharts from "./echarts/heatMapEcharts.vue";
export default {
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
            return 'Grade A';
          } else if (value === 0.625) {
            return 'Grade B';
          } else if (value === 0.375) {
            return 'Grade C';
          } else if (value === 0.125) {
            return 'Grade D';
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
          name: 'Grade Rating'
        }
        ]
        }
    ]
    },
    options2: {
        xAxis: {
            type: 'category',
            data: ['种类一', '种类二', '种类三', '种类四', '种类五', '种类六', '种类七']
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            type: 'line',
            smooth: true
            }
        ]
    },
    };
  },
  components: {
    Echart,
  },
};
</script>

<style scoped>
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.center_contetn{
  width: 500px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.col_text_content{
  padding: 8px;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  justify-content: center;
}
.title {
  margin-top: 20px;
  margin-bottom: -30px;
}
</style>
