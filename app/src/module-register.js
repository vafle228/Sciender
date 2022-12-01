import store from "@/store/index";
import router from "@/router/index";


const registerModule = (name, module) => {
    if (module.router) router.addRoute(module.router);
    if (module.store) store.registerModule(name, module.store);
}

export const registerModules = (modules) => {
    Object.keys(modules).forEach((module_name) => {
        const module = modules[module_name];
        registerModule(module_name, module);
    });
};
