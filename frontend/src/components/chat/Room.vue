<template>
    <div>
        <div>
            <button @click = "CreateRoom">
                Create room
            </button>
        </div>
        <div v-for = "room in rooms">
            <p>id:{{ room.id }}</p>
            <p>creator:{{ room.creator.username }}</p>
            <p>invited:</p>
                <ol>
                <li v-for = "user in room.invited">
                    {{ user.username }}
                </li>
            </ol>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            rooms:""
        }
    },
    methods:{
        LoadRooms(){
            console.log(1)
            // axios - функция для запросов к сайтам
            axios({
                url:"http://127.0.0.1:8000/chat/room/",
                method:"get",
                // responseType:'json',
            }).then(response => {
                console.log(response)
                this.rooms = response.data.data.data
            }).catch(error => {
                console.log(error)
            })
            },
            CreateRoom(){
            // axios - функция для запросов к сайтам
            axios({
                url:"http://127.0.0.1:8000/chat/room/",
                method:"post",
                // responseType:'json',
            }).then(response => {
                console.log(response)
                // this.rooms = response.data.data.data
                this.LoadRooms()
            }).catch(error => {
                console.log(error)
            })
            },
        },
        // ФУНКЦИЯ КОТОРАЯ ВЫПОЛНЯЕТСЯ ПРИ ЗАГРУЗКЕ СТРАНИЦЫ
        created(){
            // в каждый запрос добавляем токен
            axios.defaults.headers['authorization'] = 'Token ' + sessionStorage.getItem('authtoken')
            this.LoadRooms()
        }
}
</script>

<style>
    
</style>