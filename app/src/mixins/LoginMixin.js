import axios from "axios";
import Notification from "@/services/Notification";

import { PERMISSION_NAME, TOKEN_NAME } from "@/services/constants";

const login_root = "token/login"

export default {
    methods: {
        _authUser(payload) {
            axios.defaults.headers.common["Authorization"] = "";
            
            axios
                .post(login_root, payload)
                .then((response) => {
                    const token = response.data.auth_token;

                    this._updateLocalStorage(response);
                    this.$store.commit("setToken", token);
                    axios.defaults.headers.common["Authorization"] = `Token ${token}`;

                    this.redirectUser(response.data.user);
                })
                .catch((error) => Notification.errorNotification(error));
        },

        _updateLocalStorage(response) {
            const token = response.data.auth_token;
            const permission = response.data.user.permission;

            localStorage.setItem(TOKEN_NAME, token);
            localStorage.setItem(PERMISSION_NAME, permission);
        },

        redirectUser(user_info) { user_info; console.warn("Override redirectUser"); }
    }
}
