const ModuleLayout = () => import("./ModuleLayout.vue");
const ChatPage = () => import("./views/ChatPage.vue")


const module_routes = {
    path: "/chats",
    component: ModuleLayout,
    children: [
        {
            path: "",
            name: "chats",
            component: ChatPage,
        }
    ]
};

export default module_routes;
