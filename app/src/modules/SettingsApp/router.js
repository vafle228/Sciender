const ModuleLayout = () => import("./ModuleLayout.vue");
const SettingsPage = () => import("./views/SettingsPage.vue");


const module_routes = {
    path: "/settings",
    component: ModuleLayout,
    children: [
        {
            path: "",
            name: "settings",
            component: SettingsPage,
        }
    ]
};

export default module_routes;
