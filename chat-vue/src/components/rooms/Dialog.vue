<template>
    <mu-col span="8" xl="9">
        <mu-container class="dialog">
            <AddUsers :room="id"></AddUsers>
            <mu-row v-for="dialog in dialogs" direction="column" justify-content="start"
                    align-items="end">
                <p><strong>{{ dialog.user.username }}</strong></p>
                <p>{{ dialog.text }}</p>
                <span class="line">{{ dialog.date }}</span>
            </mu-row>
        </mu-container>
        <mu-container>
            <mu-row>
                <mu-text-field id="textInput" v-model="form.textarea"
                               full-width
                               multi-line
                               :rows="4"
                               placeholder="Your message">
                </mu-text-field>
                <mu-button round color="red" @click="update">Hide</mu-button>
                <mu-button class="button" round color="teal" @click="sendMessage">Send</mu-button>
            </mu-row>
        </mu-container>

    </mu-col>
</template>

<script>
    import AddUsers from "./AddUsers";

    export default {
        name: "Dialog",
        props: {
            id: '',
        },
        components: {
            AddUsers
        },
        data() {
            return {
                dialogs: '',
                seen: true,
                form: {
                    textarea: '',
                },
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadDialog()
            setInterval(() => {
                this.loadDialog()
            }, 2500);
        },
        methods: {
            loadDialog() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
                    type: "GET",
                    data: {
                        room: this.id
                    },
                    success: (response) => {
                        this.dialogs = response.data.data
                    }
                })
            },
            sendMessage() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/dialog/',
                    type: 'POST',
                    data: {
                        room: this.id,
                        text: this.form.textarea
                    },
                    success: (response) => {
                        this.loadDialog()
                        this.form.textarea = ''
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            },
            update() {
                window.location = '/'
            }
        }
    }
</script>

<style scoped>
    .dialog {
        border: 1px solid #300;
        margin-top: 20px;
    }

    .button {
        margin-left: auto;
        margin-right: 10px;
    }

    .line {
        box-shadow: 0px 1px 0px #000000;
    }
</style>
