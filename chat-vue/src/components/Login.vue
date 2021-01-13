<template>
    <div>
        <input v-model="login" placeholder="Логин" type="text">
        <input v-model="password" placeholder="Пароль" type="password">
        <button @click="setLogin">Войти</button><br>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/token/login',
                    type: 'POST',
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Спасибо что Вы с нами")
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400){
                            alert("Логин или пароль не верны")
                        }
                        console.log(response)
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
