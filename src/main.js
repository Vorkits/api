import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import axios from 'axios';
import Delay from 'vue-delay/src';
import AsyncComputed from 'vue-async-computed';

 
Vue.prototype.$axios = axios;
Vue.config.productionTip = false
const token = localStorage.getItem('token')
if (token) {
  Vue.prototype.$axios.defaults.headers.common['Authorization'] = token
}
Vue.use(AsyncComputed)
Vue.use(Delay)
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
