<template>
    <input 
        type="text"
        class="input"
        :name="name"
        :placeholder="placeholder"
        @input="$emit('update:modelValue', $event.target.value)"
        autocomplete="off"
    />
</template>

<script>
    export default {
        name: "StandartInput",
        
        props: {
            name: String,
            placeholder: String,
        },

        // model: {
        //     prop: "value",
        //     event: "input",
        // }
    }
</script>

<style src="@/assets/stylesheets/StandartInput.css"/>
