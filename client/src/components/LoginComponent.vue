<template>
  <form @submit.prevent="handleLogin">
    <label for="email" class="block text-900 font-medium mb-2">Email</label>
    <InputText
      v-model="userStore.username"
      id="email"
      type="text"
      class="w-full mb-3"
    />

    <label for="password" class="block text-900 font-medium mb-2"
      >Password</label
    >
    <InputText
      v-model="userStore.password"
      id="password"
      type="password"
      class="w-full mb-3"
    />

    <div class="card flex justify-content-center">
      <Toast />
      <Button
        label="Sign In"
        type="submit"
        icon="pi pi-user"
        class="w-full mb-3"
      ></Button>
    </div>
  </form>
</template>

<script setup>
import InputText from 'primevue/InputText'
import Button from 'primevue/button'
import Toast from 'primevue/toast'

import { useUserStore } from '../stores/user'

const userStore = useUserStore()

const { handleLogin } = defineProps({
  handleLogin: {
    type: Function,
    required: true,
  },
})
</script>
