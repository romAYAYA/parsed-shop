<template>
  <div class="flex flex-column justify-content-center align-items-center">
    <h1>Products</h1>
    <div class="grid grid-nogutter w-9">
      <div
        v-for="product in products"
        :key="product.product_id"
        class="col-12 sm:col-6 lg:col-12 xl:col-4 p-2"
      >
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
