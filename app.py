# -*- coding: utf-8 -*-
import streamlit as st
import os
from modules.file_manager import get_project_structure
from modules.video_player import display_video
from modules.annotation_form import display_annotation_form
from modules.data_storage import save_annotation, load_annotation
from modules.progress_manager import display_progress
from modules.history_manager import load_path_history, save_path_history, add_path_to_history, clear_path_history

def main():
    st.set_page_config(layout="wide", page_title="视频标注工具", page_icon="🎬")

    # 初始化session state（必须在任何使用之前）
    if 'project_path' not in st.session_state:
        st.session_state.project_path = None
    if 'project_structure' not in st.session_state:
        st.session_state.project_structure = None
    if 'current_video' not in st.session_state:
        st.session_state.current_video = None
    if 'annotations' not in st.session_state:
        st.session_state.annotations = {}
    if 'path_history' not in st.session_state:
        # 从本地文件加载历史记录
        st.session_state.path_history = load_path_history()
    if 'show_header' not in st.session_state:
        # 控制是否显示主标题，路径加载成功后隐藏
        st.session_state.show_header = True

    # 自定义CSS样式
    st.markdown("""
    <style>
    .sidebar .sidebar-content {
        width: 400px;
    }
    
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .status-success {
        padding: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        color: #155724;
        margin: 0.5rem 0;
    }
    
    .status-info {
        padding: 0.5rem;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        color: #0c5460;
        margin: 0.5rem 0;
    }
    
    .video-container {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    .annotation-container {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
    }
    
    div[data-testid="stSidebar"] > div:first-child {
        width: 400px;
    }
    
    div[data-testid="stSidebar"] > div:first-child {
        margin-left: -400px;
    }
    
    .sidebar-content {
        padding: 1rem;
    }
    
    /* 路径输入框和显示的样式 */
    .stTextInput input {
        word-wrap: break-word !important;
        word-break: break-all !important;
        white-space: normal !important;
    }
    
    .path-display {
        word-wrap: break-word;
        word-break: break-all;
        white-space: normal;
        max-width: 100%;
        overflow-wrap: break-word;
    }
    
    /* 历史记录样式 */
    .history-item {
        padding: 0.3rem 0.5rem;
        margin: 0.2rem 0;
        background-color: #f1f3f4;
        border-radius: 5px;
        cursor: pointer;
        font-size: 0.85rem;
    }
    
    .history-item:hover {
        background-color: #e8eaed;
    }
    </style>
    """, unsafe_allow_html=True)

    # 主标题（仅在未加载路径时显示）
    if st.session_state.show_header:
        st.markdown("""
        <div class="main-header">
            <h1>🎬 视频标注应用</h1>
            <p>智能化视频标注与分析工具</p>
        </div>
        """, unsafe_allow_html=True)

    # 侧边栏配置
    with st.sidebar:
        st.markdown("### 📁 项目配置")
        
        # 路径历史记录
        if st.session_state.path_history:
            st.markdown("#### 📋 历史路径")
            selected_history = st.selectbox(
                "选择历史路径",
                options=[""] + st.session_state.path_history,
                format_func=lambda x: "请选择..." if x == "" else os.path.basename(x) + " (" + x + ")"
            )
            
            if selected_history and selected_history != st.session_state.project_path:
                if st.button("🔄 加载选中路径", key="load_history"):
                    if os.path.isdir(selected_history):
                        st.session_state.project_path = selected_history
                        st.session_state.project_structure = get_project_structure(selected_history)
                        st.session_state.show_header = False  # 隐藏主标题
                        st.success("✅ 历史路径加载成功！")
                        st.rerun()
                    else:
                        st.error("❌ 历史路径不存在！")
            
            # 清空历史记录按钮
            if st.button("🗑️ 清空历史记录", key="clear_history"):
                if clear_path_history():
                    st.session_state.path_history = []
                    st.success("✅ 历史记录已清空！")
                    st.rerun()
                else:
                    st.error("❌ 清空历史记录失败！")
        
        st.markdown("#### 🆕 新建路径")
        project_path_input = st.text_input(
            "输入视频文件夹路径",
            st.session_state.project_path or "",
            placeholder="例如: /path/to/your/video/folder"
        )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ 确认路径", type="primary", use_container_width=True):
                if os.path.isdir(project_path_input):
                    st.session_state.project_path = project_path_input
                    st.session_state.project_structure = get_project_structure(project_path_input)
                    st.session_state.show_header = False  # 隐藏主标题
                    
                    # 添加到历史记录并保存到本地
                    st.session_state.path_history = add_path_to_history(
                        project_path_input,
                        st.session_state.path_history
                    )
                    save_path_history(st.session_state.path_history)
                    
                    st.success("✅ 项目加载成功！")
                    st.rerun()
                else:
                    st.error("❌ 路径不存在，请检查！")

        with col2:
            if st.button("🔄 重置", use_container_width=True):
                st.session_state.project_path = None
                st.session_state.project_structure = None
                st.session_state.current_video = None
                st.session_state.annotations = {}
                st.session_state.show_header = True  # 重置时恢复显示主标题
                st.rerun()

        # 显示当前路径状态
        if st.session_state.project_path:
            st.markdown("#### 📊 项目状态")
            st.markdown(f"""
            <div class="status-success">
                <strong>当前路径:</strong><br>
                <div class="path-display">{st.session_state.project_path}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.session_state.project_structure:
                display_progress(st.session_state.project_structure, st.session_state.project_path)
        else:
            st.markdown("""
            <div class="status-info">
                <strong>💡 提示:</strong><br>
                请先输入视频文件夹路径以开始标注工作
            </div>
            """, unsafe_allow_html=True)

    if st.session_state.project_path:
        # Main content area
        col1, col2 = st.columns([3, 2])

        with col1:
            st.header("视频播放器")
            # Video player will be displayed here
            if st.session_state.current_video:
                display_video(st.session_state.current_video)
            else:
                st.info("请在右侧选择一个视频进行标注。")

        with col2:
            st.header("标注区域")
            # Annotation form will be displayed here
            if st.session_state.project_structure:
                # 显示项目结构调试信息
                if st.checkbox("显示调试信息", key="debug_info"):
                    st.write("项目结构:", st.session_state.project_structure)
                    st.write("项目路径:", st.session_state.project_path)
                
                # 检查是否有视频文件
                if not st.session_state.project_structure:
                    st.warning("⚠️ 在指定路径中未找到任何视频文件")
                    st.info("支持的视频格式: .mp4, .avi, .mov, .mkv, .wmv, .flv, .webm, .m4v")
                else:
                    # Logic to select a video
                    folder_list = list(st.session_state.project_structure.keys())
                    if folder_list:
                        folder = st.selectbox(
                            "选择文件夹",
                            options=[""] + folder_list,
                            format_func=lambda x: "请选择文件夹..." if x == "" else f"{x} ({len(st.session_state.project_structure[x])} 个视频)" if x else ""
                        )
                        
                        if folder and folder in st.session_state.project_structure:
                            video_list = st.session_state.project_structure[folder]
                            if video_list:
                                video_file = st.selectbox(
                                    "选择视频",
                                    options=[""] + video_list,
                                    format_func=lambda x: "请选择视频..." if x == "" else x
                                )
                                
                                if video_file and video_file != "":
                                    # 构建视频路径
                                    if folder == "根目录":
                                        video_path = os.path.join(st.session_state.project_path, video_file)
                                    else:
                                        video_path = os.path.join(st.session_state.project_path, folder, video_file)
                                    
                                    # 验证文件是否存在
                                    if os.path.exists(video_path):
                                        # 只有当选择的视频与当前视频不同时才更新和重新运行
                                        if st.session_state.current_video != video_path:
                                            st.session_state.current_video = video_path
                                            st.success(f"✅ 已选择视频: {video_file}")
                                            
                                            # Load existing annotations
                                            st.session_state.annotations = load_annotation(video_path)
                                            
                                            # 选择新视频后立即重新运行页面以显示视频播放器
                                            st.rerun()
                                        else:
                                            # 如果是同一个视频，仍然显示标注表单
                                            updated_annotations = display_annotation_form(st.session_state.annotations)
                                            if updated_annotations:
                                                st.session_state.annotations = updated_annotations
                                                st.rerun()
                                    else:
                                        st.error(f"❌ 视频文件不存在: {video_path}")
                            else:
                                st.warning(f"⚠️ 文件夹 '{folder}' 中没有视频文件")
                    else:
                        st.warning("⚠️ 没有找到包含视频文件的文件夹")
            else:
                st.info("📋 数据加载成功后，请在此处选择视频进行标注")


if __name__ == "__main__":
    main()