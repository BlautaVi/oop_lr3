<template>
  <form @submit.prevent="addTask" class="add-task-form">
    <input v-model="title" placeholder="Нове завдання" class="form-control" />
    <button type="submit" class="btn btn-success">Додати</button>
  </form>
</template>

<script>
import { collection, addDoc } from "firebase/firestore";
import { db } from "../firebase";

export default {
  data() {
    return { title: "" };
  },
  methods: {
    async addTask() {
      if (!this.title) return;
      try {
        await addDoc(collection(db, "tasks"), {
          title: this.title,
          done: false,
          created: new Date()
        });
        this.title = "";
        this.$emit("refresh");
      } catch (error) {
        console.error("Помилка додавання завдання:", error);
      }
    }
  }
};
</script>

<style scoped>
.add-task-form {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}
.form-control {
  flex-grow: 1;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.btn-success {
  background-color: #28a745;
  border-color: #28a745;
  color: white;
  padding: 5px 10px;
}
</style>