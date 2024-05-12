import api from '@/services/api'

export default {
  fetchMessages() {
    return api.get(`account/`)
              .then(response => response.data)
  },
  postMessage(payload) {
    return api.post(`account/`, payload)
              .then(response => response.data)
  },
  deleteMessage(msgId) {
    return api.delete(`account/${msgId}`)
              .then(response => response.data)
  },
  queryMessage(payload) {
    // return api.get(`account/?search=${payload}`)
    //           .then(response => response.data)
    // return api.post(`account/query/`,payload)
    //       // .then(response => response.data)
    //       .then(response => {
    //         /* eslint-disable no-console */
    //         console.log("Failed to open the specified link");
    //         console.log(response.data);  // 打印收到的数据
    //         /* eslint-enable no-console */
    //
    //         return response.data
    //       });

    return api.post(`account/query/`,payload)
          // .then(response => response.data)
          .then(response => {
            /* eslint-disable no-console */
            console.log("Failed to open the specified link");
            console.log(response.data);  // 打印收到的数据
            /* eslint-enable no-console */

            return response.data
          });
  },
}