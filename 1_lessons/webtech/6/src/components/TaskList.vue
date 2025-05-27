<template>
  <div>
    <div v-if="tasks.length === 0" class="alert alert-info">Немає завдань.</div>
    <div v-for="task in tasks" :key="task.id" class="task-item">
      <input type="checkbox" v-model="task.done" @change="toggleDone(task)" />
      <span :style="{ textDecoration: task.done ? 'line-through' : 'none' }">{{ task.title }}</span>
      <button @click="deleteTask(task.id)" class="btn btn-danger btn-sm">🗑️</button>
    </div>
  </div>
</template>

<script>
import { db } from "../firebase";
import { collection, getDocs, doc, deleteDoc, updateDoc } from "firebase/firestore";

export default {
  data() {
    return { tasks: [] };
  },
  methods: {
    async fetchTasks() {
      try {
        const querySnapshot = await getDocs(collection(db, "tasks"));
        this.tasks = querySnapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
      } catch (error) {
        console.error("Помилка завантаження завдань:", error);
      }
    },
    async deleteTask(id) {
      try {
        await deleteDoc(doc(db, "tasks", id));
        this.fetchTasks();
      } catch (error) {
        console.error("Помилка видалення завдання:", error);
      }
    },
    async toggleDone(task) {
      try {
        await updateDoc(doc(db, "tasks", task.id), { done: task.done });
      } catch (error) {
        console.error("Помилка оновлення завдання:", error);
      }
    }
  },
  mounted() {
    this.fetchTasks();
  }
};
</script>

<style scoped>
.task-item {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}
.btn-danger {
  background-color: #dc3545;
  border-color: #dc3545;
  color: white;
}
.btn-sm {
  padding: 2px 6px;
  font-size: 0.875rem;
}
</style>