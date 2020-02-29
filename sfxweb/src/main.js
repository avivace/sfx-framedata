import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import routes from './routes'


Vue.use(VueRouter)

const router = new VueRouter({
  routes,
  base: "/sfx-framedata/",
  mode: 'history',
})

Vue.config.productionTip = false

router.afterEach((to, from) => {
  Vue.nextTick(() => {
    document.title = to.meta.title ? `${to.meta.title} | SFX - Frame Data` : 'SFX - Frame Data';
  });
})

new Vue({
  router,
  render: function (h) { return h(App) },
}).$mount('#app')
