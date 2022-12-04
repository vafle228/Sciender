<template>
    <main class="container">

        <StandartHeader :need_avatar="true">
            <h1 class="header__title">Контакты</h1>
        </StandartHeader>

        <div class="page">
            <div :class="to_matches.length ? 'card expanded' : 'card'">
                <div class="card__header">
                    <h2 class="card__title">Вы понравились этим людям</h2>
                    <svg viewBox="0 0 448 512">
                        <path d="M432.6 209.3l-191.1 183.1C235.1 397.8 229.1 400 224 400s-11.97-2.219-16.59-6.688L15.41 209.3C5.814 200.2 5.502 184.1 14.69 175.4c9.125-9.625 24.38-9.938 33.91-.7187L224 342.8l175.4-168c9.5-9.219 24.78-8.906 33.91 .7187C442.5 184.1 442.2 200.2 432.6 209.3z"/>
                    </svg>
                </div>
                <div class="card__body">
                    <div class="avatarSlider" v-if="to_matches">
                        <div 
                            class="avatarLarge"
                            v-for="(match, index) in to_matches"
                            :key="index"
                        >
                            <img :src="match.from_user.image">
                        </div>
                    </div>
                    <StandartButton>
                        <p>Просмотреть</p>
                    </StandartButton>
                </div>
            </div>

            <div :class="from_matches.length ? 'card expanded' : 'card'">
                <div class="card__header">
                    <h2 class="card__title">Вам понравились эти люди</h2>
                    <svg viewBox="0 0 448 512">
                        <path d="M432.6 209.3l-191.1 183.1C235.1 397.8 229.1 400 224 400s-11.97-2.219-16.59-6.688L15.41 209.3C5.814 200.2 5.502 184.1 14.69 175.4c9.125-9.625 24.38-9.938 33.91-.7187L224 342.8l175.4-168c9.5-9.219 24.78-8.906 33.91 .7187C442.5 184.1 442.2 200.2 432.6 209.3z"/>
                    </svg>
                </div>
                <div class="card__body">
                    <div class="avatarSlider" v-if="from_matches">
                        <div 
                            class="avatarLarge"
                            v-for="(match, index) in from_matches"
                            :key="index"
                        >
                            <img :src="match.to_user.image">
                        </div>
                    </div>
                    <StandartButton>
                        <p>Просмотреть</p>
                    </StandartButton>
                </div>
            </div>
            
            <div class="page__block">

                <div class="search">
                    <svg viewBox="0 0 512 512">
                        <path d="M504.1 471l-134-134C399.1 301.5 415.1 256.8 415.1 208c0-114.9-93.13-208-208-208S-.0002 93.13-.0002 208S93.12 416 207.1 416c48.79 0 93.55-16.91 129-45.04l134 134C475.7 509.7 481.9 512 488 512s12.28-2.344 16.97-7.031C514.3 495.6 514.3 480.4 504.1 471zM48 208c0-88.22 71.78-160 160-160s160 71.78 160 160s-71.78 160-160 160S48 296.2 48 208z"/>
                    </svg>
                    <input type="text" placeholder="Поиск...">
                </div>
                
                <div class="userList" v-if="matches">
                    <div 
                        class="user" 
                        v-for="(match, index) in matches"
                        :key="index"
                        @click="$router.push({'name': 'user_info', params: {'id': getContact(match).id}})"
                        action="Перейти в профиль"
                    >
                        <img :src="getContact(match).image" class="user__image">
                        <p class="user__name">{{ fullName(getContact(match)) }}</p>
                        <svg viewBox="0 0 11.623 8.623">
                            <path d="M17.428,8.072a1.316,1.316,0,0,1,0,1.856l-6,6a1.316,1.316,0,0,1-1.856,0l-3-3a1.313,1.313,0,0,1,1.856-1.856L10.5,13.144l5.072-5.072a1.316,1.316,0,0,1,1.856,0Z" transform="translate(-6.189 -7.689)"/>
                        </svg>               
                    </div>
                </div>
            </div>
                    
        </div>

    </main>
</template>

<script>
    import axios from "axios";
    import { 
        TO_USER_PREMATCH, 
        FROM_USER_PREMATCH, 
        USER_MATCH,
        ID_NAME
    } from "@/utils/constants";
    import Notification from "@/utils/notification";
    import StandartButton from "@/components/StandartButton.vue";
    import StandartHeader from "@/components/StandartHeader.vue";

    export default {
        name: "ContactPage",

        components: { StandartHeader, StandartButton },

        data() {
            return {
                to_matches: undefined,
                from_matches: undefined,
                matches: undefined,
            }
        },

        created() {
            axios.get(TO_USER_PREMATCH)
                .then((response) => this.to_matches = response.data)
                .catch((error) => Notification.errorNotification(error))
            
            axios.get(FROM_USER_PREMATCH)
                .then((response) => this.from_matches = response.data)
                .catch((error) => Notification.errorNotification(error))
            
            axios.get(USER_MATCH)
                .then((response) => this.matches = response.data)
                .catch((error) => Notification.errorNotification(error))
        },

        methods: {
            getContact(match) {
                const user_id = localStorage.getItem(ID_NAME);

                if (match.to_user.id == user_id)
                    return match.from_user;
                return match.to_user;
            },

            fullName(user) {
                return `${user.surname} ${user.name}`
            }
        }
    }
</script>

<style src="@/assets/stylesheets/Page.css" />
<style src="@/assets/stylesheets/PageBlock.css" />
<style src="@/assets/stylesheets/AvatarLarge.css" />
<style src="@/assets/stylesheets/AvatarSlider.css" />
<style src="@/assets/stylesheets/Search.css" />
<style src="@/assets/stylesheets/Card.css" />
<style src="@/assets/stylesheets/User.css"/>
