<template>
    <router-view />
</template>


<script>
    export default {
        beforeMount() {
            const token = localStorage.getItem("sciender-token");
            console.log(token === null);
            if (token === null) this.$router.push('/login');
        }
    }
</script>

<style src="@/assets/index.css"/>
