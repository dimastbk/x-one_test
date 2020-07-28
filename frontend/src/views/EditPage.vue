<template>
  <v-form 
    ref="form"
    v-model="valid"
    class="text-left"
    >
      <div class="text-h6 text-sm-h5 text-md-h4 text-lg-h3 pb-2" v-if="page.id">Редактировать статью</div>
      <div class="text-h6 text-sm-h5 text-md-h4 text-lg-h3 pb-2" v-else>Добавить статью</div>

      <v-text-field
        v-model="page.title"
        :rules="[rules.required]"
        label="Заголовок"
        required
      ></v-text-field>
      <tiptap-vuetify
        v-model="page.content"
        :extensions="extensions"
        :rules="[rules.required]"
        label="Содержимое"
        required
      />
      <v-row>
        <v-col
          cols="6"
          >
          <v-checkbox
            v-model="page.is_published"
            v-if="isAdmin"
            label="Опубликовать"
            class="mt-0"
            ></v-checkbox>
        </v-col>
        <v-col
          cols="6"
          class="text-right"
          >
          <v-btn
            color="blue darken-1"
            class="ml-auto"
            @click="post"
            :disabled="!valid">{{ page.id ? 'Сохранить' : 'Создать' }}</v-btn>
        </v-col>
      </v-row>
  </v-form>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex';
  import { TiptapVuetify, Heading, Bold, Italic, Strike, Underline, Code, BulletList, OrderedList, ListItem, Link, Blockquote, HardBreak, HorizontalRule, History } from 'tiptap-vuetify';
  import blog from '@/api/blog';

  export default {
    name: 'AddPage',

    components: { TiptapVuetify },
    computed: {
      ...mapGetters('auth', [
        'isAdmin',
        'isAuthenticated',
      ])
    },
    created() {
      if (!!this.$route.params.pageId && Number(this.$route.params.pageId) && Number.isInteger(Number(this.$route.params.pageId)) ) {
        blog.getPage(
          this.$route.params.pageId,
          response => this.page = response.data,
          error => console.log(error),
        )
      }
    },
    methods: {
      ...mapActions('blog', [
        'postBlogPage',
        'getPageById',
        'cleanCurrentPage',
      ]),
      post() {
        this.postBlogPage({
          title: this.page.title,
          content: this.page.content,
          is_published: this.page.is_published,
          id: this.page.id,
        })
      }
    },
    data: () => ({

      valid: false,

      page: {},

      rules: {
        required: v => !!v || 'Обязательное поле',
      },
      extensions: [
        History,
        Blockquote,
        Link,
        Underline,
        Strike,
        Italic,
        ListItem,
        BulletList,
        OrderedList,
        [Heading, {
          options: {
            levels: [1, 2, 3]
          }
        }],
        Bold,
        Code,
        HorizontalRule,
        HardBreak
      ],
    })
  }
</script>
