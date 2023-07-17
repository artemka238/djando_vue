<template>
    <div>
        <div class = "container">
            <AddUser :room = "id"></AddUser>
        </div>      
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
import AddUser from "./AddUser.vue"
import axios from "axios"
export default {
    // переменные из других компонентов называются props
    props:{
        id:""
    },
    data(){
        return{
            dialogs:"",
            form:{
                text:""
            },
        }
    },
    components:{
        AddUser
    },
    methods:{
        LoadDialog(){
            // axios - функция для запросов к сайтам
            axios({
                url:"http://127.0.0.1:8000/chat/dialog/",
                method:"get",
                params:{
                    room:this.id,
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
                room:this.id,
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

<style scoped>
        #ChatBox {
  background: #fff;
  border-radius: 0.55rem;
  border: 1px solid #ced4da;
}
#ChatBox * {
  /* width */
  /* Track */
  /* Handle */
  /* Handle on hover */
}
#ChatBox *::-webkit-scrollbar {
  width: 5px;
}
#ChatBox *::-webkit-scrollbar-track {
  background: transparent;
}
#ChatBox *::-webkit-scrollbar-thumb {
  -webkit-transition: 0.3s all;
  -moz-transition: 0.3s all;
  -ms-transition: 0.3s all;
  -o-transition: 0.3s all;
  transition: 0.3s all;
  background-color: #cccccc;
  border-radius: 0.25rem;
}
#ChatBox *::-webkit-scrollbar-thumb:hover {
  background-color: #555;
}
#ChatBox .user-avatar {
  border-radius: 9999999px;
  border: 5px solid #00000015;
  overflow: hidden;
}
#ChatBox .sidebar {
  border-right: 1px solid #ced4da;
  padding: 1rem;
}
#ChatBox .sidebar .users-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
  max-height: 100%;
  overflow-x: hidden;
  overflow-y: scroll;
}
#ChatBox .sidebar .users-list li {
  cursor: pointer;
  padding: 0.25rem;
  -webkit-transition: 0.3s all;
  -moz-transition: 0.3s all;
  -ms-transition: 0.3s all;
  -o-transition: 0.3s all;
  transition: 0.3s all;
  margin-bottom: 0.25rem;
}
#ChatBox .sidebar .users-list li.active, #ChatBox .sidebar .users-list li:hover {
  background: #efefef;
  border-radius: 0.25rem;
}
#ChatBox .sidebar .users-list li .user-name {
  font-size: 1rem;
}
#ChatBox .sidebar .users-list li .status {
  text-transform: uppercase;
  font-weight: bold;
  font-size: 9px;
  color: #adb5bd;
}
#ChatBox .chat-frame {
  padding: 1rem;
}
#ChatBox .chat-frame .action-frame {
  padding-bottom: 1rem;
  border-bottom: 1px solid #ced4da;
}
#ChatBox .chat-frame .message-history {
  max-height: 500px;
  overflow-x: hidden;
  overflow-y: scroll;
}
#ChatBox .chat-frame .message-history .message-line {
  padding: 1rem;
}
#ChatBox .chat-frame .message-history .message-line .user-avatar {
  width: fit-content;
}
#ChatBox .chat-frame .message-history .message-line.reply .message:before {
  left: 20px;
  right: initial;
}
#ChatBox .chat-frame .message-history .message-line .message {
  background: #efefef;
  border-radius: 0.55rem;
  font-size: 14px;
  color: #2d2d2d;
  padding: 1rem;
  width: fit-content;
  position: relative;
}
#ChatBox .chat-frame .message-history .message-line .message:before {
  content: "";
  display: block;
  position: absolute;
  top: -25px;
  right: 20px;
  border-top: 15px solid transparent;
  border-right: 15px solid transparent;
  border-bottom: 15px solid #efefef;
  border-left: 15px solid transparent;
}
#ChatBox .chat-frame .inputs {
  padding-top: 1rem;
  border-top: 1px solid #ced4da;
}
</style>