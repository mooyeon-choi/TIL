<template>
  <nav class="navbar">
    <font-awesome-icon class="navbar-logo" icon="leaf" />
    <span>Habit Tracker</span>
    <span class="navbar-count">{{ totalCount }}</span>
  </nav>
</template>
<script>
export default {
  props: {
    totalCount : Number
  }
}
</script>
<style>
  .navbar {
    font-size: 2rem;
    padding: 1em;
    background-color: blanchedalmond;
  }

  .navbar-logo {
    color: green;
    margin-right: 0.5em;
  }

  .navbar-count {
    display: inline-block;
    text-align: center;
    font-size: 2rem;
    width: 2.5rem;
    height: 2.5rem;
    line-height: 2.5rem;
    margin-left: 0.2em;
    background-color: green;
    color: white;
    border-radius: 50%;
  }
</style>