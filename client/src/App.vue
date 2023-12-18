<template>
  <div>
    <!-- <form @submit.prevent="registerUser">
      <input type="text" v-model="email" placeholder="Email" />
      <input type="text" v-model="password" placeholder="Password" />
      <input type="submit" value="Register" />
    </form> -->

    <form @submit.prevent="loginUser">
      <input type="text" v-model="username" placeholder="Username" />
      <input
        type="current-password"
        v-model="password"
        placeholder="Password"
      />
      <input type="submit" value="Login" />
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

// let email = ref('')
// let password = ref('')
let username = ref('')
let password = ref('')

// const registerUser = async () => {
//   try {
//     const response = await axios.post('http://127.0.0.1:8000/api/register', {
//       email: email.value,
//       hashed_password: password.value,
//     })
//     console.log(response.data)
//   } catch (error) {
//     console.error('Registration failed:', error.response.data)
//   }
// }

const loginUser = async () => {
  try {
    const response = await axios.post(
      'http://127.0.0.1:8000/api/login',
      {
        grant_type: 'password',
        username: username.value,
        password: password.value,
      },
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      }
    )
    console.log(response.data)
  } catch (error) {
    console.error('Login failed:', error.response.data)
  }
}
</script>
