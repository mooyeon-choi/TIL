<template>
  <form class="add-form" @submit="onSubmit">
    <input type="text" v-model="name" class="add-input">
    <button class="add-button">Add</button>
  </form>
</template>
<script>
export default {
  data() {
    return {
      name: '',
    }
  },
  methods: {
    onSubmit: function (event) {
      event.preventDefault();
      this.$emit('add', this.name);
      this.name = '';
    }
  },
}
</script>
<style>
.add-input {
  font-size: 2rem;
}

.add-input {
  margin-right: 0.2em;
}

.add-button {
  height: 100%;
  font-size: 1.5rem;
  padding: 0.3em 0.5em;
  background-color: green;
  color: white;
}

</style>