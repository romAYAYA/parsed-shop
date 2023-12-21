<template>
  <Toolbar
    class="bg-gray-900 shadow-2 w-9"
    style="
      border-radius: 3rem;
      background-image: linear-gradient(
        to right,
        var(--bluegray-500),
        var(--bluegray-800)
      );
    "
  >
    <template #start>
      <div class="flex flex-wrap align-items-center gap-3">
        <router-link to="/home"
          ><button
            class="p-link inline-flex justify-content-center align-items-center text-white h-3rem w-3rem border-circle hover:bg-white-alpha-10 transition-all transition-duration-200"
          >
            <i class="pi pi-home text-2xl"></i>
          </button>
        </router-link>
        <router-link to="/goods">
          <button
            class="p-link inline-flex justify-content-center align-items-center text-white h-3rem w-3rem border-circle hover:bg-white-alpha-10 transition-all transition-duration-200"
          >
            <i class="pi pi-cart-plus text-2xl"></i>
          </button>
        </router-link>
      </div>
    </template>

    <template #end>
      <div class="flex align-items-center gap-2">
        <button
          @click="handleLogout"
          class="p-link inline-flex justify-content-center align-items-center text-white h-3rem w-3rem border-circle hover:bg-white-alpha-10 transition-all transition-duration-200"
        >
          <i class="pi pi-sign-out text-2xl"></i>
        </button>
      </div>
    </template>
  </Toolbar>
</template>

<script setup>
import Button from 'primevue/button'

import Toolbar from 'primevue/toolbar'

import { ref, onMounted } from 'vue'

import { useUserStore } from '../stores/user'

const userStore = useUserStore()

const hasAccessToken = ref(false)

const handleLogout = () => {
  userStore.logoutUser()
}

onMounted(() => {
  hasAccessToken.value = !!localStorage.getItem('access_token')
})
</script>
