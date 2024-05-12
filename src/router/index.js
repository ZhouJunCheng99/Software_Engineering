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
    path: "/register",
    name: "register",
    component: () => import("../views/Register.vue"),
    meta: {
      title: '注册界面'
    }
  },
  {
    path: "/Uindex",
    name: "Uindex",
    redirect: "/Uindex/information",

    component: () => import("../views/Uindex.vue"),
    children: [
      {
        path: "/Uindex/information",
        name: "information",
        component: () => import("../views/information/index.vue"),
      },
      {
        path: "/Uindex/underwater",
        name: "underwater",
        component: () => import("../views/underwater/index.vue"),
      },
      {
        path: "/Uindex/datacenter",
        name: "datacenter",
        component: () => import("../views/datacenter/index.vue"),
      },
      {
        path: "/Uindex/intelligent",
        name: "intelligent",
        component: () => import("../views/intelligent/index.vue"),
      },
    ],
  },
  {
    path: "/Aindex",
    name: "Aindex",
    redirect: "/Aindex/information",

    component: () => import("../views/Aindex.vue"),
    children: [
      {
        path: "/Aindex/information",
        name: "information",
        component: () => import("../views/information/index.vue"),
      },
      {
        path: "/Aindex/underwater",
        name: "underwater",
        component: () => import("../views/underwater/index.vue"),
      },
      {
        path: "/Aindex/datacenter",
        name: "datacenter",
        component: () => import("../views/datacenter/index.vue"),
      },
      {
        path: "/Aindex/intelligent",
        name: "intelligent",
        component: () => import("../views/intelligent/index.vue"),
      },
      {
        path: "/Aindex/admin",
        name: "admin",
        component: () => import("../views/admin/index.vue"),
        children: [
          {
            path: "/Aindex/admin/dashboard",
            name: "adminDashboard",
            component: () => import("../views/admin/component/GaugeChart.vue"),
          },
          {
            path: "/Aindex/admin/users",
            name: "adminUsers",
            component: () => import("../views/admin/component/Userdata.vue"),
          },
          {
            path: "/Aindex/admin/situation",
            name: "adminSituation",
            component: () => import("../views/admin/component/Situation.vue"),
          }
        ]
      },
    ],

  },
];
const router = new VueRouter({
  routes,
});

export default router;
