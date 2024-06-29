<template>
  <div class="fish-growth-prediction">
    <h2>鱼类生长情况预测</h2>
    <div class="container">
      <div class="input-container">
        <div class="input-form">
          <label for="age">年龄 (月):</label>
          <input type="number" id="age" v-model="age" />
          
          <label for="initialLength">初始体长 (cm):</label>
          <input type="number" id="initialLength" v-model="initialLength" />
          
          <label for="initialWeight">初始体重 (g):</label>
          <input type="number" id="initialWeight" v-model="initialWeight" />
          
          <button @click="predictGrowth">预测</button>
        </div>
        <div v-if="nextMonthPrediction" class="prediction-result">
          <h3>预测结果</h3>
          <p>下个月的体长: {{ nextMonthPrediction.length }} cm</p>
          <p>下个月的体重: {{ nextMonthPrediction.weight }} g</p>
          <p>成熟后的体长: {{ maturePrediction.length }} cm</p>
          <p>成熟后的体重: {{ maturePrediction.weight }} g</p>
        </div>
      </div>
      <div class="chart-container">
        <div v-if="chartOptions" class="chart">
          <echart :options="chartOptions" height="400px" />
        </div>
        <div v-if="chartOptions2" class="chart">
          <echart :options="chartOptions2" height="400px" />
        </div>
      </div>
    </div>
  </div>
</template>


  
  
  
  
  
  
  
  

<script>
import Echart from "@/common/echart/index.vue";

