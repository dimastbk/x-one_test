import router from '@/router';
import blog from '@/api/blog';

const state = () => ({
  allPages: {},
  currentPage: {},
})

const actions = {
  getAllPages ({ commit }) {
    blog.getAllPages(
      response => commit('setAllPages', response.data),
      error => console.log(error),
    )
  },
  getPageById ({ commit, state }, id) {
    if (id !== state.currentPage.id) {
      commit('setCurrentPage', {});
    }
    blog.getPage(
      id,
      response => commit('setCurrentPage', response.data),
      error => console.log(error),
    )
  },
  postBlogPage ({ commit }, payload) {
    blog.postPage(
      payload,
      response => {
        commit('currentPage', response.data);
        router.push({
          name: 'page',
          params: {
            'pageId': response.data.id
          }
        })
      },
      error => console.log(error),
    )
  },
  cleanCurrentPage ({commit}) {
    commit('setCurrentPage', {});
  }
}
const mutations = {
  setAllPages (state, pages) {
    state.allPages = pages;
  },
  setCurrentPage (state, page) {
    state.currentPage = page;
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations,
}