<template>
   <div class = "main">
        <!-- <div class="prediction">
            <div class="text">MATCH DEADLINE DATE UPDATE: We have further extended the deadline for all matches and tournaments until February 20, 2021.<br>In this way we hope that each of you can return to the field without being excluded from your respective tournament.For those who have the opportunity to play, respecting the regulations and in agreement with the sports center, the matches will be considered valid.</div>
        </div> -->
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
                <div class="text"><b>Court`s name:</b> {{name}}</div>
                <div class="text"><b>Court`s city:</b> {{city}}</div>
                <div class="text"><b>Court`s adress:</b> {{adress}}</div>
                <div class="text"><b>Court`s phone:</b> {{phone}}</div>
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
<style lang="sass" scoped>
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
    display: flex
    width: 1280px
    margin: auto
    margin-bottom: 3%
    flex-direction: row
    justify-content: center
    .profile
        width: 40%
        text-align: center
        align-items: center
        float: left
        display: flex
        flex-direction: column
        img
            border-radius: 50%
            margin-top: 3vh
            width: 200px
            height: 200px
        .overlay
            position: absolute
            width: 200px
            height: 200px
            margin-top: -206px
            border-radius: 50%
            cursor: pointer
        .overlay:hover
            background-color: rgba(21, 27, 31, 0.4)
        .name
            margin-top: 2%
            margin-bottom: 5%
            cursor: pointer
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
        width: 100%
        background-color: white
        .title
            margin-top: 2%
            margin-left: 3%
            font-size: 3em
        .text
            margin: 1% 1% 1% 3%
@media(max-width: 1280px)
    .createMatch
        width: 720px
        height: 90vh
        margin-top: 20%
        .courtes
            height: 45vh
    .prediction
        width: 720px
    .player
        width: 720px
        flex-direction: column
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
            .text
                margin: 2vh 0 2vh 0
        .image-block
            width: 65%
            height: 500px
            margin: 0 auto
@media(max-width: 780px)
    .createMatch
        width: 100%
    .prediction
        width: 100vw
    .player
        width: 100vw
        flex-direction: column
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
