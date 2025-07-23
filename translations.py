# -*- coding: utf-8 -*-
"""
多语言翻译映射文件
支持简体中文和英文
"""

TRANSLATIONS = {
    # 页面标题和主要标题
    "app_title": {
        "zh": "视频标注工具",
        "en": "Video Annotation Tool"
    },
    "main_header": {
        "zh": "🎬 视频标注应用",
        "en": "🎬 Video Annotation Application"
    },
    "main_subtitle": {
        "zh": "智能化视频标注与分析工具",
        "en": "Intelligent Video Annotation and Analysis Tool"
    },
    
    # 侧边栏
    "project_config": {
        "zh": "📁 项目配置",
        "en": "📁 Project Configuration"
    },
    "history_paths": {
        "zh": "📋 历史路径",
        "en": "📋 History Paths"
    },
    "select_history": {
        "zh": "选择历史路径",
        "en": "Select History Path"
    },
    "please_select": {
        "zh": "请选择...",
        "en": "Please select..."
    },
    "load_selected_path": {
        "zh": "🔄 加载选中路径",
        "en": "🔄 Load Selected Path"
    },
    "clear_history": {
        "zh": "🗑️ 清空历史记录",
        "en": "🗑️ Clear History"
    },
    "new_path": {
        "zh": "🆕 新建路径",
        "en": "🆕 New Path"
    },
    "input_video_folder": {
        "zh": "输入视频文件夹路径",
        "en": "Input Video Folder Path"
    },
    "path_placeholder": {
        "zh": "例如: /path/to/your/video/folder",
        "en": "e.g.: /path/to/your/video/folder"
    },
    "confirm_path": {
        "zh": "✅ 确认路径",
        "en": "✅ Confirm Path"
    },
    "reset": {
        "zh": "🔄 重置",
        "en": "🔄 Reset"
    },
    "project_status": {
        "zh": "📊 项目状态",
        "en": "📊 Project Status"
    },
    "current_path": {
        "zh": "当前路径:",
        "en": "Current Path:"
    },
    "prompt_input_path": {
        "zh": "💡 提示: 请先输入视频文件夹路径以开始标注工作",
        "en": "💡 Tip: Please input video folder path to start annotation"
    },
    
    # 成功/错误消息
    "history_path_loaded": {
        "zh": "✅ 历史路径加载成功！",
        "en": "✅ History path loaded successfully!"
    },
    "history_path_not_exist": {
        "zh": "❌ 历史路径不存在！",
        "en": "❌ History path does not exist!"
    },
    "history_cleared": {
        "zh": "✅ 历史记录已清空！",
        "en": "✅ History cleared!"
    },
    "clear_history_failed": {
        "zh": "❌ 清空历史记录失败！",
        "en": "❌ Failed to clear history!"
    },
    "project_loaded": {
        "zh": "✅ 项目加载成功！",
        "en": "✅ Project loaded successfully!"
    },
    "path_not_exist": {
        "zh": "❌ 路径不存在，请检查！",
        "en": "❌ Path does not exist, please check!"
    },
    
    # 主界面
    "video_player": {
        "zh": "视频播放器",
        "en": "Video Player"
    },
    "annotation_area": {
        "zh": "标注区域",
        "en": "Annotation Area"
    },
    "select_video_prompt": {
        "zh": "请在右侧选择一个视频进行标注。",
        "en": "Please select a video on the right for annotation."
    },
    "show_debug_info": {
        "zh": "显示调试信息",
        "en": "Show Debug Info"
    },
    "project_structure": {
        "zh": "项目结构:",
        "en": "Project Structure:"
    },
    "project_path_label": {
        "zh": "项目路径:",
        "en": "Project Path:"
    },
    "no_video_found": {
        "zh": "⚠️ 在指定路径中未找到任何视频文件",
        "en": "⚠️ No video files found in the specified path"
    },
    "supported_formats": {
        "zh": "支持的视频格式: .mp4, .avi, .mov, .mkv, .wmv, .flv, .webm, .m4v",
        "en": "Supported formats: .mp4, .avi, .mov, .mkv, .wmv, .flv, .webm, .m4v"
    },
    "select_folder": {
        "zh": "选择文件夹",
        "en": "Select Folder"
    },
    "please_select_folder": {
        "zh": "请选择文件夹...",
        "en": "Please select folder..."
    },
    "videos_count": {
        "zh": "个视频",
        "en": "videos"
    },
    "select_video": {
        "zh": "选择视频",
        "en": "Select Video"
    },
    "please_select_video": {
        "zh": "请选择视频...",
        "en": "Please select video..."
    },
    "video_selected": {
        "zh": "✅ 已选择视频:",
        "en": "✅ Video selected:"
    },
    "video_not_exist": {
        "zh": "❌ 视频文件不存在:",
        "en": "❌ Video file does not exist:"
    },
    "no_video_in_folder": {
        "zh": "⚠️ 文件夹 '{folder}' 中没有视频文件",
        "en": "⚠️ No video files in folder '{folder}'"
    },
    "no_folder_found": {
        "zh": "⚠️ 没有找到包含视频文件的文件夹",
        "en": "⚠️ No folder containing video files found"
    },
    "data_loaded_prompt": {
        "zh": "📋 数据加载成功后，请在此处选择视频进行标注",
        "en": "📋 After data loaded, please select video here for annotation"
    },
    
    # 视频播放器
    "playing": {
        "zh": "正在播放:",
        "en": "Now playing:"
    },
    "video_not_exist": {
        "zh": "视频文件不存在！",
        "en": "Video file does not exist!"
    },
    
    # Co-driving Report Rating面板
    "co_driving_report_rating": {
        "zh": "Co-driving Report Rating",
        "en": "Co-driving Report Rating"
    },
    "report_label": {
        "zh": "报告:",
        "en": "Report:"
    },
    "rating_criteria": {
        "zh": "评分标准",
        "en": "Rating Criteria"
    },
    "factuality": {
        "zh": "事实性",
        "en": "Factuality"
    },
    "factuality_help": {
        "zh": "评价报告的事实准确性",
        "en": "Rate the factual accuracy of the report"
    },
    "relevance": {
        "zh": "相关性",
        "en": "Relevance"
    },
    "relevance_help": {
        "zh": "评价报告内容的相关性",
        "en": "Rate the relevance of the report content"
    },
    "coherence": {
        "zh": "连贯性",
        "en": "Coherence"
    },
    "coherence_help": {
        "zh": "评价逻辑流程和连贯性",
        "en": "Rate the logical flow and coherence"
    },
    "usefulness": {
        "zh": "实用性",
        "en": "Usefulness"
    },
    "usefulness_help": {
        "zh": "评价实际用途",
        "en": "Rate the practical usefulness"
    },
    "save_rating": {
        "zh": "保存评分",
        "en": "Save Rating"
    },
    "rating_saved": {
        "zh": "评分保存成功！（功能待实现）",
        "en": "Rating saved successfully! (Function to be implemented)"
    },
    "no_report_data": {
        "zh": "无报告数据。请先完成标注。",
        "en": "No report data available. Please complete the annotation first."
    },
    
    # 报告内容标签
    "scene_description": {
        "zh": "场景描述",
        "en": "Scene Description"
    },
    "drivers_attention": {
        "zh": "驾驶员注意力",
        "en": "Driver's Attention"
    },
    "human_machine_interaction": {
        "zh": "人机交互",
        "en": "Human-Machine Interaction"
    },
    "evaluation_suggestions": {
        "zh": "评估与建议",
        "en": "Evaluation & Suggestions"
    },
    "recommended_actions": {
        "zh": "推荐行动",
        "en": "Recommended Actions"
    },
    
    # 语言选择
    "language": {
        "zh": "语言",
        "en": "Language"
    },
    "chinese": {
        "zh": "简体中文",
        "en": "简体中文"
    },
    "english": {
        "zh": "English",
        "en": "English"
    },
    
    # 根目录
    "root_directory": {
        "zh": "根目录",
        "en": "Root Directory"
    },
    
    # 状态相关
    "prompt_tips": {
        "zh": "💡 提示:",
        "en": "💡 Tips:"
    },
    
    # 收藏相关
    "unfavorite": {
        "zh": "❤️ 取消收藏",
        "en": "❤️ Unfavorite"
    },
    "unfavorite_help": {
        "zh": "点击取消收藏此视频",
        "en": "Click to unfavorite this video"
    },
    "unfavorited_success": {
        "zh": "已取消收藏！",
        "en": "Unfavorited!"
    },
    "unfavorite_failed": {
        "zh": "取消收藏失败！",
        "en": "Failed to unfavorite!"
    },
    "favorite": {
        "zh": "🤍 收藏",
        "en": "🤍 Favorite"
    },
    "favorite_help": {
        "zh": "点击收藏此视频",
        "en": "Click to favorite this video"
    },
    "favorited_success": {
        "zh": "收藏成功！",
        "en": "Favorited!"
    },
    "favorite_failed": {
        "zh": "收藏失败！",
        "en": "Failed to favorite!"
    },
    "favorited_status": {
        "zh": "**❤️ 已收藏**",
        "en": "**❤️ Favorited**"
    },
    "unfavorited_status": {
        "zh": "**🤍 未收藏**",
        "en": "**🤍 Not Favorited**"
    },
    
    # 标注表单相关
    "required_fields": {
        "zh": "必须标注项",
        "en": "Required Fields"
    },
    "autonomous_mode": {
        "zh": "自动驾驶模式 (autonomous_mode)",
        "en": "Autonomous Mode"
    },
    "autonomous_mode_help": {
        "zh": "0: 关闭, 1: 开启, 01: 先关后开, 10: 先开后关",
        "en": "0: Off, 1: On, 01: Off then On, 10: On then Off"
    },
    "driving_control_style": {
        "zh": "驾驶操控风格 (driving_control_style)",
        "en": "Driving Control Style"
    },
    "visual_attention_style": {
        "zh": "视觉注意风格 (visual_attention_style)",
        "en": "Visual Attention Style"
    },
    "integrated_style": {
        "zh": "综合风格 (integrated_style)",
        "en": "Integrated Style"
    },
    "suggestion": {
        "zh": "建议 (suggestion)",
        "en": "Suggestion"
    },
    "optional_descriptions": {
        "zh": "详细描述 (可选, 每文件夹至少5个)",
        "en": "Detailed Descriptions (Optional, at least 5 per folder)"
    },
    "scene_description_field": {
        "zh": "场景描述 (SceneDescription)",
        "en": "Scene Description"
    },
    "drivers_attention_field": {
        "zh": "驾驶员注意力 (Driver'sAttention)",
        "en": "Driver's Attention"
    },
    "human_machine_interaction_field": {
        "zh": "人机交互 (Human-MachineInteraction)",
        "en": "Human-Machine Interaction"
    },
    "evaluation_suggestions_field": {
        "zh": "评估与建议 (Evaluation&Suggestions)",
        "en": "Evaluation & Suggestions"
    },
    "annotation_saved": {
        "zh": "标注已自动保存！",
        "en": "Annotation saved automatically!"
    },
    "save_failed": {
        "zh": "自动保存失败！",
        "en": "Auto-save failed!"
    },
    
    # 进度管理相关
    "overall_progress": {
        "zh": "#### 📈 总体进度",
        "en": "#### 📈 Overall Progress"
    },
    "completed": {
        "zh": "已完成",
        "en": "Completed"
    },
    "in_progress": {
        "zh": "进行中",
        "en": "In Progress"
    },
    "pending": {
        "zh": "待完成",
        "en": "Pending"
    },
    "progress_info": {
        "zh": "已完成: {annotated_videos} / {total_videos} 个视频",
        "en": "Completed: {annotated_videos} / {total_videos} videos"
    },
    "completion_rate": {
        "zh": "完成率:",
        "en": "Completion Rate:"
    },
    "warning": {
        "zh": "⚠️ 提示",
        "en": "⚠️ Notice"
    },
    "no_video_files": {
        "zh": "未找到视频文件",
        "en": "No video files found"
    },
    "folder_details": {
        "zh": "#### 📂 文件夹详情",
        "en": "#### 📂 Folder Details"
    },
    "no_videos": {
        "zh": "(无视频)",
        "en": "(No videos)"
    },
    
    # 文件管理相关
    "scan_error": {
        "zh": "扫描项目路径时出错: {e}",
        "en": "Error scanning project path: {e}"
    }
}