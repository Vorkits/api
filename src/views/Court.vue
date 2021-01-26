<template>
   <div class = "main">
        <div class="prediction">
            <div class="text">MATCH DEADLINE DATE UPDATE: We have further extended the deadline for all matches and tournaments until February 20, 2021.<br>In this way we hope that each of you can return to the field without being excluded from your respective tournament.For those who have the opportunity to play, respecting the regulations and in agreement with the sports center, the matches will be considered valid.</div>
        </div>
        <div class="player">
            <div class="profile">
                <div class="photo" >
                    <img src='../assets/default.jpg' v-if="photo == null">
                    <img :src = "photo" v-else>
                </div>
                <div class="name">{{name}}</div>
            </div>
            <div class="matches">
                <div class="title">Information</div>
                <div class="text">Court`s name: {{name}}</div>
                <div class="text">Court`s city: {{city}}</div>
                <div class="text">Court`s adress: {{adress}}</div>
                <div class="text">Court`s phone: {{phone}}</div>
            </div>
        </div>
   </div>
</template>

<script scoped>
    import axios from 'axios'
    export default {
        data() {
            return {
                photo: null,
                city: null,
                name: null,
                adress: null,
                phone: null
            }
        },
        methods: {
        },
        mounted () {
            var Response = null
            var route = this.$route.params.id.split(':')[1]
            axios.get(`http://82.146.45.20/api/court/get`, {
                params: {
                    coart_id: route
                }
            })
            .then(function (response) {
                Response = response
                
            })
            .catch(function (error) {
                // handle error
                console.log(error)
            })
            setTimeout(() => {
                this.photo = Response.data.photo
                this.city = Response.data.city
                this.name = Response.data.name
                this.adress = Response.data.addr
                this.phone = Response.data.phone
            }, 2000)
        },
        computed:{
        }
    }
</script>
<style lang="sass">
</style>
