<template>
  
  <div>
    <div class="text-h6 text-sm-h5 text-md-h4 text-lg-h3 pb-2">Список пользователей</div>

    <v-data-table
      :headers="headers"
      :items="users"
      :items-per-page="10"
      class="elevation-1"
      search
    >
      <template v-slot:item.is_staff="{ item }">
        <v-simple-checkbox v-model="item.is_staff" disabled></v-simple-checkbox>
      </template>
      <template v-slot:item.is_active="{ item }">
        <v-simple-checkbox v-model="item.is_active" disabled></v-simple-checkbox>
      </template>
      <template v-slot:item.date_joined="{ item }">
        <p>{{ item.date_joined | moment("HH:MM DD.MM.YYYY")}}</p>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon
          small
          @click="blockUser(item.id)"
          v-if="item.is_active"
        >
          delete
        </v-icon>
      </template>
    </v-data-table>
  </div>
</template>

<script>
  import user from '@/api/user';

  export default {
    name: 'AdminUser',

    data: () => ({
      headers: [
        {
          text: 'Логин',
          align: 'start',
          value: 'username',
        },
        { text: 'Активен', value: 'is_active', align: 'center' },
        { text: 'Администратор', value: 'is_staff', align: 'center' },
        { text: 'Зарегистрирован', value: 'date_joined' },
        { text: 'Статей', value: 'pages__sum' },
        { text: 'Действия', value: 'actions', align: 'center', sortable: false },
      ],
      users: [],
    }),
    mounted() {
      this.renderUserList();
    },
    methods: {
      renderUserList() {
        user.getAllUser(
          response => this.users = response.data,
          error => console.log(error)
        )
      },
      blockUser(id) {
        confirm('Вы уверены, что хотите заблокировать пользователя и удалить все его статьи?') &&
        user.blockUser(
          id,
          () => user.deleteUserPages(id, () => this.renderUserList(), error => console.log(error)),
          error => console.log(error)
        )
      }
    }
  }
</script>
