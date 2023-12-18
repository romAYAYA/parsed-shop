<template>
  <div>
    <form @submit.prevent="userStore.registerUser">
      <input type="text" v-model="userStore.email" />
      <input type="text" v-model="userStore.hashed_password" />
      <input type="submit" value="Register" />
    </form>

    <div v-if="userStore.error">{{ userStore.error }}</div>

    <form @submit.prevent="userStore.loginUser">
      <input type="text" v-model="userStore.username" placeholder="Username" />
      <input
        type="current-password"
        v-model="userStore.password"
        placeholder="Password"
      />
      <input type="submit" value="Login" />
    </form>
  </div>
</template>

<script setup>
import { useUserStore } from './stores/user'

const userStore = useUserStore()
</script>
