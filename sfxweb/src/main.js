import Vue from 'vue'
import App from './App.vue'

// TO DO: Replace titles with Vue router
document.title = "SFX Frame Data"

Vue.config.productionTip = false

new Vue({
  render: function (h) { return h(App) }, 
}).$mount('#app')
