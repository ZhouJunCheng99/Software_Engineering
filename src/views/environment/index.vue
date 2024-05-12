<template>
  <div>
    <div class="env_content">
      <env-left />
      <div class="vertical_layout">
        <env-map />
        <env-center />
      </div>
      <env-right />
    </div>
  </div>
</template>

<script>
import envLeft from "./components/envLeft.vue";
import envRight from "./components/envRight.vue";
import envCenter from "./components/envCenter.vue";
import envMap from "./components/envMap.vue";
export default {
  components: { envLeft, envCenter, envRight, envMap },
};
</script>

<style scoped>
.env_content {
  display: flex;
  justify-content: space-between;
}
.vertical_layout {
  flex-direction: column;
}
</style>
