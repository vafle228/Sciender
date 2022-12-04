const ModuleLayout = () => import("./ModuleLayout.vue");
const UserInfo = () => import("./views/UserInfo.vue");
const UserProjects = () => import("./views/UserProjects.vue");
const ProjectDetail = () => import("./views/ProjectDetail.vue");

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
        {
            path: "project/:id",
            name: "project_detail",
            component: ProjectDetail,
        },
    ]
};

export default module_routes;
