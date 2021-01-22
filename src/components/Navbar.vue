<template>
    <nav>
        <v-app-bar text app dark elevate-on-scroll>
            <v-app-bar-nav-icon class="grey--text" @click="drawer=!drawer"></v-app-bar-nav-icon>
            <v-toolbar-title class="text-uppercase grey--text">
                <span class="font-weight-light">Company</span>
                <span>Name</span>
            </v-toolbar-title>
            <v-spacer/>
            <v-btn v-if="isLoggedIn" v-show="user.name" href="/user" text dark>
              <span>{{ user.name }}</span>
              <v-icon>mdi-login</v-icon>
            </v-btn>
            <router-link to="/login" v-else text dark>
                <span>Login</span>
                <v-icon>mdi-login</v-icon>
            </router-link>
        </v-app-bar>

        <v-navigation-drawer v-model="drawer" class="py-md-4" color="#272727" temporary dark app ma-6>
            <v-list>
                 <v-list-item class="mb-n4">
                    <v-list-item-content class="pa-0 ma-0">
                        <v-list-item-title class="text-center">Levels</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-col cols="12" sm="6" class="py-2 pl-md-8">
                <v-btn-toggle v-model="toggle_none">
                    <v-btn x-small v-for='level in levels' :key=level.abbr :color="level.color">
                        <span>{{level.abbr}}</span>
                    </v-btn>
                </v-btn-toggle>
                </v-col>

                <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
                    <v-list-item-action>
                        <v-icon>{{link.icon}}</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>{{link.text}}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <div class="exit" @click.prevent="logout" v-if="token != ''"><div class="exit-text">EXIT</div></div>
            </v-list>
        </v-navigation-drawer>

    </nav>
</template>

<script>
import {mapGetters} from 'vuex'
export default {
    data(){
        return{
            toggle_none: null,
            drawer:false,
            links: [
                { icon: 'mdi-view-dashboard', text: 'Home', route: '/' },
                { icon: 'mdi-folder', text: 'Tournaments', route: '/tournaments' },
                { icon: 'mdi-run', text: 'Matches', route: '/matches' },
                { icon: 'mdi-account', text: 'Tennis Players', route: '/players' },
                { icon: 'mdi-help', text: 'How does it work', route: '/abour' },
            ]
        }
    },
    methods: {
        logout () {
            this.$store.dispatch('logout')
            .catch(err => {
                console.log(err)
            })
            location.reload()
        },
    },
    computed:{
        ...mapGetters(['isLoggedIn','user']),
        levels(){
            return this.$store.state.levels
        },
        token(){
            return this.$store.state.user.token
        }
    }
}
</script>>

<style>
    .exit{
        width: 100%;
        display: flex;
        justify-content: center;
        margin-top: 3%;
        cursor: pointer;
    }
    .exit-text{
        border: 1px solid red;
        width: 80%;
        text-align: center;
        padding: 3%;
    }
    .exit-text:hover{
        background-color: #5b5b5b;
    }
</style>
