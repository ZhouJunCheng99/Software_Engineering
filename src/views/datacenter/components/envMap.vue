<template>
  <div class="content">
    <p class="title">数据中心分布</p>
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
</template>

<script>
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
        { lng: 113.28064, lat: 23.125177 }, // 广州
        { lng: 116.407526, lat: 39.90403 }, // 北京
        { lng: 121.473701, lat: 31.230416 }, // 上海
      ],
    };
  },
  created() {},
  mounted() {},
  methods: {
    handler({ BMap, map }) {
      console.log(BMap, map);
      this.center.lng = 104.195397;
      this.center.lat = 35.86166;
      this.zoom = 5;
    },
  },
};
</script>

<style scoped>
.content {
  width: 100%;
  height: 55%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.title {
  margin-bottom: 10px;
  font-size: 28px;
}
.map {
  width: 100%;
  height: 100%;
}
</style>
