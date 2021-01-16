<template>
    <mu-col span="8" xl="9">
        <mu-container class="dialog">
            <mu-row v-for="dialog in dialogs" direction="column" justify-content="start"
                    align-items="end">
                <p><strong>{{ dialog.user.username }}</strong></p>
                <p>{{ dialog.text }}</p>
                <span>{{ dialog.date }}</span>
            </mu-row>
        </mu-container>
        <mu-container>
            <mu-row>
                <mu-text-field full-width multi-line :rows="4" v-model="form.textarea"
                               placeholder="Your message">
                </mu-text-field>
                <mu-button class="button" round color="teal">Send</mu-button>
            </mu-row>
        </mu-container>
    </mu-col>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Dialog",
        props: {
            id: '',
        },
        data() {
            return {
                dialogs: '',
                form: {
                    textarea: '',
                }
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadDialog()
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
</style>
