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

export default {
  data() {
    return {
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
            name: '电池电压(V)',
            value: 0,
          },
          {
            name: '盐度(‰)',
            value: 0,
          },
          {
            name: '溶解度(mg/L)',
            value: 0,
          },
          {
            name: '浊度(NTU)',
            value: 0,
          },
          {
            name: 'pH',
            value: 0,
          },
          {
            name: '水温(℃)',
            value: 0,
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
      const data = this.getDayData(); // 调用获取当日数据的方法
      if (data && data.length === 6) {
        data.forEach((item, index) => {
          // 使用 this.$set 来更新数组中的对象
          this.$set(this.waterData.data, index, {
            name: item.name,
            value: item.value.toFixed(2)  // 假设数据项的值需要保留两位小数
          });
        });
        // 手动触发重新渲染
        this.chartKey += 1;
      } else {
        console.error('获取当日数据失败或数据格式不正确');
      }
      console.log("data", data);
      console.log("this.waterData.data", this.waterData.data);
    },
    getDayData() {
      // 模拟获取当日数据的方法
      return [
        { name: '电池电压(V)', value: 25.90 },
        { name: '盐度(‰)', value: 32.16 },
        { name: '溶解度(mg/L)', value: 0.00 },
        { name: '浊度(NTU)', value: 2.05 },
        { name: 'pH', value: 8.47 },
        { name: '水温(℃)', value: 15 }
      ];
    },
  },
  mounted() {
    this.fetchData();
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
