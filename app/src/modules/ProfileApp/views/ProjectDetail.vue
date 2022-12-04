<template>
    <main class="container" v-if="project">

        <StandartHeader>
            <button class="header__button" @click="$router.go(-1)">
                <svg viewBox="0 0 320 512">
                    <path d="M206.7 464.6l-183.1-191.1C18.22 267.1 16 261.1 16 256s2.219-11.97 6.688-16.59l183.1-191.1c9.152-9.594 24.34-9.906 33.9-.7187c9.625 9.125 9.938 24.37 .7187 33.91L73.24 256l168 175.4c9.219 9.5 8.906 24.78-.7187 33.91C231 474.5 215.8 474.2 206.7 464.6z"/>
                </svg>
            </button>
            <h1 class="header__title">Просмотр проекта</h1>
            <button class="header__button">
                <svg viewBox="0 0 128 512">
                    <path d="M64 368C90.51 368 112 389.5 112 416C112 442.5 90.51 464 64 464C37.49 464 16 442.5 16 416C16 389.5 37.49 368 64 368zM64 208C90.51 208 112 229.5 112 256C112 282.5 90.51 304 64 304C37.49 304 16 282.5 16 256C16 229.5 37.49 208 64 208zM64 144C37.49 144 16 122.5 16 96C16 69.49 37.49 48 64 48C90.51 48 112 69.49 112 96C112 122.5 90.51 144 64 144z"/>
                </svg>               
            </button>
        </StandartHeader>

        <div class="page">

            <img class="banner" :src="project.image" />

            <div class="page__block">
                <h2>{{ project.name }}</h2>
                <p>{{ project.about }}</p>
                
                <div class="tagList">
                    <div 
                        class="tag"
                        v-for="(tag, index) in project.interests"
                        :key="index"
                    >
                        {{ tag.name }}
                    </div>
                </div>

            </div>

            <div class="page__block">
                <h2>Научный руководитель</h2>
                <div class="user" action="Перейти в профиль" @click="$router.push({'name': 'user_info', params: {'id': project.tutor.id}})">
                    <img :src="project.tutor.image" class="user__image">
                    <p class="user__name">{{ fullName(project.tutor) }}</p>
                    <svg viewBox="0 0 11.623 8.623">
                        <path d="M17.428,8.072a1.316,1.316,0,0,1,0,1.856l-6,6a1.316,1.316,0,0,1-1.856,0l-3-3a1.313,1.313,0,0,1,1.856-1.856L10.5,13.144l5.072-5.072a1.316,1.316,0,0,1,1.856,0Z" transform="translate(-6.189 -7.689)"/>
                    </svg>               
                </div>
            </div>
            
            <div class="page__block">
                <h2>Участники проекта</h2>
                <div 
                    class="user" action="Перейти в профиль"
                    v-for="(user, index) in project.team"
                    :key="index"
                    @click="$router.push({'name': 'user_info', params: {'id': user.id}})"
                >
                    <img :src="user.image" class="user__image">
                    <p class="user__name">{{ fullName(user) }}</p>
                    <svg viewBox="0 0 11.623 8.623">
                        <path d="M17.428,8.072a1.316,1.316,0,0,1,0,1.856l-6,6a1.316,1.316,0,0,1-1.856,0l-3-3a1.313,1.313,0,0,1,1.856-1.856L10.5,13.144l5.072-5.072a1.316,1.316,0,0,1,1.856,0Z" transform="translate(-6.189 -7.689)"/>
                    </svg>
                </div>
            </div>
        </div>

    </main>
</template>

<script>
    import axios from 'axios';

    import StandartHeader from "@/components/StandartHeader.vue";

    import Notification from "@/utils/notification";
    import { PROJECT_DETAIL } from "@/utils/constants";

    export default {
        name: "ProjectDetail",

        components: { StandartHeader },

        data() {
            return {
                project: undefined,
            }
        },

        created() {
            axios.get(PROJECT_DETAIL(this.$route.params.id))
                .then((response) => this.project = response.data)
                .catch((error) => Notification.errorNotification(error))
        },

        methods: {
            fullName(user) {
                return `${user.surname} ${user.name}`;
            }
        }
    }
</script>

<style src="@/assets/stylesheets/Page.css"/>
<style src="@/assets/stylesheets/PageBlock.css"/>
<style src="@/assets/stylesheets/User.css"/>
<style src="@/assets/stylesheets/Tag.css" />
<style src="@/assets/stylesheets/TagList.css" />
