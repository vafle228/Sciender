<template>
    <NavigationBar />
    <router-view />
</template>

<script>
    import NavigationBar from '@/components/NavigationBar.vue'; 

	export default {
        components: { NavigationBar }
    };
</script>
