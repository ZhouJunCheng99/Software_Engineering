<template>
  <div class="content">
    <div>
      <dv-border-box-2 style="padding: 8px">
          <h2>水文气象</h2>
          <dv-capsule-chart
            :config="waterData"
            width="100%"
            :key="chartKey"
          />
      </dv-border-box-2>
    </div>

    <div class="body">
      <dv-border-box-6 style="padding:10px">
        <div class="map-content">
          <baidu-map
            class="map"
            :center="center"
            :zoom="zoom"
            @ready="handler"
            :mapStyle="mapStyle"
            :scroll-wheel-zoom="true"
          >
            <bm-marker
              v-for="(item, index) of markerPoints"
              :position="item"
              :key="index"
            ></bm-marker>
          </baidu-map>
        </div>
      </dv-border-box-6>
    </div>
  </div>
</template>

<script>
import mapStyle from "@/assets/mapStyle.json";
import axios from 'axios'

export default {
  data() {
    return {
      todayData:{
        temperature: '',
        salinity: '',
        dissolved_oxygen: '',
        illumination: '',
        ph: '',
      },
      allWaterData: [],
      center: { lng: 0, lat: 0 },
      zoom: 3,
      mapStyle: {
        styleJson: mapStyle,
      },
      markerPoints: [
        { lng: 110.54455, lat: 20.5201 },
      ],
      waterData: {
        data: [
          {
            name: '电导率(mS/cm)',
            value: 0.987,
          },
          {
            name: '盐度(‰)',
            value: 4,
          },
          {
            name: '溶解氧(mg/L)',
            value: 12.49,
          },
          {
            name: '浊度(NTU)',
            value: 12.5,
          },
          {
            name: 'pH',
            value: 8.33,
          },
          {
            name: '水温(℃)',
            value: 17.5,
          },
        ],
        colors: ['#e062ae', '#fb7293', '#e690d1', '#32c5e9', '#96bfff', '#e062ae'],
        unit: ' ',
        showValue: true
      },
      
      chartKey: 0  // 添加一个用于手动触发重新渲染的 key
    };
  },
  methods: {
    handler({ BMap, map }) {
      console.log(BMap, map);
      this.center.lng = 110.54455;
      this.center.lat = 20.5201;
      this.zoom = 15;
    },
    fetchData() {
      const tdata = this.todayData;
      if (tdata && tdata.length === 6) {
        tdata.forEach((item, index) => {
          // 更新
          this.$set(this.waterData.data, index, {
            name: item.name,
            value: item.value.toFixed(2)  // 保留两位小数
          });
        });
        // 手动触发重新渲染
        this.chartKey += 1;
      } else {
        console.error('获取当日数据失败或数据格式不正确');
      }
      console.log("data", tdata);
      console.log("this.waterData.data", this.waterData.data);
    },

    async getHistoryData(){
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/history_data/');
        if (response.data.length > 0) {
          this.allWaterData = response.data; // 保存所有数据
          // 获取最新的水文数据
          this.todayData = {
              conductivity: this.allWaterData[this.allWaterData.length-1].conductivity,
              water_temperature: this.allWaterData[this.allWaterData.length-1].water_temperature,
              permanganate_index: this.allWaterData[this.allWaterData.length-1].permanganate_index,
              dissolved_oxygen: this.allWaterData[this.allWaterData.length-1].dissolved_oxygen,
              turbidity: this.allWaterData[this.allWaterData.length-1].turbidity,
              total_phosphorus: this.allWaterData[this.allWaterData.length-1].total_phosphorus,
            };
        } else {
          console.warn('数据不足');
        }
        console.log("历史数据：", this.todayData);
        this.fetchData();
      } 
      catch (error) {
        this.todayData = 
        {
        temperature: 15,
        salinity: 32.16,
        dissolved_oxygen: 0.00 ,
        illumination: 2.05,
        ph: 8.47,
        };
        console.error('获取历史数据失败', error);
      }
    }
  },
  mounted() {
    // this.fetchData();
  },
  create(){
    this.getHistoryData();
  }
};
</script>

<style scoped>
.content {
  width: 38%;
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
.map-content {
  width: 700px;
  height: 600px;
  overflow: hidden;
}
.map {
  width: 100%;
  height: 100%;
}
</style>
