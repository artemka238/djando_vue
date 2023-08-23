<template lang="">
    <div>
        <main>

<section class="py-5 text-center container">
  <div class="row py-lg-5">
    <div class="col-lg-6 col-md-8 mx-auto">
      <h1 class="fw-light">Album example</h1>
      <p class="lead text-body-secondary">Something short and leading about the collection below—its contents, the creator, etc. Make it short and sweet, but not too short so folks don’t simply skip over it entirely.</p>
      <p>
        <a href="#" class="btn btn-primary my-2">Main call to action</a>
        <a href="#" class="btn btn-secondary my-2">Secondary action</a>
      </p>
    </div>
  </div>
</section>

<div class="album py-5 bg-body-tertiary">
  <div class="container">

    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
      <div class="col" v-for = "cat in cats" :key = "cat.id">
        <div class="card shadow-sm">
            <img v-if = 'cat.image' :src = 'cat.image_url'>
          <div class="card-body">
            <p>{{ cat.name }}</p>
            <p>{{ cat.breed }}</p>
            <p>{{ cat.age }}</p>
            <p>{{ cat.cost }}</p>
            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            <div class="d-flex justify-content-between align-items-center">
              <div class="btn-group">
                <button @click = "buycat(cat)">
                  Buy
                </button>
              </div>
              <small class="text-body-secondary">9 mins</small>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

</main>
        <div v-for = "cat in cats">
            <p>{{ cat.name }}</p>
            <p>{{ cat.breed }}</p>
            <p>{{ cat.age }}</p>
            <p>{{ cat.cost }}</p>
            <img v-if = 'cat.image' :src = 'cat.image_url'>
        </div>
                {{ err }}
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
            userrname:""
        }
    },
    methods:{
        LoadRooms(){
            console.log(1)
            // axios - функция для запросов к сайтам
            axios({
                url:"http://127.0.0.1:8000/morecats/cats/",
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
              axios({
                url:"http://127.0.0.1:8000/morecats/cats/buy",
                method:"post",
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
            getinfo(){
              axios({
                url:"http://127.0.0.1:8000/morecats/info",
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