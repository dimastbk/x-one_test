<template>
  <v-form
    ref="form"
    v-model="valid"
    >
    <v-card>
      <v-card-text>
        <v-container>
          <v-row>
            <p
              v-if="signInError"
              class="error--text">{{ signInError }}</p>
            <v-col cols="12">
              <v-text-field
                v-model="username"
                :rules="[rules.required]"
                :error-messages="fieldError.username"
                label="Имя"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                v-model="password"
                :rules="[rules.required, rules.minPass]"
                :error-messages="fieldError.password"
                label="Пароль"
                type="password"
                required></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="blue darken-1"
          text
          @click="signIn"
          :disabled="!valid">Войти</v-btn>
      </v-card-actions>
    </v-card>
  </v-form>
</template>

<script>
  import { mapActions, mapState } from 'vuex'

  export default {
    name: 'SignInUp',

    data: () => ({
      valid: false,

      username: '',
      password: '',

      fieldError: {},

      rules: {
        required: v => !!v || 'Обязательное поле',
        minPass: v => v.length >= 8 || 'Пароль должен быть не менее 8 символов',
      }
    }),
    computed: mapState('auth', [
      'signInError',
    ]),
    methods: {
      ...mapActions('auth', {
        in: 'signIn',
      }),
      signIn() {
        this.in({
          credentials: {
            username: this.username,
            password: this.password
          }, 
          callbackError: this.prepareError
        });
      },
      prepareError(error) {
        if (error.response.status === 400) {
          this.fieldError = error.response.data;
        }
      }
    }
  }
</script>
