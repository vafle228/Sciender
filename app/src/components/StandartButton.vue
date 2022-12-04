<template>
    <button class="standartButton">
        <slot></slot>
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
