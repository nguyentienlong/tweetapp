<template>
  <div id="app">
      <div class="container">
          <h4 class="text-left font-weight-bold">Welcome to <router-link to="/">Tw33t App</router-link></h4>
          <router-view></router-view>
      </div>
  </div>
</template>

<script>
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
  padding: 10px;
}
</style>
