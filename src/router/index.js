import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/components/Home.vue'; // Adjust the path if needed
import JudgeView from '@/components/JudgeView.vue';
import LawyerView from '@/components/LawyerView.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/judge-view', name: 'JudgeView', component: JudgeView },
  { path: '/lawyer-view', name: 'LawyerView', component: LawyerView }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
