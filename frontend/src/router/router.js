import SignIn from "@/pages/SignIn"
import ToDoList from "@/pages/ToDoList"
import Profile from "@/pages/Profile"
import Login from "@/components/Login"
import { createRouter, createWebHistory } from "vue-router"

const routes = [
    {
        path: "/",
        component: ToDoList,
    },
    {
        path: '/login',
        name:"login",
        component: Login
    },
    {
        path: "/sign_in",
        component: SignIn
    },
    {
        path: "/user/:id",
        component: Profile
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  })
  
  export default router
