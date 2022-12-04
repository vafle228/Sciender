<template>
    <div class="header">
        <slot></slot>
        <UserAvatar v-if="need_avatar"/>
    </div>
</template>

<script>
    import UserAvatar from "./UserAvatar.vue";
    export default {
        name: "StandartHeader",

        props: {
            need_avatar: {
                type: Boolean,
                default: false,
            }
        },

        components: { UserAvatar }
    }
</script>

<style src="@/assets/stylesheets/Header.css" />
<style src="@/assets/stylesheets/Container.css" />
