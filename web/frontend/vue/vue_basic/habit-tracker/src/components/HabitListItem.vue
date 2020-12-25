<template>
  <li class="habit">
    <span class="habit-name">{{ habit.name }}</span>
    <span class="habit-count">{{ habit.count }}</span>
    <button class="habit-button" @click="$emit('increment')">
      <font-awesome-icon class="habit-button habit-increase" icon="plus-square" />
    </button>
    <button class="habit-button" @click="$emit('decrement')">
      <font-awesome-icon class="habit-button habit-decrease" icon="minus-square" />
    </button>
    <button class="habit-button" @click="$emit('delete')">
      <font-awesome-icon class="habit-button habit-delete" icon="trash" />
    </button>
  </li>
</template>
<script>
export default {
  props: ['habit']
}
</script>
<style>
.habit {
  font-size: 2.5rem;
  padding: 0.5em;
  list-style: none;
}

.habit-count {
  display: inline-block;
  text-align: center;
  font-size: 2rem;
  width: 2.5rem;
  height: 2.5rem;
  line-height: 2.5rem;
  margin-left: 0.2em;
  margin-right: 0.5em;
  background-color: darkseagreen;
  color: white;
  border-radius: 50%;
}

.habit-button {
  font-size: 2.5rem;
  margin: 0 0.1em;
  background-color: transparent;
}

.habit-button:hover {
  opacity: 0.8;
}

.habit-increase,
.habit-decrease {
  color: goldenrod;
}

.habit-delete {
  font-size: 2rem;
  color: darkred;
}
</style>