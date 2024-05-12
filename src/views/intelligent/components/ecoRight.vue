<template>
  <div class="content">
    <div>
      <dv-border-box-8 :reverse="true" style="padding: 10px">
        <div class="evaluate">
          <div class="ai-decision">
              <h1>AI决策</h1>
          </div>
          <div class="recommendations">
            <p>温度:10~20</p>
            <p>光照:20~100</p>
            <p>溶解氧:0.2~0.5</p>
            <p>PH:8~8.7</p>
            <p>盐度:0.01~0.03</p>
          </div>
        </div>
      </dv-border-box-8>
    </div>

    <div class="suggestion">
    <dv-border-box-6 style="padding: 10px">
      <p>提示:</p>
      <p>未来几天可能降雨</p>
      <p>请确保温度、风度正常</p>
      </dv-border-box-6>
    </div>

    <div class="body">
      <div class="body_table1">
        <dv-border-box-6 style="padding: 10px">
          <div class="weather">
            <div class="weather-title">
            <h1>气象数据</h1>
            </div>
            <div class="weather-data">
              <p>温度:10~20</p>
              <p>光照:20~100</p>
              <p>溶解氧:0.2~0.5</p>
              <p>PH:8~8.7</p>
              <p>盐度:0.01~0.03</p>
            </div>
          </div>
        </dv-border-box-6>
      </div>
    </div>
    
    <div>
      <dv-border-box-8 :reverse="true" style="padding: 10px">
        <div class="weather-alarm">
          <div class="weatheralarm-title">
          <h1>海啸警报</h1>
          </div>
          <div class="weatheralarm-data">
          <p>国家海洋局南海预报中心</p>
          <p>2024年5月11日9时11分</p>
          <p>二级警报</p>
          <p>影响南海部分沿海地区</p>
          <p>预计海啸波高度将达到1-3米</p>
          </div>
        </div>
      </dv-border-box-8>
    </div>
  </div>
</template>

<script>
export default {
  components: {  },
  data() {
    return {
      options1: {
        title: {
          text: "重庆市财务开销",
        },
        legend: {
          data: ["预算分配", "实际开销"],
        },
        radar: {
          // shape: 'circle',
          indicator: [
            { name: "管理", max: 6500 },
            { name: "销售", max: 16000 },
            { name: "市场", max: 30000 },
            { name: "研发", max: 38000 },
            { name: "客服", max: 52000 },
            { name: "信息技术", max: 25000 },
          ],
        },
        series: [
          {
            name: "预算分配 vs 实际开销",
            type: "radar",
            data: [
              {
                value: [4200, 3000, 20000, 35000, 50000, 18000],
                name: "实际开销",
              },
              {
                value: [5000, 14000, 28000, 26000, 42000, 21000],
                name: "预算分配",
              },
            ],
          },
        ],
      },
      options2: {
        legend: {},
        tooltip: {},
        dataset: {
          dimensions: ["product", "小麦", "玉米", "高粱"],
          source: [
            { product: "2019", 小麦: 433, 玉米: 858, 高粱: 937 },
            { product: "2020", 小麦: 831, 玉米: 734, 高粱: 551 },
            { product: "2021", 小麦: 864, 玉米: 652, 高粱: 825 },
            { product: "2023", 小麦: 724, 玉米: 539, 高粱: 391 },
          ],
        },
        xAxis: { type: "category" },
        yAxis: {},
        series: [{ type: "bar" }, { type: "bar" }, { type: "bar" }],
      },
    };
  },
};
</script>

<style scoped>
.content {
  width: 15%;
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
.body {
  margin-top: 10px;
}
.body_table1 {
  display: flex;
}
.evaluate {
  height: 200px;
  display: flex;
  flex-direction: column;
}

.ai-decision {
  height: 40px;
  margin-bottom: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.recommendations {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.recommendations p {
  margin: 5px 0;
  font-size: 22px;
}
.suggestion {
  height:160px;
  text-align: left;
}
.suggestion p {
  margin: 5px 0;
  font-size: 22px;
  margin-left: 20px;
  margin-top: 20px;
}
.weather {
  height: 200px;
  display: flex;
  flex-direction: column;
}
.weather-title {
  height: 40px;
  margin-bottom: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.weather-data {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.weather-data p {
  margin: 5px 0;
  font-size: 22px;
}
.weather-alarm {
  height: 220px;
  display: flex;
  flex-direction: column;
}
.weatheralarm-title {
  height: 40px;
  margin-bottom: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.weatheralarm-data {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.weatheralarm-data p {
  margin: 5px 0;
  font-size: 20px;
}
</style>
