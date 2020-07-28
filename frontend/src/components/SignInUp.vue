<template>
  <v-dialog v-model="signInUpDialog" max-width="400px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        v-bind="attrs"
        v-on="on"
        text
      >
        <span class="mr-2">Войти</span>
      </v-btn>
    </template>
    <v-tabs
      v-model="tab"
    >
      <v-tab key="signIn">Вход</v-tab>
      <v-tab key="signUp">Регистрация</v-tab>
    </v-tabs>
    <v-tabs-items
      v-model="tab"
    >
      <v-tab-item key="signIn">
        <SignIn />
      </v-tab-item>
      <v-tab-item key="signUp">
        <SignUp />
      </v-tab-item>
    </v-tabs-items>
  </v-dialog>
</template>

<script>
  import { mapMutations } from 'vuex';
  import SignIn from '@/components/SignIn.vue';
  import SignUp from '@/components/SignUp.vue';

  export default {
    name: 'SignInUp',

    data: () => ({
      signInUpDialog: false,
      tab: null,

    }),
    components: {
      SignIn,
      SignUp,
    },
    mounted() {
      this.removeError();
    },
    methods: mapMutations('auth', [
      'removeError',
    ]),
  }
</script>
