<template>
  <div class="wrapper">
    <img class="Avatar"/>
    <div class="Name"></div>
    <div class="City"></div>
    <div class="level"></div>
  </div>
</template>

<script>
export default {
  name: 'userCard'
}
</script>

<style lang="sass" scoped>
  *
    outline: 1px solid red
  .wrapper
    width: 200px
    height: 300px
    padding: 0
    .Avatar
      width: 100%
      height: 60%
      border-radius: 50%
</style>