<template>
  <div class="hello">
    <h1>SFX Frame Data</h1>
    <footer>
    Data, assets &copy 2018-2020 Capcom.<br>
    Feedback and support - Source Code - Discord Bot - API</footer>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
* { color: #FFF;}

.hello {
  background-color: rgba(0, 0, 0, 0.8);
  border-radius: .5rem;
  width: 500px;
  margin: auto;
  padding: 2.5rem;
  margin-top: 2rem;
}

h1 {
  margin: 0 auto 20px;
}

h3 {
  margin: 10px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
