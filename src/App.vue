<template>
  <v-app>
    <Navbar />
    <v-navigation-drawer app width="240" v-if="false" >
      <v-card height="100%" dark tile>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="title py-2 text-center">
              COMPANYNAME
            </v-list-item-title>
            <p class="text-center text-body-2 mb-3">Levels</p>
            <div class="d-flex justify-center">
              <v-avatar color="primary" size="56" width="60"></v-avatar>

            </div>
            <p class="text-center text-body-2 mt-2">name</p>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list dense nav>
          <v-list-item v-for="item in items" :key="item.title" link>
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
  import Navbar from '@/components/Navbar'

  export default {
    name: 'App',
    components: {
      Navbar
    },
  };
</script>