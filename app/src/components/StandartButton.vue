<template>
    <button class="standartButton">
        <p>{{ text }}</p>
    </button>
</template>

<script>
    export default {
        name: "StandartButton",

        props: {
            text: String,
        }
    }
</script>

<style src="@/assets/stylesheets/StandartButton.css"/>
