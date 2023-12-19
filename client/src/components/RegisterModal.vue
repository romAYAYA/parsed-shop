<template>
  <div class="card flex justify-content-center">
    <Button
      @click="visible = true"
      label="Not registered?"
      icon="pi pi-user-plus"
      class="surface-ground text-black-alpha-90 w-full"
    ></Button>

    <Dialog
      v-model:visible="visible"
      modal
      :pt="{
        mask: {
          style: 'backdrop-filter: blur(2px)',
        },
      }"
    >
      <template #container="{ closeCallback }">
        <form
          class="flex flex-column px-8 py-5 gap-4"
          style="
            border-radius: 12px;
            background-image: radial-gradient(
              circle at left top,
              var(--primary-400),
              var(--primary-700)
            );
          "
        >
          <div class="inline-flex flex-column gap-2">
            <label for="registerEmail" class="text-primary-50 font-semibold"
              >Email</label
            >
            <InputText
              v-model="userStore.email"
              id="registerEmail"
              class="bg-white-alpha-20 border-none p-3 text-primary-50"
            ></InputText>
          </div>
          <div class="inline-flex flex-column gap-2">
            <label for="registerPassword" class="text-primary-50 font-semibold"
              >Password</label
            >
            <InputText
              v-model="userStore.hashed_password"
              id="registerPassword"
              class="bg-white-alpha-20 border-none p-3 text-primary-50"
              type="password"
            ></InputText>
          </div>
          <div class="flex align-items-center gap-2">
            <Button
              label="Sign-Up"
              @click="handleRegister"
              text
              class="p-3 w-full text-primary-50 border-1 border-white-alpha-30 hover:bg-white-alpha-10"
            ></Button>
            <Button
              label="Cancel"
              @click="closeCallback"
              text
              class="p-3 w-full text-primary-50 border-1 border-white-alpha-30 hover:bg-white-alpha-10"
            ></Button>
          </div>
        </form>
      </template>
    </Dialog>
  </div>
</template>

<script setup>
import { ref } from 'vue'

import Button from 'primevue/button'
import InputText from 'primevue/InputText'
import Dialog from 'primevue/dialog'
import { useUserStore } from '../stores/user'

const userStore = useUserStore()

const { handleRegister } = defineProps({
  handleRegister: {
    type: Function,
    required: true,
  },
})

const visible = ref(false)
</script>

