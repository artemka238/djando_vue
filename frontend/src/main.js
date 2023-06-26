import { createApp } from 'vue'
import App from './App'
import axios from 'axios'
import router from "@/router/router"

// подключение bootstrap
import "bootstrap/dist/css/bootstrap.css"
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.js'

const app = createApp(App)

//app.config.globalProperties.$http = axios
app.config.globalProperties.$http = axios 

app.use(router).use(bootstrap).mount("#app")
