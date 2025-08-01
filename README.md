# 🎬 视频标注应用

一个基于 Streamlit 的智能化视频标注与分析工具，专门用于驾驶行为视频的标注工作。支持多种视频格式，提供丰富的标注选项，并具备完善的进度跟踪和数据管理功能。

## 🔥 最新更新
- 新增评分报告功能，支持真实性、准确性、相关性和连贯性评分
- 优化收藏功能，支持快速定位重要视频
- 改进文件排序算法，使用自然排序提升用户体验
- 修复多个已知问题，提升系统稳定性

## 📋 目录
- [功能特性](#功能特性)
- [系统要求](#系统要求)
- [安装指南](#安装指南)
- [使用说明](#使用说明)
- [标注规范](#标注规范)
- [文件结构](#文件结构)
- [开发指南](#开发指南)
- [常见问题](#常见问题)
- [更新日志](#更新日志)

## ✨ 功能特性

### 🎥 视频管理
- **多格式支持**: 支持 .mp4, .avi, .mov, .mkv, .wmv, .flv, .webm, .m4v 等主流视频格式
- **文件夹浏览**: 自动扫描指定路径下的所有视频文件，按文件夹分组显示
- **历史路径**: 自动保存最近使用的文件夹路径，快速切换项目
- **收藏功能**: 标记重要视频文件，方便后续查找

### 📝 标注功能
- **必填标注项**: 5个核心标注字段，确保数据完整性
- **可选详细描述**: 4个详细描述字段，支持深度分析
- **实时保存**: 标注内容自动保存，防止数据丢失
- **断点续标**: 支持暂停后继续标注，保持工作进度

### 📊 进度管理
- **整体进度**: 显示项目总体完成情况
- **文件夹进度**: 每个文件夹的标注进度统计
- **状态跟踪**: 实时更新标注状态
- **评分报告**: 支持对标注质量进行多维度评分

### 🌐 国际化支持
- **多语言界面**: 支持中文和英文界面切换
- **语言记忆**: 自动保存用户的语言偏好设置

## 💻 系统要求

### 最低配置
- **处理器**: 双核 CPU 2.0GHz 以上
- **内存**: 4GB RAM
- **存储**: 500MB 可用空间（不含视频文件）
- **显示器**: 1366x768 分辨率
- **浏览器**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

### 推荐配置
- **处理器**: 四核 CPU 3.0GHz 以上
- **内存**: 8GB RAM 以上
- **存储**: 2GB 可用空间
- **显示器**: 1920x1080 分辨率或更高
- **网络**: 稳定的互联网连接（用于加载 Streamlit 资源）

## 🚀 安装指南

### 环境要求
- Python 3.7+
- 支持的操作系统: Windows, macOS, Linux

### 安装步骤

1. **克隆项目**
   ```bash
   git clone <项目地址>
   cd videoLabel
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **创建必要的目录**
   ```bash
   mkdir -p data
   ```

4. **运行应用**
   ```bash
   streamlit run app.py --server.port 8503
   ```

5. **访问应用**
   - 在浏览器中打开 `http://localhost:8503`
   - 应用将自动启动并显示主界面
   - 首次运行可能需要下载 Streamlit 资源

### Docker 部署（可选）
```bash
# 构建 Docker 镜像
docker build -t video-annotation .

# 运行容器
docker run -p 8503:8503 -v /path/to/videos:/videos video-annotation
```

## 📖 使用说明

### 1. 初始设置

#### 选择视频文件夹
- 在左侧边栏的"📁 项目配置"区域
- 输入包含视频文件的文件夹路径
- 点击"✅ 确认路径"按钮加载项目

#### 使用历史路径
- 如果之前使用过应用，可以从"📋 历史路径"下拉菜单中选择
- 点击"🔄 加载选中路径"快速加载项目

### 2. 视频选择

#### 选择文件夹
- 在右侧标注区域，从"选择文件夹"下拉菜单中选择目标文件夹
- 显示格式：`文件夹名 (X 个视频)`

#### 选择视频文件
- 从"选择视频"下拉菜单中选择要标注的视频
- ⭐ 标记表示该视频已被收藏

### 3. 视频播放

- 选择视频后，左侧将显示视频播放器
- 支持播放、暂停、快进、快退等基本控制
- 可以随时调整播放进度进行精确标注

### 4. 标注操作

#### 收藏管理
- 🤍 **收藏**: 点击添加到收藏列表
- ❤️ **取消收藏**: 点击从收藏列表移除

#### 必须标注项 ⭐
以下字段为必填项，确保每个视频都要完成：

1. **自动驾驶模式 (autonomous_mode)**
   - 输入格式: `0`, `1`, `01`, `10`
   - `0`: 关闭自动驾驶
   - `1`: 开启自动驾驶  
   - `01`: 先关闭后开启
   - `10`: 先开启后关闭

2. **驾驶操控风格 (driving_control_style)**
   - 多选字段，最多选择 3 项
   - 选项包括：过度谨慎驾驶、谨慎驾驶、平稳驾驶、激进驾驶等

3. **视觉注意风格 (visual_attention_style)**
   - 多选字段，最多选择 3 项
   - 选项包括：专注前方、观察四周、关注行人、查看后视等

4. **综合风格 (integrated_style)**
   - 多选字段，最多选择 3 项
   - 选项包括：谨慎、稳定、激进、粗心、分心、专注

5. **建议 (suggestion)**
   - 多选字段，最多选择 3 项
   - 选项包括：减速、变道、观察行人、手动驾驶等

#### 详细描述 (可选) 📝
每个文件夹至少需要完成 5 个视频的详细描述：

1. **场景描述 (SceneDescription)**
   - 描述视频中的道路环境、天气条件、交通状况等

2. **驾驶员注意力 (Driver's Attention)**
   - 观察并记录驾驶员的注意力分布和行为特征

3. **人机交互 (Human-Machine Interaction)**
   - 记录驾驶员与车载系统的交互情况

4. **评估与建议 (Evaluation & Suggestions)**
   - 对驾驶行为进行评估并提出改进建议

### 5. 数据保存

- **自动保存**: 每次修改标注内容后会自动保存
- **保存格式**: 标注数据保存为与视频同名的 .txt 文件
- **保存位置**: 与视频文件在同一目录下

## 📋 标注规范

### 标注原则
1. **准确性**: 仔细观察视频内容，确保标注准确
2. **一致性**: 同类行为使用统一的标注标准
3. **完整性**: 必填字段必须完成，可选字段按要求完成

### 标注质量要求
- **必填项**: 每个视频都必须完成所有必填标注项
- **详细描述**: 每个文件夹至少完成 5 个视频的详细描述
- **收藏标记**: 对重要或典型案例进行收藏标记

### 数据文件格式
标注数据保存为 txt 格式，示例：
```
autonomous_mode: 1
driving_control_style: 平稳驾驶, 谨慎驾驶
visual_attention_style: 专注前方, 观察四周
integrated_style: 稳定, 谨慎
suggestions: 继续保持, 关注周围交通

-------------------------

**Scene Description:**
城市道路，天气晴朗，交通正常...

**Driver's Attention:**
驾驶员注意力集中，经常查看后视镜...

**Human-Machine Interaction:**
驾驶员与导航系统交互良好...

**Evaluation & Suggestions:**
整体驾驶表现良好，建议...
```

## 📁 文件结构

```
videoLabel/
├── app.py                      # 主应用入口
├── requirements.txt            # 项目依赖
├── README.md                   # 使用说明
├── CLAUDE.md                   # Claude AI 开发指南
├── PLAN.md                     # 技术方案
├── .streamlit/
│   └── config.toml            # Streamlit 配置
├── modules/                    # 功能模块
│   ├── __init__.py
│   ├── file_manager.py        # 文件管理
│   ├── video_player.py        # 视频播放
│   ├── annotation_form.py     # 标注表单
│   ├── data_storage.py        # 数据存储
│   ├── progress_manager.py    # 进度管理
│   ├── history_manager.py     # 历史管理
│   ├── favorites_manager.py   # 收藏管理
│   ├── report_rating.py       # 评分报告
│   └── language_manager.py    # 多语言支持
├── config/                     # 配置文件
│   ├── __init__.py
│   └── word_bank.py           # 词组库配置
├── translations/               # 翻译文件
│   ├── __init__.py
│   ├── zh_CN.py              # 中文翻译
│   └── en_US.py              # 英文翻译
└── data/                       # 数据存储
    ├── favorites.json         # 收藏列表
    ├── path_history.json      # 路径历史
    └── language_preference.json # 语言偏好
```

## 🛠️ 开发指南

### 技术栈
- **前端框架**: Streamlit
- **编程语言**: Python 3.7+
- **关键依赖**: 
  - streamlit: Web 应用框架
  - natsort: 自然排序算法
  - json: 数据序列化

### 架构设计
应用采用模块化设计，各模块职责明确：
- **app.py**: 主程序入口，协调各模块
- **file_manager**: 处理文件系统操作
- **video_player**: 视频播放控制
- **annotation_form**: 标注表单逻辑
- **data_storage**: 数据持久化
- **progress_manager**: 进度统计
- **history_manager**: 历史记录管理
- **favorites_manager**: 收藏功能
- **report_rating**: 评分报告功能
- **language_manager**: 多语言支持

### 扩展开发
1. **添加新的标注字段**：
   - 修改 `config/word_bank.py` 添加选项
   - 在 `annotation_form.py` 中添加相应的表单组件
   - 更新 `data_storage.py` 的数据结构

2. **添加新功能模块**：
   - 在 `modules/` 目录创建新模块
   - 在 `app.py` 中导入并集成
   - 遵循现有的模块化设计模式

3. **自定义样式**：
   - 修改 `app.py` 中的 CSS 样式
   - 使用 Streamlit 的主题配置

### 代码规范
- 使用 UTF-8 编码
- 遵循 PEP 8 Python 代码规范
- 函数和变量使用描述性命名
- 添加必要的错误处理和日志

## ❓ 常见问题

### Q: 应用无法启动怎么办？
A: 
1. 检查 Python 版本是否为 3.7+
2. 确认已安装所有依赖：`pip install -r requirements.txt`
3. 检查端口 8503 是否被占用

### Q: 视频无法播放怎么办？
A:
1. 确认视频格式是否支持（支持 mp4, avi, mov 等主流格式）
2. 检查视频文件是否损坏
3. 确认文件路径是否正确

### Q: 标注数据在哪里保存？
A: 标注数据保存在与视频文件同一目录下，文件名为 `视频名.txt`

### Q: 如何批量导出标注数据？
A: 可以编写脚本扫描文件夹中的所有 .txt 文件进行数据汇总

### Q: 如何重置应用状态？
A: 点击左侧边栏的"🔄 重置"按钮可以清空当前状态

### Q: 历史路径记录太多怎么办？
A: 点击"🗑️ 清空历史记录"按钮可以清除所有历史路径

### Q: 标注数据如何导入导出？
A: 
- 导出：直接复制视频目录下的所有 .txt 文件
- 导入：将 .txt 文件放置在对应视频文件的同一目录

### Q: 如何处理大量视频文件？
A: 
1. 建议按批次组织视频文件到不同文件夹
2. 使用收藏功能标记重要视频
3. 定期导出已完成的标注数据

### Q: 多人协作如何避免冲突？
A: 
1. 为每个标注员分配不同的文件夹
2. 定期合并标注结果
3. 使用版本控制系统管理标注文件

## 📈 更新日志

### v1.2.0 (2025-01)
- ✨ 新增评分报告功能
- 🌍 添加多语言支持（中文/英文）
- 🔧 优化文件排序算法
- 🐛 修复收藏功能相关bug

### v1.1.0 (2024-12)
- ✨ 新增收藏功能
- 📊 改进进度统计显示
- 🔧 优化用户界面布局

### v1.0.0 (2024-11)
- 🎉 首次发布
- 📝 基础标注功能
- 📁 文件管理功能
- 📊 进度跟踪功能

## 🤝 贡献指南

欢迎贡献代码和提出建议！

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🔧 技术支持

如果在使用过程中遇到问题：
1. 查看 [常见问题](#常见问题) 部分
2. 检查控制台错误信息
3. 提交 Issue 描述问题
4. 联系技术支持团队

---

**© 2025 视频标注应用 - 让视频标注更简单、更高效！**

<p align="center">
  Made with ❤️ by the Video Annotation Team
</p>