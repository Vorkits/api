import Vue from 'vue'
import store from '../store/index.js'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Tournaments from '../views/Tournaments.vue'
import Players from '../views/Players.vue'
import Matches from '../views/Matches.vue'
import About from '../views/About.vue'
import Login from '../views/Login.vue'
import Profile from '../views/Profile.vue'

Vue.use(VueRouter)

const routes = [{
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
        path: '/about',
        name: 'about',
        component: About
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/user',
        name: 'user',
        component: Profile,
        meta: {
            showSideBar: true,
            requiresAuth: true
        }
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
    store.commit('setShowSideBar', to.matched.some(record => record.meta.showSideBar))



    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (store.getters.isLoggedIn) {
            next()
            return
        }
        next('/login')
    } else {
        next()
    }
})

export default router