<template>
    <div class="userCard" @click="$router.push({'name': 'user_info', 'params': {'id': id}})">
        <img :src="image_link" class="userCard__image">

        <div class="userCard__content">
            <ObjectStatus :status="status"/>
            <h2 class="userCard__name">{{ username }}</h2>
            <p class="userCard__role">{{ permission }}</p>

            <div class="tagList" v-if="interests">
                <div 
                    class="tag"
                    v-for="(interest, index) in interests"
                    :key="index"
                >
                    {{ interest.name }}
                </div>
            </div>

            <div class="userCard__projectList" v-if="projects">
                <div 
                    class="projectCard"
                    v-for="(project, index) in projects"
                    :key="index"
                >
                    <h3>{{ project.name }}</h3>
                    <ObjectStatus :status="project.status"/>
                    <p>{{ project.about }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import ObjectStatus from './ObjectStatus.vue';
    
    export default {
        name: "UserCard",

        components: {
            ObjectStatus,
        },

        props: {
            id: Number,
            name: String,
            status: String,
            surname: String,
            permission: String,
            image_link: String,

            projects: Array,
            interests: Array,
        },

        computed: {
            username() {
                return `${this.name} ${this.surname}`
            },
        }
    }
</script>

<style src="@/assets/stylesheets/Tag.css" />
<style src="@/assets/stylesheets/TagList.css" />
<style src="@/assets/stylesheets/UserCard.css" />
