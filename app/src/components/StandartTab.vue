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
        },

        methods: {
            print(event) {
                console.log(event)
            }
        }
    }
</script>

<style src="@/assets/stylesheets/StandartTab.css"/>
