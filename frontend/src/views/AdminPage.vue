<template>
  <div>
    <div class="text-h6 text-sm-h5 text-md-h4 text-lg-h3 pb-2">Список статей</div>

    <v-data-table
      :headers="headers"
      :items="pages"
      :items-per-page="10"
      class="elevation-1"
      search
    >
      <template v-slot:item.is_published="{ item }">
        <v-simple-checkbox v-model="item.is_published" disabled></v-simple-checkbox>
      </template>
      <template v-slot:item.title="{ item }">
        <router-link :to="{name: 'editpage', params: { pageId: item.id }}">{{ item.title}}</router-link>
      </template>
      <template v-slot:item.created="{ item }">
        <p>{{ item.created | moment("HH:MM DD.MM.YYYY")}}</p>
      </template>
      <template v-slot:item.updated="{ item }">
        <p>{{ item.updated | moment("HH:MM DD.MM.YYYY")}}</p>
      </template>
    </v-data-table>
  </div>
</template>

<script>
  import blog from '@/api/blog';

  export default {
    name: 'AdminPage',

    data: () => ({
      headers: [
        {
          text: 'Пользователь',
          align: 'start',
          value: 'user',
        },
        { text: 'Заголовок', value: 'title' },
        { text: 'Дата создания', value: 'created' },
        { text: 'Дата обновления', value: 'updated' },
        { text: 'Опубликована', align: 'center', value: 'is_published' },
      ],
      pages: [],
    }),
    mounted() {
      this.renderPagesList();
    },
    methods: {
      renderPagesList() {
        blog.getAllPagesInfo(
          response => this.pages = response.data,
          error => console.log(error)
        )
      },
      deletePage(id) {
        blog.deletePage(
          id,
          () => this.renderPagesList(),
          error => console.log(error)
        )
      }
    }
  }
</script>
