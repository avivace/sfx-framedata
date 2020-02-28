<template>
  <div id="app">
    <img width="300px" alt="Stree Fighter V logo" src="./assets/logo.png">
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
* {
  box-sizing: border-box;
}

html, body {
  margin: 0;
  padding: 0;
}

#app {
  font-family: sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding-top: 60px;

  width: 100%;
  height: 100vh;
  background:url("assets/sfv-background.jpg");
}
</style>
