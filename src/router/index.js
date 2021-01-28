import Vue from 'vue'
import store from '../store/index.js'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Players from '../views/Players.vue'
import Matches from '../views/Matches.vue'
import About from '../views/About.vue'
import Login from '../views/Login.vue'
import Profile from '../views/Profile.vue'
import Court from '../views/Court.vue'
import courts from '../views/Courts.vue'
import OtherProfile from '../views/OtherProfile.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/OtherProfile/:id',
        name: 'OtherProfile',
        component: OtherProfile
    },
    {
        path: '/Court/:id',
        name: 'Court',
        component: Court
    },
    {
        path: '/courts',
        name: 'courts',
        component: courts
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