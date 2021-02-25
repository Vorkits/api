<template>
  <div class="wrapper">
    <div class="left-content-wrapper">
      <div class="top-content"> {{ matchData.time }} </div>
      <div class="bottom-content"> {{ matchType }} </div>
    </div>
    <div class="first-player-wrapper">
      <a class="avatar" v-bind:href="'/OtherProfile/:' + matchData.player1.id"><img :src = "matchData.player1.photo"></a>
      <div class="name" v-if="matchData.player1">{{matchData.player1.name}}</div>
    </div>
    <div class="vs-wrapper">
      VS
    </div>
    <div class="second-player-wrapper">
    <a class="avatar" v-bind:href="'/OtherProfile/:' + matchData.player2.id"><img :src = "matchData.player2.photo"></a>
      <div class="name" v-if="matchData.player2">{{matchData.player2.name}}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'matchCard',
  data: () => ({
  }),
  props: {
    matchData: {
      type: Object,

    }
  },
  computed: {
    matchType: function() {
      if (this.matchData.type === 'single')
        return '1vs1'
      return '1vs1'
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
  .wrapper
    width: 100%
    height: 120px !important
    padding: 0 !important
    background-color: white !important
    margin-bottom: 1%
    border: 1px solid #ddd
    border-radius: 3px
    display: flex
    justify-content: flex-start
    .left-content-wrapper
      width: 120px
      height: 100%
      background-color: #f2f2f2
      display: flex
      flex-direction: column
      justify-content: center
      align-items: center
      *
        height: 50%
        width: 100%
        display: flex
        justify-content: center
        align-items: center
        font-weight: 300
      .bottom-content
        border-top: 1px dashed #d9d9d9
        color: #3bb544
    .vs-wrapper
      width: 120px
      height: 100%
      display: flex
      justify-content: center
      align-items: center
    .first-player-wrapper, .second-player-wrapper
      width: 120px
      height: 100%
      display: flex
      flex-direction: column
      justify-content: center
      align-items: center
      .avatar
        height: 70px
        width: 70px
        border-radius: 50%
        border: 1px solid silver
        img
          width: 100%
          height: 100%
          border-radius: 50%
      .name
        height: 70%
        display: flex
        justify-content: center
        text-align: center
        align-items: center
</style>