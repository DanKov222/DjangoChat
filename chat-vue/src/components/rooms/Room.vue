<template>
    <HomeSlot>
        <mu-col span="4" xl="2" class="room-list">
            <mu-button @click="addRoom">Create Room</mu-button>
            <div v-for="room in rooms">
                <h3 @click="openDialog(room.id)" @dblclick="openDialog(room.id)">{{ room.creator.username}}</h3>
                <small>{{ room.date }}</small>
            </div>
        </mu-col>
    </HomeSlot>
</template>

<script>
    import HomeSlot from '../Home'

    export default {
        name: "Room",
        data() {
            return {
                rooms: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadRoom()
        },
        methods: {
            loadRoom() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: "GET",
                    success: (response) => {
                        this.rooms = response.data.data
                    }
                })
            },
            openDialog(id) {
                this.visible = false
                this.$emit('openDialog', id)
            },
            addRoom() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: 'POST',
                    success: (response) => {
                        this.loadRoom()
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            }
        }
    }
</script>

<style scoped>
    h3 {
        cursor: pointer;
    }

    .room-list {
        box-shadow: 1px 4px 5px #999999;
        margin-right: 10px;
        margin-top: 20px;
    }
</style>
