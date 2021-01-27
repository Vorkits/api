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

            <div class = "End-block" id = "end-block" v-if="IsEnd">
                <svg @click="IsEnd = false" style = "margin-left: 85%; margin-top: 2%" height="32pt" viewBox="0 0 329.26933 329" width="32pt" xmlns="http://www.w3.org/2000/svg"><path d="m194.800781 164.769531 128.210938-128.214843c8.34375-8.339844 8.34375-21.824219 0-30.164063-8.339844-8.339844-21.824219-8.339844-30.164063 0l-128.214844 128.214844-128.210937-128.214844c-8.34375-8.339844-21.824219-8.339844-30.164063 0-8.34375 8.339844-8.34375 21.824219 0 30.164063l128.210938 128.214843-128.210938 128.214844c-8.34375 8.339844-8.34375 21.824219 0 30.164063 4.15625 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921875-2.089844 15.082031-6.25l128.210937-128.214844 128.214844 128.214844c4.160156 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921874-2.089844 15.082031-6.25 8.34375-8.339844 8.34375-21.824219 0-30.164063zm0 0" fill = "white"/></svg>
                <div class="score">
                    <div class="YS">
                        <div class="YSText">Your Score</div>
                        <input type="number" v-model="Firnumber">
                    </div>
                    <div class="OS">
                        <div class="OSText">Your Opponent`s Score</div>
                        <input type="number" v-model="Secnumber">
                    </div>
                </div>
                <button class = "but" @click="clickEnd">End</button>
            </div>

            <div class = "change-block" id = "change-block" v-if="IsChange">
                <svg @click="IsChange = false" height="20pt" viewBox="0 0 329.26933 329" width="20pt" xmlns="http://www.w3.org/2000/svg"><path d="m194.800781 164.769531 128.210938-128.214843c8.34375-8.339844 8.34375-21.824219 0-30.164063-8.339844-8.339844-21.824219-8.339844-30.164063 0l-128.214844 128.214844-128.210937-128.214844c-8.34375-8.339844-21.824219-8.339844-30.164063 0-8.34375 8.339844-8.34375 21.824219 0 30.164063l128.210938 128.214843-128.210938 128.214844c-8.34375 8.339844-8.34375 21.824219 0 30.164063 4.15625 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921875-2.089844 15.082031-6.25l128.210937-128.214844 128.214844 128.214844c4.160156 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921874-2.089844 15.082031-6.25 8.34375-8.339844 8.34375-21.824219 0-30.164063zm0 0" fill = "white"/></svg>
                <input type="text" v-model="NewVal" id = '1'>
                <button class = "but white2" @click="clickChange">Изменить</button>
            </div>

            <div class="modalBalance" v-show="modalBalanceToggle">
                <svg @click="modalBalanceToggle = false" height="15pt" viewBox="0 0 329.26933 329" width="15pt" xmlns="http://www.w3.org/2000/svg"><path d="m194.800781 164.769531 128.210938-128.214843c8.34375-8.339844 8.34375-21.824219 0-30.164063-8.339844-8.339844-21.824219-8.339844-30.164063 0l-128.214844 128.214844-128.210937-128.214844c-8.34375-8.339844-21.824219-8.339844-30.164063 0-8.34375 8.339844-8.34375 21.824219 0 30.164063l128.210938 128.214843-128.210938 128.214844c-8.34375 8.339844-8.34375 21.824219 0 30.164063 4.15625 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921875-2.089844 15.082031-6.25l128.210937-128.214844 128.214844 128.214844c4.160156 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921874-2.089844 15.082031-6.25 8.34375-8.339844 8.34375-21.824219 0-30.164063zm0 0" fill = "white"/></svg>
                <label for="addBalance">Enter the replenishment amount:</label>
                <input v-model="inputBalance" type="number" id="addBalance">
                <PayPal
                    :amount="String(inputBalance)"
                    currency="USD"
                    :client="credentials"
                    @payment-completed="payment_completed_cb"
                    env="sandbox"
                ></PayPal>
            </div>

            <div class="profile">
                <div class="photo" @click = "IsImage = true">
                    <img src='../assets/default.jpg' id = 'NewPhoto' v-if="photo == null">
                    <img :src = "photo" id = 'NewPhoto' v-else>
                    <div class="overlay"></div>
                </div>
                <div class="name" style="font-size: 1.7em;" @click = 'IsChange = true; Val = "name"'>Name: {{name}}</div>
                <div class="player-city" style="font-size: 1.1em;" @click = 'IsChange = true; Val = "city"'>City: {{city}}</div>
                <div class="level">Level: {{level}}</div>
                <div class="balance">
                    Balance: {{ score }}$
                    <div class="icon-add" @click="openModalWindow">+</div>
                </div>
            </div>
            <div class="matches">
                <div class="titleM">Matches</div>
                <div class="titleM">
                    <div class="choose green2" v-if="IsMatch == 'current'">Current</div>
                    <div class="choose red2" @click="IsMatch = 'current'" v-else>Current</div>
                    <div class="choose green2" v-if="IsMatch == 'finished'"> Finished</div>
                    <div class="choose red2" @click="IsMatch = 'finished'" v-else>Finished</div>
                </div>

                <div class="matches" v-for="(element, b) in matches" :key="b">
                    <div class="match2" v-if="element.status == 'start' && IsMatch == 'current'">
                            <div class="time">{{element.time}}</div>
                        <div class="players">
                            <div class="match-player">
                                <div class="player-image"><img :src = "element.player1.photo"></div>
                                <div class="player-name">{{element.player1.name}}</div>
                                <div class="player-city">{{element.player1.city}}</div>
                                <div class="player-level">level: {{element.player1.level}}</div>
                            </div>
                                <div class="between">CourtName</div>
                            <div class="match-player">
                                <div class="player-image"><img :src = "element.player2.photo"></div>
                                <div class="player-name">{{element.player2.name}}</div>
                                <div class="player-city">{{element.player2.city}}</div>
                                <div class="player-level">Level: {{element.player2.level}}</div>
                            </div>
                        </div>
                        <div class="MatchEnd">
                            <div class="End" @click = "IsEnd = true; CurrentId = b">End</div>
                        </div>
                    </div>
                    <div class="match2" v-else-if="element.status == 'finished' && IsMatch == 'finished'">
                                <div class="time">{{element.time}}</div>
                            <div class="players">
                                <div class="match-player">
                                    <div class="player-score">{{element.score1}}</div>
                                    <div class="player-image"><img :src = "element.player1.photo"></div>
                                    <div class="player-name">{{element.player1.name}}</div>
                                    <div class="player-city">{{element.player1.city}}</div>
                                    <div class="player-level">level: {{element.player1.level}}</div>
                                </div>
                                    <div class="between">CourtName<br><b style="font-size: 1.5em">Score</b></div>
                                <div class="match-player">
                                    <div class="player-score">{{element.score2}}</div>
                                    <div class="player-image"><img :src = "element.player2.photo"></div>
                                    <div class="player-name">{{element.player2.name}}</div>
                                    <div class="player-city">{{element.player2.city}}</div>
                                    <div class="player-level">Level: {{element.player2.level}}</div>
                                </div>
                            </div>
                    </div>
                </div>

                <a class="action-but" href="/matches">
                    <div class="text2">Organize the game by contacting a tennis player from {{city}}</div>
                </a>
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
    import PayPal from 'vue-paypal-checkout'
    export default {
        data() {
            return {
                image: null,
                IsMatch: 'current',
                IsImage: false,
                fileName: 'Выберите фото',
                nameUs: null,
                IsEnd: false,
                Firnumber: 0,
                Secnumber: 0,
                IsChange: false,
                Val: null,
                CurrentId: null,
                modalBalanceToggle: false,
                inputBalance: 10,
                credentials: {
                    sandbox: 'AfA-qkSiJVNQDYSSucQlEGrzR0tGAagOnxCf9nW2AFhqtsH_8Tsv9a9KyPIGSYa9MlPFM_jjWMToeOUO',
                    production: 'AQERBcxNqb3kwmgFLESTMQsJh5qK1EafQIANBc327-NU0wxn3HKCG8a1vnjmdkEg8WcSGMswdfWrhkKU'
                }
            }
        },
        components: {
            PayPal
        },
        methods: {
            payment_completed_cb(res) {
                console.log('completed', res)
                var CurrentPay = res.transactions[0].amount.total
                const formData = new FormData()
                    formData.append('token', this.token)
                    formData.append('field', 'score')
                    formData.append('value', parseInt(CurrentPay) + parseInt(this.score))
                    axios.post('http://82.146.45.20/api/user/change_field', formData, {
                        headers: {
                        'Content-Type': 'multipart/form-data'
                        }
                    })
                window.location.reload()
            },
            openModalWindow () {
                this.modalBalanceToggle = true
            },
            clickChange() {
                const formData = new FormData()
                var NewVal = document.getElementById('1').value

                    formData.append('token', this.token)
                    formData.append('field', this.Val)
                    formData.append('value', NewVal)
                    axios.post('http://82.146.45.20/api/user/change_field', formData, {
                        headers: {
                        'Content-Type': 'multipart/form-data'
                        }
                    })
            },
            change1 () {
                var preview = document.getElementById('1111');
                var preview2 = document.getElementById('NewPhoto');
                var file = document.querySelector('input[type=file]').files[0];
                var reader = new FileReader();
                this.fileName = document.querySelector('input[type=file]').files[0].name
                reader.onloadend = function () {
                    preview.src = reader.result;
                    preview2.src = reader.result;
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
                if (this.image)  {
                    const formData = new FormData()
                    formData.append(this.token, this.image)
                    axios.post('http://82.146.45.20/api/user/upload_photo', formData, {
                        headers: {
                        'Content-Type': 'multipart/form-data'
                        }
                    })
                    // .then(function (response) {
                    //     // console.log(response);
                    // })
                    .catch(function (error) {
                        console.log(error);
                    })
                }
                this.IsImage = false
            },
            clickEnd () {
                const formData = new FormData()
                formData.append('match_id', this.CurrentId)
                formData.append('score1', this.Firnumber)
                formData.append('score2', this.Secnumber)
                axios.post('http://82.146.45.20/api/games/finish', formData, {
                    headers: {
                    'Content-Type': 'multipart/form-data'
                    }
                })
                // .then(function () {
                //     location.reload()
                // })
                .catch(function (error) {
                    console.log(error);
                })
            }
        },
        mounted() {
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
            },
            Id(){
                return this.$store.state.user.id
            },
            score(){
                return this.$store.state.user.score
            }
        },
        asyncComputed: {
            // async cityUser(){
            //     console.log(this.path)
            //     return new Promise((resolve) => {
            //         setTimeout(() => {
            //             axios.get(`http://82.146.45.20/api/user/get_user/${this.path}`, {
            //             })
            //             .then(function (response) {
            //                 resolve(response.data.city)
            //             })
            //             .catch(function (error) {
            //                 console.log(error)
            //             })
            //         }, 3000)
            //     })
            // },
            async matches(){
                return new Promise((resolve) => {
                    setTimeout(() => {
                        const formData = new FormData()
                        formData.append('id', this.Id)
                        
                        axios.post('http://82.146.45.20/api/games/get_users_match', formData, {
                            headers: {
                            'Content-Type': 'multipart/form-data'
                            }
                        })
                        .then(function (response) {
                            console.log(response.data.data)
                            resolve(response.data.data)
                        })
                        .catch(function (error) {
                            console.log(error)
                        })
                    }, 3000)
                })
            },
        }
    }
