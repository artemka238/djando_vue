<template>
    <div>
        <div>
            <select v-model="option">
                <option v-for="user in users" :value = "user.id">
                    {{ user.username }}
                </option>
            </select>
            <button @click = "add_user">
                Добавить пользователя
            </button>
        </div>
    </div>
</template>

<script>
import axios from "axios"
export default {
    data(){
        return{
            users:"",
            option:""
        }
    },
    methods:{
        LoadUser(){
            // axios - функция для запросов к сайтам
            axios({
                url:"http://127.0.0.1:8000/chat/users/",
                method:"get",
                // params:{
                //     room:1,
                // }
                // responseType:'json',
            }).then(response => {
                console.log(response)
                this.users = response.data.data
            }).catch(error => {
                console.log(error)
            })
            },
            add_user(){
            // axios - функция для запросов к сайтам
            axios({
            url:"http://127.0.0.1:8000/chat/users/",
            method:"post",
            data:{
                room:1,
                user:parseInt(this.option)
            }
          }).then(response=>{
            alert("пользователь добавлен")
          }).catch(error=>{
            console.log(error.statusText)
          })
            },
            
        },
        created(){
            axios.defaults.headers['authorization'] = 'Token ' + sessionStorage.getItem('authtoken')
            this.LoadUser()
        }
}
</script>

<style>
    
</style>