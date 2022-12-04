<template>
    <main class="container" v-if="user">

        <StandartHeader>
            <UserAvatar :link="user.image"/>
            <div class="column mrauto">
                <h2 class="header__title">{{ full_name }}</h2>
                <ObjectStatus :status="user.status"/>
            </div>
            
            <button class="header__button">
                <svg viewBox="0 0 128 512">
                    <path d="M64 368C90.51 368 112 389.5 112 416C112 442.5 90.51 464 64 464C37.49 464 16 442.5 16 416C16 389.5 37.49 368 64 368zM64 208C90.51 208 112 229.5 112 256C112 282.5 90.51 304 64 304C37.49 304 16 282.5 16 256C16 229.5 37.49 208 64 208zM64 144C37.49 144 16 122.5 16 96C16 69.49 37.49 48 64 48C90.51 48 112 69.49 112 96C112 122.5 90.51 144 64 144z"/>
                </svg>               
            </button>
        </StandartHeader>

        <div class="page">

            <div class="actions">
                <div class="action" v-if="!is_visitor">
                    <h2 class="action__title">Верификация</h2>
                    <p class="action__subtitle">Пройдите проверку данных</p>
                    <svg viewBox="0 0 512 512">
                        <path d="M466.5 83.71l-192-80c-5.875-2.5-12.16-3.703-18.44-3.703S243.5 1.203 237.6 3.703L45.61 83.71C27.73 91.08 16 108.6 16 127.1C16 385.4 205.4 512 255.9 512C305.2 512 496 387.3 496 127.1C496 108.6 484.3 91.08 466.5 83.71zM256 464C158.5 423.4 64 297.3 64 128l192-80L448 128C448 301.8 349.6 425 256 464zM200.1 247C196.3 242.3 190.1 239.1 184 239.1c-13.71 0-24 11.21-24 24C160 270.1 162.3 276.3 167 280.1l48 48C219.5 333.5 225.7 335.1 232 335.1c2.595 0 11.46-.4962 18.22-8.375l96-112c3.881-4.528 5.781-10.09 5.781-15.62c0-7.405-5.79-23.99-23.98-23.99c-6.756 0-13.48 2.831-18.24 8.362L230.7 276.7L200.1 247z"/>
                    </svg>
                </div>
                <div class="action" v-if="!is_visitor">
                    <h2 class="action__title">Редактировать профиль</h2>
                    <p class="action__subtitle">Изменить информацию о себе</p>
                    <svg viewBox="0 0 512 512">
                        <path d="M58.57 323.5L362.7 19.32C387.7-5.678 428.3-5.678 453.3 19.32L492.7 58.75C495.8 61.87 498.5 65.24 500.9 68.79C517.3 93.63 514.6 127.4 492.7 149.3L188.5 453.4C187.2 454.7 185.9 455.1 184.5 457.2C174.9 465.7 163.5 471.1 151.1 475.6L30.77 511C22.35 513.5 13.24 511.2 7.03 504.1C.8198 498.8-1.502 489.7 .976 481.2L36.37 360.9C40.53 346.8 48.16 333.9 58.57 323.5L58.57 323.5zM82.42 374.4L59.44 452.6L137.6 429.6C143.1 427.7 149.8 424.2 154.6 419.5L383 191L320.1 128.1L92.51 357.4C91.92 358 91.35 358.6 90.8 359.3C86.94 363.6 84.07 368.8 82.42 374.4L82.42 374.4z"/>
                    </svg>
                </div>
                <div class="action" v-if="is_visitor">
                    <h2 class="action__title">Отправить сообщение</h2>
                    <p class="action__subtitle">Создать личный чат</p>
                    <svg viewBox="0 0 640 512">
                        <path d="M208 0C322.9 0 416 78.8 416 176C416 273.2 322.9 352 208 352C189.3 352 171.2 349.7 153.9 345.8C123.3 364.8 79.13 384 24.95 384C14.97 384 5.93 378.1 2.018 368.9C-1.896 359.7-.0074 349.1 6.739 341.9C7.26 341.5 29.38 317.4 45.73 285.9C17.18 255.8 0 217.6 0 176C0 78.8 93.13 0 208 0zM164.6 298.1C179.2 302.3 193.8 304 208 304C296.2 304 368 246.6 368 176C368 105.4 296.2 48 208 48C119.8 48 48 105.4 48 176C48 211.2 65.71 237.2 80.57 252.9L104.1 277.8L88.31 308.1C84.74 314.1 80.73 321.9 76.55 328.5C94.26 323.4 111.7 315.5 128.7 304.1L145.4 294.6L164.6 298.1zM441.6 128.2C552 132.4 640 209.5 640 304C640 345.6 622.8 383.8 594.3 413.9C610.6 445.4 632.7 469.5 633.3 469.9C640 477.1 641.9 487.7 637.1 496.9C634.1 506.1 625 512 615 512C560.9 512 516.7 492.8 486.1 473.8C468.8 477.7 450.7 480 432 480C350 480 279.1 439.8 245.2 381.5C262.5 379.2 279.1 375.3 294.9 369.9C322.9 407.1 373.9 432 432 432C446.2 432 460.8 430.3 475.4 426.1L494.6 422.6L511.3 432.1C528.3 443.5 545.7 451.4 563.5 456.5C559.3 449.9 555.3 442.1 551.7 436.1L535.9 405.8L559.4 380.9C574.3 365.3 592 339.2 592 304C592 237.7 528.7 183.1 447.1 176.6L448 176C448 159.5 445.8 143.5 441.6 128.2H441.6z"/>
                    </svg>
                </div>
                <div class="action" v-if="is_visitor">
                    <h2 class="action__title">Лайк</h2>
                    <p class="action__subtitle">Поставить оценку</p>
                    <svg viewBox="0 0 512 512">
                        <path d="M96 191.1H32c-17.67 0-32 14.33-32 31.1v223.1c0 17.67 14.33 31.1 32 31.1h64c17.67 0 32-14.33 32-31.1V223.1C128 206.3 113.7 191.1 96 191.1zM512 227c0-36.89-30.05-66.92-66.97-66.92h-99.86C354.7 135.1 360 113.5 360 100.8c0-33.8-26.2-68.78-70.06-68.78c-46.61 0-59.36 32.44-69.61 58.5c-31.66 80.5-60.33 66.39-60.33 93.47c0 12.84 10.36 23.99 24.02 23.99c5.256 0 10.55-1.721 14.97-5.26c76.76-61.37 57.97-122.7 90.95-122.7c16.08 0 22.06 12.75 22.06 20.79c0 7.404-7.594 39.55-25.55 71.59c-2.046 3.646-3.066 7.686-3.066 11.72c0 13.92 11.43 23.1 24 23.1h137.6C455.5 208.1 464 216.6 464 227c0 9.809-7.766 18.03-17.67 18.71c-12.66 .8593-22.36 11.4-22.36 23.94c0 15.47 11.39 15.95 11.39 28.91c0 25.37-35.03 12.34-35.03 42.15c0 11.22 6.392 13.03 6.392 22.25c0 22.66-29.77 13.76-29.77 40.64c0 4.515 1.11 5.961 1.11 9.456c0 10.45-8.516 18.95-18.97 18.95h-52.53c-25.62 0-51.02-8.466-71.5-23.81l-36.66-27.51c-4.315-3.245-9.37-4.811-14.38-4.811c-13.85 0-24.03 11.38-24.03 24.04c0 7.287 3.312 14.42 9.596 19.13l36.67 27.52C235 468.1 270.6 480 306.6 480h52.53c35.33 0 64.36-27.49 66.8-62.2c17.77-12.23 28.83-32.51 28.83-54.83c0-3.046-.2187-6.107-.6406-9.122c17.84-12.15 29.28-32.58 29.28-55.28c0-5.311-.6406-10.54-1.875-15.64C499.9 270.1 512 250.2 512 227z"/>
                    </svg>
                </div>
            </div>

            <div class="tabs">
                <StandartTab :active="true" text="Информация" @click="$router.push({'name': 'user_info', params: {'id': $route.params.id}})"/>
                <StandartTab text="Проекты" @click="$router.push({'name': 'projects_info', params: {'id': $route.params.id}})"/>
            </div>

            <div class="page__block">
                <h2>О себе</h2>
                <p>{{ user.about }}</p>
            </div>

            <div class="page__block">
                <h2>Должность</h2>
                <p>{{ user.permission }}</p>
            </div>

            <div class="page__block">
                <h2>Образование</h2>
                <p>{{ user.specialty }}</p>
            </div>

            <div class="page__block">
                <h2>Публикации</h2>
                <p 
                    v-for="(link, index) in user.work_links"
                    :key="index"
                >
                    {{ link }}
                </p>
            </div>
        </div>

    </main>
</template>

<script>
    import axios from "axios";
    import { USER_INFO } from "@/utils/constants";
    
    import StandartTab from "@/components/StandartTab.vue";
    import UserAvatar from "@/components/UserAvatar.vue";
    import StandartHeader from "@/components/StandartHeader.vue";
    import ObjectStatus from "@/components/ObjectStatus.vue";

    import Notification from "@/utils/notification";


    export default {
        name: "UserInfo",

        components: { UserAvatar, StandartHeader, ObjectStatus, StandartTab },

        data() {
            return {
                user: undefined,
                is_visitor: false,
            }
        },

        beforeMount() {
            axios.get(USER_INFO(this.$route.params.id))
                .then((response) => {
                    this.user = response.data;
                    this.is_visitor = this.user.id != this.$route.params.id
                })
                .catch((error) => Notification.errorNotification(error))
        },

        computed: {
            full_name() {  return `${this.user.surname} ${this.user.name}`; }
        }
    }
</script>

<style src="@/assets/stylesheets/Page.css"/>
<style src="@/assets/stylesheets/PageBlock.css"/>
<style src="@/assets/stylesheets/Action.css"/>
<style src="@/assets/stylesheets/Actions.css"/>