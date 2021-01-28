<template>
  <div class="wrapper">
    <div class="Avatar" :style="{background: 'url(' + courtData.photo + ') center no-repeat', 'background-size': 'cover'}">
      <router-link :to="'/Court/:' + courtData.id"></router-link>
    </div>
    <div class="Name">{{ courtData.name }}</div>
    <div class="City">{{ courtData.city }}</div>
    <router-link class="goOver" :to="'/Court/:' + courtData.id">go over</router-link>
  </div>
</template>

<script>
export default {
  name: 'userCard',
  data: () => ({
  }),
  props: {
    courtData: {
      type: Object,
      default: () => ({
        photo: null,
        city: null,
        name: null,
        price: null
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
      a
        display: block
        width: 100%
        height: 100%
        border-radius: 50%
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
    .goOver
      @include adaptive-font(16, 13)
      width: 100%
      background-color: lighten(green, 12.5%)
      height: 30px
      color: white
      margin-top: 10px
      display: flex
      justify-content: center
      align-items: center
      cursor: pointer
      text-transform: capitalize
</style>