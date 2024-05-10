import dataV from '@jiaminghi/data-view';
//引入echart
//4.x 引用方式
import * as echarts from 'echarts';
import Vue from 'vue';
// 按需引入vue-awesome图标
import Icon from 'vue-awesome/components/Icon';
import 'vue-awesome/icons/align-left.js';
import 'vue-awesome/icons/chart-area.js';
import 'vue-awesome/icons/chart-bar.js';
import 'vue-awesome/icons/chart-line.js';
import 'vue-awesome/icons/chart-pie.js';
import BaiduMap from 'vue-baidu-map';
import App from './App.vue';
// 引入全局css
import './assets/scss/style.scss';
import router from './router';
import store from './store';


//5.x 引用方式为按需引用
//希望使用5.x版本的话,需要在package.json中更新版本号,并切换引用方式
//import * as echarts from 'echarts'
Vue.prototype.$echarts = echarts
Vue.config.productionTip = false;//阻止 vue 在启动时生成生产提示。避免无用的体积


// 新加
import vueParticles from 'vue-particles'
import Vcomp from './components/index'
import Toast from './components/toast'
import '@/assets/styles/base.scss'
import '@/assets/styles/common.scss'
import '@/assets/iconfont/iconfont.css'

Vue.use(vueParticles)
Vue.use(Vcomp)

Vue.prototype.$Toast = Toast

// 改标签页名字的,跳转后更改标签页标题
router.beforeEach((to, from, next) => { //路由守卫
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})

// 全局注册
Vue.component('icon', Icon);
Vue.use(dataV);
//申请百度地图key
Vue.use(BaiduMap, { ak: '' })
new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
