<template>
  <h1>{{ message }}</h1>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

let message = ref('')

onMounted(() => {
  axios
    .get('http://127.0.0.1:8000/hi')
    .then((response) => {
      message.value = response.data.message
    })
    .catch((error) => {
      console.error('Error:', error)
    })
})
</script>
