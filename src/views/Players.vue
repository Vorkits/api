<template>
  <div class="wrapper">
    <div class="front">
      <section class="first">
        <div class="searchBy-block">
          <div class="Label-searchBy">
            Search by:
          </div>
          <div ref="varFirstButton" class="var-first-button" @click="searchVariableToggle(true)">CITY AND LEVEL</div>
          <div ref="varSecondButton" class="var-second-button" @click="searchVariableToggle(false)">FIRST AND LAST NAME</div>
        </div>
        <div class="searchByCityAndLevel">
          
        </div>
        <div class="searchByFirstAndLastName">

        </div>
      </section>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Players',
  data: () => ({
    searchCurrentType: true
  }),
  methods: {
    searchVariableToggle (type) {
      this.searchCurrentType = type
      if (type) {
        this.$refs.varFirstButton.classList.add('active')
        this.$refs.varSecondButton.classList.remove('active')
      }
      else {
        this.$refs.varSecondButton.classList.add('active')
        this.$refs.varFirstButton.classList.remove('active')
      }
    }
  },
  components: {
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
    .front
      background-clip: black
      width: 1280px
      margin: 0 auto
      @media (max-width: 1280px)
        width: 90%
      .first
        width: 100%
        height: 25vh
        background-color: #fff
        padding: 2%
        .searchBy-block
          width: 100%
          height: 25%
          display: flex
          justify-content: flex-start
          align-items: center
          box-shadow: inset 0 -2px 0 0 #eeeeee
          & *
            height: 100%
            display: flex
            justify-content: center
            align-items: center
            padding: 1%
            @include adaptive-font(14, 11)
          .var-first-button, .var-second-button
            cursor: pointer
            color: #7a7a7a
          .active
            background-color: rgb(233, 231, 231)
            border-bottom: 2px solid black
            margin-bottom: -2px
            color: black
</style>
