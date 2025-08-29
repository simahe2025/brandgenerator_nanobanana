# 产品广告生成器 / Product Ad Generator


一个基于 nano-banana Gemini 2.5 Flash API 的智能产品广告生成工具，能够将您的产品图片无缝集成到各种专业广告场景中。

## 功能特性

- 🖼️ **多格式支持**：支持 PNG、JPG、WEBP 格式的产品图片上传
- 🎨 **10种广告场景**：从时代广场广告牌到社交媒体帖子，多样化场景选择
- 🤖 **AI 驱动**：基于 Google Gemini 2.5 Flash 的先进图像生成技术
- 📱 **响应式设计**：完美适配桌面端和移动端
- 🌙 **深色模式**：支持明暗主题切换
- ⚡ **智能重试**：内置错误处理和自动重试机制
- 🔒 **安全可靠**：API 密钥本地存储，不上传到服务器

## 快速开始

### 方法一：直接使用 HTML 版本

1. 打开 `index.html` 文件
2. 在浏览器中运行
3. 输入您的 [Gemini API 密钥](https://aistudio.google.com/app/apikey)
4. 上传产品图片并选择广告格式
5. 点击生成按钮

### 方法二：集成 React 组件

1. 安装依赖：
```bash
npm install react react-dom lucide-react
npm install -D tailwindcss
```

2. 导入组件：
```javascript
import App from './simahe_image_generator.py'; // 重命名为 .jsx
```

3. 在您的应用中使用：
```javascript
function MyApp() {
  return <App />;
}
```

## API 配置

### 获取 Gemini API 密钥

1. 访问 [Google AI Studio](https://aistudio.google.com/app/apikey)
2. 登录您的 Google 账户
3. 创建新的 API 密钥
4. 复制密钥并在应用中使用

### API 使用限制

- 免费层：每分钟 15 次请求
- 付费层：根据您的订阅计划
- 图片大小：建议不超过 4MB

## 广告场景选项

| 场景 | 描述 |
|------|------|
| 🌪️ Billboard | 繁华城市中心如时代广场的巨型广告牌 |
| 📰 Magazine | 时尚杂志的全页彩色广告 |
| 🚌 Bus | 伦敦经典红色双层巴士侧面广告 |
| 📺 Airport | 未来感机场航站楼的数字屏幕广告 |
| ☕ Coffee Shop | 鹅卵石街道上温馨咖啡店外的木质招牌 |
| 📱 Social Media | 知名网红社交媒体动态中的赞助帖子 |
| 🧱 Vintage Poster | 时尚小巷砖墙上的复古风格海报 |
| 🏟️ Jumbotron | 爆满体育场大屏幕上的广告 |
| 🎬 Movie Placement | 高预算电影场景中桌上的产品植入 |
| ✈️ Airplane | 商用飞机座椅背面的广告 |

## 技术架构

### 前端技术栈
- **React 18**：现代化的用户界面框架
- **Tailwind CSS**：实用优先的 CSS 框架
- **Lucide React**：美观的图标库
- **Babel Standalone**：浏览器端 JSX 转换

### API 集成
- **Gemini 2.0 Flash**：Google 最新的多模态 AI 模型
- **REST API**：标准的 HTTP 请求处理
- **Base64 编码**：图片数据传输格式

### 核心功能实现

```javascript
// 图片上传处理
const handleImageChange = (e) => {
  const file = e.target.files[0];
  const reader = new FileReader();
  reader.readAsDataURL(file);
};

// API 调用
const generateAd = async () => {
  const payload = {
    contents: [{
      parts: [
        { text: `生成广告场景：${selectedFormat.text}` },
        { inlineData: { mimeType: "image/png", data: base64Data } }
      ]
    }],
    generationConfig: { responseModalities: ['TEXT', 'IMAGE'] }
  };
};
```

## 项目结构

```
gemini_image_generator/
├── index.html                    # 完整的 HTML 应用
├── simahe_image_generator.py     # React 组件源码
├── README.md                     # 项目说明文档
└── assets/                       # 静态资源（可选）
    ├── icons/
    └── images/
```

## 使用示例

### 基本使用流程

1. **上传产品图片**
   ```
   支持格式：PNG, JPG, WEBP
   建议尺寸：1024x1024 或更高
   文件大小：< 4MB
   ```

2. **选择广告场景**
   ```
   从 10 种预设场景中选择
   每种场景都有独特的视觉风格
   ```

3. **生成广告**
   ```
   AI 处理时间：10-30 秒
   输出格式：PNG 图片
   分辨率：高清质量
   ```

## 故障排除

### 常见问题

**Q: API 密钥无效**
- 确保从 Google AI Studio 获取正确的密钥
- 检查密钥是否已激活 Gemini API 访问权限

**Q: 图片上传失败**
- 检查图片格式是否支持（PNG/JPG/WEBP）
- 确保文件大小不超过 4MB
- 尝试使用不同的图片

**Q: 生成失败**
- 检查网络连接
- 确认 API 配额未超限
- 尝试选择不同的广告场景

**Q: 生成速度慢**
- 这是正常现象，AI 图片生成需要时间
- 复杂场景可能需要更长时间
- 请耐心等待，避免重复点击

## 开发计划

### 即将推出的功能

- [ ] 批量处理多张图片
- [ ] 自定义广告文案输入
- [ ] 更多广告场景模板
- [ ] 图片编辑和调整功能
- [ ] 历史记录和收藏功能
- [ ] 多语言界面支持

### 技术优化

- [ ] 图片压缩和优化
- [ ] 缓存机制实现
- [ ] 离线模式支持
- [ ] PWA 应用封装

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建功能分支：`git checkout -b feature/new-feature`
3. 提交更改：`git commit -am 'Add new feature'`
4. 推送分支：`git push origin feature/new-feature`
5. 提交 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 联系方式

- 项目维护：Simahe
- 技术支持：通过 GitHub Issues
- 更新日志：查看 [Releases](../../releases)

---


**注意**：本工具仅供学习和研究使用，生成的广告内容请遵守相关法律法规和平台规定。


