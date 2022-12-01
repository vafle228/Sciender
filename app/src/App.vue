<template>
    <router-view @error="print"/>
</template>

<script>
    export default {
        name: "MainPage",

        methods: {
            print(event) {
                console.log(event)
            }
        }
    }
</script>

<style src="@/assets/index.css"/>
