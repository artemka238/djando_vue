import { createApp } from 'vue'
import App from './App'
import axios from 'axios'
import router from "@/router/router"

const app = createApp(App)

//app.config.globalProperties.$http = axios
app.config.globalProperties.$http = axios 

app.use(router).mount("#app")
