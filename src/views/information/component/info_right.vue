<template>
  <div class="column_content">
    <dv-border-box-6 style="padding-top: 20px">
      <!-- <h2 class="title">2010-2022年牧场环境质量（温度+PH）</h2>
      <Echart :options="options1" height="500px" width="600px" /> -->
      <div class="history_record">
          <h2 class="title">历史记录</h2>
          <div class="select_content">
            <div class="time_range_content">
              <el-date-picker
                v-model="startDate"
                type="datetime"
                placeholder="开始日期"
                size="mini"
              />
              <span> 至 </span>
              <el-date-picker
                v-model="endDate"
                type="datetime"
                placeholder="结束日期"
                size="mini"
              />
              <el-button size="mini" @click="fetchData">查询</el-button>
            </div>

            <div class="time_buttons">
              <el-button size="mini" @click="setTimeRange('day')">近一天</el-button>
              <el-button size="mini" @click="setTimeRange('week')">近一周</el-button>
              <el-button size="mini" @click="setTimeRange('month')">近一月</el-button>
              <el-button size="mini" @click="setTimeRange('year')">近一年</el-button>
              <el-select size="mini" v-model="selected_data_option" placeholder="选择类型">
                <el-option
                  v-for="option in data_options"
                  :key="option.value"
                  :label="option.label"
                  :value="option.value"
                />
              </el-select>
            </div>
          </div>
          <Echart :options="options1" height="500px" width="100%" />
      </div>

    </dv-border-box-6>
      <div class="device_content">
        <dv-border-box-12 style="padding: 20px">
            <h1>设备状态</h1>
        <div class="row_content">
          <el-button class="device_button" v-for="(option, index) in device_options" :key="option" @click="select(index)" :round="true">
            {{ option }}
          </el-button>
          
        </div>
          <div class="air" v-if="device_selectid == 0" height="500px" width="600px">
            <h2>设备信息0</h2>
            <h2>设备信息0</h2>
            <h2>设备信息0</h2>
            <h2>设备信息0</h2>
          </div>
          <div class="air" v-if="device_selectid == 1" height="500px" width="600px">
            <h2>设备信息1</h2>
            <h2>设备信息1</h2>
            <h2>设备信息1</h2>
            <h2>设备信息1</h2>
          </div>
          <div class="air" v-if="device_selectid == 2" height="500px" width="600px">
            <h2>设备信息2</h2>
            <h2>设备信息2</h2>
            <h2>设备信息2</h2>
            <h2>设备信息2</h2>
          </div>
          <div class="air" v-if="device_selectid == 3" height="500px" width="600px">
            <h2>设备信息3</h2>
            <h2>设备信息3</h2>
            <h2>设备信息3</h2>
            <h2>设备信息3</h2>
          </div>
        </dv-border-box-12>
      </div>
  </div>
</template>

<script>
import Echart from "@/common/echart/index.vue";

