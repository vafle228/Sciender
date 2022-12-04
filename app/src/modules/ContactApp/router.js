const ModuleLayout =  () => import("./ModuleLayout.vue");
const ContactPage = () => import("./views/ContactPage.vue");

const module_routes = {
    path: "/contacts",
    component: ModuleLayout,
    children: [
        {
            path: "",
            name: "contacts",
            component: ContactPage,
        }
    ]
}

export default module_routes;
