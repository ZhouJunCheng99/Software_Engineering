<template>
  <div class="content">
    <div>
      <dv-border-box-8 :reverse="true" style="padding: 10px">
        <div class="evaluate">
          <div class="ai-decision">
              <h1>AI决策</h1>
          </div>
          <div class="recommendations">
            <p>水温:15~25℃</p>
            <p>溶解氧:≥5mg/L</p>
            <p>PH:6.8~8.7</p>
            <p>电导率:500~1000μS/cm</p>
            <p>浊度:0.1~10NTU</p>
            <p>高锰酸钾指数:≤6mg/L</p>
            <p>氨氮:≤1.0mg/L</p>
            <p>总磷:≤0.2mg/L</p>
            <p>总氮:≤10mg/L</p>
          </div>
        </div>
      </dv-border-box-8>
    </div>

<!--    <div class="suggestion">-->
<!--    <dv-border-box-6 style="padding: 10px">-->
<!--      <p>提示:</p>-->
<!--      <p>未来几天可能降雨</p>-->
<!--      <p>请确保温度、风度正常</p>-->
<!--      </dv-border-box-6>-->
<!--    </div>-->

    <div class="body">
      <div class="body_table1">
        <dv-border-box-6 style="padding: 10px">
          <div class="weather">
            <div class="weather-title">
            <h1>气象与水文数据</h1>
            </div>
            <div class="weather-data">
              <p>水温:{{waterData.water_temperature ? waterData.water_temperature.toFixed(1) : 'N/A'}}℃</p>
              <p>溶解氧:{{waterData.dissolved_oxygen ? waterData.dissolved_oxygen.toFixed(2) : 'N/A'}}mg/L</p>
              <p>PH:{{waterData.pH ? waterData.pH.toFixed(2) : 'N/A'}}</p>
              <p>电导率:{{waterData.conductivity ? waterData.conductivity.toFixed(1) : 'N/A'}}μS/cm</p>
              <p>浊度:{{waterData.turbidity ? waterData.turbidity.toFixed(1) : 'N/A'}}NTU</p>
              <p>高锰酸钾指数:{{waterData.permanganate_index ? waterData.permanganate_index.toFixed(2) : 'N/A'}}mg/L</p>
              <p>氨氮:{{waterData.ammonia_nitrogen ? waterData.ammonia_nitrogen.toFixed(3) : 'N/A'}}mg/L</p>
              <p>总磷:{{waterData.total_phosphorus ? waterData.total_phosphorus.toFixed(3) : 'N/A'}}mg/L</p>
              <p>总氮:{{waterData.total_nitrogen ? waterData.total_nitrogen.toFixed(2) : 'N/A'}}mg/L</p>
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
          <p>{{currdate.dateYear}}年{{currdate.dateMonth}}月{{currdate.dateDay-1}}日9时11分</p>
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
import axios from 'axios'
export default {
  components: {  },
  data() {
    return {
      allWaterData: [], // 保存所有水质数据
      dataIndex: 0, // 当前数据索引
      waterData:{
        temperature: '',
        illumination: '',
        dissolved_oxygen: '',
        ph: '',
        salinity: ''
      },
      currdate:{
        dateDay: null,
        dateYear: null,
        dateMonth:null,
      },
    };
  },
  created() {
    this.setCurrentDate();
    this.fetchWaterData();
    this.startDataUpdateInterval();
  },
  methods:{
    async fetchWaterData(){
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/water-data/');
        if (response.data.length > 0) {
          // this.waterData = response.data[0];  // 获取第一条数据
          this.allWaterData = response.data; // 保存所有数据
          this.updateWaterData(); // 初始化第一次数据
        }
      } catch (error) {
        console.error('Error fetching water data:', error);
      }
    },
    setCurrentDate() {
      const today = new Date();
      this.currdate.dateYear = today.getFullYear();
      this.currdate.dateMonth = today.getMonth() + 1;
      this.currdate.dateDay = today.getDate();
    },
    updateWaterData() {
      if (this.allWaterData.length > 0) {
        this.waterData = this.allWaterData[this.dataIndex];
        this.dataIndex = (this.dataIndex + 1) % this.allWaterData.length;
      }
    },
    startDataUpdateInterval() {
      setInterval(this.updateWaterData, 10000); // 每隔10秒更新一次数据
    },
  }
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
  height: 310px;
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
  height: 310px;
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
