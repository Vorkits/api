import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {},
    token: localStorage.getItem('token') || '',
    companyName:'Company Name',
    levels: [
      {name:'Total Beginner', abbr: 'T', color:'#467E32'}, {name: 'Beginner', abbr: 'B', color:'#8BC34A'},
      {name:'Intermediate', abbr: 'I', color:'#F6C02D'}, {name: 'Advanced', abbr: 'A', color:'#EA7A00'},
      {name:'Pro', abbr: 'P', color:'#BF3B0C'}
    ],
    info: [
      {category: 'Tennis Players', val: '32.111'},{category: 'Tennis Players Chat', val: '277.380'},{category: 'Scheduled Matches', val: '105.781'}
    ]
  },
  mutations: {
    auth_request(state){
      state.status = 'loading'
    },
    auth_success(state, token, user){
      state.status = 'success'
      state.token = token
      state.user = user
    },
    auth_error(state){
      state.status = 'error'
    },
    logout(state){
      state.status = ''
      state.token = ''
    },
  },
  actions: {
    login({commit}, user){
      return new Promise((resolve, reject) => {
        commit('auth_request')

        const formData = new FormData()
        Object.keys(user).forEach((key) => {
          formData.append(key, user[key])
        })

        axios({url: '/api/auth/sign_in', data: formData, method: 'POST' })
            .then(resp => {
              const token = resp.data.token
              localStorage.setItem('token', token)
              axios.defaults.headers.common['Authorization'] = token
              commit('auth_success', token, user)
              resolve(resp)
            })
            .catch(err => {
              commit('auth_error')
              localStorage.removeItem('token')
              reject(err)
            })
      })
    },
    register({commit}, user){
      return new Promise((resolve, reject) => {
        commit('auth_request')

        const formData = new FormData()
        Object.keys(user).forEach((key) => {
          formData.append(key, user[key])
        })

        axios({
          method: 'post',
          url: '/api/auth/create_user',
          data: formData,
        })
        .then(resp => {
          debugger
          const token = resp.data.token
          localStorage.setItem('token', token)
          axios.defaults.headers.common['Authorization'] = token
          commit('auth_success', token, user)
          resolve(resp)
        })
        .catch(err => {
          debugger
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
  },
  modules: {
  }
})
