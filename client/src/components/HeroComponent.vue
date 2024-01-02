<template>
  <div class="grid grid-nogutter surface-section text-800">
    <div
      class="col-12 md:col-6 p-6 text-center md:text-left flex align-items-center"
    >
      <section>
        <span class="block text-6xl font-bold mb-1"
          >Create the screens your</span
        >
        <div class="text-6xl text-primary font-bold mb-3">
          visitors deserve to see
        </div>
        <p class="mt-0 mb-4 text-700 line-height-3">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
        <router-link to="/goods">
          <Button
            label="What do we have"
            type="button"
            class="mr-3 p-button-raised"
          ></Button>
        </router-link>
        <Button
          @click="handleLogout"
          label="Leave"
          type="button"
          class="p-button-outlined"
        ></Button>
      </section>
    </div>
    <div class="col-12 md:col-6 overflow-hidden">
      <img
        src="../assets/images/underwater-hello-im-under-water.gif"
        alt="Image"
        class="md:ml-auto block md:h-full border-rounded"
        style="clip-path: polygon(8% 0, 100% 0%, 100% 100%, 0 100%)"
      />
    </div>
  </div>
</template>

<script setup>
import Button from 'primevue/button'

import { useUserStore } from '../stores/user'

const userStore = useUserStore()

const handleLogout = () => {
  userStore.logoutUser()
}
</script>
