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
                <div class="level">Level: {{level}}</div>
            </div>
            <div class="matches2">
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
            <label for="appt">Choose a time for your meeting:</label>
            <input type="time" id="appt" v-model="time" name="appt" required>
            <label for="appt2">Choose number of houres:</label>
            <input type="number" class = "m" id="appt2" v-model="houres" required>
            <div class="players">
                <div class="firstPl">
                    <a v-bind:href="'/OtherProfile/:' + myId">
                        <img :src="photo2" class="photoPl">
                    </a>
                    <div class="text" style="font-size: 2em">{{name2}}</div>
                    <div class="text">{{city}}</div>
                </div>
                <div class="space">VS</div>
                <div class="secondPl">
                    <a v-bind:href="'/OtherProfile/:' + Idd">
                        <img :src="photo" class="photoPl">
                    </a>
                    <div class="text" style="font-size: 2em">{{name}}</div>
                    <div class="text">{{city}}</div>
                </div>
            </div>
            <div class="CourtesTit" style="font-size: 3em">Courtes</div>
            <div class="courtes">
                <div class="courts" v-for="(court,i) in Courtes" :key = 'i'>
                    <div class = "court">
                        <a class="courtPhoto" v-bind:href="'/Court/:' + court.id"><img :src="court.photo"></a>
                        <div class="courtInfo">
                            <div class="courtName">{{court.name}}</div>
                            <div class="courtCity">{{court.city}}</div>
                            <div class="courtAdress">{{court.addr}}</div>
                            <div class="courtCost">{{court.cost}}$</div>
                            <div class="courtbut" @click="IsClick = true; CourtId = court.id; cost = court.cost">Choose that court</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="create" @click="Created()">Create Match</div>
        </div>
   </div>
</template>

<script>
    import axios from 'axios'
    import Swal from 'sweetalert2'
    export default {
        data() {
            return {
                response: null,
                photo: null,
                city: null,
                name: null,
                level: 1,
                IsClick: false,
                time: null,
                CourtId: null,
                Id: null,
                houres: null,
                cost: null,
                Idd: null
            }
        },
        methods: {
            Created() {
                if (this.balance >= this.houres * this.cost && this.time != null && this.CourtId != null && this.houres != null && this.houres > 0) {
                    const formData = new FormData()
                        formData.append('player1_id', this.Id)
                        formData.append('player2_id', this.UserId)
                        formData.append('time', this.time)
                        formData.append('coart_id', this.CourtId)
                        formData.append('type', '1')
                        formData.append('hours', this.houres)
                        console.log('aaaa')
                        axios.post('http://82.146.45.20/api/games/create', formData, {
                            headers: {
                            'Content-Type': 'multipart/form-data'
                            }
                        })
                        .catch(function (error) {
                            console.log(error)
                        })
                    setTimeout(() => {
                        const formData2 = new FormData()
                        formData2.append('token', this.token)
                        formData2.append('field', 'balance')
                        formData2.append('value', parseInt(this.balance) - (this.houres * this.cost))
                        axios.post('http://82.146.45.20/api/user/change_field', formData2, {
                            headers: {
                            'Content-Type': 'multipart/form-data'
                            }
                        })
                        .then(function(){
                            Swal.fire('Success', `Match has been created`, 'success')
                            document.location.href = "/user";
                            })
                    }, 1000);
                } else if(this.balance < this.houres * this.cost){
                    Swal.fire('Error', `Your Balance is too low`, 'error')
                } else if(this.time == null){
                    Swal.fire('Error', 'Choose the correct time', 'error')
                } else if(this.CourtId == null){
                    Swal.fire('Error', `Choose the correct court`, 'error')
                } else if(this.houres == null || this.houres <= 0){
                    Swal.fire('Error', `Choose correct duration of the match`, 'error')
                } else{
                    Swal.fire('Error', `Big Error`, 'error')
                }
            }
        },
        mounted () {
            var Response = null
            var route = this.$route.params.id.split(':')[1]
            this.Id = route
            axios.get(`http://82.146.45.20/api/user/get_user/${route}`, {
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
                this.Idd = Response.data.id
                this.level = Response.data.level
            }, 3000)
        },
        computed:{
            name2(){
                return this.$store.state.user.name
            },
            myId(){
                return this.$store.state.user.id
            },
            photo2(){
                return this.$store.state.user.photo
            },
            token() {
                return this.$store.state.user.token
            },
            balance(){
                return this.$store.state.user.balance
            }
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
            },
            async UserId() {
                return new Promise((resolve) => {
                    setTimeout(() => {
                        axios.get(`http://82.146.45.20/api/user/get_user`, {
                        params: {
                            token: this.token
                        }
                        })
                        .then(function (response) {
                            resolve(response.data.id)
                        })
                        .catch(function (error) {
                            console.log(error)
                        })
                    }, 2000)
                })
            }
        }
    }
</script>
<style lang="sass">

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
        align-items: center
        .createMatch
            width: 1280px
            background-color: #bdbdbd
            position: absolute
            margin: 0 auto
            display: flex
            flex-direction: column
            align-items: center
            input
                background-color: grey
                padding: 1% 4% 1% 4%
                border-radius: 10px
            .m
                padding:  0 0 0 0
                background-color: grey
                border-radius: 10px
                text-align: center
            .courtes
                overflow: auto
                width: 100%
                height: 40vh
                text-align: center       
                .court
                    margin-left: calc(15px + 10vw)
                    border: 1px solid #636363
                    display: flex
                    flex-direction: row
                    margin-top: 3vh
                    width: 70%
                    .courtPhoto
                        width: 30%
                        border-right: 2px solid #808080
                        border-radius: 0%
                        overflow: hidden
                        img
                            padding: 5%
                            width: 100px
                            height: 100px
                            border-radius: 50%
                    .courtInfo
                        width: 70%
                        display: flex
                        flex-direction: column
                        align-items: center
                        .courtbut
                            cursor: pointer
                            background-color: #757575
                            padding: 1% 3% 1% 3%
                            width: 40%
                            margin-bottom: 1vh
                            &:hover
                                background-color: #948181

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
                margin-bottom: -1%
                @media(max-width: 1280px)
                    margin-left: 90%
            .titleClick
                font-size: 2em
                margin-top: -2%
            .players
                display: flex
                flex-direction: row
                align-items: center
                width: 100%
                @media(max-width: 780px)
                    width: 100vw
                .photoPl
                    width: 100px
                    height: 100px
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
            .matches2
                width: 60%
                background-color: white
                .title
                    margin-top: 2%
                    margin-left: 3%
                    font-size: 2em
                .text
                    margin: 3vh 0 4vh 3%
                .match
                    margin: 3vh 3vh 4vh 3vh
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
                .matches2
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
            .createMatch
                width: 100%
            .prediction
                width: 100vw
            .player
                width: 100vw
                flex-direction: column
                .profile
                    width: 100%
                .matches2
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
