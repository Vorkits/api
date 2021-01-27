<template>
  <div class="Matches">
    <div class="front">
      <section class="first">
        <router-link to="/login" class="login-button">
          Plan a new public match
        </router-link>
      </section>
      <section class="second">
        <div class="label">Near:</div>
        <div class="content-wrapper">
          <div class="svg-bundle">
            <div class="svg-fix">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-geo-alt-fill" viewBox="0 0 16 16">
<path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/>
</svg></div>
            <input @keypress.enter="getMatches" v-model="currentCity" placeholder="insert your address" type="text" id="Near">
          </div>
          <div @click="getMatches" class="search-button">
            Search
          </div>
        </div>
      </section>
      <section class="third">
        <matchCard
          v-for="match in responseMatches.data"
          :key="(Math.random()*1e8).toString(16) + match.coart"
          :matchData="match"
        />
      </section>
    </div>
  </div>
</template>

<script>
import matchCard from '@/components/matchCard.vue'
import axios from 'axios'
export default {
  name: 'matches',
  data: () => ({
    responseMatches: new Array(),
    currentCity: null
  }),
  components: {
    matchCard
  },
  methods: {
    async getMatches () {
      await axios.get('http://82.146.45.20/api/games/get')
        .then(response => {
          this.responseMatches = response.data
          console.log(this.responseMatches)
        })
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
  .Matches
    width: 100%
    height: 100%
    background-color: rgb(233, 231, 231)
    padding-top: 3%
    .front
      width: 1280px
      margin: 0 auto
      @media (max-width: 1280px)
        width: 90%
      .first
        width: 100%
        background-color: #fff
        padding: 1.5%
        display: flex
        justify-content: center
        align-items: center
        .login-button
          width: 50%
          padding: .5%
          text-align: center
          background-color: #ffc107
          color: white
          cursor: pointer
          border-radius: 2px
          text-decoration: none
    .second
      width: 100%
      height: 100%
      background-color: #fff
      padding: 1.5%
      margin-top: 3%
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
    .third
      padding: 1.5%
      background-color: #fff
</style>