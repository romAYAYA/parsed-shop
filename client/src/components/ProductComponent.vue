<template>
  <div class="p-4 border-1 surface-border surface-card border-round">
    <div class="flex flex-column align-items-center gap-3 py-5">
      <img
        class="w-9 h-14rem shadow-2 border-round"
        :src="product.img"
        :alt="product.name"
      />
      <div class="text-xl font-bold">
        {{ product.name.slice(0, 35)
        }}<span v-if="product.name.length > 20">...</span>
      </div>
    </div>
    <div class="flex align-items-center justify-content-between">
      <span class="text-xl font-semibold">{{ product.price }}</span>
      <Button
        @click="visible = true"
        icon="pi pi-shopping-cart"
        rounded
      ></Button>
      <Dialog
        v-model:visible="visible"
        modal
        :header="product.name"
        :style="{ width: '50rem' }"
        :breakpoints="{ '1199px': '75vw', '575px': '90vw' }"
      >
        <p>Ya nejnau kak prodatt ribov, sorry</p>
      </Dialog>
    </div>
  </div>
</template>

<script setup>
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'

import { ref } from 'vue'

const { product } = defineProps(['product'])
const { name, img, price } = product

const visible = ref(false)
</script>
