<template>
  <div class="content">
    <div class="body">
      <div class="body_table1">
        <div>
        <dv-border-box-6>
          <Echart :options="options3" height="400px" width="720px" />
        </dv-border-box-6>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Echart from "@/common/echart/index.vue";
export default {
  components: { Echart },
  data() {
    return {
      options3 : {
        title: {
          text: '数据类型占比'
        },
       radar: {
          indicator: [
            { name: 'type1', max: 6500 },
            { name: 'type2', max: 16000 },
            { name: 'type3', max: 30000 },
            { name: 'type4', max: 38000 },
            { name: 'type5', max: 52000 },
            { name: 'type6', max: 25000 }
          ]
        },
        series: [
          {
            name: 'Budget vs spending',
            type: 'radar',
            data: [
              {
                value: [4200, 3000, 20000, 35000, 50000, 18000],
                name: 'Allocated Budget'
              },
            ]
          }
        ]
      },
    };
  },
};
</script>

<style scoped>
.content {
  width: 38%;
}
.body {
  margin-top: 10px;
}
.body_table1 {
  display: flex;
}
</style>
