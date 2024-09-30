<template>
  <li class="task-item">
    <div class="task-details">
      <div class="task-header">
        <span :class="{ completed: task.completed }" class="task-name">{{
          task.name
        }}</span>
        <span class="task-category">{{ task.category }}</span>
      </div>
      <span class="task-due" :class="{ overdue: isOverdue(task.dueDate) }">
        Due: {{ task.dueDate }}
      </span>
    </div>
    <div class="task-actions">
      <button @click="$emit('toggle')" class="complete-btn">
        {{ task.completed ? "Undo" : "Complete" }}
      </button>
      <button @click="$emit('remove')" class="delete-btn">Delete</button>
      <button @click="$emit('edit')" class="edit-btn">Edit</button>
    </div>
  </li>
</template>

<script>
export default {
  props: {
    task: Object,
  },
  methods: {
    isOverdue(dueDate) {
      const today = new Date().toISOString().split("T")[0];
      return dueDate < today && !this.task.completed;
    },
  },
};
</script>

<style scoped>
.task-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f9f9f9;
  border-radius: 10px;
  padding: 15px;
  margin-bottom: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
}

.task-item:hover {
  background-color: #f1f1f1;
}

.task-details {
  flex: 1;
}

.task-header {
  display: flex;
  justify-content: space-between;
}

.task-name {
  font-size: 16px;
}

.completed {
  text-decoration: line-through;
  color: #777;
}

.task-category {
  background-color: #f0f0f0;
  padding: 5px 10px;
  border-radius: 10px;
  font-size: 12px;
  color: #555;
}

.task-due {
  display: block;
  font-size: 12px;
  margin-top: 5px;
  color: #666;
}

.overdue {
  color: #e53935;
}

.task-actions {
  display: flex;
  gap: 10px;
}

.complete-btn,
.delete-btn,
.edit-btn {
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
  border: none;
  transition: background-color 0.3s ease;
}

.complete-btn {
  background-color: #007bff;
  color: white;
}

.complete-btn:hover {
  background-color: #0056b3;
}

.delete-btn {
  background-color: #dc3545;
  color: white;
}

.delete-btn:hover {
  background-color: #c82333;
}

.edit-btn {
  background-color: #ffc107;
  color: white;
}

.edit-btn:hover {
  background-color: #e0a800;
}
</style>
