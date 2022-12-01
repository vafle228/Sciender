const ModuleLayout = () => import("./ModuleLayout.vue");
const LoginPage = () => import("./views/LoginPage.vue");


const module_routes = {
    path: "/auth",
    component: ModuleLayout,
    children: [
        {
            path: "login",
            name: "login",
            component: LoginPage,
        },
    ]
};

export default module_routes;
