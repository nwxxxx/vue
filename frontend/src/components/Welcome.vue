<template>
  <!-- 欢迎页面根容器 -->
  <div class="welcome">
    <!-- 使用Element UI的Card组件作为欢迎卡片容器 -->
    <el-card class="box-card">
      <!-- 卡片头部区域 -->
      <div slot="header" class="clearfix">
        <!-- 主标题 -->
        <h1>欢迎使用金融工具集</h1>
      </div>
      
      <!-- 卡片内容区域 -->
      <div class="text item">
        <!-- 动态显示服务器时间 -->
        <p>当前服务器时间: {{ serverTime }}</p>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'Welcome',  // 组件名称(必须)
  
  // 组件数据
  data() {
    return {
      serverTime: ''  // 存储服务器时间的变量，初始为空
    }
  },
  
  // 生命周期钩子 - 组件创建时调用
  created() {
    this.fetchServerTime()  // 组件创建后立即获取服务器时间
  },
  
  // 方法定义
  methods: {
    /**
     * 异步获取服务器时间
     * 使用fetch API调用后端接口
     * 成功时更新serverTime，失败时显示错误信息
     */
    async fetchServerTime() {
      try {
        // 发送GET请求到后端API
        const response = await fetch('http://localhost:5000/api/time')
        
        // 检查响应状态
        if (!response.ok) {
          throw new Error(`HTTP错误! 状态码: ${response.status}`)
        }
        
        // 解析JSON响应
        const data = await response.json()
        
        // 更新组件数据
        this.serverTime = data.time || '时间数据无效'
      } catch (error) {
        // 错误处理
        console.error('获取服务器时间失败:', error)
        this.serverTime = '无法获取服务器时间'
        
        // 可添加用户提示
        // this.$message.error('获取服务器时间失败')
      }
    }
    
    // 可选：添加定时刷新功能
    // startTimer() {
    //   this.timer = setInterval(() => {
    //     this.fetchServerTime()
    //   }, 60000) // 每分钟刷新一次
    // }
  },
  
  // 可选：组件销毁时清除定时器
  // beforeDestroy() {
  //   if (this.timer) {
  //     clearInterval(this.timer)
  //   }
  // }
}
</script>

<style scoped>
/* 页面容器样式 */
.welcome {
  padding: 20px;  /* 内边距，使内容不贴边 */
}

/* 卡片样式 */
.box-card {
  max-width: 600px;  /* 限制卡片最大宽度 */
  margin: 0 auto;    /* 水平居中 */
  text-align: center; /* 文本居中 */
  
  /* 可选的阴影效果 */
  /* box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1); */
}

/* 响应式设计示例 */
/* @media (max-width: 768px) {
  .box-card {
    max-width: 90%;
  }
} */
</style>