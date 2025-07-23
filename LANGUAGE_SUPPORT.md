# 多语言支持说明

## 概述
本项目已实现完整的中英文切换功能。语言选择器位于左侧边栏顶部。

## 实现细节

### 1. 语言管理系统
- **translations.py**: 包含所有UI文本的中英文翻译映射
- **word_bank_translations.py**: 包含标注选项值的翻译映射
- **language_manager.py**: 提供语言切换和文本获取功能

### 2. 关键改进

#### 语言选择器位置
- 已从主页面移至左侧边栏顶部
- 使用下拉框形式，显示国旗和语言名称

#### 根目录处理
- 内部使用固定标识符 `__ROOT__` 代替翻译文本
- 避免语言切换时路径匹配失败
- 仅在显示时翻译为对应语言

#### 选项值处理
- 标注选项在不同语言间正确映射
- 保存时转换为原始中文值
- 加载时转换为当前语言显示

### 3. 使用方法

#### 添加新的翻译文本
在 `translations.py` 中添加新的键值对：
```python
"new_key": {
    "zh": "中文文本",
    "en": "English Text"
}
```

#### 在代码中使用翻译
```python
from modules.language_manager import get_text
st.write(get_text("new_key"))
```

#### 添加新的选项值翻译
在 `word_bank_translations.py` 中添加：
```python
"新选项": {
    "zh": "新选项",
    "en": "New Option"
}
```

### 4. 注意事项
- 不要直接修改 `word_bank.py` 中的值，它们作为内部标识符使用
- 所有面向用户的文本都应通过 `get_text()` 获取
- HTML模板字符串必须使用 f-string 格式化
- 文件夹名称在内部保持不变，仅在显示时翻译

### 5. 已完成的模块
- ✅ app.py - 主应用界面
- ✅ modules/annotation_form.py - 标注表单
- ✅ modules/progress_manager.py - 进度管理
- ✅ modules/file_manager.py - 文件管理
- ✅ modules/video_player.py - 视频播放器
- ✅ modules/language_manager.py - 语言管理器

### 6. 测试建议
1. 切换语言后检查所有界面文本是否正确显示
2. 确认标注数据在不同语言间能正确保存和加载
3. 验证文件夹路径在语言切换后仍能正常工作
4. 检查进度统计是否正确显示