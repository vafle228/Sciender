<template>
    <div :class="`tabs__link ${active ? 'active' : ''}`">{{ text }}</div>
</template>

<script>
    export default {
        name: "StandartTab",

        props: {
            active: {
                type: Boolean,
                default: false,
            },
            text: String,
        }
    }
</script>

<style src="@/assets/stylesheets/StandartTab.css"/>
