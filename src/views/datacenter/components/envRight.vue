<template>
  <div class="content">
    <div>
      <dv-border-box-8 :reverse="true">
        <div class="head">
          <div class="head_content">
            <h2>平均传输时长</h2>
            <h2>02:45</h2>
          </div>
          <div class="head_uint">
            <h3>单位 分钟:秒</h3>
          </div>
          <div class="head_content">
            <h2>评价处理时长</h2>
            <h2>00:02</h2>
          </div>
        </div>
      </dv-border-box-8>
    </div>

    <div class="body">
      <dv-border-box-6 style="padding: 10px">
        <div class="body_table1">
          <table>
          <thead>
          <tr>
            <th>设备</th>
            <th>编号</th>
            <th>类型</th>
            <th>大小</th>
          </tr>
          </thead>
          <tbody>
          <tr>
            <td>水底摄像头</td>
            <td>video-1</td>
            <td>H.264</td>
            <td>4Mb</td>
          </tr>
          <tr>
            <td>水底摄像头</td>
            <td>video-2</td>
            <td>4CIF</td>
            <td>128kb</td>
          </tr>
          <tr>
            <td>水面摄像头</td>
            <td>video-3</td>
            <td>H.264</td>
            <td>16Mb</td>
          </tr>
          <tr>
            <td>云台</td>
            <td>holder-1</td>
            <td>4CIF</td>
            <td>4Mb</td>
          </tr>
          <tr>
            <td>声纳</td>
            <td>sensor-1</td>
            <td>CSV</td>
            <td>512kb</td>
          </tr>
          <tr>
            <td>传感器</td>
            <td>sensor-2</td>
            <td>4CIF</td>
            <td>64kb</td>
          </tr>
          </tbody>
          </table>
        </div>
      </dv-border-box-6>
      <dv-border-box-6 style="padding: 10px">
        <div class="database-info">
          <div class="info-row">
            <h2>服务信息</h2>
          </div>
          <div class="info-row">
            <p>数据库: MySQL, HBase</p>
          </div>
          <div class="info-row">
            <p>查询次数: 567890</p>
          </div>
          <div class="info-row">
            <p>成功次数: 567890</p>
          </div>
          <div class="info-row">
            <p>累计查询时间: 573.9s</p>
          </div>
          <div class="info-row">
            <p>单次查询时间: 0.001s</p>
          </div>
          <div class="info-title">
            <span>访问数据服务系统</span>
          </div>
        </div>
      </dv-border-box-6>
    </div>
  </div>
</template>

<script>
export default {
  components: {  },
  data() {
    return {
      options1: {
        legend: {
          top: "bottom",
        },
        toolbox: {
          show: true,
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        series: [
          {
            name: "Nightingale Chart",
            type: "pie",
            radius: [50, 180],
            center: ["50%", "50%"],
            roseType: "area",
            itemStyle: {
              borderRadius: 8,
            },
            data: [
              { value: 15, name: "SO2" },
              { value: 50, name: "PM2.5" },
              { value: 80, name: "PM10" },
              { value: 60, name: "NO2" },
              { value: 106, name: "O3" },
              { value: 90, name: "CO" },
            ],
          },
        ],
      },
      options2: {
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: ["PM2.5", "PM10", "SO2", "NO2", "O3"],
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
          data: ["1月", "3月", "5月", "7月", "9月", "11月"],
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            name: "PM2.5",
            type: "line",
            data: [41, 60, 43, 46, 70, 50],
            smooth: true,
          },
          {
            name: "PM10",
            type: "line",
            data: [71, 78, 90, 70, 76, 80],
            smooth: true,
          },
          {
            name: "SO2",
            type: "line",
            data: [15, 23, 20, 15, 19, 10],
            smooth: true,
          },
          {
            name: "NO2",
            type: "line",
            data: [103, 90, 60, 70, 40, 35],
            smooth: true,
          },
          {
            name: "O3",
            type: "line",
            data: [60, 70, 85, 105, 120, 80],
            smooth: true,
          },
        ],
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
  padding: 10px;
  height: 80px;
  display: flex;
  margin: 10px;
  justify-content: space-around;
}
.head_content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
.head_uint {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  align-self: flex-end;
}
.body {
  margin-top: 10px;
}
.body_table1 {
  display: flex;
  height:450px;
}
.table-container {
  width: 100%;
  height: 100%;
  overflow: auto;
}
.database-info {
  height: 320px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.database-info p::before {
  content: "\2022";
  margin-right: 10px;
}
.info-row {
  display: flex;
  align-items: center;
  height: 30px;
  margin-top: 10px;
}
.info-title {
  font-size: 24px;
  margin-top: 30px;
}
table {
  width: 100%;
  border-collapse: collapse;
  text-align: center;
  margin-top: 10px;
}
</style>
