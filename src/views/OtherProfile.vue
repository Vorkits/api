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
                <div class="match" @click="IsClick = true">Create Match with {{name}}</div>
            </div>
        </div>
        <div class="createMatch" v-if="IsClick">
            <svg @click="IsClick = false" height="30pt" viewBox="0 0 329.26933 329" width="30pt" xmlns="http://www.w3.org/2000/svg"><path d="m194.800781 164.769531 128.210938-128.214843c8.34375-8.339844 8.34375-21.824219 0-30.164063-8.339844-8.339844-21.824219-8.339844-30.164063 0l-128.214844 128.214844-128.210937-128.214844c-8.34375-8.339844-21.824219-8.339844-30.164063 0-8.34375 8.339844-8.34375 21.824219 0 30.164063l128.210938 128.214843-128.210938 128.214844c-8.34375 8.339844-8.34375 21.824219 0 30.164063 4.15625 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921875-2.089844 15.082031-6.25l128.210937-128.214844 128.214844 128.214844c4.160156 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921874-2.089844 15.082031-6.25 8.34375-8.339844 8.34375-21.824219 0-30.164063zm0 0" fill = "white"/></svg>
            <div class="titleClick">Create Match</div>
            <div class="players">
                <div class="firstPl">
                    <img :src="photo2" class="photoPl">
                    <div class="text" style="font-size: 2em">{{name2}}</div>
                    <div class="text">{{city}}</div>
                </div>
                <div class="space">VS</div>
                <div class="secondPl">
                    <img :src="photo" class="photoPl">
                    <div class="text" style="font-size: 2em">{{name}}</div>
                    <div class="text">{{city}}</div>
                </div>
            </div>
            <div class="courtes">
                <div class="courts" v-for="(court,i) in Courtes" :key = 'i'>
                    <div class = "court">{{court.city}}</div>
                </div>
            </div>
            <div class="create" @click="Created(); IsClick = false">Create Match</div>
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
                level: 1,
                IsClick: false
            }
        },
        methods: {
            Created() {
                console.log(2)
            }
        },
        mounted () {
            var Response = null
            var route = this.$route.params.id.split(':')[1]
            axios.get(`http://82.146.45.20/api/user/get_user/${route}`, {
                params: {
                    token: 'ada3d69b54a34bb0bf136523d037b959'
                }
            })
            .then(function (response) {
                Response = response
                // console.log(Response)
                
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
            name2(){
                return this.$store.state.user.name
            },
            photo2(){
                return this.$store.state.user.photo
            },
        },
        asyncComputed: {
            async Courtes(){
                return new Promise((resolve) => {
                    setTimeout(() => {
                        axios.get(`http://82.146.45.20/api/court/get_all`, {
                        })
                        .then(function (response) {       
                            console.log(response.data)
                            resolve(response.data)
                        })
                        .catch(function (error) {
                            console.log(error)
                        })
                    }, 1000)
                })
            }
        }
    }
</script>
<style lang="sass">
*
    border-radius: 10px

::-webkit-scrollbar
  width: 15px

::-webkit-scrollbar-track
  background: #f1f1f1
 
::-webkit-scrollbar-thumb
  background: #888

::-webkit-scrollbar-thumb:hover
  background: #555

.theme--light.v-application
    background-color: #edecec
    .main
        background-color: #edecec
        display: flex
        flex-direction: column
        justify-content: center
        align-items: center
        .createMatch
            width: 1280px
            height: 80vh
            background-color: #bdbdbd
            position: absolute
            margin: 0 auto
            margin-top: 10%
            display: flex
            flex-direction: column
            align-items: center
            .courtes
                overflow: auto
                width: 100%
                height: 300px
                text-align: center
                .court
                    margin-left: 15px
            .create
                padding: 1% 3% 1% 3%
                margin-bottom: 1%
                background-color: #6d6d6d
                color: white
                margin-top: 3%
                cursor: pointer
                &:hover
                    background-color: #929292
            .space
                text-align: center
                font-size: 2em
            svg
                margin-left: 95%
                margin-top: 1%
                margin-bottom: 1%
                @media(max-width: 1280px)
                    margin-left: 90%
                @media(max-width: 720px)
                    margin-left: 80%
                @media(max-width: 630px)
                    margin-left: 70%
                @media(max-width: 555px)
                    margin-left: 60%
                @media(max-width: 485px)
                    margin-left: 50%
                @media(max-width: 416px)
                    margin-left: 40%
            .titleClick
                font-size: 2em
            .players
                display: flex
                flex-direction: row
                align-items: center
                width: 100%
                @media(max-width: 780px)
                    width: 100vw
                .photoPl
                    width: 140px
                    height: 140px
                    border-radius: 50%
                    @media(max-width: 780px)
                        width: 100px
                        height: 100px
                .firstPl
                    width: 40%
                    text-align: center
                .secondPl
                    width: 40%
                    text-align: center
                .space
                    width: 20%
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
            display: flex
            flex-direction: row
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
            .matches
                width: 60%
                background-color: white
                .title
                    margin-top: 2%
                    margin-left: 3%
                    font-size: 2em
                .text
                    margin: 3vh 0 4vh 3%
                .match
                    margin: 3vh 0 4vh 3%
                    text-align: center
                    width: 30%
                    padding: 1% 3% 1% 3%
                    background-color: red
                    color: white
                    cursor: pointer
                    &:hover
                        background-color: #ff3a3a
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
                        margin: 3vh 0 4vh 0
                .image-block
                    width: 65%
                    height: 500px
                    margin: 0 auto
        @media(max-width: 780px)
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
