import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/login",
    name: "login",
    component: () => import("../views/Login.vue"),
    meta: {
      title: '登录界面'
    }
  },
  {
    path: "/",
    redirect: "/login",
  },
  {
    path: "/index",
    name: "index",
    redirect: "/index/traffic",

    component: () => import("../views/index.vue"),
    children: [
      {
        path: "/index/traffic",
        name: "traffic",
        component: () => import("../views/traffic/index.vue"),
      },
      {
        path: "/index/population",
        name: "population",
        component: () => import("../views/population/index.vue"),
      },
      {
        path: "/index/environment",
        name: "environment",
        component: () => import("../views/environment/index.vue"),
      },
      {
        path: "/index/economy",
        name: "economy",
        component: () => import("../views/economy/index.vue"),
      },
    ],

  },
];
const router = new VueRouter({
  routes,
});

export default router;
