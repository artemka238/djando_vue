<template lang="">
    <div>
        <h2>
            Форма регистрации
        </h2>
        <form>
            <div>
                <label for="username">
                    введите имя пользователя
                </label>
                <input type="text" id = "username" v-model = "user.username" required>
            </div>
            <div>
                <label for="password">
                    введите пароль
                </label>
                <input type="text" id = "password" v-model = "user.password" required>
            </div>
            <div>
                <label for="password2">
                    подтвердите пароль
                </label>
                <input type="text" id = "password2" v-model = "user.password2" required>
            </div>
            <div>
                <button type = "submit" @click.prevent = "registration">
                    Зарегистрироваться
                </button>
            </div>
        </form>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    data(){
        return {
            user:{
                username:"",
                password:"",
                password2:""
            }
        }
    },
    methods:{
        registration(){
            if (this.user.password !== this.user.password2)
            {
                alert("пароли не совпадают")
                return
            }
            const payload = {
                username:this.user.username,
                password:this.user.password
            }
            axios.post("http://127.0.0.1:8000/auth/users/", payload).then((response)=>{
                // this.$store.commit("updateToken", response.data.token)
                console.log(response.data)
                localStorage.setItem("access",response.data.token.access)
                localStorage.setItem("refresh",response.data.token.refresh)
            }
            )
        }
    }
}
</script>
<style lang="">
    
</style>