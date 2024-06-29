<template>
  <div class="content">
    <div>
      <dv-border-box-8 :reverse="true" style="padding: 10px">
        <div class="hardware">
            <h2>网箱信息</h2>
            <dv-border-box-12 style="padding: 20px">
            <div class="hardware_info">
                <p>网箱长度：150m</p>
                <p>网箱宽度：70m</p>
                <p>网箱深度：40m</p>
                <p>网箱经度：130.456  网箱纬度：58.789</p>
            </div>
            </dv-border-box-12>
        </div>
        <div class="hardware">
            <h2>水底传感器</h2>
            <dv-border-box-12 style="padding: 20px">
            <div class="hardware_info">
                <p>运行时间：18天6小时29分钟</p>
                <p>下次检修：40天后</p>
                <p>上次校准：2023年11月20日</p>
                <p>保修过期：2034年05月15日</p>
            </div>
            </dv-border-box-12>
        </div>
        <div class="hardware">
            <h2>供电系统</h2>
            <dv-border-box-12 style="padding: 20px">
            <div class="hardware_info">
                <p>电池电量：70%</p>
                <p>上次更换：2023年10月05日</p>
                <p>下次更换：2024年10月05日</p>
                <p>保修过期：2034年05月15日</p>
            </div>
            </dv-border-box-12>
        </div>
      </dv-border-box-8>
    </div>

    <div class="body">
      <dv-border-box-6  style="padding: 10px">
        <Echart :options="options2" height="400px"
      /></dv-border-box-6>
    </div>
  </div>
</template>

<script>
import Echart from "@/common/echart/index.vue";
import axios from 'axios';
export default {
  components: { Echart },
  data() {
    return {
      all_fish_data: [], // 保存所有数据
      need_fish_data: [],
      options2: {
        title: {
          text: '鱼类统计',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        color: ['#FF7F50', '#87CEFA', '#DA70D6', '#32CD32', '#6495ED', '#FF69B4', '#BA55D3'],
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: ['40%', '70%'],
            data: [],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            },
          },
        ],
      },
    };
  },
  methods:{
    fetchFishData() {
      this.getFishData();

      // 还需要对all_fish_data进行处理
      // 鱼类数量
      // 设置图表数据格式为{ value: 32, name: '种类一' }

    },
    async getFishData(){
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/fish_data/');
        if (response.data.length > 0) {
          this.all_fish_data = response.data; // 保存所有数据
          this.need_fish_data = this.all_fish_data.slice(0, 7);
          const dataMap = this.need_fish_data.map(d => ({
            value: d.fish_group_total,
            name: d.species
          }));
          this.options2.series[0].data = dataMap;
        } else {
          console.warn('数据不足');
        }
        // console.log("历史数据：", this.all_fish_data);
      } 
      catch (error) {
        console.error('获取历史数据失败', error);
      }
    }
  },
  created() {
    this.fetchFishData(); // 在组件创建时获取数据
  }
};
</script>

<style scoped>
.content {
  width: 30%;
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
.hardware{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: stretch;    
}
.hardware_info{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: stretch;    
}
.body {
  margin-top: 10px;
}
</style>
