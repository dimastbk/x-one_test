import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import VueMoment from 'vue-moment'

import ru from 'vuetify/es5/locale/ru'
import { TiptapVuetifyPlugin } from 'tiptap-vuetify';

import 'material-design-icons-iconfont/dist/material-design-icons.css'
import 'tiptap-vuetify/dist/main.css';

const vuetify = new Vuetify({
  icons: {
    iconfont: 'md',
  },
  lang: {
    locales: { ru },
    current: 'ru',
  },
})

Vue.use(VueMoment)
Vue.use(Vuetify);
Vue.use(TiptapVuetifyPlugin, {
  vuetify,
  iconsGroup: 'md'
})

export default vuetify;
