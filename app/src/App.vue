<template>
    <router-view />
</template>


<script>
    export default {
        created() {
            const token = localStorage.getItem("sciender-token");
            if (token === null) this.$router.push('/login');
        }
    }
</script>

<style src="@/assets/index.css"/>
