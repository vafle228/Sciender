<template>
    <input 
        class="input"
        autocomplete="off"
        @input="$emit('update:modelValue', $event.target.value)"
    />
</template>

<script>
    export default {
        name: "StandartInput",
    }
</script>

<style src="@/assets/stylesheets/StandartInput.css"/>
