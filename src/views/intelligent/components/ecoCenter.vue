<template>
  <div class="content">
    <div>
      <dv-border-box-8 :reverse="true">
        <div class="head">
          <div class="video-container">
          <h3>识别效果</h3>
          <video autoplay="autoplay" width="100%" height="95%">
              <source src="../../../assets/webm/ocean.mp4" type="video/mp4"/>
          </video>
          </div>
          <div class="side-videos">
          <h3>左目镜头</h3>
          <video autoplay="autoplay" width="100%" height="95%">
              <source src="../../../assets/webm/ocean.mp4" type="video/mp4"/>
          </video>
          <h3>右目镜头</h3>
          <video autoplay="autoplay" width="100%" height="95%">
              <source src="../../../assets/webm/ocean.mp4" type="video/mp4"/>
          </video>
          </div>
        </div>
      </dv-border-box-8>
    </div>

    <div class="body">
      <dv-border-box-6 style="padding:10px">
        <div class="fish-content">
          <div class="fish-info">
            <div>
            <p>编号</p>
            <p>fish-9527</p>
            </div>
          </div>
          <div class="fish-info">
          <div>
            <p>鱼种</p>
            <p>moonfish</p>
            </div>
          </div>
          <div class="fish-info">
            <div>
            <p>体长</p>
            <p>10寸</p>
            </div>
          </div>
          <div class="fish-info">
            <div>
            <p>体重</p>
            <p>5kg</p>
            </div>
          </div>
          <div class="fish-info">
            <div>
            <p>健康状况</p>
            <p>疑似患病(眼)</p>
            </div>
          </div>
          <div class="fish-info">
            <div>
            <p>鱼群状况</p>
            <p>异常(集群)</p>
            </div>
          </div>
          <div class="fish-info">
            <div>
            <p>是否进入繁殖期</p>
            <p>否</p>
            </div>
          </div>
          <div class="fish-info">
            <div>
            <p>鱼群总量</p>
            <p>10t</p>
            </div>
          </div>
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
  width: 65%;
}
.head {
  padding: 10px;
  height: 560px;
  display: flex;
  justify-content: space-around;
}

.video-container {
  width: 66.66%; /* 第一组视频占据 2/3 宽度 */
  display: flex;
  flex-direction: column; /* 垂直排列 */
}


.side-videos {
  width: 33.33%; /* 右侧视频占据 1/3 宽度 */
  height: 45%;
  display: flex;
  flex-direction: column; /* 垂直排列 */
  margin:20px;
}

.side-videos > div {
  margin-bottom: 20px;
}

.body {
  margin-top: 10px;
}
.fish-content {
  width: 100%;
  height: 320px;
  display: flex;
  flex-wrap: wrap;
}
.fish-info {
  width: 25%;
  height: 50%;
  overflow: hidden;
  border: 1px solid #ccc;
  padding: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.fish-info p {
  margin: 5px 0;
  font-size: 24px;
}
</style>