export default {
  components: { Echart },
  data() {
    return {
      age: 0,
      initialLength: 0,
      initialWeight: 0,
      chartOptions: null,
      chartOptions2: null,
      nextMonthPrediction: null,
      maturePrediction: null
    };
  },
  mounted() {
    this.setChartOptions();
    this.setChartOptions2();
  },
  methods: {
    setChartOptions() {
      // 体长数据集
      const data1 = [
        ["2024-06-05", 10], ["2024-06-06", 12], ["2024-06-07", 15], ["2024-06-08", 18],
        ["2024-06-09", 20], ["2024-06-10", 22], ["2024-06-11", 25], ["2024-06-12", 28],
        ["2024-06-13", 30], ["2024-06-14", 33], ["2024-06-15", 35], ["2024-06-16", 38],
        ["2024-06-17", 40], ["2024-06-18", 42], ["2024-06-19", 45], ["2024-06-20", 48],
        ["2024-06-21", 50], ["2024-06-22", 52], ["2024-06-23", 55], ["2024-06-24", 58],
        ["2024-06-25", 60], ["2024-06-26", 62], ["2024-06-27", 65], ["2024-06-28", 68],
        ["2024-06-29", 70], ["2024-06-30", 72], ["2024-07-01", 75], ["2024-07-02", 78],
        ["2024-07-03", 80], ["2024-07-04", 82], ["2024-07-05", 85], ["2024-07-06", 88],
        ["2024-07-07", 90], ["2024-07-08", 92], ["2024-07-09", 95], ["2024-07-10", 98],
        ["2024-07-11", 100], ["2024-07-12", 102], ["2024-07-13", 105], ["2024-07-14", 108],
        ["2024-07-15", 110], ["2024-07-16", 112], ["2024-07-17", 115], ["2024-07-18", 118],
        ["2024-07-19", 120], ["2024-07-20", 122], ["2024-07-21", 125], ["2024-07-22", 125],
        ["2024-07-23", 125], ["2024-07-24", 125]
      ];
    
      const dateList1 = data1.map(item => item[0]);
      const valueList1 = data1.map(item => item[1]);
    
      this.chartOptions = {
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            min: 0,
            max: 140
          }
        ],
        title: {
          left: 'center',
          text: '鱼的体长变化'
        },
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          data: dateList1
        },
        yAxis: {},
        series: [
          {
            type: 'line',
            showSymbol: false,
            data: valueList1
          }
        ]
      };
    },
    setChartOptions2() {
      // 体重数据集
      const data2 = [
        ["2024-06-05", 100], ["2024-06-06", 110], ["2024-06-07", 120], ["2024-06-08", 130],
        ["2024-06-09", 140], ["2024-06-10", 150], ["2024-06-11", 160], ["2024-06-12", 170],
        ["2024-06-13", 180], ["2024-06-14", 190], ["2024-06-15", 200], ["2024-06-16", 210],
        ["2024-06-17", 220], ["2024-06-18", 230], ["2024-06-19", 240], ["2024-06-20", 250],
        ["2024-06-21", 260], ["2024-06-22", 270], ["2024-06-23", 280], ["2024-06-24", 290],
        ["2024-06-25", 300], ["2024-06-26", 310], ["2024-06-27", 320], ["2024-06-28", 330],
        ["2024-06-29", 340], ["2024-06-30", 350], ["2024-07-01", 360], ["2024-07-02", 370],
        ["2024-07-03", 380], ["2024-07-04", 390], ["2024-07-05", 400], ["2024-07-06", 410],
        ["2024-07-07", 420], ["2024-07-08", 430], ["2024-07-09", 440], ["2024-07-10", 450],
        ["2024-07-11", 460], ["2024-07-12", 470], ["2024-07-13", 480], ["2024-07-14", 490],
        ["2024-07-15", 500], ["2024-07-16", 501], ["2024-07-17", 507], ["2024-07-18", 509],
        ["2024-07-19", 520], ["2024-07-20", 530], ["2024-07-21", 550], ["2024-07-22", 550],
        ["2024-07-23", 550], ["2024-07-24", 550]
      ];
    
      const dateList2 = data2.map(item => item[0]);
      const valueList2 = data2.map(item => item[1]);
    
      this.chartOptions2 = {
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            min: 0,
            max: 600
          }
        ],
        title: {
          left: 'center',
          text: '鱼的体重变化'
        },
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          data: dateList2
        },
        yAxis: {},
        series: [
          {
            type: 'line',
            showSymbol: false,
            data: valueList2
          }
        ]
      };
    },
    predictGrowth() {
      const nextMonthGrowthRate = 0.05; // 假设每月增长5%
      const matureGrowthRate = 0.6; // 假设成熟后的增长为初始值的60%
      
      const nextMonthLength = (this.initialLength * (1 + nextMonthGrowthRate)).toFixed(2);
      const nextMonthWeight = (this.initialWeight * (1 + nextMonthGrowthRate)).toFixed(2);
      
      const matureLength = (this.initialLength * (1 + matureGrowthRate)).toFixed(2);
      const matureWeight = (this.initialWeight * (1 + matureGrowthRate)).toFixed(2);
      
      this.nextMonthPrediction = {
        length: nextMonthLength,
        weight: nextMonthWeight
      };
      
      this.maturePrediction = {
        length: matureLength,
        weight: matureWeight
      };
      
      this.setChartOptions2();
    }
  }
};
</script>


  

  

  


  
<style scoped>
.fish-growth-prediction {
  padding: 20px;
}

.container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.input-container {
  flex: 0 0 30%; /* 占30%宽度 */
  padding-right: 20px;
}

.chart-container {
  flex: 0 0 70%; /* 占70%宽度 */
  display: flex;
  flex-direction: column;
}

.chart {
  margin-bottom: 20px;
}

.input-form {
  display: flex;
  flex-direction: column;
  max-width: 100%;
  font-size: 1.2rem; /* 调整字体大小 */
}

.input-form label {
  margin: 10px 0;
}

.input-form input {
  margin: 5px 0 20px;
  padding: 10px;
  font-size: 1.2rem; /* 调整输入框字体大小 */
}

.input-form button {
  padding: 15px;
  font-size: 1.2rem; /* 调整按钮字体大小 */
  cursor: pointer;
}

h2 {
  font-size: 2rem; /* 调整标题字体大小 */
  margin-bottom: 20px;
}

.prediction-result {
  margin-top: 20px;
  font-size: 1.2rem;
}

.prediction-result h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.prediction-result p {
  margin: 5px 0;
}
</style>
