import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/main.css'
import './style.css'

import PrimeVue from 'primevue/config'
import Aura from '@primeuix/themes/aura'
import 'primeicons/primeicons.css'

import sidebar from './layouts/sidebar.vue'

import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import InputText from 'primevue/inputtext';

const app = createApp(App)

app.use(router)
app.use(PrimeVue, {
  theme: {
    preset: Aura
  }
})

app.component('sidebar', sidebar)

app.component('DataTable', DataTable)
app.component('Column', Column)
app.component('Button', Button)
app.component('IconField', IconField)
app.component('InputIcon', InputIcon)
app.component('InputText', InputText)

app.mount('#app')
