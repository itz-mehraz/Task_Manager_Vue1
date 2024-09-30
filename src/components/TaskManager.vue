<template>
  <div class="task-manager">
    <h1>Task Manager</h1>

    <!-- Search Bar -->
    <input
      type="text"
      v-model="searchTerm"
      placeholder="Search tasks..."
      class="search-input"
    />

    <!-- Task Input Section -->
    <div class="input-container">
      <input
        type="text"
        v-model="newTask"
        @keyup.enter="addTask"
        placeholder="Add a new task"
        class="task-input"
      />
      <input type="date" v-model="newTaskDate" class="date-input" />
      <select v-model="newTaskCategory" class="category-selector">
        <option value="Work">Work</option>
        <option value="Personal">Personal</option>
        <option value="Shopping">Shopping</option>
        <option value="Others">Others</option>
      </select>
      <button @click="addTask" class="add-btn">Add Task</button>
    </div>

    <!-- Task List -->
    <ul class="task-list">
      <TaskItem
        v-for="(task, index) in filteredTasks"
        :key="index"
        :task="task"
        @toggle="toggleTaskCompletion(task)"
        @remove="removeTask(index)"
        @edit="editTask(task, index)"
      />
    </ul>

    <p v-if="filteredTasks.length === 0" class="empty">No tasks available.</p>

    <!-- Task Summary and Actions -->
    <div class="task-summary">
      <p><strong>Total Tasks:</strong> {{ tasks.length }}</p>
      <p><strong>Completed Tasks:</strong> {{ completedTasks.length }}</p>
      <p><strong>Pending Tasks:</strong> {{ incompleteTasks.length }}</p>
    </div>
    <button class="clear-btn" @click="clearCompleted">
      Clear Completed Tasks
    </button>
  </div>
</template>

<script>
import TaskItem from "./TaskItem.vue";

export default {
  components: {
    TaskItem,
  },
  data() {
    return {
      newTask: "",
      newTaskDate: "",
      newTaskCategory: "Work",
      searchTerm: "",
      tasks: [
        {
          name: "Learn Vue.js",
          completed: false,
          dueDate: "2023-09-30",
          category: "Work",
        },
        {
          name: "Buy groceries",
          completed: false,
          dueDate: "2023-10-01",
          category: "Shopping",
        },
      ],
    };
  },
  computed: {
    completedTasks() {
      return this.tasks.filter((task) => task.completed);
    },
    incompleteTasks() {
      return this.tasks.filter((task) => !task.completed);
    },
    filteredTasks() {
      const searchTerm = this.searchTerm.toLowerCase();
      return this.tasks.filter((task) =>
        task.name.toLowerCase().includes(searchTerm)
      );
    },
  },
  methods: {
    addTask() {
      const taskName = this.newTask.trim();
      if (taskName && this.newTaskDate) {
        this.tasks.push({
          name: taskName,
          completed: false,
          dueDate: this.newTaskDate,
          category: this.newTaskCategory,
        });
        this.newTask = "";
        this.newTaskDate = "";
      } else {
        alert("Please enter both task and due date!");
      }
    },
    removeTask(index) {
      this.tasks.splice(index, 1);
    },
    toggleTaskCompletion(task) {
      task.completed = !task.completed;
    },
    clearCompleted() {
      this.tasks = this.tasks.filter((task) => !task.completed);
    },
    editTask(task, index) {
      const newName = prompt("Edit task name:", task.name);
      if (newName) {
        this.tasks[index].name = newName;
      }
    },
  },
};
</script>

<style scoped>
.task-manager {
  max-width: 800px;
  margin: 0 auto;
  background: #fff;
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #333;
  font-size: 2.4rem;
  margin-bottom: 20px;
}

/* Search Input */
.search-input {
  width: 100%;
  padding: 12px;
  margin-bottom: 20px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-size: 16px;
}

/* Input Section */
.input-container {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.task-input {
  flex: 2;
  padding: 12px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-size: 16px;
}

.date-input {
  flex: 1;
  padding: 12px;
  border-radius: 8px;
  border: 1px solid #ccc;
}

.category-selector {
  flex: 1;
  padding: 12px;
  border-radius: 8px;
  border: 1px solid #ccc;
}

.add-btn {
  background-color: #28a745;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 8px;
  cursor: pointer;
}

.add-btn:hover {
  background-color: #218838;
}

/* Task List */
ul.task-list {
  list-style: none;
  padding: 0;
}

.empty {
  text-align: center;
  color: #666;
}

/* Task Summary */
.task-summary {
  margin-top: 20px;
  text-align: center;
}

.clear-btn {
  background-color: #ff4444;
  color: white;
  padding: 10px 15px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  margin-top: 20px;
}

.clear-btn:hover {
  background-color: #e53838;
}
</style>
