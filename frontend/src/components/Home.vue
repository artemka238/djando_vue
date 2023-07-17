<template>
    <div>
        <div class="container">
    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
      <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none">
        <svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"></use></svg>
        <span class="fs-4">Simple header</span>
      </a>

      <ul class="nav nav-pills">
        <li class="nav-item"><a href="#" class="nav-link active" aria-current="page">Home</a></li>
        <li class="nav-item"><a href="#" class="nav-link">Features</a></li>
        <li class="nav-item"><a href="#" class="nav-link">Pricing</a></li>
        <li class="nav-item"><a href="#" class="nav-link">FAQs</a></li>
        <li class="nav-item"><a href="#" class="nav-link">About</a></li>
      </ul>
    </header>
  </div>
        <div>
            <button v-if="!auth" @click="LogIn">
                LogIn
            </button>
            <button v-else @click="LogOut">
                LogOut
            </button>
        </div>

        <div class="container">
    <div class="row">
        <div class="col-12 my-3">
            <h1>Messages</h1>
            <hr>
            <hr>
        </div>
    </div>
    <div id="ChatBox">
        <div class="row">
            <div class="col-md-4">
                <Room @open_dialog="open_dialog"></Room>
            </div>
            
            <div class="col-md-8">
                <div class="chat-frame d-flex flex-column justify-content-between">
                    <div class="action-frame d-flex align-items-center">
                        <div class="user-avatar me-3">
                            <img src="https://plhold.com/avatar/60?text=Angelien+Austėja+Rakes" alt="" />
                        </div>
                        <div class="d-flex flex-column">
                            <strong class="user-name">Angelien Austėja Rakes</strong>
                            <span class="status">
                                <i class="fas fa-circle text-danger"></i>
                                Last seen 1 day ago
                            </span>
                        </div>
                        <div class="action-buttons d-flex ms-auto">
                            <button class="btn btn-outline-secondary me-2"><i class="fas fa-camera"></i></button>
                            <button class="btn btn-outline-info me-2"><i class="fas fa-image"></i></button>
                            <button class="btn btn-outline-primary me-2"><i class="fas fa-cogs"></i></button>
                            <div class="dropstart">
                                <button class="btn btn-outline-success dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                                    <i class="fas fa-ellipsis-v"></i>
                                </button>
                                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                                    <li><a class="dropdown-item" href="#">Block</a></li>
                                    <li><a class="dropdown-item" href="#">Ignore</a></li>
                                    <li><a class="dropdown-item" href="#">Remove friend</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
                </div>
            </div>
        </div>
    </div>
</div>
    </div>
</template>

<script>
import Room from './chat/Room.vue';
import Dialog from './chat/Dialog.vue';

export default {
    components:{
        Room,
        Dialog,
    },
    data(){
        return{
            dialog:{
                id:"",
                show:false
            }
        }
    },
    methods:{
        open_dialog(id){
            this.dialog.id = id
            this.dialog.show = true
            console.log(id)
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
            LogOut(){
              sessionStorage.removeItem("authtoken")
              window.location = "login/"
            },
            LogIn(){
              this.$router.push({name:"login"})
            }
        },
    computed:{
        auth(){
          if(sessionStorage.getItem("authtoken")){
            return true
          }
        }
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