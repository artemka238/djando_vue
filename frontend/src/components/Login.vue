<template>
    <div>
        <input type="text" v-model = "login" placeholder = "введите логин">
        <input type="text" v-model = "password" placeholder = "введите пароль">
        <button @click = "setLogin">Войти</button>
    </div>
</template>

<script>
import axios from 'axios';
export default{
    name:'Login',
    data(){
        return{
            login:"",
            password:""
        }
    },
    methods:{
        setLogin(){
            console.log(1)
            axios({
                url:"http://127.0.0.1:8000/auth/token/",
                method:"post",
                // responseType:'json',
                data:{
                    username: this.login,
                    password: this.password
                }
            }).then(response => {
                console.log(response)
            })
            }
        }
    }
</script>

<style lang="">
    
</style>