<template>
  <div>
    <div class="pt-2 flex flex-column align-items-center">
      <HeaderComponent v-if="displayHeader" />
      <router-view></router-view>
    </div>
  </div>
</template>

<script setup>
import HeaderComponent from './components/HeaderComponent.vue'

import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const displayHeader = ref(true)

watch(() => {
  displayHeader.value = route.path !== '/'
})
</script>
