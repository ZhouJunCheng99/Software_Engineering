<template>
  <div class="colum_content">
    <dv-border-box-8 style="padding: 3px">
    <div class="vedio_content">
      <h2>视频监控</h2>

        <div class="row_content" style="padding: 8px">
          <button v-for="option in options" :key="option" @click="select(option)" round=true>
            {{ option }}
          </button>
        </div>

        <div style="width: 100%; height: 70%">
          <video autoplay="autoplay" width="100%" height="100%">
              <source src="../../../assets/webm/ocean.mp4" type="video/mp4"/>
          </video>
      </div>
    </div>
      </dv-border-box-8>
    
    <div class="content1">
      <dv-border-box-8 style="padding: 3px">
      <div class="content2">
      <h2>附加功能</h2>
      <div>
        <div class="row_content" style="padding: 8px">
        <div>
          <label>开关1状态:</label>
          <input type="checkbox" v-model="switchValue1" @change="toggleSwitch(1)">
        </div>
        <div>   
          <label>开关2状态:</label>
          <input type="checkbox" v-model="switchValue1" @change="toggleSwitch(2)">
        </div>
        <div>
          <label>开关3状态:</label>
          <input type="checkbox" v-model="switchValue1" @change="toggleSwitch(3)">
        </div>
        </div>
        <div class="row_content" style="padding: 8px">
        <div>
          <label>开关4状态:</label>
          <input type="checkbox" v-model="switchValue1" @change="toggleSwitch(4)">
        </div>
        <div>   
          <label>开关5状态:</label>
          <input type="checkbox" v-model="switchValue1" @change="toggleSwitch(5)">
        </div>
        <div>
          <label>开关6状态:</label>
          <input type="checkbox" v-model="switchValue1" @change="toggleSwitch(6)">
        </div>
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
    };
  },
  methods: {
    select(option) {
      // 选项选择逻辑
      console.log('选中选项:', option);
    },
    toggleSwitch(index) {
      // 开关切换逻辑
      console.log('开关', index, '状态:', this.switchValues[index - 1]);
    }
  }
};
</script>

<style scoped>
.colum_content {
  width: 40%;
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
.vedio_content{
  margin-top: 10px;
  display: flex;
  flex-direction: column;
}
.content1{
  margin-top: 10px;
}
.content2{
  width: 100%;
  height: 100px;
  display: flex;
  flex-direction: column;  
  align-items: center;
  justify-content: space-between;
  flex-grow: 1;
}

h2{
  margin: 10px;
}
button {
  width: 100px;
  height: 50px;
}
</style>
