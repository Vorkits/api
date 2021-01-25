<template>
  <div class="wrapper">
    <div class="Avatar" :style="{background: 'url(' + userData.photo + ') center no-repeat', 'background-size': 'cover'}"></div>
    <div class="Name">{{ userData.name }}</div>
    <div class="City">{{ userData.city }}</div>
    <div class="level" :style="levelColor">{{ levelData[userData.level - 1] }}</div>
  </div>
</template>

<script>
export default {
  name: 'userCard',
  data: () => ({
    levelData: [
      'No level',
      'Total beginner',
      'Beginner',
      'Intermediate',
      'Advanced',
      'Pro'
    ]
  }),
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
      else
        return { background: '#9e9e9e' }
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
    max-width: calc( (100% / 6) - 1rem )
    min-width: 200px
    height: 300px !important
    padding: 0 !important
    background-color: white !important
    .Avatar
      height: 197px
      width: 197px
      margin: 0 auto
      border-radius: 50%
      margin-top: 10px
    .Name, .City, .level
      text-align: center
      display: flex
      justify-content: center
      align-items: center
    .Name
      @include adaptive-font(16, 13)
      font-weight: 700
      height: 30px
      white-space: nowrap
    .City
      @include adaptive-font(14, 11)
      font-weight: 300
      height: 20px
      text-transform: capitalize
      margin-top: 3px
    .level
      @include adaptive-font(16, 13)
      height: 30px
      color: white
      margin-top: 10px
</style>