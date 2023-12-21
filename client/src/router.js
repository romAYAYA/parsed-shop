import { useUserStore } from './stores/user'

import { createRouter, createWebHistory } from 'vue-router'

import authPage from './pages/authPage.vue'
import homePage from './pages/homePage.vue'
import goodsPage from './pages/goodsPage.vue'
import errorPage from './pages/errorPage.vue'

const routes = [
  { path: '/', component: authPage },
  { path: '/home', component: homePage },
  { path: '/goods', component: goodsPage },
  { path: '/:pathMatch(.*)*', component: errorPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
