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
        <button @click="PreFishData">上一个</button>
        <button @click="NextFishData">下一个</button>
        <div class="fish-content">
          <div class="fish-info">
            <div>
            <p>编号</p>
            <p>{{currFishdata.pk}}</p>
            </div>
          </div>
          <div class="fish-info">
          <div>
            <p>鱼种</p>
            <p>{{currFishdata.species}}</p>
            </div>
          </div>
          <div class="fish-info">
            <div>
            <p>体长</p>
            <p>{{currFishdata.body_length}}cm</p>
            </div>
          </div>
          <div class="fish-info">
            <div>
            <p>体重</p>
            <p>{{currFishdata.body_weight}}kg</p>
            </div>
          </div>
          <div class="fish-info">
            <div>
            <p>健康状况</p>
            <p>{{currFishdata.health_status}}</p>
            </div>
          </div>
          <div class="fish-info">
            <div>
            <p>鱼群状况</p>
            <p>{{currFishdata.fish_group_status}}</p>
            </div>
          </div>
          <div class="fish-info">
            <div>
            <p>繁殖期</p>
            <p>{{currFishdata.breeding_period}}</p>
            </div>
          </div>
          <div class="fish-info">
            <div>
            <p>鱼群总量</p>
            <p>{{currFishdata.fish_group_total}}t</p>
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
import axios from "axios";
export default {
  components: {},
  data() {
    return {
      currFishdata:'',
      FishData:[],
      dataIndex:0,
      center: { lng: 0, lat: 0 },
      zoom: 3,
      mapStyle: {
        styleJson: mapStyle,
      },
    };
  },
  created() {
    this.fetchFishData();
  },
  methods: {
    async fetchFishData(){
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/fish-data/');
        if (response.data.length > 0) {
          // this.waterData = response.data[0];  // 获取第一条数据
          console.log('suc',response.data[0]);
          this.FishData = response.data; // 保存所有数据
          this.currFishdata = this.FishData[0];
        }
      } catch (error) {
        console.error('Error fetching water data:', error);
      }
    },
    PreFishData(){
      if(this.dataIndex>0) {
        this.dataIndex -= 1;
        this.currFishdata = this.FishData[this.dataIndex];
      }
    },
    NextFishData(){
      if(this.dataIndex<this.FishData.length-1) {
        this.dataIndex += 1;
        this.currFishdata = this.FishData[this.dataIndex];
      }
    },
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
  height: 540px;
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
