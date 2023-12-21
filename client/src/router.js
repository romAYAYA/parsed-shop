import { useUserStore } from './stores/user'

import { createRouter, createWebHistory } from 'vue-router'

import authPage from './pages/authPage.vue'
import homePage from './pages/homePage.vue'
import goodsPage from './pages/goodsPage.vue'
import errorPage from './pages/errorPage.vue'

const routes = [
  { path: '/', component: authPage },
  { path: '/home', component: homePage, meta: { requiresAuth: true } },
  { path: '/goods', component: goodsPage, meta: { requiresAuth: true } },
  { path: '/:pathMatch(.*)*', component: errorPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const userStore = useUserStore()

  if (to.meta.requiresAuth && !userStore.accessToken) {
    userStore.logoutUser()
    return next('/')
  }

  next()
})

export default router
