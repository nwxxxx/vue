<template>
  <!-- 使用Element UI的Menu组件创建垂直导航菜单 -->
  <el-menu
    default-active="/"                
    class="el-menu-vertical-demo"     
    background-color="#545c64"       
    text-color="#fff"                 
    active-text-color="#ffd04b"      
    router                            
  >
    <!-- 首页菜单项 -->
    <el-menu-item index="/">          <!-- index对应路由路径 -->
      <i class="el-icon-s-home"></i>  <!-- Element UI的首页图标 -->
      <span slot="title">主页</span>   <!-- 菜单标题 -->
    </el-menu-item>

    <!-- 贷款计算菜单项 -->
    <el-menu-item index="/loan">      <!-- 点击跳转到/loan路由 -->
      <i class="el-icon-money"></i>   <!-- 货币图标 -->
      <span slot="title">贷款计算</span>
    </el-menu-item>

    <!-- 股票估值菜单项 -->
    <el-menu-item index="/stock">     <!-- 点击跳转到/stock路由 -->
      <i class="el-icon-trend-charts"></i>  <!-- 趋势图图标 -->
      <span slot="title">股票估值</span>
    </el-menu-item>

    <!-- 财报解读菜单项 -->
    <el-menu-item index="/report">    <!-- 点击跳转到/report路由 -->
      <i class="el-icon-document"></i><!-- 文档图标 -->
      <span slot="title">财报解读</span>
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  name: 'Navi',  // 组件名称（用于调试和keep-alive缓存标识）
  // 注意：这里可以添加数据或方法（当前为纯展示组件，无需逻辑）
}
</script>

<!-- 可选的样式补充（如需自定义样式可在此添加） -->
<style scoped>
/* 示例：调整菜单宽度 */
.el-menu-vertical-demo {
  width: 200px;
  height: 100vh; /* 撑满整个视口高度 */
}
</style>