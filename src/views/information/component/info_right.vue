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
              <el-button size="mini" @click="setTimeRange('custom')">查询</el-button>
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
            <h2>设备ID：8D19C331-4F08-47A1</h2>
            <h2>版本：V0.1.1</h2>
            <h2>温度：39.64°C</h2>
            <h2>连接：断开</h2>
          </div>
          <div class="air" v-if="device_selectid == 1" height="500px" width="600px">
            <h2>上次校准：2024年06月15日</h2>
            <h2>下次校准：2025年06月15日</h2>
            <h2>时钟偏差：+0.002秒</h2>
            <h2> </h2>
          </div>
          <div class="air" v-if="device_selectid == 2" height="500px" width="600px">
            <h2>通道1：正常</h2>
            <h2>通道2：异常</h2>
            <h2>通道3：正常</h2>
            <h2>通道4：正常</h2>
          </div>
          <div class="air" v-if="device_selectid == 3" height="500px" width="600px">
            <h2>警告1：温度过高（39.64°C）</h2>
            <h2>警告2：通信异常（次控断开）</h2>
            <h2>警告3：通道2断开</h2>
            <h2> </h2>
          </div>
        </dv-border-box-12>
      </div>
  </div>
</template>

<script>
import Echart from "@/common/echart/index.vue";
import axios from 'axios'
export default {
  data() {
    return {
      device_options: ['主控', '时间校准', '通道', '警告'],
      device_selectid : 0,
      startDate: null,
      endDate: null,
      selected_data_option: '选项1',
      data_options: [
        { value: '选项1', label: '水温', unit: '℃' },
        { value: '选项2', label: '盐度', unit: '‰' },
        { value: '选项3', label: '溶解度', unit: 'mg/L' },
        { value: '选项4', label: '浊度', unit: 'NTU' },
        { value: '选项5', label: 'pH', unit: '' },
      ],
      allWaterData: [], // 保存所有水质数据
      history_data: [],
      dataIndex: 0, // 当前数据索引
      waterData:{
        temperature: '',
        salinity: '',
        dissolved_oxygen: '',
        illumination: '',
        ph: '',
      },
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
            data: [],
            axisPointer: {
              type: "shadow",
            },
          },
        ],
        yAxis: [
          {
            type: "value",
            name: "℃",
            min: 0,
            max: 40,
            interval: 5,
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
            data: [15, 35, 32, 12, 17, 25, 26, 16, 16, 14, 27,36, 25,],
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
      let interval;
      let interval_num;
      switch (range) {
        case 'day':
          start = new Date(now.setDate(now.getDate() - 1));
          interval_num = 12;
          break;
        case 'week':
          start = new Date(now.setDate(now.getDate() - 7));
          interval_num = 7;
          break;
        case 'month':
          start = new Date(now.setMonth(now.getMonth() - 1));
          interval_num = 10;
          break;
        case 'year':
          start = new Date(now.setFullYear(now.getFullYear() - 1));
          interval_num = 12;
          break;
        case 'custom':
          // 用户多选框选择时间
          start = this.startDate;
          interval_num = 12;
          break;
      }

      this.startDate = start;
      this.endDate = new Date();
      interval = (this.endDate.getTime() - this.startDate.getTime()) / interval_num;
      
      let intervals = [];
      for (let i = 0; i <= interval_num; i++) {
        intervals.push(new Date(start.getTime() + interval * i));
      }
      const formattedIntervals = intervals.map(interval => this.formatDate(interval, range));
      this.options1.xAxis[0].data = formattedIntervals;
      console.log("formattedIntervals: ", formattedIntervals);
      
    },
    formatDate(date, type) {
      const options = {};
      switch (type) {
        case 'day':
          options.hour = '2-digit';
          options.minute = '2-digit';
          break;
        case 'week':
          options.weekday = 'short';
          break;
        case 'month':
          options.month = 'short';
          options.day = '2-digit';
          break;
        case 'year':
          options.month = 'short';
          break;
        case 'custom':
          options.month = 'short';
          options.day = '2-digit';          
          break;
      }
      return date.toLocaleString('en-US', options);
    },
    fetchHistoryData() {
      const data = {
        '选项1': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130],
        '选项2': [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135],
        '选项3': [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
        '选项4': [25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],
        '选项5': [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
      };

      const dataMap = {
        '选项1': this.history_data.map(d => d.water_temperature),
        '选项2': this.history_data.map(d => d.permanganate_index),
        '选项3': this.history_data.map(d => d.dissolved_oxygen),
        '选项4': this.history_data.map(d => d.turbidity),
        '选项5': this.history_data.map(d => d.total_phosphorus),
      };
      // 根据时间获取数据
      // 确保数据长度一致
      const xAxisDataLength = this.options1.xAxis[0].data.length;
      const selectedOptionData0 = dataMap['选项1'];
      if (selectedOptionData0.length > xAxisDataLength) {
        this.options1.series[0].data = selectedOptionData0.slice(0, xAxisDataLength);
      } else {
        this.options1.series[0].data = selectedOptionData0;
      }
      // this.options1.series[0].data = dataMap['选项1'];
      
      // 设置图表的第二属性
      const selectedOption = this.data_options.find(option => option.value === this.selected_data_option);
      this.options1.yAxis[1].name = selectedOption.unit;
      this.options1.yAxis[1].axisLabel.formatter = '{value} ' + selectedOption.unit;
      this.options1.yAxis[1].min = 0;
      this.options1.yAxis[1].max = Math.max(...data[this.selected_data_option]);
      this.options1.yAxis[1].interval = Math.round((this.options1.yAxis[0].max - this.options1.yAxis[0].min) / 5);

      // 确保数据长度一致
      const selectedOptionData1 = dataMap[this.selected_data_option];
      if (selectedOptionData1.length > xAxisDataLength) {
        this.options1.series[1].data = selectedOptionData1.slice(0, xAxisDataLength);
      } else {
        this.options1.series[1].data = selectedOptionData1;
      }

      // this.options1.series[1].data = dataMap[this.selected_data_option];
      this.options1.legend.data = [this.options1.series[0].name, this.options1.series[1].name];
    },
    async getHistoryData(){
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/history_data/');
        if (response.data.length > 0) {
          this.allWaterData = response.data; // 保存所有数据
          // console.log(this.allWaterData);
          this.history_data = [];

          // 获取与时间匹配的 13 条数据
          // 

          // 获取随机13 条数据
          const totalData = this.allWaterData.length;
          const numberOfData = totalData < 13 ? totalData : 13;
          const randomIndices = [];
          while (randomIndices.length < numberOfData) {
            const randomIndex = Math.floor(Math.random() * totalData);
            if (!randomIndices.includes(randomIndex)) {
              randomIndices.push(this.allWaterData[randomIndex]);
            }
          }
          const latestData = randomIndices.slice(-13);
          // 根据所选的类型处理历史数据
          latestData.forEach((dataPoint) => {
            this.history_data.push({
              monitoring_time: dataPoint.monitoring_time,
              water_temperature: dataPoint.water_temperature,
              permanganate_index: dataPoint.permanganate_index,
              dissolved_oxygen: dataPoint.dissolved_oxygen,
              turbidity: dataPoint.turbidity,
              total_phosphorus: dataPoint.pH,
            });
          });
        } else {
          console.warn('数据不足 13 条');
          this.allWaterData = response.data;
          this.history_data = this.allWaterData; // 如果数据不足 13 条，获取所有数据
        }
        console.log("历史数据：", this.history_data);
      } 
      catch (error) {
        console.error('获取历史数据失败', error);
      }
      this.fetchHistoryData();
    }
  },
  watch: {
    selected_data_option() {
      console.log("---:",this.selected_data_option);
      this.fetchHistoryData();
    }
  },
  mounted() {
    this.fetchHistoryData();
    this.setTimeRange('month'); // 默认显示近一周的数据
  },
  created(){
    this.getHistoryData();
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
