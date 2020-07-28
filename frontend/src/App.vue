<template>
  <v-app>

    <Navbar />

    <v-main>
      <v-container>
        <v-row class="text-center">
          <v-col
            cols="12"
            offset="0"
            sm="10"
            offset-sm="1"
            lg="8"
            offset-lg="2"
          >
          <router-view/>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  import Navbar from '@/components/Navbar.vue';

  export default {
    name: 'MainPage',

    components: {
      Navbar,
    },
    created() {
      this.$store.dispatch('auth/updateUserInfo');
    }
  }
</script>
