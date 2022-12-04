<template>
    <p class="status" :status="statusClass">{{ status }}</p>
</template>

<script>
    export default {
        name: "ObjectStatus",
        
        props: {
            status: String
        },

        computed: {
            statusClass() {
                switch (this.status) {
                    case "Завершён": return "grey";
                    case "В работе": return "yellow";
                    
                    default: return "green";
                }
            }
        }
    }
</script>

<style scoped src="@/assets/stylesheets/Status.css" />
