<template>
    <div>
        <select v-model="option">
            <option v-for="user in list" :value="user.id">
                {{ user.attributes.username }}
            </option>
        </select>
        <mu-button class="btn-send" round color="teal" @click="addUser">Add user</mu-button>
    </div>
</template>

<script>
    export default {
        name: "AddUsers",
        props: {
            room: ''
        },
        data() {
            return {
                option: '',
                list: '',
            }
        },
        created() {
            this.loadUsers();
        },
        methods: {
            loadUsers() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/users/",
                    type: 'GET',
                    success: (response) => {
                        this.list = response.data
                    }
                })
            },
            addUser() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/users/",
                    type: 'POST',
                    data: {
                        room: this.room,
                        user: parseInt(this.option)
                    },
                    success: (response) => {
                        alert('User added')
                    },
                    error: (response) => {
                        alert('Error')
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
