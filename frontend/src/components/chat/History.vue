<template lang="">
    <div>
        <main>

          <nav class="navbar navbar-expand navbar-dark bg-dark" aria-label="Second navbar example">
    <!-- <div class="container-fluid">
      <a class="navbar-brand" href="#">Always expand</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample02" aria-controls="navbarsExample02" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarsExample02">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <p class="nav-link" href="#">{{ username }}</p>
          </li>
          <li class="nav-item">
            <p class="nav-link" href="#">{{ balance }}</p>
          </li>
        </ul>
        <form role="search">
          <input class="form-control" type="search" placeholder="Search" aria-label="Search">
        </form>
      </div>
    </div> -->
  </nav>

<div class="album py-5 bg-body-tertiary">
  <div class="container">
    <h1>
        История
    </h1>

    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
      <div class="col" v-for = "cat in cats" :key = "cat.id">
        <div class="card shadow-sm">
            <img v-if = 'cat.cat.image1' :src="`http://127.0.0.1:8000${cat.image}`">
            <img v-else src="https://img.tourister.ru/files/2/4/3/4/1/8/4/4/original.jpg">
          <div class="card-body">
            <p> Продавец {{ cat.buyer.username }}</p>
            <p> Покупатель {{ cat.seller.username }}</p>
            <p> Дата {{ cat.date }}</p>
            <p> Кот {{ cat.cat.name }}</p>
            <p> Стоимость {{ cat.cost }}</p>
            <!-- <div class="d-flex justify-content-between align-items-center">
              <div class="btn-group">
                <button @click = "buycat(cat.id)">
                  Buy
                </button>
              </div>
              <small class="text-body-secondary">9 mins</small>
            </div> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

</main>
        <!-- <div v-for = "cat in cats">
            <p>{{ cat.name }}</p>
            <p>{{ cat.breed }}</p>
            <p>{{ cat.age }}</p>
            <p>{{ cat.cost }}</p>
            <img v-if = 'cat.image' :src = 'cat.image'>
        </div> -->
                <!-- {{ err }} -->
    </div>
</template>

<script>
import axios from 'axios'
export default {
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
</script>

<style lang="">
    
</style>