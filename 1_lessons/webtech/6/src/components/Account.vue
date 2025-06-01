<template>
  <div>
    <h2>Ваш акаунт</h2>
    <p>{{ user?.email }}</p>
    <button @click="logout">Вийти</button>
  </div>
</template>

<script>
import { auth } from "../firebase";
import { signOut } from "firebase/auth";

export default {
  data() {
    return { user: auth.currentUser };
  },
  methods: {
    async logout() {
      await signOut(auth);
      this.$router.push("/auth");
    }
  }
};
</script>
