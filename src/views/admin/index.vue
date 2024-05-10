<template>
  <div class="admin-container">
    <header class="admin-header">
      <div class="header-content">
        <h1>管理员界面</h1>
        <nav>
          <ul>
            <li><a href="#dashboard">仪表盘</a></li>
            <li><a href="#users">用户管理</a></li>
            <li><a href="#settings">设置</a></li>
          </ul>
        </nav>
      </div>
    </header>
    <main class="admin-main">
      <div class="dashboard-users-container">
        <section id="dashboard">
          <h2>仪表盘</h2>
          <!-- 使用 GaugeChart 组件 -->
          <GaugeChart />
          <!-- 使用 Situation 组件 -->
          <Situation />
        </section>
        <section id="users">
          <h2>用户管理</h2>
          <!-- 使用 Userdata 组件 -->
          <Userdata />
          <form @submit.prevent="addUser" class="user-form">
            <div>
              <label for="username">用户名:</label>
              <input type="text" id="username" v-model="newUser.username">
            </div>
            <div>
              <label for="email">邮箱:</label>
              <input type="email" id="email" v-model="newUser.email">
            </div>
            <button type="submit">添加用户</button>
          </form>
          <ul>
            <li v-for="user in users" :key="user.id">{{ user.username }} ({{ user.email }})</li>
          </ul>
        </section>
      </div>
    </main>
    <footer class="admin-footer">
      <p>版权所有 © 2024</p>
    </footer>
  </div>
</template>

<script>
import GaugeChart from './component/GaugeChart.vue'; // 引入 GaugeChart 组件
import Userdata from './component/Userdata.vue'; // 引入 Userdata 组件
import Situation from './component/Situation.vue'; // 引入 Situation 组件

export default {
  name: 'AdminIndex',
  components: {
    GaugeChart,
    Userdata,
    Situation
  },
  data() {
    return {
      newUser: {
        username: '',
        email: ''
      },
      users: []
    };
  },
  methods: {
    addUser() {
      this.users.push({ ...this.newUser, id: this.users.length + 1 });
      this.newUser.username = '';
      this.newUser.email = '';
    }
  }
};
</script>

<style scoped>
.admin-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.admin-header {
  background-color: #2c3e50;
  color: #ecf0f1;
  padding: 1rem;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.admin-header h1 {
  margin: 0;
  font-size: 1.5rem;
}

.admin-header nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
}

.admin-header nav ul li {
  margin-left: 1rem;
}

.admin-header nav ul li a {
  color: #ecf0f1;
  text-decoration: none;
  font-size: 1rem;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.admin-header nav ul li a:hover {
  background-color: #34495e;
}

.admin-main {
  flex: 1;
  padding: 1rem;
}

.dashboard-users-container {
  display: flex;
  justify-content: space-between;
}

#dashboard, #users {
  flex: 1;
  margin: 0 1rem;
}

.user-form {
  margin-top: 1rem;
}

.user-form div {
  margin-bottom: 1rem;
}

.user-form label {
  display: block;
  margin-bottom: 0.5rem;
}

.user-form input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.user-form button {
  background-color: #2c3e50;
  color: #ecf0f1;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.user-form button:hover {
  background-color: #34495e;
}

.admin-footer {
  background-color: #2c3e50;
  color: #ecf0f1;
  text-align: center;
  padding: 1rem;
}
</style>
