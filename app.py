# -*- coding: utf-8 -*-
import streamlit as st
import os
from modules.file_manager import get_project_structure
from modules.video_player import display_video
from modules.annotation_form import display_annotation_form
from modules.data_storage import save_annotation, load_annotation
from modules.progress_manager import display_progress

def main():
    st.set_page_config(layout="wide", page_title="视频标注工具", page_icon="🎬")

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

    # 主标题
    st.markdown("""
    <div class="main-header">
        <h1>🎬 视频标注应用</h1>
        <p>智能化视频标注与分析工具</p>
    </div>
    """, unsafe_allow_html=True)

    # 初始化session state
    if 'project_path' not in st.session_state:
        st.session_state.project_path = None
    if 'project_structure' not in st.session_state:
        st.session_state.project_structure = None
    if 'current_video' not in st.session_state:
        st.session_state.current_video = None
    if 'annotations' not in st.session_state:
        st.session_state.annotations = {}
    if 'path_history' not in st.session_state:
        st.session_state.path_history = []

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
                        st.success("✅ 历史路径加载成功！")
                        st.rerun()
                    else:
                        st.error("❌ 历史路径不存在！")
        
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
                    
                    # 添加到历史记录
                    if project_path_input not in st.session_state.path_history:
                        st.session_state.path_history.insert(0, project_path_input)
                        # 只保留最近10个路径
                        st.session_state.path_history = st.session_state.path_history[:10]
                    
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
                st.rerun()

        # 显示当前路径状态
        if st.session_state.project_path:
            st.markdown("#### 📊 项目状态")
            st.markdown(f"""
            <div class="status-success">
                <strong>当前路径:</strong><br>
                {st.session_state.project_path}
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
                # Logic to select a video
                folder = st.selectbox("选择文件夹", list(st.session_state.project_structure.keys()))
                if folder:
                    video_file = st.selectbox("选择视频", st.session_state.project_structure[folder])
                    if video_file:
                        video_path = os.path.join(st.session_state.project_path, folder, video_file)
                        st.session_state.current_video = video_path
                        
                        # Load existing annotations
                        st.session_state.annotations = load_annotation(video_path)
                        
                        # Display annotation form and update session state
                        updated_annotations = display_annotation_form(st.session_state.annotations)
                        if updated_annotations:
                            st.session_state.annotations = updated_annotations
                            st.rerun()


if __name__ == "__main__":
    main()