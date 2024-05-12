<template>
  <div class="content">
    <div>
      <dv-border-box-8 :reverse="true">
        <div class="head">
          <div class="data">
            <h1>1020TB</h1>
          </div>
          <div class="head_content">
            <h3>数据总量</h3>
          </div>
          <div class="head_content">
            <h4>今日新增</h4>
            <h4>8</h4>
          </div>
          <div class="head_content">
            <h4>今日处理</h4>
            <h4>8</h4>
          </div>
        </div>
      </dv-border-box-8>
    </div>

    <div class="body">
      <!-- 硬件信息 -->
      <dv-border-box-6>
        <div class="hardware">
          <div class="info">
            <div class="circle">
              <svg height="200" width="200">
                <defs>
                  <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:white;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:blue;stop-opacity:1" />
                  </linearGradient>
                </defs>
                <circle cx="100" cy="100" r="80" stroke="url(#grad2)" stroke-width="3" fill="transparent" />
                <text x="100" y="80" text-anchor="middle" dominant-baseline="middle" fill="white" font-size="28">999</text>
                <text x="100" y="120" text-anchor="middle" dominant-baseline="middle" fill="white" font-size="24">进程总量</text>
              </svg>
            </div>
            <div class="disk">
              <div class="lui-column-bg">
                <div class="lui-inner" :class="dangerclass" :style="{ height: 33 + '%' }"></div>
              </div>
            </div>
            <div class="disk-info">
              <p>磁盘：</p>
              <p>已使用100T</p>
              <p>剩余200T</p>
            </div>
          </div>
          <div class="device">
            <div class="device_label">CPU运行状态</div>
            <div class="device-usage">
              <div class="cpu-usage" :style="{ width: 60 + '%' }"></div>
            </div>
          </div>
          <div class="device">
            <div class="device_label">内存运行状态</div>
            <div class="device-usage">
              <div class="mem-usage" :style="{ width: 70 + '%' }"></div>
            </div>
          </div>
          <div class="device">
            <div class="device_label">GPU运行状态</div>
            <div class="device-usage">
              <div class="gpu-usage" :style="{ width: 40 + '%' }"></div>
            </div>
          </div>
        </div>
      </dv-border-box-6>
      <!-- 数据类型统计 -->
      <dv-border-box-10>
        <Echart :options="options2" height="420px"/>
      </dv-border-box-10>
    </div>
  </div>
</template>

<script>
import Echart from "@/common/echart/index.vue";
export default {
  components: { Echart },
  data() {
    return {
      options2 : {
        title: {
          text: "数据交互处理",
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          },
          formatter: function(params) {
            var result = params[0].name + '<br/>';
            params.forEach(function(item) {
              var value = item.value;
              if (value < 0) {
                value = -value;
              }
              result += item.marker + item.seriesName + ': ' + value + '<br/>';
            });
            return result;
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'value',
            axisLabel: {
              show: false
            },
          }
        ],
        yAxis: [
          {
            type: 'category',
            axisTick: {
              show: false
            },
            data: ['type1', 'type2', 'type3', 'type4', 'type5', 'type6', 'type7', 'type8','type9']
          }
        ],
        series: [
          {
            name: '处理后',
            type: 'bar',
            stack: 'Total',
            emphasis: {
              focus: 'series'
            },
            data: [320, 302, 341, 374, 390, 450, 420, 360, 320]
          },
          {
            name: '处理前',
            type: 'bar',
            stack: 'Total',
            emphasis: {
              focus: 'series'
            },
            data: [-320, -302, -341, -374, -390, -450, -420, -360, -320]
          }
        ]
      },
    };
  },
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
  margin: 5px 0;
}
.body {
  margin-top: 10px;
}
.data {  
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.hardware {
  height:400px;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 10px;
}
.info {
  padding: 15px;
  display: flex;
  justify-content: space-between;
}
.circle {
  display: inline-block;
  width: 100%;
  height: 100%;
  margin-left: 15px;
}
.disk {
  padding: 10px;
  display: flex;
  justify-content: space-between;
}
.disk-info {
  width: 220px;
  height: 140px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 20px;
} 
.lui-column-bg {
  position: relative;
  width: 100px;
  height: 140px;
  margin-top: 20px;
  background-color: #d1d1d1;
}
.lui-column-bg:before {
  position: absolute;
  content: "";
  display: block;
  height: 20px;
  width: 100%;
  border-radius: 50%;
  top: -10.5px;
  z-index: 1;
  background-color: #e8e8e8;
}

.lui-column-bg:after {
  position: absolute;
  content: "";
  display: block;
  height: 30px;
  width: 100%;
  border-radius: 50%;
  bottom: -15px;
  background-color: #e8e8e8;
}

.lui-inner {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 50%;
  background-color: #6495ED;
  text-align: center;
}
.lui-inner::before {
  position: absolute;
  content: "";
  display: block;
  height: 20px;
  width: 100%;
  background-color: #6495ED;
  border-radius: 50%;
  top: -10.5px;
  z-index: 1;
}
.lui-inner:after {
  position: absolute;
  z-index: 10;
  content: "";
  display: block;
  height: 30px;
  width: 100%;
  border-radius: 50%;
  background-color: #6495ED;
  bottom: -14px;
}
.dangerclass {
  background-color: #e1677a;
}
.successclass {
  background-color: #42b029;
}
.warningclass {
  background-color: #eaaa00;
}


.device {
  margin: 10px;
  padding: 5px;
  display: flex;
  align-items: center;
}
.device-usage {
  width: 75%;
  height: 20px;
  background-color: #f0f0f0;
  border-radius: 5px;
}
.device_label {
  margin-right: 10px;
}
.cpu-usage {
  height: 100%;
  border-radius: 5px;
  background-color: #007bff;
}
.mem-usage {
  height: 100%;
  border-radius: 5px;
  background-color: #DA70D6;
}
.gpu-usage {
  height: 100%;
  border-radius: 5px;
  background-color: #FF1493;
}
</style>
