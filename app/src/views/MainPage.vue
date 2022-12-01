<template>
    <main class="container">

        <div class="header">
            <h1 class="header__title">Главная</h1>
            <div class="avatar">
                <img src="">
            </div>
        </div>

        <div class="page">

            <div class="userCard">
                <img src="" class="userCard__image">

                <div class="userCard__content">
                    <p class="status" status="green">В поиске команды</p>
                    <h2 class="userCard__name">Имя Фамилия</h2>
                    <p class="userCard__role">Научный сотрудник</p>

                    <div class="tagList">
                        <div class="tag">
                            Направление
                        </div>
                    </div>

                    <div class="userCard__projectList">
                        <div class="projectCard">
                            <h3>Название проекта</h3>
                            <p class="status" status="green">Набор команды</p>
                            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam nam corrupti vitae.</p>
                        </div>
                        <div class="projectCard">
                            <h3>Название проекта</h3>
                            <p class="status" status="yellow">В работе</p>
                            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam nam corrupti vitae.</p>
                        </div>
                        <div class="projectCard">
                            <h3>Название проекта</h3>
                            <p class="status" status="grey">Завершен</p>
                            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam nam corrupti vitae.</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row g24">
                <button class="anotherButton">
                    <svg viewBox="0 0 320 512">
                        <path d="M206.7 464.6l-183.1-191.1C18.22 267.1 16 261.1 16 256s2.219-11.97 6.688-16.59l183.1-191.1c9.152-9.594 24.34-9.906 33.9-.7187c9.625 9.125 9.938 24.37 .7187 33.91L73.24 256l168 175.4c9.219 9.5 8.906 24.78-.7187 33.91C231 474.5 215.8 474.2 206.7 464.6z"/>
                    </svg>
                </button>
                <button class="standartButton">
                    <p>Лайк</p>
                </button>
                <button class="anotherButton">
                    <svg viewBox="0 0 320 512">
                        <path d="M113.3 47.41l183.1 191.1c4.469 4.625 6.688 10.62 6.688 16.59s-2.219 11.97-6.688 16.59l-183.1 191.1c-9.152 9.594-24.34 9.906-33.9 .7187c-9.625-9.125-9.938-24.38-.7187-33.91l168-175.4L78.71 80.6c-9.219-9.5-8.906-24.78 .7187-33.91C88.99 37.5 104.2 37.82 113.3 47.41z"/>
                    </svg>
                </button>
            </div>

        </div>
    </main>
</template>

<script>
    export default {
        name: "MainPage",
    }
</script>