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

        props: {
            link: {
                type: String,
                default: ""
            }
        },

        data() {
            return {
                user_image: undefined,
            }
        },

        beforeMount() {
            if (this.link === "")
                axios.get(USER_IMAGE_URL)
                    .then((response) => this.user_image = response.data.image)
                    .catch((error) => console.log(error));
            else this.user_image = this.link;
        }
    }
</script>

<style src="@/assets/stylesheets/Avatar.css" />
