import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/login",
    name: "login",
    component: () => import("../views/Login.vue"),
  },
  {
    path: "/",
    redirect: "/login",
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
      },
    ],
  },
];
const router = new VueRouter({
  routes,
});

export default router;
