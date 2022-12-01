const ModuleLayout = () => import("./ModuleLayout.vue");
const MainPage = () => import("./views/MainPage.vue");


const module_routes = {
    path: "/sciender",
    component: ModuleLayout,
    children: [
        {
            path: "main",
            name: "main",
            component: MainPage,
        }
    ]
};

export default module_routes;
