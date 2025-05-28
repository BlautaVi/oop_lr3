<template>
  <div>
    <h1>Трекер домашніх завдань</h1>
    <AddTask @refresh="refreshTasks" />
    <TaskList ref="taskList" />
  </div>
</template>

<script>
import AddTask from "../components/AddTask.vue";
import TaskList from "../components/TaskList.vue";

export default {
  components: { AddTask, TaskList },
  methods: {
    refreshTasks() {
      this.$refs.taskList.fetchTasks();
    }
  }
};
</script>
