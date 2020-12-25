<template>
  <div id="app">
    <Navbar :totalCount="habits.filter(item => item.count > 0).length"/>
    <HabitList 
      :habits="habits"
      @increment="onIncrease" 
      @decrement="onDecrease"
      @reset="onReset"
      @delete="onDelete"
      @add="onAdd"
    />
  </div>
</template>

<script>
import HabitList from './components/HabitList.vue'
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    HabitList,
    Navbar
  },
  data() {
    return {
      habits: [
        { id: 0, name: 'Reading', count: 0},
        { id: 1, name: 'Running', count: 0},
        { id: 2, name: 'Coding', count: 0}
      ]
    }
  },
  methods: {
    onIncrease(habitId) {
      const index = this.habits.findIndex(item => item.id === habitId)
      this.$set(this.habits, index, { ...this.habits[index], count: ++this.habits[index].count })
    },

    onDecrease(habitId) {
      const index = this.habits.findIndex(item => item.id === habitId)
      const count = this.habits[index].count - 1;
      this.$set(this.habits, index, { ...this.habits[index], count: count < 0 ? 0 : count })
    },

    onReset() {
      const habits = this.habits.map(habit => {
        if(habit.count !== 0) {
          return { ...habit, count: 0 }
        }
        return habit
      })
      this.habits = habits
    },

    onDelete(habitId) {
      const index = this.habits.findIndex(item => item.id === habitId)
      this.$delete(this.habits, index)
    },

    onAdd(name) {
      this.habits.push({ id: Date.now(), name, count: 0 })
    }
  }
}
</script>

<style>
body {
  margin: 0;
}

#app {
  box-sizing: border-box;
}

button {
  outline: none;
  border: 0;
  cursor: pointer;
}
</style>
