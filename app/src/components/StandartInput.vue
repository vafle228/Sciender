<template>
    <input 
        class="input"
        @input="$emit('update:modelValue', $event.target.value)"
        autocomplete="off"
    />
</template>

<script>
    export default {
        name: "StandartInput",
    }
</script>

<style src="@/assets/stylesheets/StandartInput.css"/>
