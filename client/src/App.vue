<template>
  <form @submit.prevent="registerUser">
    <input type="text" v-model="email" />
    <input type="text" v-model="hashed_password" />
    <input type="submit" value="Register" />
  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

let email = ref('')
let hashed_password = ref('')

const registerUser = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/users', {
      email: email.value,
      hashed_password: hashed_password.value,
    })
    console.log(response.data)
  } catch (error) {
    console.error('Registration failed:', error.response.data)
  }
}
</script>
