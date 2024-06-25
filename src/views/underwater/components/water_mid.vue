<template>
  <div class="content">
    <!-- <heat-map-echarts height="580px" width="680px" /> -->
    <div class="center_contetn">
        <div class="col_text_content">
          <div class="air"  style="padding: 30px">
            <h1>鱼类信息</h1>
            <div>
              <p>鱼种数量：50+</p>
              <p>鱼苗：500尾</p>
              <p>生长：600尾</p>
            </div>
          </div>
        </div>

        <div class="col_text_content">
          <div class="air"  style="padding: 30px">
            <h1>设备信息</h1>
            <div>
              <p>镜头：5+</p>
              <p>声纳：2</p>
              <p>云台：1</p>
            </div>
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
      max: 2000,
      splitNumber: 8,
      axisLine: {
        lineStyle: {
          width: 6,
          color: [
            [0.25, "#FF6E76"],
            [0.5, "#FDDD60"],
            [0.75, "#58D9F9"],
            [1, "#7CFFB2"]
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
          if (value === 500) {
            return '500w';
          } else if (value === 1000) {
            return '1000w';
          } else if (value === 1500) {
            return '1500w';
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
          return Math.round(value * 10000) + '';
        },
        color: 'inherit'
      },
      data: [
        {
          value: 1560,
          name: '保障鱼群'
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
