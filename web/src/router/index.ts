import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import CustomerList from "@/components/customers/CustomerList.vue";
import RestaurantList from "@/components/restaurants/RestaurantList.vue";
import ReservationList from "@/components/reservations/ReservationList.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/reservations",
    name: "reservations",
    component: ReservationList
  },
  {
    path: "/restaurants",
    name: "restaurants",
    component: RestaurantList
  },
  {
    path: "/customers",
    name: "customers",
    component: CustomerList
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