export default {
  data() {
    return {
      device_options: ['主控', '时间校准', '通道', '警告'],
      device_selectid : 0,
      startDate: null,
      endDate: null,
      selected_data_option: '选项1',
      data_options: [
        { value: '选项1', label: '电池电压', unit: 'V' },
        { value: '选项2', label: '盐度', unit: '‰' },
        { value: '选项3', label: '溶解度', unit: 'mg/L' },
        { value: '选项4', label: '浊度', unit: 'NTU' },
        { value: '选项5', label: 'pH', unit: '' },
        { value: '选项6', label: '水温', unit: '℃' }
      ],
      options1: {
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
            crossStyle: {
              color: "#999",
            },
          },
        },
        toolbox: {
          feature: {
            dataView: { show: true, readOnly: false },
            magicType: { show: true, type: ["line", "bar"] },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        legend: {
          data: [],
        },
        xAxis: [
          {
            type: "category",
            data: [
              "2010",
              "2011",
              "2012",
              "2013",
              "2014",
              "2015",
              "2016",
              "2017",
              "2018",
              "2019",
              "2020",
              "2021",
              "2022",
            ],
            axisPointer: {
              type: "shadow",
            },
          },
        ],
        yAxis: [
          {
            type: "value",
            name: "℃",
            min: 2700,
            max: 3300,
            interval: 100,
            axisLabel: {
              formatter: "{value}",
            },
          },
          {
            type: "value",
            name: "", // Will be updated dynamically
            min: 0,  // Update dynamically based on selected option
            max: 0,  // Update dynamically based on selected option
            interval: 0,  // Update dynamically based on selected option
            axisLabel: {
              formatter: "{value}",
            },
          },
        ],
        series: [
          {
            name: "温度",
            type: "bar",
            tooltip: {
              valueFormatter: function (value) {
                return value + " ℃";
              },
            },
            data: [2920, 2950, 2970, 3010, 3040, 3070, 3110, 3150, 3160, 3190, 3210,3220, 3250,],
          },
          {
            name: "",
            type: "line",
            yAxisIndex: 1,
            tooltip: {
              valueFormatter: function (value) {
                return value + " ";
              },
            },
            data: [],
          },
        ],
      },
    };
  },
  components: {
    Echart,
  },
  methods: {
    select(index) {
      // 选项选择逻辑
      this.device_selectid = index;
      console.log('选中选项:', index);
    },
    setTimeRange(range) {
      const now = new Date();
      let start;
      switch (range) {
        case 'day':
          start = new Date(now.setDate(now.getDate() - 1));
          break;
        case 'week':
          start = new Date(now.setDate(now.getDate() - 7));
          break;
        case 'month':
          start = new Date(now.setMonth(now.getMonth() - 1));
          break;
        case 'year':
          start = new Date(now.setFullYear(now.getFullYear() - 1));
          break;
      }
      this.startDate = start;
      this.endDate = new Date();
      this.fetchData();
    },
    fetchData() {
      // Get data based on selected time range and update chart options
      const data = {
        '选项1': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130],
        '选项2': [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135],
        '选项3': [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
        '选项4': [25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],
        '选项5': [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
        '选项6': [35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],
      };
      // const temp_data = [2920, 2950, 2970, 3010, 3040, 3070, 3110, 3150, 3160, 3190, 3210,3220, 3250,];
      

      const selectedOption = this.data_options.find(option => option.value === this.selected_data_option);
      this.options1.yAxis[1].name = selectedOption.unit;
      
      this.options1.yAxis[1].axisLabel.formatter = '{value} ' + selectedOption.unit;

      this.options1.yAxis[1].min = 0;
      this.options1.yAxis[1].max = Math.max(...data[this.selected_data_option]);
      this.options1.yAxis[1].interval = Math.round((this.options1.yAxis[0].max - this.options1.yAxis[0].min) / 5);
      this.options1.series[1].data = data[this.selected_data_option];
      this.options1.legend.data = [this.options1.series[0].name, this.options1.series[1].name];

    },
    
  },
  watch: {
    selected_data_option() {
      console.log("---:",this.selected_data_option);
      this.fetchData();
    }
  },
  mounted() {
    this.fetchData();
  }
};
</script>

<style>
.column_content{
  width: 38%;
  display: flex;
  flex-direction: column;
}
.title {
  display: flex;
  justify-content: center;
  margin-bottom: 10px;
}
.device_content{
  height: 40%;
  flex-grow: 1;
  display: flex;
}
.row_content {
  width: 100%;
  height: 20%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}
.select_content{
  width: 100%;
  height: 20%;
  display: flex;
  flex-direction: column;
  align-items: center
}
.time_range_content {
  width: 90%;
  height: 20%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}
.time_buttons{
  width: 90%;
  height: 20%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}


.device_button {
  width: 20%;
  height: 80%;
}

</style>
