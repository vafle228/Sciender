<template>
    <NavigationBar active="profile" :id="id"/>
    <router-view />
</template>

<script>
    import UseridMixin from '@/utils/GetUserid';
    import NavigationBar from '@/components/NavigationBar.vue'; 

	export default {
        mixins: [ UseridMixin ],
        components: { NavigationBar }
    };
</script>
