<template>
    <input 
        type="text"
        class="input"
        :name="name"
        :placeholder="placeholder"
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
    }
</script>

<style src="@/assets/stylesheets/StandartInput.css"/>
