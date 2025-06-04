// 从vue-router导入createRouter和createWebHistory
// createRouter用于创建路由器实例，createWebHistory用于创建基于HTML5 History API的history对象
import { createRouter, createWebHistory } from 'vue-router'

// 导入各个组件，这些组件将用作路由的匹配组件
import Welcome from './components/Welcome.vue'
import Loan from './components/Loan.vue'
import Stock from './components/Stock.vue'
import Report from './components/Report.vue'

// 定义路由配置数组routes
// 每个路由对象包含path属性（路由路径）和component属性（对应路径下的组件）
const routes = [
  // 根路径'/'对应显示Welcome组件
  { path: '/', component: Welcome },
  // 路径'/loan'对应显示Loan组件
  { path: '/loan', component: Loan },
  // 路径'/stock'对应显示Stock组件
  { path: '/stock', component: Stock },
  // 路径'/report'对应显示Report组件
  { path: '/report', component: Report }
  // 可以继续添加其他路由...
]

// 使用createRouter函数和createWebHistory创建路由器实例
// 并导出这个实例供其他文件使用
export default createRouter({
  // 指定history模式为基于HTML5 History API的history模式
  history: createWebHistory(),
  // 将定义的路由配置传入路由器实例
  routes
})