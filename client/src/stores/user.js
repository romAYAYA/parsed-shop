import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

import { useToast } from 'primevue/usetoast'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore('user', () => {
  const username = ref('')
  const password = ref('')
  const email = ref('')
  const hashed_password = ref('')
  const accessToken = ref('')
  const error = ref('')

  const toast = useToast()
  const router = useRouter()

  const setAccessToken = (token) => {
    accessToken.value = token
    localStorage.setItem('access_token', token)
  }

  const registerUser = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/register', {
        email: email.value,
        hashed_password: hashed_password.value,
      })
      setAccessToken(response.data.access_token)
      router.push('/home')
    } catch (err) {
      showToast('error', 'Error', 'An error occurred. Please try again.')
      clearAccessToken()
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
      router.push('/home')
    } catch (err) {
      showToast('error', 'Error', 'An error occurred, try again')
      clearAccessToken()
    }
  }

  const logoutUser = () => {
    clearAccessToken()
    showToast('info', 'Info', 'Successfully logged out.')
    router.push('/')
  }

  const clearAccessToken = () => {
    accessToken.value = ''
    localStorage.removeItem('access_token')
  }

  const showToast = (severity, summary, detail) => {
    toast.add({
      severity,
      summary,
      detail,
      life: 3000,
    })
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
    logoutUser,
  }
})
