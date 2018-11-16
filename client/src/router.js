import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import PasswordReset from './views/PasswordReset.vue';
import Standings from './views/Standings.vue';
import Schedule from './views/Schedule.vue';
import Teams from './views/Teams.vue';
import Admin from './views/Admin.vue';

import store from './store/index';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/reset',
      name: 'reset',
      component: PasswordReset,
    },
    {
      path: '/standings',
      name: 'standings',
      component: Standings,
    },
    {
      path: '/schedule',
      name: 'schedule',
      component: Schedule,
    },
    {
      path: '/teams',
      name: 'teams',
      component: Teams,
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin,
      beforeEnter: (to, from, next) => {
        if (store.getters.user) {
          next('/admin/leagues');
        }
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user) {
              next('/admin/leagues');
            }
          });
        }
        next('/');
      },
    },
    {
      path: '/admin/leagues',
      name: 'admin-leagues',
      component: Admin,
      beforeEnter: (to, from, next) => {
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user && user.userType === 'Admin') {
              next();
            }
          });
        }
        next('/');
      },
    },
    {
      path: '/admin/teams',
      name: 'admin-teams',
      component: Admin,
      beforeEnter: (to, from, next) => {
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user && (user.userType === 'Admin' || user.userType === 'Coordinator')) {
              next();
            }
          });
        }
        next('/');
      },
    },
    {
      path: '/admin/players',
      name: 'admin-players',
      component: Admin,
      beforeEnter: (to, from, next) => {
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user &&
              (user.userType === 'Admin'
              || user.userType === 'Coordinator'
              || user.userType === 'Manager')) {
              next();
            }
          });
        }
        next('/');
      },
    },
    {
      path: '/admin/leagues/create',
      name: 'admin-leagues-create',
      component: Admin,
      beforeEnter: (to, from, next) => {
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user && user.userType === 'Admin') {
              next();
            }
          });
        }
        next('/');
      },
    },
    {
      path: '/admin/teams/create',
      name: 'admin-teams-create',
      component: Admin,
      beforeEnter: (to, from, next) => {
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user && (user.userType === 'Admin' || user.userType === 'Coordinator')) {
              next();
            }
          });
        }
        next('/');
      },
    },
  ],
});

router.beforeEach((to, from, next) => {
  next();
});

export default router;
