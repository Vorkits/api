<template>
  <v-app>
    <Navbar/>
    
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import store from '@/store/index.js'
import {mapGetters} from 'vuex'
import Navbar from '@/components/Navbar'

export default {
  name: 'App',
  data: () => ({
    iconItems: [
      {
        title: 'Home',
        icon: 'mdi-view-dashboard'
      },
      {
        title: 'Tournaments',
        icon: 'mdi-image'
      },
      {
        title: 'Matches',
        icon: 'mdi-help-box'
      },
      {
        title: 'Tennis players',
        icon: 'mdi-help-box'
      },
      {
        title: 'Smash',
        icon: 'mdi-help-box'
      },
      {
        title: 'How does it work',
        icon: 'mdi-help-box'
      },

    ]
  }),
  created() {
    const isLoggedIn = store.getters.isLoggedIn;
    if(isLoggedIn) {
      store.dispatch('getUser')
    }
    this.$axios.interceptors.response.use(undefined, function (err) {
      return new Promise(function () {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
          this.$store.dispatch('logout')
        }
        throw err;
      });
    });
  },
  mounted() {

  },
  components: {
    Navbar
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'user', 'showSideBar']),
  }
};
</script>
