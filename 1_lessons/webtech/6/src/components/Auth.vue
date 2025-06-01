<template>
  <div class="auth-fullscreen">
    <div class="auth-card">
      <h2>{{ isLogin ? 'Увійти' : 'Реєстрація' }}</h2>
      <input v-model="email" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Пароль" />
      <button @click="handleAuth">{{ isLogin ? 'Увійти' : 'Зареєструватися' }}</button>
      <p @click="isLogin = !isLogin" class="switch-mode">
        {{ isLogin ? 'Немає акаунту? Зареєструйтесь' : 'Вже є акаунт? Увійдіть' }}
      </p>
    </div>
  </div>
</template>

<script>
import { auth } from "@/firebase";
import { signInWithEmailAndPassword, createUserWithEmailAndPassword } from "firebase/auth";

export default {
  data() {
    return {
      email: "",
      password: "",
      isLogin: true,
    };
  },
  methods: {
    async handleAuth() {
      try {
        if (this.isLogin) {
          await signInWithEmailAndPassword(auth, this.email, this.password);
        } else {
          await createUserWithEmailAndPassword(auth, this.email, this.password);
        }
      } catch (err) {
        alert("Помилка: " + err.message);
      }
    },
  },
};
</script>
