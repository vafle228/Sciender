<template>
    <main class="container">

        <StandartHeader :need_avatar="true">
            <div class="search">
                <svg viewBox="0 0 512 512">
                    <path d="M504.1 471l-134-134C399.1 301.5 415.1 256.8 415.1 208c0-114.9-93.13-208-208-208S-.0002 93.13-.0002 208S93.12 416 207.1 416c48.79 0 93.55-16.91 129-45.04l134 134C475.7 509.7 481.9 512 488 512s12.28-2.344 16.97-7.031C514.3 495.6 514.3 480.4 504.1 471zM48 208c0-88.22 71.78-160 160-160s160 71.78 160 160s-71.78 160-160 160S48 296.2 48 208z"/>
                </svg>
                <input type="text" placeholder="Поиск...">
            </div>
        </StandartHeader>

        <div class="page">

            <nav class="tabs">
                <StandartTab :active="true" text="Все" @click="changeType('All')"/>
                <StandartTab text="Личные" @click="changeType('Personal')"/>
                <StandartTab text="Командные" @click="changeType('Team')"/>
            </nav>

            <div class="chatList">
                <div 
                    class="chat" 
                    v-for="(chat_room, index) in chat_rooms"
                    :key="index"
                >
                    <img src="../images/avatars/СД.png" class="chat__thumbnail">
                    <div class="chat__info">
                        <p class="chat__name">Название беседы</p>
                        <p class="chat__lastMessage">Текст последнего сообщения</p>
                    </div>
                    <div class="chat__date">08.11</div>
                </div>
                <div class="chat">
                    <img src="../images/avatars/СЭ.png" class="chat__thumbnail">
                    <div class="chat__info">
                        <p class="chat__name">Название беседы</p>
                        <p class="chat__lastMessage">Текст последнего сообщения</p>
                    </div>
                    <div class="chat__date">08.11</div>
                </div>
                <div class="chat">
                    <img src="../images/avatars/БА.png" class="chat__thumbnail">
                    <div class="chat__info">
                        <p class="chat__name">Название беседы</p>
                        <p class="chat__lastMessage">Текст последнего сообщения</p>
                    </div>
                    <div class="chat__date">08.11</div>
                </div>
            </div>
        </div>

        <button class="createChatButton">
            <svg viewBox="0 0 512 512">
                <path d="M58.57 323.5L362.7 19.32C387.7-5.678 428.3-5.678 453.3 19.32L492.7 58.75C495.8 61.87 498.5 65.24 500.9 68.79C517.3 93.63 514.6 127.4 492.7 149.3L188.5 453.4C187.2 454.7 185.9 455.1 184.5 457.2C174.9 465.7 163.5 471.1 151.1 475.6L30.77 511C22.35 513.5 13.24 511.2 7.03 504.1C.8198 498.8-1.502 489.7 .976 481.2L36.37 360.9C40.53 346.8 48.16 333.9 58.57 323.5L58.57 323.5zM82.42 374.4L59.44 452.6L137.6 429.6C143.1 427.7 149.8 424.2 154.6 419.5L383 191L320.1 128.1L92.51 357.4C91.92 358 91.35 358.6 90.8 359.3C86.94 363.6 84.07 368.8 82.42 374.4L82.42 374.4z"/>
            </svg>           
        </button>

    </main>
</template>

<script>
    import StandartTab from "@/components/StandartTab.vue";
    import StandartHeader from "@/components/StandartHeader.vue";
    import axios from "axios";

    import Notification from "@/utils/notification";

    import { USER_CHATS } from "@/utils/constants";

    export default {
        name: "ChatPage",

        data() {
            return {
                type: "All",
                chat_rooms: undefined
            }
        },

        components: { StandartHeader, StandartTab, },

        created() {
            axios.get(`${USER_CHATS}?type=${this.type}`)
                .then((response) => this.chat_rooms = response.data)
                .catch((error) => Notification.errorNotification(error))
        },

        methods: {
            changeType(new_type) { 
                this.type = new_type;
                
                axios.get(`${USER_CHATS}?type=${this.type}`)
                    .then((response) => this.chat_rooms = response.data)
                    .catch((error) => Notification.errorNotification(error))
            },
        },
    }
</script>

<style src="@/assets/stylesheets/Search.css" />
<style src="@/assets/stylesheets/Chat.css" />
<style src="@/assets/stylesheets/Page.css" />
<style src="@/assets/stylesheets/CreateChatButton.css" />