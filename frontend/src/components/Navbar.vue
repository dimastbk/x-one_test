<template>
  <v-app-bar
    app
    color="primary"
    dark
  >
    <div class="d-flex align-center">
      <router-link :to="{name: 'home'}">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />
      </router-link>
      <router-link :to="{name: 'home'}">
        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </router-link>
    </div>

    <v-spacer></v-spacer>

    <v-btn :to="{name: 'editpage', params: {pageId: 'new'}}" text v-if="isAuthenticated">
      <span>Добавить статью</span>
    </v-btn>
    <v-btn :to="{name: 'admin_page'}" text v-if="isAdmin">
      <span>Статьи</span>
    </v-btn>
    <v-btn :to="{name: 'admin_user'}" text v-if="isAdmin">
      <span>Пользователи</span>
    </v-btn>
    <v-btn @click="signOut" text v-if="isAuthenticated">
      <span>Выйти</span>
    </v-btn>

    <SignInUp v-else />

  </v-app-bar>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex';
  import SignInUp from '@/components/SignInUp.vue';

  export default {
    name: 'Navbar',

    components: {
      SignInUp,
    },
    computed: mapGetters('auth', [
      'isAdmin',
      'isAuthenticated',
    ]),
    methods: mapActions('auth', [
      'signOut',
    ]),
  }
</script>