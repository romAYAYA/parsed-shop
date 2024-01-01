import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

export const useProductsStore = defineStore('products', () => {
  const products = ref([])

  const setProducts = (newProducts) => {
    products.value = newProducts
  }

  const getProducts = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/products')
      setProducts(response.data)
    } catch (err) {
      console.log(err)
    }
  }

  return { products, getProducts }
})
