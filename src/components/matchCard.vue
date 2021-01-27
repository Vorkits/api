<template>
  <div class="wrapper">
    <div class="left-content-wrapper">
      <div class="top-content"> {{ matchData.time }} </div>
      <div class="bottom-content"> {{ matchType }} </div>
    </div>
    <div class="first-player-wrapper">
      <div class="avatar"></div>
      <div class="name">Name</div>
    </div>
    <div class="vs-wrapper">
      VS
    </div>
    <div class="second-player-wrapper">
      <div class="avatar"></div>
      <div class="name">Name</div>
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
      default: () => ({
        coart: null,
        player1: null,
        player2: null,
        score1: null,
        score2: null,
        status: null,
        time: null,
        type: null,
        winner: null,
        player1data: null,
        player2data: null
      })
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
    height: 100px !important
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
        height: 70%
        width: 70px
        border-radius: 50%
        border: 1px solid silver
      .name
        height: 30%
        display: flex
        justify-content: center
        align-items: center
</style>