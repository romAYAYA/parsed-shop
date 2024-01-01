<template>
  <div class="flex flex-column justify-content-center align-items-center">
    <h1>Products</h1>
    <div class="grid grid-nogutter w-9">
      <div
        v-for="product in products"
        :key="product.product_id"
        class="col-12 sm:col-6 lg:col-12 xl:col-4 p-2"
      >
        <!-- <div class="p-4 border-1 surface-border surface-card border-round">
          <div class="flex flex-column align-items-center gap-3 py-5">
            <img
              class="w-9 h-14rem shadow-2 border-round"
              :src="product.img"
              :alt="product.name"
            />
            <div class="text-xl font-bold">
              {{ product.name.slice(0, 35) }}<span v-if="product.name.length > 20">...</span>
            </div>
          </div>
          <div class="flex align-items-center justify-content-between">
            <span class="text-xl font-semibold">{{ product.price }}</span>
            <Button icon="pi pi-shopping-cart" rounded></Button>
          </div>
        </div> -->
        <ProductComponent  :product="product" />
      </div>
    </div>
  </div>
</template>

<script setup>
import ProductComponent from '../components/ProductComponent.vue'

import { ref, onMounted } from 'vue'
import { useProductsStore } from '../stores/products'

const productsStore = useProductsStore()
const products = ref([])

onMounted(async () => {
  if (productsStore.products.length === 0) {
    await productsStore.getProducts()
    products.value = [...productsStore.products]
  } else {
    products.value = [...productsStore.products]
  }
})
</script>
