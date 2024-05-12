import messageService from '../../services/messageService'

const state = {
  messages: [],
  queryResult: 0
}

const getters = {
  messages: state => {
    return state.messages
  },
  queryResult: state => {
    return state.queryResult
  }
}

const actions = {
  getMessages ({ commit }) {
    messageService.fetchMessages()
    .then(messages => {
      commit('setMessages', messages)
    })
  },
  addMessage({ commit }, message) {
    messageService.postMessage(message)
    .then(() => {
      commit('addMessage', message)
    })
  },
  deleteMessage( { commit }, msgId) {
    messageService.deleteMessage(msgId)
    commit('deleteMessage', msgId)
  },
  queryMessage({ commit }, message) {
    messageService.queryMessage(message)
    // .then(messages => {
    //   commit('setMessages', messages)
    .then(result => {

      console.log("Failed to open the specified link1");
      console.log(result);  // 打印收到的数据


      // this.queryResult = result
      commit('setQueryResult', result)


    })
  }
  // 优化queryMessage
  // queryMessage({commit}, message){
  //   return new Promise((resolve) => {
  //     // 执行异步操作，并在操作完成后调用 resolve 或 reject
  //     // resolve 时将查询结果赋值给 this.queryResult
  //     // reject 时处理错误
  //     messageService.queryMessage(message)
  //     resolve(result => {
  //       commit('setQueryResult', result)
  //     })
  //
  //   });
  // }
}

const mutations = {
  setMessages (state, messages) {
    state.messages = messages
  },
  addMessage(state, message) {
    state.messages.push(message)
  },
  deleteMessage(state, msgId) {
    state.messages = state.messages.filter(obj => obj.pk !== msgId)
  },
  setQueryResult(state, result) {
    state.queryResult = result
    console.log("muta:",state.queryResult);
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}