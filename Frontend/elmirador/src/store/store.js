// store.js
import { createStore } from 'vuex';

const store = createStore({
  state: {
    residentesCount: 0,
  },
  mutations: {
    setResidentesCount(state, count) {
      state.residentesCount = count;
    },
  },
  actions: {
    updateResidentesCount({ commit }, count) {
      commit('setResidentesCount', count);
    },
  },
  getters: {
    getResidentesCount(state) {
      return state.residentesCount;
    },
  },
});

export default store;
