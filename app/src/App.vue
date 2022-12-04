<template>
    <router-view />
</template>

<script>
    import axios from "axios";
    import { TOKEN_NAME } from "@/utils/constants";

    export default {
        name: "RootLayout",

        beforeCreate() {
            const token = localStorage.getItem(TOKEN_NAME);
            axios.defaults.headers.common["Authorization"] = `Token ${token}`;
        }
    }
</script>

<style src="@/assets/index.css"/>
