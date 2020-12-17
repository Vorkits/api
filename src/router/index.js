import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Tournaments from '../views/Tournaments.vue'
import Players from '../views/Players.vue'
import Matches from '../views/Matches.vue'
import About from '../views/About.vue'
import Smash from '../views/Smash.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/tournaments',
    name: 'tournaments',
    component: Tournaments
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    //component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/players',
    name: 'players',
    component: Players
  },
  {
    path: '/matches',
    name: 'matches',
    component: Matches
  },
  {
    path: '/smash',
    name: 'smash',
    component: Smash
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
