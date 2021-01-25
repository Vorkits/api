<template>
  <div class="wrapper">
    <div class="Avatar" :style="{background: 'url(' + userData.photo + ') center no-repeat', 'background-size': 'cover'}"></div>
    <div class="Name">{{ userData.name }}</div>
    <div class="City">{{ userData.city }}</div>
    <div class="level" :style="levelColor">level: {{ userData.level }}</div>
  </div>
</template>

<script>
export default {
  name: 'userCard',
  props: {
    userData: {
      type: Object,
      default: () => ({
        photo: null,
        city: null,
        name: null,
        level: null
      })
    }
  },
  computed: {
    levelColor: function() {
      if (this.userData.level === 1)
        return { background: '#9e9e9e' }
      else if (this.userData.level === 2)
        return { background: '#2E7D32' }
      else if (this.userData.level === 3)
        return { background: '#8BC34A' }
      else if (this.userData.level === 4)
        return { background: '#FBC02D' }
      else if (this.userData.level === 5)
        return { background: '#F57C00' }
      else if (this.userData.level === 6)
        return { background: '#BF360C' }
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
    outline: 1px solid red
  .wrapper
    max-width: calc( 100% / 6 )
    min-width: 200px
    height: 300px !important
    padding: 0 !important
    background-color: white !important
    .Avatar
      height: 180px
      width: 180px
      margin: 0 auto
      border-radius: 50%
      margin-top: 10px
    .Name, .City, .level
      text-align: center
      display: flex
      justify-content: center
      align-items: center
    .Name
      @include adaptive-font(19, 17)
      font-weight: 700
      height: 40px
    .City
      @include adaptive-font(18, 16)
      font-weight: 300
      height: 30px
    .level
      @include adaptive-font(19, 17)
      height: 40px
</style>