<template>
  <div class="content">
    <!-- <heat-map-echarts height="580px" width="680px" /> -->
    <div class="center_contetn">
        <div class="col_text_content">
          <div class="air"  style="padding: 30px">
            <h1>鱼类信息</h1>
            <div>
              <p>鱼种数量：50+</p>
              <p>鱼苗：500尾</p>
              <p>生长：600尾</p>
            </div>
          </div>
        </div>

        <div class="col_text_content">
          <div class="air"  style="padding: 30px">
            <h1>设备信息</h1>
            <div>
              <p>镜头：5+</p>
              <p>声纳：2</p>
              <p>云台：1</p>
            </div>
          </div>
        </div>
    </div>
    <Echart :options="options1" height="400px" width="500px"/>
    <div class="fish_info">
      <dv-border-box-7>
        <div class="fish_info_buttons">
          <el-button size="mini" @click="setFishInfo('weight')">鱼类重量</el-button>
          <el-button size="mini" @click="setFishInfo('length')">鱼类尺寸</el-button>
          <el-button size="mini" @click="setFishInfo('life')">鱼类生命</el-button>
        </div>
        <h2 class="title">{{ fish_info_select }}</h2>
        <Echart :options="options2" height="350px" width="680px" />

      </dv-border-box-7>
    </div>
  </div>
</template>

<script>
import Echart from "@/common/echart/index.vue";
import axios from 'axios'
// import heatMapEcharts from "./echarts/heatMapEcharts.vue";
export default {
  data() {
    return {
    fish_info_select: '鱼类重量',
    need_fish_data: [],
    options1: {
    series: [
    {
      type: 'gauge',
      startAngle: 180,
      endAngle: 0,
      center: ['50%', '75%'],
      radius: '90%',
      min: 0,
      max: 2000,
      splitNumber: 8,
      axisLine: {
        lineStyle: {
          width: 6,
          color: [
            [0.25, "#FF6E76"],
            [0.5, "#FDDD60"],
            [0.75, "#58D9F9"],
            [1, "#7CFFB2"]
          ]
        }
      },
      pointer: {
        icon: 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
        length: '12%',
        width: 20,
        offsetCenter: [0, '-60%'],
        itemStyle: {
          color: 'auto'
        }
      },
      axisTick: {
        length: 12,
        lineStyle: {
          color: 'auto',
          width: 2
        }
      },
      splitLine: {
        length: 20,
        lineStyle: {
          color: 'auto',
          width: 5
        }
      },
      axisLabel: {
        color: '#464646',
        fontSize: 20,
        distance: -60,
        rotate: 'tangential',
        formatter: function (value) {
          if (value === 500) {
            return '500w';
          } else if (value === 1000) {
            return '1000w';
          } else if (value === 1500) {
            return '1500w';
          } 
          return '';
        }
      },
      title: {
        offsetCenter: [0, '-10%'],
        fontSize: 20
      },
      detail: {
        fontSize: 30,
        offsetCenter: [0, '-35%'],
        valueAnimation: true,
        formatter: function (value) {
          return Math.round(value * 10000) + '';
        },
        color: 'inherit'
      },
      data: [
        {
          value: 1560,
          name: '保障鱼群'
        }
        ]
        }
    ]
    },
    options2: {
        xAxis: {
            type: 'category',
            data: ['种类一', '种类二', '种类三', '种类四', '种类五', '种类六', '种类七']
        },
        yAxis: {
            type: ''
        },
        series: [
            {
            data: [],
            type: 'line',
            smooth: true
            }
        ]
    },
    };
  },
  components: {
    Echart,
  },
  created() {
    // 初始化时显示默认数据
    this.fish_info_select = '鱼类重量';
    this.getFishData();
    this.updateOptions2(this.fish_info_select);
  },
  methods: {
    setFishInfo(type) {
      switch (type) {
        case 'weight':
          this.fish_info_select = '鱼类重量';
          this.updateOptions2(this.fish_info_select);
          break;
        case 'length':
          this.fish_info_select = '鱼类尺寸';
          this.updateOptions2(this.fish_info_select);
          break;
        case 'life':
          this.fish_info_select = '鱼类生命';
          this.updateOptions2(this.fish_info_select);
          break;
        default:
          break;
      }
    },
    updateOptions2(type) {
      switch (type) {
        case '鱼类重量':
          this.options2.yAxis = {
            type: 'value',
            axisLabel: {
              formatter: '{value} 千克'
            }
          };
          // this.options2.series[0].data = [820, 932, 901, 934, 1290, 1330, 1320];
          break;
        case '鱼类尺寸':
          this.options2.yAxis = {
            type: 'value',
            axisLabel: {
              formatter: '{value} 厘米'
            }
          };
          // this.options2.series[0].data = [120, 220, 150, 234, 290, 330, 320];
          break;
        case '鱼类生命':
          this.options2.yAxis = {
            type: 'value',
            axisLabel: {
              formatter: '{value}'
            }
          };
          // this.options2.series[0].data = [50, 60, 70, 80, 90, 100, 110];
          break;
        default:
          break;
      }
      this.fetchFishData();
    },
    fetchFishData() {
      // this.getFishData();
      // 还需要对need_fish_data进行处理
      
      // 鱼类重量、鱼类尺寸、鱼类数量
      const dataMap = {
        '鱼类重量': this.need_fish_data.map(d => [d.species, d.body_weight]),
        '鱼类尺寸': this.need_fish_data.map(d => [d.species, d.body_length]),
        '鱼类生命': this.need_fish_data.map(d => [d.species, d.fish_group_total]),
      };
      const selectedOption = this.fish_info_select;
      console.log('s',dataMap[selectedOption])
      
      // 设置图表数据格式为[time, data]
      this.options2.series[0].data = dataMap[selectedOption].map(item => item[1]);
    },
    async getFishData(){
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/fish_data/');
        if (response.data.length > 0) {
          this.all_fish_data = response.data; // 保存所有数据
          // 需要七个不同种类的鱼类数据
          this.need_fish_data = this.all_fish_data.slice(0, 7);
          this.fetchFishData();
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
};
</script>

<style scoped>
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.center_contetn{
  width: 500px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.col_text_content{
  padding: 8px;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  justify-content: center;
}
.fish_info{
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.fish_info_buttons{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.title {
  margin-top: 20px;
  margin-bottom: -30px;
}
</style>
