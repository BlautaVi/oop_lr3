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
      <div class="day-card add-card" @click="addNewDay">
        <div class="plus-icon">+</div>
      </div>
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
  <AddTask @refresh="fetchTasks" />

</template>


<script>
import {auth, db} from "../firebase";
import { collection, getDocs, doc, deleteDoc, updateDoc, addDoc } from "firebase/firestore";
import { query, where } from "firebase/firestore";

import {onAuthStateChanged} from "firebase/auth";

export default {
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
      return {[this.selectedDay]: this.groupedTasks[this.selectedDay] || []};
    }
  },
  data() {
    return {
      tasks: [],
      selectedDay: '',
      days: {
        0: "Неділя",
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "П’ятниця",
        6: "Субота",
      }
    };
  },
  methods: {
    async fetchTasks() {
      const q = query(collection(db, "tasks"), where("userId", "==", auth.currentUser.uid));
      const querySnapshot = await getDocs(q);
      this.tasks = querySnapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    },
    async deleteTask(id) {
      await deleteDoc(doc(db, "tasks", id));
      await this.fetchTasks();
    },
    async toggleDone(task) {
      await updateDoc(doc(db, "tasks", task.id), {done: task.done});
    },
    async addNewDay() {
      const title = prompt("Введіть завдання:");
      if (!title) return;
      try {
        await addDoc(collection(db, "tasks"), {
          title,
          done: false,
          created: new Date(),
          userId: auth.currentUser.uid
        });
        await this.fetchTasks();
      } catch (error) {
        console.error("Помилка додавання:", error);
      }

    }
  },
  mounted() {
    onAuthStateChanged(auth, (user) => {
      if (user) this.fetchTasks();
    });
  },

};
</script>
