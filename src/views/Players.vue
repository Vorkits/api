<template>
  <div class="wrapper">
    <div class="front">
      <section class="first">
        <div class="searchBy-block">
          <div class="div-searchBy">
            Search by:
          </div>
          <div ref="varFirstButton" class="var-first-button active" @click="searchVariableToggle(true)">CITY AND LEVEL</div>
          <div ref="varSecondButton" class="var-second-button" @click="searchVariableToggle(false)">FIRST AND LAST NAME</div>
        </div>
        <div class="searchByCityAndLevel">
          <div class="first-search-column search-column">
            <div class="left-content-wrapper">
              <div>Near:</div>
              <div class="svg-bundle">
              <div class="svg-fix">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-geo-alt-fill" viewBox="0 0 16 16">
  <path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/>
</svg></div>
              <input type="text" id="Near">
              </div>
            </div>
            <div class="right-content-wrapper">
              <div class="left-input">
                <div>Within the range of:</div>
                <select name="range" id="range">
                  <option value="5km">5km</option>
                  <option value="10km">10km</option>
                  <option value="15km">15km</option>
                  <option value="20km">20km</option>
                  <option value="25km">25km</option>
                  <option value="30km">30km</option>
                  <option value="35km">35km</option>
                  <option value="40km">40km</option>
                  <option value="45km">45km</option>
                  <option value="50km">50km</option>
                </select>
              </div>
              <div class="right-input">
                <div>Ability level:</div>
                <select name="abilityLevel" id="abilityLevel">
                  <option value="All levels">All levels</option>
                  <option value="Total beginner">Total beginner</option>
                  <option value="Beginner">Beginner</option>
                  <option value="Intermediate">Intermediate</option>
                  <option value="Advanced">Advanced</option>
                  <option value="Pro">Pro</option>
                </select>
              </div>
            </div>
          </div>
          <div class="second-search-column search-column">
            <div class="left-content-wrapper">
              <div>Available to play on:</div>
              <div class="svg-bundle">
              <div class="svg-fix fix">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-calendar-event" viewBox="0 0 16 16">
  <path d="M11 6.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1z"/>
  <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z"/>
</svg></div>
              <DatePicker placeholder="   Click Here..." input-class="select" wrapper-class="wrapper-select" class="select"></DatePicker>
              </div>
            </div>
            <div class="right-content-wrapper">
              <div>From:</div>
              <div class="svg-bundle">
              <div class="svg-fix fix">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clock" viewBox="0 0 16 16">
  <path d="M8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71V3.5z"/>
  <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm7-8A7 7 0 1 1 1 8a7 7 0 0 1 14 0z"/>
</svg></div>
              <TimeSelector placeholder="   Click Here..." class="select"></TimeSelector>
              </div>
            </div>
          </div>
          <div class="third-search-column search-column">
            <div class="left-content-wrapper">
              <div>Sex:</div>
              <select name="Sex" id="Sex">
                <option value="Both">Both</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>
            <div class="right-content-wrapper">
              <div>Age</div>
              <select name="Age" id="Age">
                <option value="All">All</option>
                <option value="18-25">18-25 years</option>
                <option value="26-30">26-30 years</option>
                <option value="31-35">31-35 years</option>
                <option value="36-40">36-40 years</option>
                <option value="41-45">41-45 years</option>
                <option value="46-50">46-50 years</option>
                <option value="51-55">51-55 years</option>
                <option value="56-60">56-60 years</option>
                <option value="61-99">61-99 years</option>
              </select>
            </div>
          </div>
          <div class="four-search-column search-column">
            <div class="left-button">
              Advanced
            </div>
            <div class="right-button">
              Search
            </div>
          </div>
        </div>
        <div class="searchByFirstAndLastName">

        </div>
      </section>
    </div>
  </div>
</template>

<script>
import DatePicker from 'vuejs-datepicker'
import TimeSelector from 'vue-timeselector'
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
    DatePicker,
    TimeSelector
  }
}
</script>

<style lang="sass">
@import url('../plugins/datepicker.min.css')
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
        height: 35vh
        background-color: #fff
        padding: 2%
        .searchByCityAndLevel
          width: 100%
          height: 83%
          display: flex
          flex-direction: column
          justify-content: space-between
          align-items: center
          margin-top: 2%
          .search-column
            width: 100%
            height: 25%
            display: flex
            justify-content: space-evenly
            align-items: center
            .left-content-wrapper, .right-content-wrapper
              width: 50%
              height: 100%
            .svg-fix
              width: 7%
              height: 100%
              display: flex
              justify-content: center
              align-items: center
              border: 1px solid #e8e8e8
              border-right: none
              background-color: rgb(251, 251, 251)
            .fix
              width: calc(7% + 2.91px)
            .svg-bundle
              width: 90%
              height: 60%
              display: flex
            svg
              width: 100%
              height: 40%
            input
              width: 93%
              height: 100%
              border: 1px solid #e8e8e8
            .wrapper-select
              width: 100%
              height: 100%
            .select div:nth-child(1), .select
              width: 100%
              height: 100%
            select
              width: 90%
              height: 60%
              border: 1px solid #e8e8e8
        .searchBy-block
          width: 100%
          height: 15%
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
