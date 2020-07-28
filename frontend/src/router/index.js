import Vue from 'vue';
import VueRouter from 'vue-router';
import auth from '@/store/modules/auth';

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import("@/views/Home.vue"),
  },
  {
    path: '/page/edit/:pageId',
    name: 'editpage',
    component: () => import("@/views/EditPage.vue"),
    meta: { 
      requiresAuth: true,
    }
  },
  {
    path: '/page/:pageId',
    name: 'page',
    component: () => import("@/views/BlogPage.vue"),
  },
  {
    path: '/admin/user',
    name: 'admin_user',
    component: () => import("@/views/AdminUser.vue"),
    meta: { 
      requiresAuth: true,
      requiresAdmin: true,
    }
  },
  {
    path: '/admin/page',
    name: 'admin_page',
    component: () => import("@/views/AdminPage.vue"),
    meta: { 
      requiresAuth: true,
      requiresAdmin: true,
    }
  },
  { 
    path: '/500', 
    component: () => import("@/views/Error500.vue")
  },
  { 
    path: '/403',
    component: () => import("@/views/Error403.vue")
  },
  { 
    path: '*', 
    component: () => import("@/views/Error404.vue")
  }
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  base: '/',
  routes
})

router.beforeEach((to, from, next) => {
  if ((to.matched.some(record => record.meta.requiresAuth) && !auth.getters.isAuthenticated) ||
      (to.matched.some(record => record.meta.requiresAdmin) && !auth.getters.isAdmin)
  ) {
    next('/403')
  }

  next()
})

export default router;
