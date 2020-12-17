import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
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
  },
  actions: {
  },
  modules: {
  }
})
