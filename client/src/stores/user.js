import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const username = ref('')
  const password = ref('')
  const email = ref('')
  const hashed_password = ref('')
  const accessToken = ref('')
  const error = ref('')

  const setAccessToken = (token) => {
    accessToken.value = token
    localStorage.setItem('access_token', token)
  }

  const clearAccessToken = () => {
    accessToken.value = ''
    localStorage.removeItem('access_token')
  }

  const registerUser = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/register', {
        email: email.value,
        hashed_password: hashed_password.value,
      })
      setAccessToken(response.data.access_token)
      console.log(response.data)
    } catch (err) {
      console.error('Registration failed:', err.response.data)
    }
  }

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
      setAccessToken(response.data.access_token)
      console.log(response.data)
    } catch (error) {
      console.error('Login failed:', err.response.data)
    }
  }

  return {
    username,
    password,
    email,
    hashed_password,
    accessToken,
    error,
    registerUser,
    loginUser,
  }
})
