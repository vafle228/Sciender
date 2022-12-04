<template>
    <main class="container">

        <StandartHeader :need_avatar="true">
            <h1 class="header__title">Главная</h1>
        </StandartHeader>

        <div class="page">

            <UserCard
                v-if="card"

                :name="card.name"
                :status="card.status"
                :surname="card.surname"
                :image_link="card.image"
                :projects="card.projects"
                :interests="card.interests"
            />

            <div class="row g24">
                <AnotherButton @click="previousPage">
                    <svg viewBox="0 0 320 512">
                        <path d="M206.7 464.6l-183.1-191.1C18.22 267.1 16 261.1 16 256s2.219-11.97 6.688-16.59l183.1-191.1c9.152-9.594 24.34-9.906 33.9-.7187c9.625 9.125 9.938 24.37 .7187 33.91L73.24 256l168 175.4c9.219 9.5 8.906 24.78-.7187 33.91C231 474.5 215.8 474.2 206.7 464.6z"/>
                    </svg>
                </AnotherButton>
                
                <StandartButton>
                    <p>Лайк</p>
                </StandartButton>
                
                <AnotherButton @click="nextPage">
                    <svg viewBox="0 0 320 512">
                        <path d="M113.3 47.41l183.1 191.1c4.469 4.625 6.688 10.62 6.688 16.59s-2.219 11.97-6.688 16.59l-183.1 191.1c-9.152 9.594-24.34 9.906-33.9 .7187c-9.625-9.125-9.938-24.38-.7187-33.91l168-175.4L78.71 80.6c-9.219-9.5-8.906-24.78 .7187-33.91C88.99 37.5 104.2 37.82 113.3 47.41z"/>
                    </svg>
                </AnotherButton>
            </div>

        </div>
    </main>
</template>

<script>
    import axios from "axios";

    import UserCard from "@/components/UserCard.vue";
    import AnotherButton from "@/components/AnotherButton.vue";
    import StandartButton from "@/components/StandartButton.vue";
    import StandartHeader from "@/components/StandartHeader.vue";

    import { USER_CARD_URL } from "@/utils/constants";

    export default {
        name: "MainPage",

        components: {
            UserCard,
            StandartButton,
            AnotherButton,
            StandartHeader,
        },

        data() {
            return {
                user_cards: [],
                current_card: 0,
            }
        },

        created () {
            axios.get(USER_CARD_URL)
                .then((response) => this.user_cards = response.data)
                .catch((error) => console.log(error));
        },

        methods: {
            nextPage() {
                this.current_card++;

                if (this.current_card === this.user_cards.length)
                    this.current_card %= this.user_cards.length;
            },
            
            previousPage() { 
                if (this.current_card === 0)
                    this.current_card = this.user_cards.length;
                this.current_card--;
            },
        },

        computed: {
            card() { return this.user_cards[this.current_card]; },
        }
    }
</script>

<style src="@/assets/stylesheets/Container.css" />
<style src="@/assets/stylesheets/Header.css" />
<style src="@/assets/stylesheets/Page.css" />
