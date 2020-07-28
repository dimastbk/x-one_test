<template>
  <div>
      <v-badge
        :value="!page.is_published"
        content="На модерации"
        color="blue"
      >
        <div class="text-h5 text-sm-h4 text-md-h3 text-lg-h2 pb-2">{{ page.title }}</div>
      </v-badge>

    <div class="text-body-2 text-sm-body-1 text-left" v-html="page.content"></div>
  </div>

</template>

<script>
  import { mapActions, mapState } from 'vuex';

  export default {
    name: 'BlogPage',

    mounted() {
      this.getPageById(this.$route.params.pageId);
    },
    computed: mapState('blog', {
      page: 'currentPage',
    }),
    methods: mapActions('blog', [
      'getPageById',
    ])
  }
</script>
