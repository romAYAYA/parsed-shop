<template>
  <div>
    <div class="h-screen flex justify-content-center align-items-center">
      <router-view></router-view>
    </div>
  </div>
</template>

<script setup>
import authPage from './pages/authPage.vue'

import { useUserStore } from './stores/user'

const userStore = useUserStore()
</script>
