<template>
  <div id="app">
    <img width="300px" alt="Stree Fighter V logo" src="./assets/logo-2.png">
    <router-view></router-view>
  </div>
</template>

<script>

export default {}
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
  background:url("assets/sfv-background-2.jpg") no-repeat center;
  background-size: 100%;
}
</style>
