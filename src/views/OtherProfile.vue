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
                <div class="level">Level: {{level}}</div>
            </div>
            <div class="matches">
                <div class="title">Information</div>
                <div class="text">Player`s name: {{name}}</div>
                <div class="text">Player`s city: {{city}}</div>
                <div class="text">Player`s level: {{level}}</div>
            </div>
        </div>
   </div>
</template>

<script scoped>
    import axios from 'axios'
    export default {
        data() {
            return {
                response: null,
                photo: null,
                city: null,
                name: null,
                level: 1
            }
        },
        methods: {
        },
        mounted () {
            var Response = null
            var route = this.$route.params.id.split(':')[1]
            axios.get(`http://82.146.45.20/api/user/get_user/${route}`, {
            })
            .then(function (response) {
                Response = response
                console.log(Response)
                
            })
            .catch(function (error) {
                // handle error
                console.log(error)
            })
            setTimeout(() => {
                this.photo = Response.data.photo
                this.city = Response.data.city
                this.name = Response.data.name
                this.level = Response.data.level
            }, 1000)
        },
        computed:{
        }
    }
</script>
<style lang="sass">
*
    border-radius: 10px

.theme--light.v-application
    background-color: #edecec
    .main
        background-color: #edecec
        .prediction
            width: 1280px
            margin: auto
            margin-top: 5%
            margin-bottom: 5%
            display: flex
            align-items: center
            justify-content: center
            background-color: #fb7979
            .text
                width: 80%
                padding: 1vw
                color: white
        .player
            background-color: #f8f8f8
            width: 1280px
            margin: auto
            margin-top: 5%
            margin-bottom: 3%
            justify-content: center
            .profile
                width: 40%
                text-align: center
                align-items: center
                display: flex
                flex-direction: column
                img
                    border-radius: 50%
                    margin-top: 3vh
                    width: 200px
                    height: 200px
                .name
                    margin-top: 2%
                .level
                    margin-top: 3%
                    margin-bottom: 3%
                    padding: 1.6% 7% 1.6% 7%
                    text-align: center
                    max-width: 70%
                    background-color: #9e9e9e
                    color: white
                .friends
                    margin-top: 2%
                    margin-bottom: 8%
                    display: flex
                    flex-direction: column
                    text-align: center
                    .friend
            .matches
                width: 60%
                background-color: white
                .title
                    margin-top: 2%
                    margin-left: 4%
                    font-size: 2em
                .text
                    margin: 3vh 0 4vh 4%
        @media(max-width: 1280px)
            .prediction
                width: 720px
            .player
                width: 720px
                .profile
                    width: 100%
                .matches
                    width: 100%
                    margin-top: 3%
                    display: flex
                    flex-direction: column
                    align-items: center
                    .title
                        margin-left: 0
                    .action-but
                        margin-left: 0
                .image-block
                    width: 65%
                    height: 500px
                    margin: 0 auto
        @media(max-width: 780px)
            .prediction
                width: 100vw
            .player
                width: 100vw
                .profile
                    width: 100%
                .matches
                    width: 100%
                    margin-top: 3%
                    display: flex
                    flex-direction: column
                    align-items: center
                    .title
                        margin-left: 0
                    .action-but
                        margin-left: 0
                .image-block
                    height: 400px
</style>
