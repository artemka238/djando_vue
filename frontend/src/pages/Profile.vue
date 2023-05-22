<template>
    <div>
        <h1>
            Профиль пользователя
        </h1>
        <h2>
            {{  }}
        </h2>
    </div>
</template>

<script>
import axios from "axios"
export default {
    data(){
        {
            user: {}
        }
    },
    methods: {
        async fetchUser(id){
            const token = await this.getToken()
            axios.defaults.headers.common["Authorization"] = "Bearer" + token
            const response = await axios.get(`http://127.0.0.1:8000/auth/user/${id}/`)
            this.user = response.data
        },
        async getToken(){
            access = localStorage.getItem("access")
            return access
        }
    },
    created() {
        // this.fetchUser(this.$route.params.id)
        this.fetchUser(this.$route.params.id)
    },
}
</script>

<style scoped>
    
</style>