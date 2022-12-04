<template>
    <div class="avatar">
        <img :src="user_image"/>
    </div>
</template>

<script>
    import axios from "axios";

    import { USER_IMAGE_URL } from "@/utils/constants";

    export default {
        name: "UserAvatar",

        data() {
            return {
                user_image: undefined,
            }
        },

        beforeMount() {
            axios.get(USER_IMAGE_URL)
                .then((response) => this.user_image = response.data.image)
                .catch((error) => console.log(error));
        }
    }
</script>

<style src="@/assets/stylesheets/Avatar.css" />
