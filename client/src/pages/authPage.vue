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

    <div>
      <label for="email1" class="block text-900 font-medium mb-2">Email</label>
      <InputText id="email1" type="text" class="w-full mb-3" />

      <label for="password1" class="block text-900 font-medium mb-2"
        >Password</label
      >
      <InputText id="password1" type="password" class="w-full mb-3" />

      <Button label="Sign In" icon="pi pi-user" class="w-full"></Button>
    </div>
  </div>
</template>

<script setup>
import InputText from 'primevue/InputText'
import Button from 'primevue/button'
</script>

<style scoped></style>
