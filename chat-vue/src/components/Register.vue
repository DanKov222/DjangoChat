<template>
    <div>
        <input v-model="login" placeholder="Логин" type="text"><br>
        <input v-model="password" placeholder="Пароль" type="password"><br>
        <button style="margin-top: 5px" @click="register">Зарегаться1</button>
        <br>
    </div>
</template>

<script>
    export default {
        name: "Register",
        data() {
            return {
                login: '',
                password: '',
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
                        password: this.password
                    },
                    success: (response) => {
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Ой! Кажется ваши пароль/имя неудовлетворяют требованиям безопасности!")
                        }
                        console.log(response)
                    }
                })
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/token/login/',
                    type: 'POST',
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Добро пожаловать")
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Что-то не так:( Свяжитесь с администрацией сайта и сообщите ей об данной ошибке")
                        }
                        console.log(response)
                        console.log(this.login)
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
