<template>
  <div class="content">
    <div>
      <dv-border-box-2 style="padding: 8px">
          <h2>水文气象</h2>
          <dv-capsule-chart
            :config="waterData"
            width="100%"
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
// import Echart from "@/common/echart/index.vue";
import mapStyle from "@/assets/mapStyle.json";
export default {
  components: {},
  data() {
    return {
      center: { lng: 0, lat: 0 },
      zoom: 3,
      mapStyle: {
        styleJson: mapStyle,
      },
      markerPoints: [
        { lng: 106.505, lat: 29.5332 },
        { lng: 106.51, lat: 29.5332 },
        { lng: 106.524, lat: 29.53 },
      ],
      waterData: {
        data: [
          {
            name: '电池电压(V)',
            value: 25.90
          },
          {
            name: '盐度()',
            value: 67
          },
          {
            name: '溶解度()',
            value: 123
          },
          {
            name: '浊度()',
            value: 55
          },
          {
            name: 'pH()',
            value: 98
          },
          {
            name: '水温()',
            value: 167
          },
        ],
        colors: ['#e062ae', '#fb7293', '#e690d1', '#32c5e9', '#96bfff', '#e062ae'],
        unit: ' ',
        showValue: true
      },
    };
  },
  methods: {
    handler({ BMap, map }) {
      console.log(BMap, map);
      this.center.lng = 106.505;
      this.center.lat = 29.5332;
      this.zoom = 15;
    },
  },
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
