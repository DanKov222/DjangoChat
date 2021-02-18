<template>
    <mu-col xl="12" class="room-list">
    <mu-container>
        <mu-text-field v-model="email" label="Email"
                       help-text=""></mu-text-field>
        <br/>
        <mu-text-field v-model="login" label="Логин"
                       help-text=""></mu-text-field>
        <br/>
        <mu-text-field v-model="password" label="Пароль" :type="visibility ? 'text' : 'password'">
        </mu-text-field><br/>
        <mu-button round @click="register" color="#38b1c1">Зарегистрироваться на сайте</mu-button>
    </mu-container>
    </mu-col>
</template>

<script>
    export default {
        name: "Register",
        data() {
            return {
                login: '',
                password: '',
                email: ''
            }
        },
        methods: {
            // пользователь сначала регистрируется(имя + пароль), а затем ему выдается токен
            register() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/users/',
                    type: 'POST',
                    data: {
                        username: this.login,
                        password: this.password,
                        email: this.email
                    },
                    success: (response) => {
                        this.getToken()
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Ой! Кажется ваши пароль/имя неудовлетворяют требованиям безопасности!")
                        }
                        console.log(response)
                    }
                })
            },
            getToken() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/token/login/',
                    type: 'POST',
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Отлично! Теперь выполните вход на сайт")
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Что-то не так:( Свяжитесь с администрацией сайта и сообщите ей об данной ошибке")
                        }
                        console.log(response)
                    }
                })
            }
        }
    }
</script>

<style scoped>
body {
    color: #38b1c1;
}
</style>
