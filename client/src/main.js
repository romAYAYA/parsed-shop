import { createApp } from 'vue'
import App from './App.vue'

import './assets/css/default.css'

import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config'

import 'primevue/resources/primevue.min.css'
import 'primevue/resources/themes/saga-blue/theme.css'
import 'primeicons/primeicons.css'
import '/node_modules/primeflex/primeflex.css'
import ToastService from 'primevue/toastservice'

const pinia = createPinia()

const app = createApp(App)

app.use(pinia)
app.use(PrimeVue)
app.use(ToastService)
app.mount('#app')
