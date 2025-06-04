# 导入Flask库，用于创建Web应用
from flask import Flask, jsonify
# 导入datetime库，用于处理日期和时间
from datetime import datetime
# 导入flask_cors库，用于添加跨域支持
from flask_cors import CORS

# 创建一个Flask应用实例
app = Flask(__name__)

# 启用跨域资源共享（CORS），允许不同源的网页调用API
CORS(app)

# 定义一个路由 '/api/time'，当使用GET方法访问时触发
@app.route('/api/time', methods=['GET'])
def get_time():
    # 获取当前的日期和时间
    now = datetime.now()
    # 格式化日期时间为字符串，格式为 '年-月-日 时:分:秒'
    formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
    # 返回一个JSON格式的响应，包含当前时间和状态
    return jsonify({
        'time': formatted_time,  # 当前时间
        'status': 'success'    # 请求状态
    })

# 如果这个脚本是作为主程序运行，那么执行下面的代码
if __name__ == '__main__':
    # 运行Flask应用，设置host为'0.0.0.0'表示允许任何IP地址访问，
    # 端口号设置为5000，debug设置为True表示开启调试模式
    app.run(host='0.0.0.0', port=5000, debug=True)