</script>
<style lang="sass" scoped>
*
    border-radius: 10px
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
            margin-bottom: 3%
            flex-direction: row
            justify-content: center
            .change-block
                background-color: grey
                display: flex
                flex-direction: column
                align-items: center
                svg
                    margin-left: 80%
                    margin-top: 2%
                    margin-bottom: 3%
                input
                    background-color: white
                .white2
                    color: white
                    background-color: #808080
            .image-block
                background-color: #999999
                position: fixed
                width: 60%
                height: 500px
                margin: -10% auto
                display: flex
                flex-direction: column
                align-items: center
                z-index: 10
                .image
                    width: 200px
                    height: 200px
                    border-radius: 50%
                label
                    margin-top: 2%
                    padding: 2%
                    &:hover
                        background-color: #6d6d6d
                input
                    width: 200px
                .but
                    margin-top: 5%
                    padding: 1%
                    border-radius: 10px
                    background: #f8f8f8
            .End-block
                background-color: #999999
                position: fixed
                width: 1280px
                height: 300px
                margin: -10% auto
                display: flex
                flex-direction: column
                align-items: center
                z-index: 10
                .score
                    display: flex
                    width: 80%
                    flex-direction: row
                    align-items: flex-end
                    .YS
                        display: flex
                        width: 40%
                        text-align: center
                        flex-direction: column
                        .YSText
                            font-size: 1.1em
                            color: white
                        input
                            background-color: white
                            text-align: center
                            border: none
                    .OS
                        display: flex
                        text-align: center
                        width: 40%
                        flex-direction: column
                        margin-left: 20%
                        .OSText
                            font-size: 1.1em
                            color: white
                        input
                            background-color: white
                            text-align: center
                            border: none

                .but
                    margin-top: 5%
                    padding: 1% 6% 1% 6%
                    border-radius: 10px
                    background: #f8f8f8
            .modalBalance
                position: fixed
                width: 30%
                height: 25%
                background-color: darken(#ddd, 12.5%)
                border-radius: 10px
                left: 50%
                top: 50%
                transform: translate(-50%, -50%)
                z-index: 1000000000
                display: flex
                flex-direction: column
                justify-content: space-evenly
                align-items: center
                font-family: 'Roboto', sans-serif
                font-weight: 300
                label
                    font-size: 1.5rem
                    width: 100%
                    text-align: left
                    padding-left: 5%
                input
                    width: 60%
                    text-align: center
                    background-color: #fff
                    outline: none
                svg
                    position: absolute
                    right: 0
                    top: 0
                    cursor: pointer
            .profile
                width: 40%
                text-align: center
                align-items: center
                float: left
                display: flex
                flex-direction: column
                position: relative
                max-height: 500px
                .player-city
                    cursor: pointer
                .balance
                    height: 50px
                    display: flex
                    justify-content: center
                    align-items: center
                    .icon-add
                        width: 40px
                        height: 40px
                        font-size: 2rem
                        margin-left: 2%
                        font-weight: 200
                        border-radius: 50%
                        box-shadow: inset 0 0 8px 1px rgba(0, 0, 0, 0.1)
                        display: flex
                        justify-content: center
                        align-items: center
                        cursor: pointer
                img
                    border-radius: 50%
                    margin-top: 3vh
                    width: 200px
                    height: 200px
                .overlay
                    width: 200px
                    height: 200px
                    margin-top: -206px
                    border-radius: 50%
                    cursor: pointer
                .overlay:hover
                    background-color: rgba(21, 27, 31, 0.4)
                .name
                    margin-top: 2%
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
                .titleM
                    margin-top: 2%
                    text-align: center
                    font-size: 2em
                    display: flex
                    flex-direction: row
                    align-items: center
                    justify-content: center
                    .green2
                        color: #5eca5e
                        &:hover
                            color: #3c863c
                    .red2
                        color: #bd5b5b
                        &:hover
                            color: #ce1e1e
                    .choose
                        padding: 2%
                        cursor: pointer
                .match2
                    border: 1px solid red
                    width: 90%
                    display: flex
                    flex-direction: column
                    align-items: center
                    justify-content: center
                    margin-left: 5%
                    @media (max-width: 1280px)
                        margin-left: 0
                    .time
                        font-size: 2em
                    .players
                        display: flex
                        flex-direction: row
                        width: 100%
                        .match-player
                            margin-top: 3vh
                            display: flex
                            flex-direction: column
                            align-items: center
                            justify-content: center
                            width: 40%
                            .player-image
                                img
                                    width: 100px
                                    height: 100px
                                    border-radius: 50%
                            .player-name
                                font-size: 1.5em
                            .player-score
                                font-size: 1.7em
                            .player-level
                                margin-top: 3%
                                margin-bottom: 3%
                                padding: 1.6% 7% 1.6% 7%
                                text-align: center
                                max-width: 70%
                                background-color: #5d5d5d
                                color: white
                        .between
                            width: 20%
                            text-align: center
                    .MatchEnd
                        display: flex
                        align-items: center
                        justify-content: center
                        width: 100%
                        text-align: center
                        margin-bottom: 1%
                        .End
                            width: 20%
                            font-size: 1.3em
                            background-color: #ff5252
                            padding: 1%
                            cursor: pointer
                            color: white
                            &:hover
                                background-color: #ff1818
                .action-but
                    max-width: 90%
                    display: flex
                    flex-direction: column
                    text-decoration: none
                    margin: 3vh 0 4vh 5%
                    background-color: #ff5252
                    text-align: center
                    cursor: pointer
                    .text2
                        color: white
                        padding: 1vw
                    &:hover
                         background-color: #ff1818
                .textInfo
                    margin: 2vh 0 2vh 3%
        @media(max-width: 1280px)
            .prediction
                width: 720px
            .player
                flex-direction: column
                width: 720px
                .profile
                    width: 100%
                    .player-city
                        cursor: pointer
                .change-block
                    svg
                        margin-left: 90%
                .matches
                    width: 100%
                    margin-top: 3%
                    display: flex
                    flex-direction: column
                    align-items: center
                    .titleM
                        margin-left: 0
                        text-align: center
                    .action-but
                        width: 90%
                        margin: 1vh 0 1vh 0
                        .textInfo
                            margin: 3vh 0 4vh 0
                .image-block
                    top: 40%
                    width: 720px
                    height: 450px
                .End-block
                    top: 40%
                    width: 720px
                    height: 300px
            .infoPl
                width: 720px
                flex-direction: column
                .tennis-players
                    width: 100%
                .tennis-players-chat
                    width: 100%
                .scheduled-matches
                    width: 100%
        @media(max-width: 760px)
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
                    .titleM
                        margin-left: 0
                    .action-but
                        margin-left: 0
                .image-block
                    top: 40%
                    width: 100%
                    height: 400px
                .End-block
                    top: 40%
                    width: 100%
                    height: 300px
            .infoPl
                width: 100vw
</style>
