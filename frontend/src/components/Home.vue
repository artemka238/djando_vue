<template>
    <div>
        <div>
            <button v-if="!auth">
                LogIn
            </button>
            <button v-else>
                LogOut
            </button>
        </div>
        


        <div class="container">
    <div class="row">
        <div class="col-12 my-3">
            <h1>Bootstrap 5 chat app</h1>
            <hr>
            Support my work @ MMLTech | <a href="https://ko-fi.com/mmltech" target="_blank"><i class="fas fa-coffee"></i> Buy me a coffee</a> | <a href="https://streamcd.net">StreamCD</a> | <a href="https://obscountdown.com">OBSCountdown</a> | <a href="https://avatarplaceholder.com">AvatarPlaceholder</a>
            <hr>
        </div>
    </div>
    <div id="ChatBox">
        <div class="row">
            <div class="col-md-4">
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
                        <li class="user-profile d-flex align-items-center">
                            <div class="user-avatar me-3">
                                <img src="https://plhold.com/avatar/60?text=john+doe" alt="" />
                            </div>
                            <div class="d-flex flex-column">
                                <strong class="user-name">John Doe</strong>
                                <span class="status">
                                <i class="fas fa-circle text-success"></i>
                                Online
                            </span>
                            </div>
                        </li>
                        <li class="user-profile d-flex align-items-center active">
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
                        </li>
                        <li class="user-profile d-flex align-items-center">
                            <div class="user-avatar me-3">
                                <img src="https://plhold.com/avatar/60?text=Temuri+Naja+Rigby" alt="" />
                            </div>
                            <div class="d-flex flex-column">
                                <strong class="user-name">Temuri Naja Rigby</strong>
                                <span class="status">
                                <i class="fas fa-circle text-warning"></i>
                                Away
                            </span>
                            </div>
                        </li>
                        <li class="user-profile d-flex align-items-center">
                            <div class="user-avatar me-3">
                                <img src="https://plhold.com/avatar/60?text=Izem+Estela+McAfee" alt="" />
                            </div>
                            <div class="d-flex flex-column">
                                <strong class="user-name">Izem Estela McAfee</strong>
                                <span class="status">
                                <i class="fas fa-circle text-info"></i>
                                Do Not Disturb
                            </span>
                            </div>
                        </li>
                        <li class="user-profile d-flex align-items-center">
                            <div class="user-avatar me-3">
                                <img src="https://plhold.com/avatar/60?text=Luz+Ruža+Whittle" alt="" />
                            </div>
                            <div class="d-flex flex-column">
                                <strong class="user-name">Luz Ruža Whittle</strong>
                                <span class="status">
                                <i class="fas fa-circle text-success"></i>
                                Online
                            </span>
                            </div>
                        </li>
                        <li class="user-profile d-flex align-items-center">
                            <div class="user-avatar me-3">
                                <img src="https://plhold.com/avatar/60?text=Govinda+Coriander+Ármannsson" alt="" />
                            </div>
                            <div class="d-flex flex-column">
                                <strong class="user-name">Govinda Coriander Ármannsson</strong>
                                <span class="status">
                                <i class="fas fa-circle text-success"></i>
                                Online
                            </span>
                            </div>
                        </li>
                        <li class="user-profile d-flex align-items-center">
                            <div class="user-avatar me-3">
                                <img src="https://plhold.com/avatar/60?text=Shikha+Dionisia+Sarkissian" alt="" />
                            </div>
                            <div class="d-flex flex-column">
                                <strong class="user-name">Shikha Dionisia Sarkissian</strong>
                                <span class="status">
                                <i class="fas fa-circle text-success"></i>
                                Online
                            </span>
                            </div>
                        </li>
                    </ul>
                </div>
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
                    <div class="message-history py-3">
                        <div class="message-line d-flex flex-column">
                            <div class="d-flex justify-content-end mb-3">
                                <div class="user-avatar">
                                    <img src="https://plhold.com/avatar/60?text=Angelien+Austėja+Rakes" alt="" />
                                </div>
                            </div>
                            <p class="message ms-auto">
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                <small class="date d-flex justify-content-start mt-3">11 Nov 2022 13:00</small>
                            </p>
                        </div>
                        <div class="message-line reply d-flex flex-column">
                            <div class="d-flex align-items-end mb-3">
                                <div class="user-avatar">
                                    <img src="https://plhold.com/avatar/60?text=Shikha+Dionisia+Sarkissian" alt="" />
                                </div>
                            </div>
                            <p class="message">
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                <small class="date d-flex justify-content-end mt-3">11 Nov 2022 13:00</small>
                            </p>
                        </div>
                        <div class="message-line reply d-flex flex-column">
                            <div class="d-flex align-items-end mb-3">
                                <div class="user-avatar">
                                    <img src="https://plhold.com/avatar/60?text=Shikha+Dionisia+Sarkissian" alt="" />
                                </div>
                            </div>
                            <p class="message">
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                <small class="date d-flex justify-content-end mt-3">11 Nov 2022 13:00</small>
                            </p>
                        </div>
                    </div>
                    <div class="inputs mt-auto">
                        <div class="input-group mb-3">
                            <input type="text" class="form-control" placeholder="Your message" aria-label="Your message" aria-describedby="button-addon2">
                            <button class="btn btn-outline-secondary" type="button" id="button-addon2"><i class="fas fa-paper-plane"></i></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
    </div>
</template>

<script>
export default {
    
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