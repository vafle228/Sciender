import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

import axios from 'axios';

import { BASE_URL } from '@/services/constants'

axios.defaults.baseURL = BASE_URL;

createApp(App).use(store).use(router).mount('#app');
