<template>
  <div class="wrapper">
    <div class="front">
      <section class="first">
        <div class="label">Near:</div>
        <div class="content-wrapper">
          <div class="svg-bundle">
            <div class="svg-fix">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-geo-alt-fill" viewBox="0 0 16 16">
              <path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/>
            </svg></div>
            <input @keypress.enter="getCourts" v-model="currentCity" placeholder="insert your address" type="text" id="Near">
          </div>
          <div @click="getCourts" class="search-button">
            Search
          </div>
        </div>
      </section>
      <section v-if="responseUsers.length !== 0" class="pre-second">
        found {{ responseUsers.length }} tennis players
      </section>
      <section class="second">
        <courtCard
          class="userCard"
          v-for="userData in showedUsers"
          :key="userData.token"
          :userData="userData"
        />
      </section>
      <section v-if="responseUsers.length > 30 && responseUsers.length !== showedUsers.length" class="third">
        <div @click="showMoreUsers" class="showMoreButton">
          Show More
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import courtCard from '@/components/CourtCard.vue'
export default {
  name: 'Players',
  data: () => ({
    currentCity: null,
    searchCurrentType: true,
    responseUsers: new Array(),
    showedUsers: new Array(),
    inFindProcess: true
  }),
  components: {
    courtCard
  },
  methods: {
    showMoreUsers () {
      this.showedUsers = this.showedUsers.concat(this.responseUsers.slice(this.showedUsers.length, this.showedUsers.length + 30))
    },
    async getCourts () {
      if (this.currentCity && this.inFindProcess) {
        this.inFindProcess = false
        this.responseUsers = new Array()
        this.showedUsers = new Array()
        await axios.get(`http://82.146.45.20/api/user/get_city?city=${this.currentCity}`)
          .then(async response => {
            for (const userId in response.data) {
              const element = response.data[userId]
              if (element.id) {
                await axios.get(`http://82.146.45.20/api/user/get_user/${element.id}`)
                  .then(outResponse => {
                    console.log(outResponse.data)
                    this.responseUsers.push(outResponse.data)
                    if (this.responseUsers.length <= 30) {
                      this.showedUsers.push(outResponse.data)
                    }
                  })
                  .catch(err => {
                    console.log(err)
                  })
              }
            }
          })
          .catch(err => {
            console.log(err)
          })
        this.inFindProcess = true
      }
    }
  }
}
</script>

<style lang="sass" scoped>
$maxWidth: 1280

@mixin adaptive-font($pcSize, $mobSize)
  $addSize: $pcSize - $mobSize
  $addMobSize: $addSize + $addSize * 0.7
  @media (max-width: 767px)
    font-size: calc( #{$mobSize + px} + #{$addMobSize} * ((100vw - 320px) / #{$maxWidth}) )
  @media (min-width: 767px)
    font-size: calc( #{$mobSize + px} + #{$addSize} * (100vw / #{$maxWidth}) )
*
  box-sizing: border-box
  font-family: 'Roboto', sans-serif
  line-height: 1.42857143
  .wrapper
    width: 100%
    height: 100%
    background-color: rgb(233, 231, 231)
    padding-top: 3%
    .pre-second
      width: 100%
      background-color: #ddd
      height: 7vh
      display: flex
      justify-content: flex-start
      align-items: center
      padding-left: 5%
    .second
      width: 100%
      height: 100%
      display: flex
      flex-wrap: wrap
      gap: 1rem
      background-color: white
    .third
      width: 100%
      height: 7vh
      display: flex
      justify-content: center
      align-items: center
      .showMoreButton
        background-color: #ff3d00
        padding: 1%
        border: 1px
        color: white
        cursor: pointer
    .front
      width: 1280px
      margin: 0 auto
      @media (max-width: 1280px)
        width: 90%
      .first
        width: 100%
        height: 100%
        background-color: #fff
        padding: 2%
        .content-wrapper
          width: 100%
          height: 40px
          display: flex
          justify-content: center
          align-items: center
          .svg-bundle
            width: 80%
            height: 100%
            display: flex
            input
              width: 95%
              height: 100%
              border: 1px solid #e8e8e8
              outline: none
              padding-left: 1%
              &:focus
                border: 1px solid darken(rgb(251, 251, 251), 12.25%)
            .svg-fix
              width: 5%
              height: 100%
              display: flex
              justify-content: center
              align-items: center
              border: 1px solid #e8e8e8
              border-right: none
              background-color: rgb(251, 251, 251)
              svg
                width: 100%
                font-size: .4rem
          .search-button
            width: 20%
            padding: 1%
            background-color: rgb(255, 61, 0)
            display: flex
            justify-content: center
            align-items: center
            color: white
            height: 100%
            cursor: pointer
          .label
            font-size: adaptive-font(18, 12)
            font-weight: 500
</style>
