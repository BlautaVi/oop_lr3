<template>
  <div>
    <div class="filter-container">
      <label>Фільтрувати по дню:</label>
      <select v-model="selectedDay">
        <option value="">Усі дні</option>
        <option v-for="(dayName, key) in days" :key="key" :value="key">{{ dayName }}</option>
      </select>
    </div>

    <div class="card-grid">
      <div
          v-for="(group, day) in filteredGroups"
          :key="day"
          class="day-card card"
      >
        <div class="card-header">
          {{ days[day] }} ({{ group.length }})
        </div>
        <ul class="card-body">
          <li v-for="task in group" :key="task.id" class="task-row">
            <input type="checkbox" v-model="task.done" @change="toggleDone(task)" />
            <span :class="{ done: task.done }">{{ task.title }}</span>
            <button @click="deleteTask(task.id)" class="delete-btn">-</button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { db } from "../firebase";
import { collection, getDocs, doc, deleteDoc, updateDoc } from "firebase/firestore";

export default {
  data() {
    return {
      tasks: [],
      selectedDay: '',
      days: {
        0: "Понеділок",
        1: "Вівторок",
        2: "Середа",
        3: "Четвер",
        4: "П’ятниця",
      }
    };
  },
  computed: {
    groupedTasks() {
      const groups = {};
      this.tasks.forEach(task => {
        const date = task.created?.toDate ? task.created.toDate() : new Date(task.created);
        const day = date.getDay();
        if (!groups[day]) groups[day] = [];
        groups[day].push(task);
      });
      return groups;
    },
    filteredGroups() {
      if (!this.selectedDay) return this.groupedTasks;
      return { [this.selectedDay]: this.groupedTasks[this.selectedDay] || [] };
    }
  },
  methods: {
    async fetchTasks() {
      try {
        const querySnapshot = await getDocs(collection(db, "tasks"));
        this.tasks = querySnapshot.docs.map(doc => ({
          id: doc.id,
          ...doc.data()
        }));
      } catch (error) {
        console.error("Помилка завантаження завдань:", error);
      }
    },
    async deleteTask(id) {
      await deleteDoc(doc(db, "tasks", id));
      this.fetchTasks();
    },
    async toggleDone(task) {
      await updateDoc(doc(db, "tasks", task.id), { done: task.done });
    }
  },
  mounted() {
    this.fetchTasks();
  }
};
</script>
