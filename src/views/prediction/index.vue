<template>
    <div class="prediction">
      <h2>智能预测</h2>
      <FishGrowthPrediction />
    </div>
  </template>



<script>
import FishGrowthPrediction from "./components/FishGrowthPrediction.vue";

export default {
  components: { FishGrowthPrediction },
};
</script>


<style scoped>
.prediction {
  padding: 20px;
}

h2 {
  font-size: 24px;
  margin-bottom: 20px;
}
</style>
