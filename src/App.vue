<template>
  <v-app>
    <Navbar/>
    <v-navigation-drawer app width="240" v-if="showSideBar">
      <v-card height="100%" dark tile>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="title py-2 text-center">COMPANYNAME</v-list-item-title>
            <p class="text-center text-body-2 mb-3">Levels</p>
            <div class="d-flex justify-center">
              <v-avatar color="primary" size="56" width="60"></v-avatar>
            </div>
            <p class="text-center text-body-2 mt-2">{{ user.name }}</p>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list dense nav>
          <v-list-item v-for="item in iconItems" :key="item.title" link>
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card>
      <!-- -->
    </v-navigation-drawer>
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
