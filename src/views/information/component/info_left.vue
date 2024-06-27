<template>
  <div class="colum_content">
    <div class="content1">
    <dv-border-box-8>
      <div class="vedio_content">
        <h2>视频监控</h2>
        <div class="row_content">
          <el-button size="small" class="vedio_btn" v-for="(option, index) in options" :key="option" @click="select(index)" :round="true">
            {{ option }}
          </el-button>
          
        </div>
        <div style="width: 100%; height: 70%">
           <video ref="videoPlayer" :key="vedio_src" autoplay="autoplay" width="100%" height="400px">
            <source v-bind:src="vedio_src" type="video/mp4"/>
          </video>
        </div>
      </div> 
    </dv-border-box-8>
    </div>

    <div class="content1">
      <dv-border-box-8 style="padding: 3px">
      <div class="content2">
      <h2>附加功能</h2>
        <!-- <div class="row_content" style="padding: 8px">
        <div>
          <el-switch  v-model="switchValues[0]"  active-color="#13ce66"  inactive-color="#ff4949" @change="toggleSwitch(0)">
            摄像机
          </el-switch>
          <label>摄像机:</label>
          <input type="checkbox" v-model="switchValues[0]" @change="toggleSwitch(0)">
        </div>
        <div>   
          <label>灯光:</label>
          <input type="checkbox" v-model="switchValues[1]" @change="toggleSwitch(1)">
        </div>
        <div>
          <label>清洁刷:</label>
          <input type="checkbox" v-model="switchValues[2]" @change="toggleSwitch(2)">
        </div>--->


        <!-- <div class="row_content" style="padding: 8px">
        <div>
          <label>开关4状态:</label>
          <input type="checkbox" v-model="switchValues[3]" @change="toggleSwitch(3)">
        </div>
        <div>   
          <label>开关5状态:</label>
          <input type="checkbox" v-model="switchValues[4]" @change="toggleSwitch(4)">
        </div>
        <div>
          <label>开关6状态:</label>
          <input type="checkbox" v-model="switchValues[5]" @change="toggleSwitch(5)">
        </div>
        </div> -->
        <!-- <div class="row_switch_content">
          <el-switch  v-model="switchValues[3]" active-text="附加功能4" active-color="#13ce66"  inactive-color="#ff4949" @change="toggleSwitch(3)">
          </el-switch>

          <el-switch  v-model="switchValues[4]" active-text="附加功能5" active-color="#13ce66"  inactive-color="#ff4949" @change="toggleSwitch(4)">
          </el-switch>

          <el-switch  v-model="switchValues[5]" active-text="附加功能6" active-color="#13ce66"  inactive-color="#ff4949" @change="toggleSwitch(5)">
          </el-switch>
        </div> -->
        <div class="row_switch_content">
          <div class="column_switch_content">
            <el-switch  v-model="switchValues[0]" active-text="摄像机" active-color="#13ce66"  inactive-color="#FF0000" @change="toggleSwitch(0)">
            </el-switch>

            <el-switch  v-model="switchValues[3]" active-text="附加功能4" active-color="#13ce66"  inactive-color="#FF0000" @change="toggleSwitch(3)">
            </el-switch>
          </div>

          <div class="column_switch_content">
            <el-switch  v-model="switchValues[1]" active-text="灯光" active-color="#13ce66"  inactive-color="#FF0000" @change="toggleSwitch(1)">
            </el-switch>

            <el-switch  v-model="switchValues[4]" active-text="附加功能5" active-color="#13ce66"  inactive-color="#ff4949" @change="toggleSwitch(4)">
            </el-switch>
          </div>

          <div class="column_switch_content">
            <el-switch  v-model="switchValues[2]" active-text="清洁刷" active-color="#13ce66"  inactive-color="#ff4949" @change="toggleSwitch(2)">
            </el-switch>

            <el-switch  v-model="switchValues[5]" active-text="附加功能6" active-color="#13ce66"  inactive-color="#ff4949" @change="toggleSwitch(5)">
            </el-switch>
          </div>
        </div>
      </div>
    </dv-border-box-8>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      options: ['视频1', '视频2', '视频3', '视频4'],
      switchValues: [false, false, false, false, false, false], // 使用一个数组来保存所有开关的状态
      vedio_src : require("../../../assets/webm/ocean.mp4"),
    };
  },
  methods: {
    select(index) {
      // 选项选择逻辑
      const videos = [
        require("../../../assets/webm/ocean.mp4"),
        require("../../../assets/webm/CAMERAV.webm"),
        require("../../../assets/webm/ocean.mp4"),
        require("../../../assets/webm/CAMERAV.webm"),
      ];
      this.vedio_src = videos[index];
      console.log('选中选项:', index);
    },
    toggleSwitch(index) {
      // const state = this.switchValues[index] ? '打开' : '关闭';
      // alert(`开关${index}已经${state}`);
      console.log('开关', index, '状态:', this.switchValues[index]);
    }
  }
};
</script>

<style scoped>
.colum_content {
  width: 40%;
  display: inline-flex;
  flex-direction: column;
  flex-wrap: nowrap;
  justify-content: normal;
  align-items: stretch;
  align-content: normal;
}
.vedio_content{
  height: 600px;
  display: flex;
  flex-direction: column;
}
.row_content {
  width: 100%;
  height: 100%;
  padding: 10px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}
.row_switch_content {
  height: 60%;
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}
.column_switch_content{
  width: 100%;
  height: 100%;
  padding: 10px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-between;
}
.vedio_btn {
  width: 20%;
  height: 100px;
}

.content1{
  margin-top: 10px;
}

.content2{
  width: 100%;
  height: 200px;
  display: flex;
  flex-direction: column;  
}
h2{
  margin: 10px;
}

</style>