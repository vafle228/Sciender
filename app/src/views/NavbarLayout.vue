<template>
    <NavigationBar />
    <router-view />
</template>

<script>
    import NavigationBar from "@/components/NavigationBar.vue";

    export default {
        name: "NavbarLayout",

        components: { NavigationBar, },
    }
</script>