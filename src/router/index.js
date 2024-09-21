import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/components/Home.vue'; // Adjust the path if needed
import JudgeView from '@/components/JudgeView.vue';
import CaseAnalysis from '@/components/CaseAnalysis.vue';
import DocumentSummarization from '@/components/DocumentSummarization.vue';
import ArgumentPrediction from '@/components/ArgumentPrediction.vue';


const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/judge-view', name: 'JudgeView', component: JudgeView },
  { path: '/case-analysis', name: 'CaseAnalysis', component: CaseAnalysis },
  { path: '/document-summarization', name: 'DocumentSummarization', component: DocumentSummarization }, 
  { path: '/argument-prediction', name: 'ArgumentPrediction', component: ArgumentPrediction},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
