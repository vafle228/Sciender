import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';

import AuthApp from '@/modules/AuthApp';
import MainApp from '@/modules/MainApp';
import ProfileApp from '@/modules/ProfileApp';
import SettingsApp from './modules/SettingsApp';
import ContactApp from './modules/ContactApp';

import { BASE_URL } from '@/utils/constants'

import { registerModules } from './module-register';


axios.defaults.baseURL = BASE_URL;

registerModules({
    authapp: AuthApp,
    mainapp: MainApp,
    profileapp: ProfileApp,
    settingsapp: SettingsApp,
    contactapp: ContactApp,
});

createApp(App).use(store).use(router).mount('#app');
