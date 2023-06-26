<template>
    <div>
        <div class="col-md-8">
                <div class="chat-frame d-flex flex-column justify-content-between">
                    
                    <div class="message-history py-3" v-for = "dialog in dialogs">
                        <div class="message-line d-flex flex-column">
                            <div class="d-flex justify-content-end mb-3">
                                <div class="user-avatar">
                                    <span>{{ dialog.user.username }}</span>
                                    <img src="https://plhold.com/avatar/60?text=Angelien+Austėja+Rakes" alt="" />
                                </div>
                            </div>
                            <p class="message ms-auto">
                                {{ dialog.text }}
                                <small class="date d-flex justify-content-start mt-3">{{ dialog.date }}</small>
                            </p>
                        </div>
                    </div>
                    <div class="inputs mt-auto">
                        <div class="input-group mb-3">
                            <input type="text" class="form-control" placeholder="Your message" aria-label="Your message" aria-describedby="button-addon2" v-model = "form.text">
                            <button class="btn btn-outline-secondary" type="button" id="button-addon2"><i class="fas fa-paper-plane" @click = "send_message"></i></button>
                        </div>
                    </div>
                </div>
            </div>
        <!-- <div v-for = "dialog in dialogs">
            <p>
                {{ dialog.user.username }}
            </p>
            <p>
                {{ dialog.text }}
            </p>
            <p>
                {{ dialog.date }}
            </p>
        </div>
        <div>
            <input type = "text" placeholder="введите сообщение" v-model = "form.text">
            <button @click = "send_message">
                Отправить
            </button>
        </div> -->
    </div>
</template>

<script>
import axios from "axios"
export default {
    data(){
        return{
            dialogs:"",
            form:{
                text:""
            },
        }
    },
    methods:{
        LoadDialog(){
            // axios - функция для запросов к сайтам
            axios({
                url:"http://127.0.0.1:8000/chat/dialog/",
                method:"get",
                params:{
                    room:1,
                }
                // responseType:'json',
            }).then(response => {
                console.log(response)
                this.dialogs = response.data.data
            }).catch(error => {
                console.log(error)
            })
            },
            send_message(){
            // axios - функция для запросов к сайтам
            console.log(this.form.text)
            axios({
            url:"http://127.0.0.1:8000/chat/dialog/",
            method:"post",
            data:{
                room:1,
                text:this.form.text
            }
          }).then(response=>{
            this.LoadDialog()
            this.form.text=""
          }).catch(error=>{
            console.log(error.statusText)
          })
            },
            
        },
        created(){
            axios.defaults.headers['authorization'] = 'Token ' + sessionStorage.getItem('authtoken')
            this.LoadDialog()
        }
}
</script>

<style>
    
</style>