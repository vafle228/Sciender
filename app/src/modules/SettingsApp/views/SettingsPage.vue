<template>
   <main class="container">

    <StandartHeader>
        <h1 class="header__title">Настройки</h1>
    </StandartHeader>

    <div class="page">

        <div class="card expanded">
            <h2 class="card__title">
                Внешний вид
            </h2>
            <div class="card__body">
                <div class="card__block">
                    <p>Темная тема</p>
                    <input type="checkbox" :checked="theme_color === 'dark'" class="toggle" @input="changeTheme">
                </div>
            </div>
        </div>

        <div class="card expanded">
            <h2 class="card__title">
                Язык интерфейса
            </h2>
            <div class="card__body">
                <div class="languageSelect">
                    <div class="language active">
                        <img src="@/assets/flags/russia.png" class="language__flag">
                        <p class="language__name">Русский</p>
                        <svg viewBox="0 0 11.623 8.623">
                            <path d="M17.428,8.072a1.316,1.316,0,0,1,0,1.856l-6,6a1.316,1.316,0,0,1-1.856,0l-3-3a1.313,1.313,0,0,1,1.856-1.856L10.5,13.144l5.072-5.072a1.316,1.316,0,0,1,1.856,0Z" transform="translate(-6.189 -7.689)"/>
                        </svg>
                    </div>
                    <div class="language">
                        <img src="@/assets/flags/united-kingdom.png" class="language__flag">
                        <p class="language__name">English</p>
                        <svg viewBox="0 0 11.623 8.623">
                            <path d="M17.428,8.072a1.316,1.316,0,0,1,0,1.856l-6,6a1.316,1.316,0,0,1-1.856,0l-3-3a1.313,1.313,0,0,1,1.856-1.856L10.5,13.144l5.072-5.072a1.316,1.316,0,0,1,1.856,0Z" transform="translate(-6.189 -7.689)"/>
                        </svg>
                    </div>
                </div>
            </div>
        </div>

        <div class="aboutDevelopers">
            <p>Создано для конкурса именной стипендии <a>Пик_IT</a></p><br>
            <p>Разработчики</p>
            <a>Смышляев Дмитрий</a><br>
            <a>Каратаев Вадим</a><br>
        </div>
    </div>

    </main>
</template>

<script>
    import StandartHeader from "@/components/StandartHeader.vue";

    export default {
        name: "SettingsPage",

        components: { StandartHeader },

        data() {
            return {
                theme_color: "",
            }
        },

        created() { this.theme_color = document.body.getAttribute("appearance"); },

        methods: {
            changeTheme() {
                switch (this.theme_color) {
                    case "dark": this.theme_color = "light"; break;
                    case "light": this.theme_color = "dark"; break;

                    default: this.theme_color = "dark";
                }
                document.body.setAttribute("appearance", this.theme_color);
            }
        }
    }
</script>

<style src="@/assets/stylesheets/Page.css" />
<style src="@/assets/stylesheets/Language.css" />
<style src="@/assets/stylesheets/LanguageSelect.css" />
<style src="@/assets/stylesheets/AboutDevelopers.css"/>
<style src="@/assets/stylesheets/Card.css"/>
<style src="@/assets/stylesheets/Toggle.css"/>
