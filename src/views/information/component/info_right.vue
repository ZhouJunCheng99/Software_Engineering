<template>
  <div class="column_content">
    <dv-border-box-6 style="padding-top: 20px">
      <h2 class="title">2010-2022年牧场环境质量（温度+PH）</h2>
      <Echart :options="options1" height="500px" width="600px" />
    </dv-border-box-6>
      <div class="device_content">
        <dv-border-box-12 style="padding: 20px">
            <h1>设备状态</h1>
          <div class="air" height="500px" width="600px">
            <h2>设备信息</h2>
            <h2>设备信息</h2>
            <h2>设备信息</h2>
            <h2>设备信息</h2>
          </div>
        </dv-border-box-12>
      </div>
  </div>
</template>

<script>
import Echart from "@/common/echart/index.vue";
export default {
  data() {
    return {
      options1: {
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
            crossStyle: {
              color: "#999",
            },
          },
        },
        toolbox: {
          feature: {
            dataView: { show: true, readOnly: false },
            magicType: { show: true, type: ["line", "bar"] },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        legend: {
          data: ["pH", "水温"],
        },
        xAxis: [
          {
            type: "category",
            data: [
              "2010",
              "2011",
              "2012",
              "2013",
              "2014",
              "2015",
              "2016",
              "2017",
              "2018",
              "2019",
              "2020",
              "2021",
              "2022",
            ],
            axisPointer: {
              type: "shadow",
            },
          },
        ],
        yAxis: [
          {
            type: "value",
            name: "℃",
            min: 2700,
            max: 3300,
            interval: 100,
            axisLabel: {
              formatter: "{value}",
            },
          },
          {
            type: "value",
            name: " ",
            min: 0,
            max: 70,
            interval: 10,
            axisLabel: {
              formatter: "{value}",
            },
          },
        ],
        series: [
          {
            name: "温度",
            type: "bar",
            tooltip: {
              valueFormatter: function (value) {
                return value + " ℃";
              },
            },
            data: [
              2920, 2950, 2970, 3010, 3040, 3070, 3110, 3150, 3160, 3190, 3210,
              3220, 3250,
            ],
          },
          {
            name: "pH",
            type: "line",
            yAxisIndex: 1,
            tooltip: {
              valueFormatter: function (value) {
                return value + " ";
              },
            },
            data: [
              40.21, 59.81, 30.45, 36.15, 32.45, 26.54, 39.94, 33.55, 19.63,
              24.7, 21.09, 3.5, 4.21,
            ],
          },
        ],
      },
    };
  },
  components: {
    Echart,
  },
};
</script>

<style>
.column_content{
  width: 38%;
  display: flex;
  flex-direction: column;
}
.title {
  display: flex;
  justify-content: center;
  margin-bottom: 10px;
}
.device_content{
  height: 40%;
  flex-grow: 1;
  display: flex;
}
</style>
