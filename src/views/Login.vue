<!--
 描述: 登录模板
 作者: Software Engineering Group
 日期: 2024-05
-->

<template>
  <div class="login-container">
    <div class="layer">
      <div class="some-space">
        <div class="form">
          <h2>海洋牧场监测可视化系统</h2>
          <div class="item">
            <i class="iconfont icon-user"></i>
            <input autocomplete="off"
                   type="text"
                   class="input"
                   v-model="userName"
                   placeholder="请输入用户名" />
          </div>
          <div class="item">
            <i class="iconfont icon-password"></i>
            <input autocomplete="off"
                   type="password"
                   class="input"
                   v-model="userPwd"
                   maxlength="20"
                   @keyup.enter="login"
                   placeholder="请输入密码" />
          </div>
          <button class="loginBtn"
                  @click="query_login"
                  :disabled="!userName || !userPwd">
            立即登录
          </button>

          <br><br>
          没有账户,请先点击注册:
          <router-link to="/register" class="register-link">注册界面</router-link>

          <div class="tip">
            默认用户名：user ，管理员名：admin ，密码：123456
          </div>
        </div>
      </div>
    </div>

    <vue-particles color="#6495ED"
                   :particleOpacity="0.7"
                   :particlesNumber="80"
                   shapeType="circle"
                   :particleSize="4"
                   linesColor="#6495ED"
                   :linesWidth="1"
                   :lineLinked="true"
                   :lineOpacity="0.6"
                   :linesDistance="150"
                   :moveSpeed="3"
                   :hoverEffect="true"
                   hoverMode="grab"
                   :clickEffect="true"
                   clickMode="push">
    </vue-particles>

    <bgAnimation />

    <modal title="提示"
           :content="modalContent"
           :visible.sync="visible"
           @confirm="confirm">
    </modal>

  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Login',
  components: {},
  data () {
    return {
      // adminName: 'admin',
      // adminPwd: '123456',
      userName: 'user',
      userPwd: '123456',
      visible: false,
      modalContent: '这是一段自定义模态框消息',
      // 这里不能加入queryResult属性，因为queryResult是异步获取的，需要在computed中定义

    }
  },
  computed: mapState({
      messages: state => state.messages.messages,
      queryResult: state => state.messages.queryResult//.result

  }),

  created () { },
  mounted () {

  },
  methods: {
    // ...mapActions('messages', ['queryMessage', 'addMessage', 'deleteMessage']),
    // 定义 sleep 函数
    sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    },
    async query_login() {
      // 先执行 queryMessage，然后再调用 login
      this.queryMessage({ name: this.userName, password: this.userPwd })

      // 这里异步执行,console.log(this.queryResult)太快了,queryResult查询还没返回赋值就判断完了
      // 暂时先这么解决
      await this.sleep(500);

      this.login()
    },

    login () {
      // this.queryResult为null
      // this.queryMessage({name: this.userName, password: this.userPwd});
      console.log(this.queryResult);
      // 查询结果返回为0,说明不存在
      if (this.queryResult.result == "admin") {
        this.$router.push({
          path: '/Aindex'
        })
      } 
      else if (this.queryResult.result == "user") {
        this.$router.push({
          path: '/Uindex'
        })
      }
      else {
        this.$Toast({
          content: '请输入正确的用户名和密码',
          type: 'error',
          hasClose: true
        })
      }
    },

    // async login () {
    //   await this.queryMessage({name: this.userName, password: this.userPwd});
    //   console.log(this.queryResult);
    //   if (this.queryResult == true) {
    //     this.$router.push({
    //       path: '/index'
    //     })
    //   } else {
    //     this.$Toast({
    //       content: '请输入正确的用户名和密码',
    //       type: 'error',
    //       hasClose: true
    //     })
    //   }
    // },

    confirm () {
      this.visible = false;
      console.log('点击确定')
    },

    ...mapActions('messages', ['queryMessage', 'addMessage', 'deleteMessage']),
  }
}
</script>

