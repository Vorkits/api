<template>
   <div class = "main">
        <div class="prediction">
            <div class="text">MATCH DEADLINE DATE UPDATE: We have further extended the deadline for all matches and tournaments until February 20, 2021.<br>In this way we hope that each of you can return to the field without being excluded from your respective tournament.For those who have the opportunity to play, respecting the regulations and in agreement with the sports center, the matches will be considered valid.</div>
        </div>
        <div class="player">
            <div class = "image-block" id = "image-block" v-if="IsImage">
                <svg @click="IsImage = false" style = "margin-left: 85%; margin-top: 2%" height="32pt" viewBox="0 0 329.26933 329" width="32pt" xmlns="http://www.w3.org/2000/svg"><path d="m194.800781 164.769531 128.210938-128.214843c8.34375-8.339844 8.34375-21.824219 0-30.164063-8.339844-8.339844-21.824219-8.339844-30.164063 0l-128.214844 128.214844-128.210937-128.214844c-8.34375-8.339844-21.824219-8.339844-30.164063 0-8.34375 8.339844-8.34375 21.824219 0 30.164063l128.210938 128.214843-128.210938 128.214844c-8.34375 8.339844-8.34375 21.824219 0 30.164063 4.15625 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921875-2.089844 15.082031-6.25l128.210937-128.214844 128.214844 128.214844c4.160156 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921874-2.089844 15.082031-6.25 8.34375-8.339844 8.34375-21.824219 0-30.164063zm0 0" fill = "white"/></svg>
                <img class = 'image' src = '../assets/default.jpg' id = '1111'>
                <label for="image" style = "color: white">{{fileName}}</label>
                <input type="file" style="display: none" class = "img" id = "image" @change="change1" ref = "text1" required multiple accept="image/*">
                <button class = "but" @click="click">Создать</button>
            </div>
            <div class="profile">
                <div class="photo" @click = "IsImage = true">
                    <img src='../assets/default.jpg' v-if="photo == null">
                    <img :src = "photo" v-else>
                    <div class="overlay"></div>
                </div>
                <div class="name">{{name}}</div>
                <div class="level">Level: {{level}}</div>
            </div>
            <div class="matches">
                <div class="title">Matches</div>
                <div class="action-but">
                    <div class="text">Organize the game by contacting a tennis player from {{city}}</div>
                </div>
            </div>
        </div>
        <div class="infoPl">
            <div class="tennis-players ten">
                <div class="block">
                    <div class="peopleAmount">100000</div>
                    <div class="AmountName">tennis players</div>
                </div>
            </div>
            <div class="tennis-players-chat ten">
                <div class="block">
                    <div class="peopleAmount">300000</div>
                    <div class="AmountName">tennis players chat</div>
                </div>
            </div>
            <div class="scheduled-matches ten">
                <div class="block">
                    <div class="peopleAmount">1000</div>
                    <div class="AmountName">scheduled matches</div>
                </div>
            </div>
        </div>
   </div>
</template>

<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                items: [{
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
                ],
                image: null,
                IsImage: false,
                fileName: 'Выберите фото'
            }
        },
        methods: {
            change1 () {
                var preview = document.getElementById('1111');
                var file = document.querySelector('input[type=file]').files[0];
                var reader = new FileReader();
                this.fileName = document.querySelector('input[type=file]').files[0].name
                reader.onloadend = function () {
                    preview.src = reader.result;
                }

                if (file) {
                    reader.readAsDataURL(file);
                } else {
                    preview.src = "";
                }

                if (this.$refs.text1.files.length === null) this.image = null
                else {
                    this.image = this.$refs.text1.files[0]
                }
            },
            click () {
                // axios.get('http://82.146.45.20/api/user/get_city', {
                //     params: {
                //         city: 'almaty'
                //     }
                // })
                // .then(function (response) {
                //     // handle success
                //     console.log(response);
                // })
                // .catch(function (error) {
                //     // handle error
                //     console.log(error);
                // })
                if (this.image)  {
                    console.log('start')
                    const formData = new FormData()
                    formData.append('image', this.image)
                    const NA = {
                        token: this.token,
                        image: formData
                    }
                    console.log(this.token);
                    axios.post('http://82.146.45.20/api/user/upload_photo', NA, {
                    })
                    .then(function (response) {
                        console.log(response);
                    })
                    .catch(function (error) {
                        console.log(error);
                    })
                }
                this.IsImage = false
            }
        },
        mounted () {
           
        },
        computed:{
            photo(){
                return this.$store.state.user.photo
            },
            city(){
                return this.$store.state.user.city
            },
            token(){
                return this.$store.state.user.token
            },
            name(){
                return this.$store.state.user.name
            },
            level(){
                return this.$store.state.user.level
            }
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
        .infoPl
            text-transform: uppercase
            display: flex
            flex-direction: row
            text-align: center
            width: 1280px
            margin: auto
            margin-top: 1%
            margin-bottom: 5%
            background-color: #dddd
            .ten
                display: flex
                align-items: center
                justify-content: center
            .tennis-players
                width: calc(1280px / 3)
            .tennis-players-chat
                width: calc(1280px / 3)
                text-align: center
            .scheduled-matches
                width: calc(1280px / 3)
                text-align: center
            .block
                width: 90%
                padding: 3%
                margin: 3% 0 3% 0
                border-radius: 10px
                background-color: #e5e5e5
                
        .player
            background-color: #f8f8f8
            display: flex
            width: 1280px
            margin: auto
            margin-top: 5%
            margin-bottom: 3%
            flex-direction: row
            justify-content: center
            .image-block
                background-color: #999999
                position: fixed
                width: 70%
                height: 500px
                margin: -10% auto
                display: flex
                flex-direction: column
                align-items: center
                .image
                    margin-bottom: 5%
                    width: 200px
                    height: 200px
                    border-radius: 50%
                input
                    width: 200px
                .but
                    margin-top: 5%
                    padding: 1%
                    border-radius: 10px
                    background: #f8f8f8
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
                .action-but
                    max-width: 70%
                    margin: 3vh 0 4vh 4%
                    background-color: red
                    text-align: center
                    border-radius: 7px
                    .text
                        color: white
                        padding: 1vw
        @media(max-width: 1280px)
            .prediction
                width: 720px
            .player
                flex-direction: column
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
                    width: 55%
                    height: 400px
                    margin: 0 auto
            .infoPl
                width: 720px
                flex-direction: column
                .tennis-players
                    width: 100%
                .tennis-players-chat
                    width: 100%
                .scheduled-matches
                    width: 100%
        @media(max-width: 780px)
            .prediction
                width: 100vw
            .player
                flex-direction: column
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
                    width: 60%
                    height: 400px
                    margin: 0 auto
            .infoPl
                width: 100vw
</style>
