<template>
 <h1>
  Tasks
 </h1>
 <div>
  <form @submit.prevent = "sub_form">
<div>
  <label for="title">
    Title
  </label>
  <input type="text" id = "title" v-model = "title">
</div>
<div>
  <label for="description">
    Description
  </label>
  <input type="text" id = "description" v-model = "description">
</div>
<button type="submit">
  Add
</button>
  </form>
 </div>
 <ul>
  <li v-for = "task in tasks" :key = "task.id">
    <h2>
      {{ task.title }}
    </h2>
    <p>
      {{ task.description }}
    </p>
    <button @click = "update_task(task)">
      {{ task.complited ? "вернуть":"выполнить" }}
    </button>
    <button @click = "delete_task(task)">
      Удалить
    </button>
  </li>
 </ul>
</template>

<script>
export default {
    data(){
        return {
            tasks:[],
            title:"",
            description:"",
        }
    },
    methods:{
      async sub_form()
      {
        try{
          const response = await this.$http.post(
            "http://127.0.0.1:8000/api/tasks",
            {title:this.title,
            description:this.description,
            complited:false}
          )
           this.getData();
        }
        catch(error){
          console.log(error)
        }
      },
      async getData()
      {
        try{
          const response = await this.$http.get(
            "http://127.0.0.1:8000/api/tasks"
          )
          this.tasks = response.data 
        }
        catch(error){
          console.log(error)
        }
      },
      async update_task(task)
      {
        try{
          const response = await this.$http.put(
            `http://127.0.0.1:8000/api/tasks/${task.id}/`,
            {title:task.title,
            description:task.description,
            complited:!task.complited}
          )
           this.getData();
        }
        catch(error){
          console.log(error)
        }
      },
      async delete_task(task)
      {
        try{
          const response = await this.$http.delete(
            `http://127.0.0.1:8000/api/tasks/${task.id}/`
          )
          this.getData()
        }
        catch(error){
          console.log(error)
        }
      },

  },
  created(){
    this.getData()

  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
