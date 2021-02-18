<template>
    <mu-col xl="12" class="room-list">
    <mu-container>
        <mu-text-field v-model="login" label="Логин"
                       help-text=""></mu-text-field>
        <br/>
        <mu-text-field v-model="password" label="Пароль" :type="visibility ? 'text' : 'password'">
        </mu-text-field><br/>
        <mu-button round @click="setLogin" color="#af5fc4">Войти</mu-button>
    </mu-container>
    </mu-col>
</template>

<script>

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
                        if (response.status === 400) {
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
