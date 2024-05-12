<template>
  <div>
    <div class="env_content">
      <left-content />
      <center-map />
      <right-content />
    </div>
  </div>
</template>

<script>
import centerMap from "./component/info_mid.vue";
import leftContent from "./component/info_left.vue";
import rightContent from "./component/info_right.vue";
export default {
  components: { centerMap, leftContent, rightContent},
};
</script>

<style lang="scss" scoped>
.env_content {
  display: flex;
  justify-content: space-between;
}
</style>
