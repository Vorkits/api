<template>
  <div class="about">
    <div class="front">
      <div class="text-path">
        COMPANYNAME - как это работает
      </div>
      <section class="first">
        <div class="top-content-block">
        COMPANYNAME - is for those who play <span> tennis with passion and for fun. </span><br>
You can <span> find new tennis player friends </span> to play with with the opportunity to select <span> ability level, availability and area. </span><br>
With oratennis every player can <span> plan matches and join amateur tournaments </span> in your area. <br>
        </div>
        <div class="bottom-content-block">
          <div class="grid-content-block">
            <div class="img"></div>
            <div class="text">
              Meet new <br>
              tennis player friends
            </div>
          </div>
          <div class="grid-content-block">
            <div class="img"></div>
            <div class="text">
              Manage <br>
              your time
            </div>
          </div>
          <div class="grid-content-block">
            <div class="img"></div>
            <div class="text">
              No ranking, <br>
              just fun!
            </div>
          </div>
        </div>
      </section>
      <section class="second">
        <div class="content-wrapper">
          <div class="text-content">
            <h4> Meet new tennis player friends </h4>
<p>
Selected by level, availability and area there are <span> 32.248 tennis players, </span> ready to meet you on the tennis court and play amateur matches and tournaments every day.
</p>
          </div>
          <div class="img-content"></div>
        </div>
        <div class="content-wrapper">
          <div class="img-content"></div>
          <div class="text-content">
            <h4> Manage your time </h4>
<p>
play, <span> when and where you want, </span> and schedule your matches and tournaments directly with your rivals.
</p>
          </div>
        </div>
        <div class="content-wrapper">
          <div class="text-content">
            <h4> No ranking, just fun! </h4>
<p>
you can <span> share your passion for tennis </span> for fun and with loyalty, ranking will never be part of our community.
</p>
          </div>
          <div class="img-content"></div>
        </div>
      </section>
      <section class="third">
        <router-link to="/login">
          Register for free
        </router-link>
      </section>
      <VFooter class="footer"/>
    </div>
  </div>
</template>

<script>
import VFooter from '@/components/VFooter'
export default {
  name: 'About',
  components: {
    VFooter
  }
}
</script>

<style lang="sass" scoped>
$maxWidth: 1280

@mixin adaptive-font($pcSize, $mobSize)
  $addSize: $pcSize - $mobSize
  $addMobSize: $addSize + $addSize * 0.7
  @media (max-width: 767px)
    font-size: calc( #{$mobSize + px} + #{$addMobSize} * ((100vw - 320px) / #{$maxWidth}) ) !important
  @media (min-width: 767px)
    font-size: calc( #{$mobSize + px} + #{$addSize} * (100vw / #{$maxWidth}) ) !important
*
  box-sizing: border-box
  font-family: 'Roboto', sans-serif
  line-height: 1.42857143
.about
  width: 100%
  height: 100%
  background-color: rgb(233, 231, 231)
  padding-top: 1%
.front
  width: 1280px
  margin: 0 auto
  @media (max-width: 1280px)
    width: 90%
  .text-path
    padding-left: 2%
    @include adaptive-font(16, 14)
    margin-bottom: 1%
  .first
    background-color: #fff
    padding: 3%
    padding-top: 2%
    width: 100%
    min-height: 45vh
    box-shadow: 0 1px 1px rgba(0, 0, 0, 0.07)
    .top-content-block
      @include adaptive-font(19, 16)
      font-weight: 300
      margin-bottom: 3%
      span
        font-weight: 500
    .bottom-content-block
      @include adaptive-font(23.6, 18)
      font-weight: 300
      display: flex
      justify-content: space-between
      align-items: center
      @media (max-width: 1000px)
        flex-direction: column
        .grid-content-block
          width: 60% !important
          .img
            height: 40vh !important
            background-size: 65% !important
      .grid-content-block
        width: 25%
        .img
          height: 20vh
        .text
          text-align: center
        &:nth-child(1) .img
          background: url(../assets/howDoesItWork/first.png) center no-repeat
          background-size: 63%
        &:nth-child(2) .img
          background: url(../assets/howDoesItWork/second.png) center no-repeat
          background-size: 63%
        &:nth-child(3) .img
          background: url(../assets/howDoesItWork/third.png) center no-repeat
          background-size: 63%
  .second
    height: 100vh
    display: flex
    flex-direction: column
    justify-content: space-between
    align-items: center
    @media (max-width: 1000px)
      height: 240vh
    .content-wrapper
      width: 100%
      height: 33.3333333333%
      display: flex
      @media (max-width: 1000px)
        flex-direction: column
        height: 80vh !important
        &:nth-child(1), &:nth-child(3)
          .text-content
            order: 2
          .img-content
            order: 1
        .img-content
          width: 100% !important
          height: 65% !important
        .text-content
          width: 100% !important
          height: 35% !important
      .text-content, .img-content
        width: 50%
        height: 100%
      .text-content
        padding: 7%
        display: flex
        flex-direction: column
        justify-content: center
        align-items: center
        h4, p
          width: 100%
        h4
          @include adaptive-font(20.8, 15)
          font-weight: 500
        p
          @include adaptive-font(17.6, 13)
          padding-top: 2%
          font-weight: 300
        span
          font-weight: 400
      .img-content
        background-size: cover !important
      &:nth-child(1) .img-content
        background: url(../assets/howDoesItWork/bottom-first.jpg) center no-repeat
      &:nth-child(2) .img-content
        background: url(../assets/howDoesItWork/bottom-second.jpg) center no-repeat
      &:nth-child(3) .img-content
        background: url(../assets/howDoesItWork/bottom-third.jpg) center no-repeat
  .third
    height: 34vh
    background: url(../assets/howDoesItWork/bottom.jpg) center no-repeat
    background-size: cover
    display: flex
    justify-content: center
    align-items: center
    a
      background-color: rgb(251, 35, 7)
      padding: 1%
      border-radius: 3px
      text-decoration: none
      color: white
      @include adaptive-font(19.2, 13)
      text-transform: uppercase
  footer .grey
    background: rgb(228,225,225) !important
</style>