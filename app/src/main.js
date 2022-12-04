import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';

import AuthApp from '@/modules/AuthApp';
import MainApp from '@/modules/MainApp';
import ProfileApp from '@/modules/ProfileApp';

import { BASE_URL } from '@/utils/constants'

import { registerModules } from './module-register';


axios.defaults.baseURL = BASE_URL;

registerModules({
    authapp: AuthApp,
    mainapp: MainApp,
    profileapp: ProfileApp,
});

createApp(App).use(store).use(router).mount('#app');
