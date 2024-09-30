<template>
  <div id="app">
    <TaskManager />
  </div>
</template>

<script>
import TaskManager from "./components/TaskManager.vue";

export default {
  name: "App",
  components: {
    TaskManager,
  },
};
</script>

<style scoped>
#app {
  text-align: center;
  background: linear-gradient(135deg, #f5f5f5, #e2e8f0);
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
