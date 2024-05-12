<template>
  <div class="content">
    <div>
      <dv-border-box-8 :reverse="true" style="padding: 10px">
        <div class="hardware">
            <h2>硬件1</h2>
            <dv-border-box-12 style="padding: 20px">
            <div class="hardware_info">
                <p>设备信息</p>
                <p>设备信息</p>
                <p>设备信息</p>
                <p>设备信息</p>
            </div>
            </dv-border-box-12>
        </div>
        <div class="hardware">
            <h2>硬件2</h2>
            <dv-border-box-12 style="padding: 20px">
            <div class="hardware_info">
                <p>设备信息</p>
                <p>设备信息</p>
                <p>设备信息</p>
                <p>设备信息</p>
            </div>
            </dv-border-box-12>
        </div>
      </dv-border-box-8>
    </div>

    <div class="body">
      <!-- 衣食住行支出比例 -->
      <dv-border-box-6  style="padding: 10px">
        <Echart :options="options2" height="400px"
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
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: ["收入", "支出"],
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        toolbox: {
          feature: {
            saveAsImage: {},
          },
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: ["2016", "2017", "2018", "2019", "2020", "2021", "2022"],
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            name: "收入",
            type: "line",
            data: [800, 910, 900, 920, 1400, 1500, 1550],
          },
          {
            name: "支出",
            type: "line",
            data: [220, 610, 600, 620, 890, 1000, 1100],
          },
        ],
      },
      options2: {
  title: {
    text: '鱼类统计',
    left: 'center'
  },
  tooltip: {
    trigger: 'item'
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
       radius: ['40%', '70%'],
      data: [
        { value: 32, name: '种类一' },
        { value: 21, name: '种类二' },
        { value: 24, name: '种类三' },
        { value: 10, name: '种类四' },
        { value: 13, name: '种类五' },
        { value: 10, name: '种类六' },
        { value: 15, name: '种类七' },
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
}
    };
  },
};
</script>

<style scoped>
.content {
  width: 30%;
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
.hardware{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: stretch;    
}
.hardware_info{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: stretch;    
}
.body {
  margin-top: 10px;
}
</style>
