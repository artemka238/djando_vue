<template>
    <div class = "app">
        <nav class="navbar navbar-expand navbar-dark bg-dark" aria-label="Second navbar example">
            <div class="container-fluid">
            <a class="navbar-brand" href="#">Cat shop</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample02" aria-controls="navbarsExample02" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarsExample02">
                <ul class="navbar-nav me-auto">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#"><router-link to="/history" > История </router-link></a>
                </li>d
                <li class="nav-item">
                    <a class="nav-link" to="nav-item" href="#"><router-link to="/home" > Домашняя </router-link></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" to="nav-item" href="#"><router-link to="/cat" > Коты </router-link></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" to="nav-item" href="#"><router-link to="/profile" > Профиль </router-link></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" to="nav-item" href="#"><router-link to="/login" > Войти </router-link></a>
                </li>
                <!-- <li class="nav-item">
                    <p class="nav-link" href="#">{{ username }}</p>
                </li>
                <li class="nav-item">
                    <p class="nav-link" href="#">{{ balance }}</p>
                </li> -->
                </ul>
                <form role="search">
                <input class="form-control" type="search" placeholder="Search" aria-label="Search">
                </form>
            </div>
            </div>
        </nav>

        <!-- <nav id="navbar" >
            <router-link to="/history" > История </router-link>
            <router-link to="/home" > Домашняя </router-link>
            <router-link to="/cat" > Коты </router-link>
            <router-link to="/profile" > Профиль </router-link>
        </nav> -->
        <RouterView></RouterView>
    </div>
</template>

<!-- <script>
import axios from 'axios'
export default {
    name:"App",
    data(){
        return{
            cats:"",
            err:"",
            balance:"",
            username:""
        }
    },
    methods:{
        LoadRooms(){
            console.log(1)
            // axios - функция для запросов к сайтам
            axios({
                url:"http://127.0.0.1:8000/morecats/cat_history/",
                method:"get",
                // responseType:'json',
            }).then(response => {
              console.log(response)
                console.log(response.status)
                this.cats = response.data.data
            }).catch(error => {
                console.log(error.response)
                if (error.response.status === 403)
                {
                    this.err = "you have not permission, buy 10 cats or leave"
                }
            })
            },
            CreateRoom(){
            // axios - функция для запросов к сайтам
            axios({
                url:"http://127.0.0.1:8000/morecats/cats/",
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
            buycat(cat){
              console.log(cat)
              const dataform = new FormData
              dataform.append('id_cat',cat)
              axios({
                url:"http://127.0.0.1:8000/morecats/cats/buy/",
                method:"post",
                data:dataform
                
                
            
                // responseType:'json',
            }).then(response => {
              console.log(response)
                console.log(response.status)
            }).catch(error => {
                console.log(error.response)
                if (error.response.status === 403)
                {
                    this.err = "you have not permission, buy 10 cats or leave"
                }
            })
            },
            getinfo(){
              axios({
                url:"http://127.0.0.1:8000/morecats/info",
                method:"get",
                // responseType:'json',
            }).then(response => {
              console.log(response)
                console.log(response.status)
                this.username = response.data.user.username
                this.balance = response.data.balance
            }).catch(error => {
                console.log(error.response)
                if (error.response.status === 403)
                {
                    this.err = "you have not permission, buy 10 cats or leave"
                }
            })
            }
        },
        // ФУНКЦИЯ КОТОРАЯ ВЫПОЛНЯЕТСЯ ПРИ ЗАГРУЗКЕ СТРАНИЦЫ
        created(){
            // в каждый запрос добавляем токен
            axios.defaults.headers['authorization'] = 'Token ' + sessionStorage.getItem('authtoken')
            this.LoadRooms()
            this.getinfo()
        }

}
</script> -->

<style >
    #navbar{
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align:center;
        color:black;
    }
    nav{
        padding: 10px;
    }
    nav a{
        font-weight: bold;
    }
    nav a.router-link-exact-active {
        color: #42b983;
    }
</style>

