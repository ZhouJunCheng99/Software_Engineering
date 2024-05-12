<template>
  <div class="admin-container">
    <header class="admin-header">
      <div class="header-content">
        <h1>管理员界面</h1>
        <nav>
          <ul>
            <li><router-link to="/Aindex/admin/dashboard">海洋牧场总体得分</router-link></li>
            <li><router-link to="/Aindex/admin/users">用户管理</router-link></li>
            <li><router-link to="/Aindex/admin/settings">设置</router-link></li>
          </ul>
        </nav>
      </div>
    </header>
    <main class="admin-main">
      <div class="dashboard-users-container">
        <section id="dashboard" class="dashboard-section">
          <h2>海洋牧场总体得分</h2>
          <!-- 使用 GaugeChart 组件 -->
          <GaugeChart />
          <!-- 使用 Situation 组件 -->
          <Situation />
        </section>
        <section id="users" class="users-section">
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
            <div>
              <label for="userType">用户类别:</label>
              <select id="userType" v-model="newUser.userType">
                <option value="" disabled>请选择用户类别</option>
                <option value="管理员">管理员</option>
                <option value="普通用户（养殖户）">普通用户（养殖户）</option>
                <option value="科研工作者">科研工作者</option>
                <option value="供应链合作伙伴">供应链合作伙伴</option>
                <option value="投资者及财务分析专家">投资者及财务分析专家</option>
              </select>
            </div>
            <button type="submit">添加用户</button>
          </form>
          <ul>
            <li v-for="user in users" :key="user.id">
              {{ user.username }} ({{ user.email }}) - {{ user.userType }}
              <button @click="deleteUser(user.id)" class="action-button">删除</button>
              <button @click="resetPassword(user.id)" class="action-button">重置密码</button>
            </li>
          </ul>
        </section>
      </div>
    </main>
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
        email: '',
        userType: '' // 添加用户类别字段
      },
      users: []
    };
  },
  methods: {
    addUser() {
      this.users.push({ ...this.newUser, id: this.users.length + 1 });
      this.newUser.username = '';
      this.newUser.email = '';
      this.newUser.userType = ''; // 重置用户类别字段
    },
    deleteUser(userId) {
      this.users = this.users.filter(user => user.id !== userId);
    },
    resetPassword(userId) {
      alert(`密码已重置，用户ID: ${userId}`);
      // 这里可以加入实际的重置密码逻辑，比如调用API，之后再加
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
  margin: 0; /* 去掉默认的 h1 外边距 */
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
  color: #ecf0f1; /* 字体颜色 */
  text-decoration: none;  /* 去掉下划线 */
  font-size: 1.2rem;   /* 字体大小 */
  /* 上下居中 */
  padding: 0.5rem 1rem; /* 上下左右内边距 */
  border-radius: 4px; /* 圆角边框 */
  transition: background-color 0.2s;  /* 鼠标悬停时背景色渐变 */
}

.admin-header nav ul li a:hover {
  background-color: #34495e;
}

.admin-main {
  flex: 1;
  padding: 1rem;
}

.dashboard-users-container {
  display: flex; /* 横向布局 */
  justify-content: space-between; /* 两个部分左右对齐 */
  flex-grow: 1; /* 使容器随着页面高度自适应 */
  gap: 1rem;
}

.dashboard-section, .users-section {
  flex: 1;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 1rem;
  min-width: 300px; /* 设置最小宽度 */
  max-height: 800px; /* 设置最大高度 */
  overflow-y: auto; /* 添加垂直滚动条 */
}

.dashboard-section {
  margin-right: 1rem;/* 海洋牧场总体得分部分右边距 */
}

.dashboard-section h2, .users-section h2 {
  margin-top: 0;
  font-size: 1.25rem;
  color: #16a5be;
  border-bottom: 2px solid #2c3e50;
  padding-bottom: 0.5rem;
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

.user-form input, .user-form select {
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

ul {
  list-style: none;
  padding: 0;
}

li {
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
}

.action-button {
  margin-left: 1rem;
  background-color: #e74c3c;
  color: #ecf0f1;
  border: none;
  border-radius: 4px;
  padding: 0.25rem 0.5rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.action-button:hover {
  background-color: #c0392b;
}

.admin-footer {
  background-color: #2c3e50;
  color: #ecf0f1;
  text-align: center;
  padding: 1rem;
}
</style>
