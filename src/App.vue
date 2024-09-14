<!-- src/App.vue -->
<template>
  <div>
    <AppHeader />
    <router-view />
  </div>
</template>

<script>
import AppHeader from "@/components/AppHeader.vue";

export default {
  name: "App",
  components: {
    AppHeader,
  },
};
</script>

<style>
/* Global styles (if any) */
</style>
