const ModuleLayout = () => import("./ModuleLayout.vue");

const module_routes = {
    path: "/contacts",
    component: ModuleLayout,
    children: [
        {
            
        }
    ]
}

export default module_routes;
