<template>
  <div class="surface-card p-4 shadow-2 border-round w-full lg:w-6">
    <div class="flex flex-column justify-content-center align-items-center">
      <img
        src="../assets/images/underwater-hello-im-under-water.gif"
        alt="Image"
        height="250"
        class="mb-3"
      />
      <div class="text-900 text-3xl font-medium mb-3">
        Hello, my dearest friends
      </div>
      <span class="text-600 font-medium line-height-3"
        >Today we're not going to learn si plusplus</span
      >
      <p class="font-medium no-underline ml-2 text-blue-500">
        Lets shop today!
      </p>
    </div>
    <button v-if="userStore.accessToken" @click="handleLogout">Logout</button>
    <LoginComponent :handleLogin="handleLogin" />
    <RegisterModal :handleRegister="handleRegister" />
  </div>
</template>

<script setup>
import RegisterModal from '../components/RegisterModal.vue'
import LoginComponent from '../components/LoginComponent.vue'

import { useUserStore } from '../stores/user'

import { useRouter } from 'vue-router'

const userStore = useUserStore()

const router = useRouter()

const handleLogin = async () => {
  await userStore.loginUser()
  userStore.username = ''
  userStore.password = ''
  router.push('/home')
}

const handleRegister = async () => {
  await userStore.registerUser()
  userStore.hashed_password = ''
  userStore.email = ''
  router.push('/home')
}

const handleLogout = () => {
  userStore.logoutUser()
}
</script>
