<template>
    <div>
        <div>
            <button @click = "CreateRoom">
                Create room
            </button>
        </div>
        <!-- <div v-for = "room in rooms">
            <p>id:{{ room.id }}</p>
            <p @click = "$emit('open_dialog',room.id)">creator:{{ room.creator.username }}</p>
            <p>invited:</p>
                <ol>
                <li v-for = "user in room.invited">
                    {{ user.username }}
                </li>
            </ol>
        </div> -->

        <div class="sidebar h-100">
                    <form>
                        <div class="form-group">
                            <div class="input-group mb-3">
                                <span class="input-group-text" id="basic-addon1"><i class="fas fa-search"></i></span>
                                <input type="text" class="form-control" placeholder="Search user" aria-label="Search user" aria-describedby="basic-addon1">
                            </div>
                        </div>
                    </form>
                    <hr>
                    <ul class="users-list">
                        <li class="user-profile d-flex align-items-center" v-for = "room in rooms" @click = "$emit('open_dialog',room.id)">
                            
                            <div class="user-avatar me-3">
                                <img src="https://plhold.com/avatar/60?text=john+doe" alt="" />
                            </div>
                            <div class="d-flex flex-column">
                                <strong class="user-name">{{ room.id }}</strong>
                                <span class="status">
                                <i class="fas fa-circle text-success"></i>
                                Online
                            </span>
                            </div>
                        </li>
                    </ul>
                </div>
                
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            rooms:""
        }
    },
    methods:{
        LoadRooms(){
            console.log(1)
            // axios - функция для запросов к сайтам
            axios({
                url:"http://127.0.0.1:8000/chat/room/",
                method:"get",
                // responseType:'json',
            }).then(response => {
                console.log(response)
                this.rooms = response.data.data
            }).catch(error => {
                console.log(error)
            })
            },
            CreateRoom(){
            // axios - функция для запросов к сайтам
            axios({
                url:"http://127.0.0.1:8000/chat/room/",
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
        },
        // ФУНКЦИЯ КОТОРАЯ ВЫПОЛНЯЕТСЯ ПРИ ЗАГРУЗКЕ СТРАНИЦЫ
        created(){
            // в каждый запрос добавляем токен
            axios.defaults.headers['authorization'] = 'Token ' + sessionStorage.getItem('authtoken')
            this.LoadRooms()
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