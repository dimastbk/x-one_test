<template>
  <v-row>
    <v-col
      v-for="(page, i) in allPages"
      :key="i"
      class="mb-2"
      cols="12"
      md="6"
      lg="4"
    >
      <v-card>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="headline text-left text-truncate">
              {{ page.title }}
            </v-list-item-title>
            <v-list-item-subtitle class="text-left">{{ page.user }} ({{ page.created | moment("DD.MM.YYYY")  }})</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-card-text class="text-left text-truncate" style="height: 3em;" v-html="page.description" />

        <v-card-actions class="text-right">
          <v-btn :to="{ name: 'page', params: { pageId: page.id }}" text>Читать</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
  import { mapState } from 'vuex';

  export default {
    name: 'MainPage',

    computed: mapState('blog', [
      'allPages',
    ]),
    created() {
      this.$store.dispatch('blog/getAllPages');
    }
  }
</script>
