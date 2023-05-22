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
                method:"POST",
                responseType:'json',
                data:{
                    username: this.login,
                    password: this.password
                }
            }).then(function(response){
                console.log(response)
            }).catch(function(error){
                console.log(error)
            })
        }
    }
}
</script>

<style lang="">
    
</style>