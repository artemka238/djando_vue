import SignIn from "@/pages/SignIn"
import ToDoList from "@/pages/ToDoList"
import Profile from "@/pages/Profile"
import Login from "@/components/Login"
import Room from "@/components/chat/Room"
import Dialog from "@/components/chat/Dialog"
import AddUser from "@/components/chat/AddUser"
import Home from "@/components/Home"
import Main from "@/components/mainHome"
import About from "@/components/about"
import Contact from "@/components/contact"
import { createRouter, createWebHistory } from "vue-router"
import AboutCats from "@/components/chat/cats"

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
    },
    {
        path: '/room',
        name:"room",
        component: Room
    },
    {
        path: '/dialog',
        name:"dialog",
        component: Dialog
    },
    {
        path: '/add',
        name:"add",
        component: AddUser
    },
    {
        path: '/home',
        name:"home",
        component: Home
    },
    {
        path:"/main",
        name:"main",
        component: Main
    },
    {
        path:"/about",
        name:"about",
        component: About
    },
    {
        path:"/contact",
        name:"contact",
        component:Contact
    },
    {
        path:"/cat",
        name:"cat",
        component:AboutCats
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  })
  
  export default router