<style lang="scss" scoped>
.login-container {
  .layer {
    position: absolute;
    height: 100%;
    width: 100%;
  }
  #particles-js {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1000;
  }
  .some-space {
    color: white;
    font-weight: 100;
    letter-spacing: 2px;
    position: absolute;
    top: 50%;
    left: 50%;
    z-index: 1001;
    -webkit-transform: translate3d(-50%, -50%, 0);
    transform: translate3d(-50%, -50%, 0);

    -ms-animation: cloud 2s 3s ease-in infinite alternate;
    -moz-animation: cloud 2s 3s ease-in infinite alternate;
    -webkit-animation: cloud 2s 3s ease-in infinite alternate;
    -o-animation: cloud 2s 3s ease-in infinite alternate;
    -webkit-animation: cloud 2s 3s ease-in infinite alternate;
    animation: cloud 2s 3s ease-in infinite alternate;

    .form {
      width: 460px;
      height: auto;
      background: rgba(36, 36, 85, 0.5);
      margin: 0 auto;
      padding: 35px 30px 25px;
      box-shadow: 0 0 25px rgba(255, 255, 255, 0.5);
      border-radius: 10px;
      .item {
        display: flex;
        align-items: center;
        margin-bottom: 25px;
        border-bottom: 1px solid #d3d7f7;
        i {
          color: #d3d7f7;
          margin-right: 10px;
        }
      }
      h2 {
        text-align: center;
        font-weight: normal;
        font-size: 26px;
        color: #d3d7f7;
        padding-bottom: 35px;
      }
      .input {
        font-size: 16px;
        line-height: 30px;
        width: 100%;
        color: #d3d7f7;
        outline: none;
        border: none;
        background-color: rgba(0, 0, 0, 0);
        padding: 10px 0;
      }
      .loginBtn {
        width: 100%;
        padding: 12px 0;
        border: 1px solid #d3d7f7;
        font-size: 16px;
        color: #d3d7f7;
        cursor: pointer;
        background: transparent;
        border-radius: 4px;
        margin-top: 10px;
        &:hover {
          color: #fff;
          background: #0090ff;
          border-color: #0090ff;
        }
      }
      .tip {
        font-size: 12px;
        padding-top: 20px;
      }
    }
  }
}

input::-webkit-input-placeholder {
  color: #d3d7f7;
}
input::-moz-placeholder {
  /* Mozilla Firefox 19+ */
  color: #d3d7f7;
}
input:-moz-placeholder {
  /* Mozilla Firefox 4 to 18 */
  color: #d3d7f7;
}
input:-ms-input-placeholder {
  /* Internet Explorer 10-11 */
  color: #d3d7f7;
}

@-ms-keyframes cloud {
  0% {
    -ms-transform: translate(-50%, -50%);
  }
  40% {
    opacity: 1;
  }
  60% {
    opacity: 1;
  }
  100% {
    -ms-transform: translate(-50%, -40%);
  }
}
@-moz-keyframes cloud {
  0% {
    -moz-transform: translate(-50%, -50%);
  }
  40% {
    opacity: 1;
  }
  60% {
    opacity: 1;
  }
  100% {
    -moz-transform: translate(-50%, -40%);
  }
}
@-o-keyframes cloud {
  0% {
    -o-transform: translate(-50%, -50%);
  }
  40% {
    opacity: 1;
  }
  60% {
    opacity: 1;
  }
  100% {
    -o-transform: translate(-50%, -40%);
  }
}
@-webkit-keyframes cloud {
  0% {
    -webkit-transform: translate(-50%, -50%);
  }
  40% {
    opacity: 1;
  }
  60% {
    opacity: 1;
  }
  100% {
    -webkit-transform: translate(-50%, -40%);
  }
}
@keyframes cloud {
  0% {
    transform: translate(-50%, -50%);
  }
  40% {
    opacity: 1;
  }
  60% {
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -40%);
  }
}

//.register-link {
//  text-decoration: underline;
//}
.register-link {
  text-decoration: underline;
  color: #6495ED; /* 改变链接的颜色 */
  font-size: 14px; /* 改变字体大小 */
  transition: color 0.3s ease; /* 添加颜色过渡效果 */
}

.register-link:hover {
  color: #0090ff; /* 当鼠标悬停时改变链接的颜色 */
}

</style>
