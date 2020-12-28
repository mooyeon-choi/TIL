<template>
  <div class="habit-list">
    <HabitAddForm @add="$emit('add', $event)"/>
    <ul v-for="habit in habits" :key="habit.id">
      <HabitListItem 
        :habit="habit" 
        @increment="$emit('increment', habit.id)" 
        @decrement="$emit('decrement', habit.id)"
        @delete="$emit('delete', habit.id)"
      />
      </ul>
    <button class="habits-reset" @click="$emit('reset')">
      Reset All
    </button>
  </div>
</template>
<script>
import HabitAddForm from './HabitAddForm.vue'
import HabitListItem from './HabitListItem.vue'
export default {
  props: { 
    habits : Object
  },
  components: { HabitListItem, HabitAddForm },
}
</script>
<style>
.habit-list {
  padding: 0.5em;
  padding-top: 2em;
}

.habits-reset {
  font-size: 1.5rem;
  padding: 0.2em 1em;
  background-color: green;
  color: white;
}
</style>