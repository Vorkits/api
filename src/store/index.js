import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        showSideBar: false,
        token: localStorage.getItem('token') || '',
        user: {
            name: '',
            photo: '',
            level: 0,
            city: '',
            score: '',
            token: '',
            id: '',
            balance: ''
        },
        companyName: 'Company Name',
        levels: [
            { name: 'Total Beginner', abbr: 'T', color: '#467E32' }, { name: 'Beginner', abbr: 'B', color: '#8BC34A' },
            { name: 'Intermediate', abbr: 'I', color: '#F6C02D' }, { name: 'Advanced', abbr: 'A', color: '#EA7A00' },
            { name: 'Pro', abbr: 'P', color: '#BF3B0C' }
        ],
        info: [
            { category: 'Tennis Players', val: '32.111' }, {
                category: 'Tennis Players Chat',
                val: '277.380'
            }, { category: 'Scheduled Matches', val: '105.781' }
        ]
    },
    mutations: {
        setShowSideBar(state, isShowSideBar) {
            state.showSideBar = isShowSideBar
        },
        auth_request(state) {
            state.status = 'loading'
        },
        auth_success(state, token) {
            state.status = 'success'
            state.token = token
        },
        auth_error(state) {
            state.status = 'error'
        },
        logout(state) {
            state.status = ''
            state.token = ''
        },
        set_user(state, user) {
            state.user = user
        }
    },
    actions: {
        getUser({ commit, state }) {
            const token = state.token
            return new Promise((resolve, reject) => {
                const formData = new FormData()
                formData.append('token', token)
                axios.get(`http://82.146.45.20/api/user/get_user`, {
                    params: {
                        token: token
                    }
                })
                    .then(resp => {
                        localStorage.setItem('token', token)
                        axios.defaults.headers.common['Authorization'] = token
                        commit('set_user', resp.data)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('auth_error')
                        localStorage.removeItem('token')
                        reject(err)
                    })
            })
        },
        logout(){
            localStorage.removeItem('token')
        },
        login({ commit, dispatch }, user) {
            console.log(1)
            return new Promise((resolve, reject) => {
                commit('auth_request')

                const formData = new FormData()
                Object.keys(user).forEach((key) => {
                    formData.append(key, user[key])
                })

                axios({ url: 'http://127.0.0.1:5000/api/auth/sign_in', data: formData, method: 'POST' })
                    .then(resp => {
                        commit('auth_success', resp.data.token)
                        dispatch('getUser')
                            .then(resp => {
                                resolve(resp)
                            })
                            .catch(err => {
                                reject(err)
                            })
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('auth_error')
                        localStorage.removeItem('token')
                        reject(err)
                    })
            })
        },
        register({ commit, dispatch }, user) {
            return new Promise((resolve, reject) => {
                commit('auth_request')

                const formData = new FormData()
                Object.keys(user).forEach((key) => {
                    formData.append(key, user[key])
                })

                axios({
                        method: 'post',
                        url: 'http://127.0.0.1:5000/api/auth/create_user',
                        data: formData,
                    })
                    .then(resp => {
                        commit('auth_success', resp.data.token)
                        dispatch('getUser')
                            .then(resp => {
                                resolve(resp)
                            })
                            .catch(err => {
                                reject(err)
                            })
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('auth_error', err)
                        localStorage.removeItem('token')
                        reject(err)
                    })

            })
        },
    },
    getters: {
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status,
        user: state => state.user,
        showSideBar: state => state.showSideBar,
    },
    modules: {}
})