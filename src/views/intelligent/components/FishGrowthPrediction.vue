<template>
    <div class="fish-growth-prediction">
      <h2>鱼类生长情况预测</h2>
      <div class="input-form">
        <label for="age">年龄 (月):</label>
        <input type="number" id="age" v-model="age" />
        
        <label for="initialLength">初始体长 (cm):</label>
        <input type="number" id="initialLength" v-model="initialLength" />
        
        <label for="initialWeight">初始体重 (g):</label>
        <input type="number" id="initialWeight" v-model="initialWeight" />
        
        <button @click="predictGrowth">预测</button>
      </div>
      <div v-if="predictionData">
        <echart :options="chartOptions" height="400px" />
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
      predictionData: null,
      chartOptions: {}
    };
  },
  methods: {
    predictGrowth() {
      // 各种鱼类种类
      const fishSpecies = [
        '大黄鱼',
        '小黄鱼',
        '带鱼',
        '鲳鱼',
        '鲈鱼',
        '鲅鱼',
        '鲷鱼',
        '鲳鱼'
      ];
      
      const datasetWithFilters = [];
      const seriesList = [];

      fishSpecies.forEach(fish => {
        const datasetId = 'dataset_' + fish;
        datasetWithFilters.push({
          id: datasetId,
          fromDatasetId: 'dataset_raw',
          transform: {
            type: 'filter',
            config: {
              and: [
                { dimension: '月份', gte: 1 },
                { dimension: '鱼类', '=': fish }
              ]
            }
          }
        });
        seriesList.push({
          type: 'line',
          datasetId: datasetId,
          showSymbol: false,
          name: fish,
          endLabel: {
            show: true,
            formatter: function (params) {
              return params.value[3] + ': ' + params.value[0];
            }
          },
          labelLayout: {
            moveOverlap: 'shiftY'
          },
          emphasis: {
            focus: 'series'
          },
          encode: {
            x: '月份',
            y: '体长',
            label: ['鱼类', '体长'],
            itemName: '月份',
            tooltip: ['体长']
          }
        });
      });

      const rawData = this.generateRawData(fishSpecies);

      this.chartOptions = {
        animationDuration: 10000,
        dataset: [
          {
            id: 'dataset_raw',
            source: rawData
          },
          ...datasetWithFilters
        ],
        title: {
          text: '不同海洋鱼类的生长预测'
        },
        tooltip: {
          order: 'valueDesc',
          trigger: 'axis'
        },
        xAxis: {
          type: 'category',
          nameLocation: 'middle'
        },
        yAxis: {
          name: '体长 (cm)'
        },
        grid: {
          right: 140
        },
        series: seriesList
      };
    },
    generateRawData(fishSpecies) {
      const rawData = [];
      fishSpecies.forEach(fish => {
        for (let month = 1; month <= 12; month++) {
          rawData.push({
            鱼类: fish,
            月份: month,
            体长: (this.initialLength + month * Math.random() * 2).toFixed(2), // 假设每月增长0-2cm
            体重: (this.initialWeight + month * Math.random() * 20).toFixed(2) // 假设每月增长0-20g
          });
        }
      });
      return rawData;
    }
  }
};
</script>


<style scoped>
.fish-growth-prediction {
  padding: 20px;
}

.input-form {
  display: flex;
  flex-direction: column;
  max-width: 300px;
  margin-bottom: 20px;
}

.input-form label {
  margin: 5px 0;
}

.input-form input {
  margin: 5px 0 10px;
  padding: 5px;
  font-size: 16px;
}

.input-form button {
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}

h2 {
  font-size: 24px;
  margin-bottom: 20px;
}
</style>

  
  