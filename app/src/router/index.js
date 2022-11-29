import { createRouter, createWebHistory } from "vue-router";

import LoginPage from "@/views/LoginPage.vue";
import NavbarLayout from "@/views/NavbarLayout.vue";
import MainPage from "@/views/MainPage.vue"

import { 
    USER_PERMISSION, 
    PERMISSION_NAME, 
    TOKEN_NAME, 
    ADMIN_PERMISSION 
} from "@/services/constants";


const routes = [
    {
        path: "/login",
        name: "login",
        component: LoginPage,
    },
    {
        path: "/sciender",
        name: "navigation",
        component: NavbarLayout,

        beforeEnter: (to, from, next) => {
            if (localStorage.getItem(TOKEN_NAME)) {
                const permission = localStorage.getItem(PERMISSION_NAME)
                if (permission === USER_PERMISSION) return next();
                if (permission === ADMIN_PERMISSION) return next({ name: "login" })
            } 
            return next({ name: "login" });
        },

        children: [
            {
                path: "main",
                name: "main_page",
                component: MainPage,
            }
        ]
    },
    {
        path: "",
        redirect: { name: "login" },
    }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
