<template>
  <div id="app">
    <img width="96px" alt="Vue logo" src="./assets/logo.png">
    <SFX />
  </div>
</template>

<script>
import SFX from './components/SFX.vue'

export default {
  name: 'App',
  components: {
    SFX
  }
}
</script>

<style>
#app {
  font-family: sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
