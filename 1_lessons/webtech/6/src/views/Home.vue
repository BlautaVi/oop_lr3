<template>
  <div>
    <div v-if="isAuthenticated" class="jumbotron">
      <h1>Вітаємо, {{ userEmail }}!</h1>
    </div>
    <Auth v-if="!isAuthenticated" @close="showAuth = false" />
    <TaskList v-if="isAuthenticated" />
  </div>
</template>

<script>
import Auth from "@/components/Auth.vue";
import TaskList from "@/components/TaskList.vue";
import { auth } from "../firebase";
import { onAuthStateChanged } from "firebase/auth";

export default {
  components: { Auth, TaskList },
  data() {
    return {
      showAuth: true,
      isAuthenticated: false,
      userEmail: null
    };
  },
  mounted() {
    onAuthStateChanged(auth, (user) => {
      if (user) {
        this.isAuthenticated = true;
        this.userEmail = user.email;
        this.showAuth = false;
      } else {
        this.isAuthenticated = false;
        this.userEmail = null;
        this.showAuth = true;
      }
    });
  }
};
</script>
