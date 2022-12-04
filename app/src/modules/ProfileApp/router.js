const ModuleLayout = () => import("./ModuleLayout.vue");
const UserInfo = () => import("./views/UserInfo.vue");
const UserProjects = () => import("./views/UserProjects.vue");

const module_routes = {
    path: "/profile",
    component: ModuleLayout,
    children: [
        {
            path: "info/:id",
            name: "user_info",
            component: UserInfo,
        },
        {
            path: "projects/:id",
            name: "projects_info",
            component: UserProjects,
        },
    ]
};

export default module_routes;
