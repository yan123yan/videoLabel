# -*- coding: utf-8 -*-
import streamlit as st
import os
from modules.file_manager import get_project_structure
from modules.video_player import display_video
from modules.annotation_form import display_annotation_form
from modules.data_storage import save_annotation, load_annotation
from modules.progress_manager import display_progress
from modules.history_manager import load_path_history, save_path_history, add_path_to_history, clear_path_history
from modules.favorites_manager import load_favorites, is_favorited
from modules.language_manager import init_language, get_text, display_language_selector_sidebar

def get_display_folder_name(folder_name):
    """获取文件夹的显示名称（处理根目录的翻译）"""
    if folder_name == "__ROOT__":
        return get_text("root_directory")
    return folder_name

def main():
    # 初始化语言设置（必须在set_page_config之前）
    init_language()
    
    st.set_page_config(layout="wide", page_title=get_text("app_title"), page_icon="🎬")

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
    if 'favorites' not in st.session_state:
        # 从本地文件加载收藏记录
        st.session_state.favorites = load_favorites()
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
        st.markdown(f"""
        <div class="main-header">
            <h1>{get_text("main_header")}</h1>
            <p>{get_text("main_subtitle")}</p>
        </div>
        """, unsafe_allow_html=True)

    # 侧边栏配置
    with st.sidebar:
        # 语言选择器放在最顶部
        display_language_selector_sidebar()
        st.divider()
        
        st.markdown(f"### {get_text('project_config')}")
        
        # 路径历史记录
        if st.session_state.path_history:
            st.markdown(f"#### {get_text('history_paths')}")
            selected_history = st.selectbox(
                get_text("select_history"),
                options=[""] + st.session_state.path_history,
                format_func=lambda x: get_text("please_select") if x == "" else os.path.basename(x) + " (" + x + ")"
            )
            
            if selected_history and selected_history != st.session_state.project_path:
                if st.button(get_text("load_selected_path"), key="load_history"):
                    if os.path.isdir(selected_history):
                        st.session_state.project_path = selected_history
                        st.session_state.project_structure = get_project_structure(selected_history)
                        st.session_state.show_header = False  # 隐藏主标题
                        st.success(get_text("history_path_loaded"))
                        st.rerun()
                    else:
                        st.error(get_text("history_path_not_exist"))
            
            # 清空历史记录按钮
            if st.button(get_text("clear_history"), key="clear_history"):
                if clear_path_history():
                    st.session_state.path_history = []
                    st.success(get_text("history_cleared"))
                    st.rerun()
                else:
                    st.error(get_text("clear_history_failed"))
        
        st.markdown(f"#### {get_text('new_path')}")
        project_path_input = st.text_input(
            get_text("input_video_folder"),
            st.session_state.project_path or "",
            placeholder=get_text("path_placeholder")
        )

        col1, col2 = st.columns(2)
        with col1:
            if st.button(get_text("confirm_path"), type="primary", use_container_width=True):
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
                    
                    st.success(get_text("project_loaded"))
                    st.rerun()
                else:
                    st.error(get_text("path_not_exist"))

        with col2:
            if st.button(get_text("reset"), use_container_width=True):
                st.session_state.project_path = None
                st.session_state.project_structure = None
                st.session_state.current_video = None
                st.session_state.annotations = {}
                st.session_state.show_header = True  # 重置时恢复显示主标题
                st.rerun()

        # 显示当前路径状态
        if st.session_state.project_path:
            st.markdown(get_text("project_status"))
            st.markdown(f"""
            <div class="status-success">
                <strong>{get_text('current_path')}</strong><br>
                <div class="path-display">{st.session_state.project_path}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.session_state.project_structure:
                display_progress(st.session_state.project_structure, st.session_state.project_path)
        else:
            st.markdown(f"""
            <div class="status-info">
                <strong>{get_text('prompt_tips')}</strong><br>
                {get_text('prompt_input_path')}
            </div>
            """, unsafe_allow_html=True)

    if st.session_state.project_path:
        # Main content area
        col1, col2 = st.columns([3, 2])

        with col1:
            st.header(get_text("video_player"))
            # Video player will be displayed here
            if st.session_state.current_video:
                display_video(st.session_state.current_video)
            else:
                st.info(get_text("select_video_prompt"))

        with col2:
            st.header(get_text("annotation_area"))
            # Annotation form will be displayed here
            if st.session_state.project_structure:
                # 显示项目结构调试信息
                if st.checkbox(get_text("show_debug_info"), key="debug_info"):
                    st.write(get_text("project_structure"), st.session_state.project_structure)
                    st.write(get_text("project_path_label"), st.session_state.project_path)
                
                # 检查是否有视频文件
                if not st.session_state.project_structure:
                    st.warning(get_text("no_video_found"))
                    st.info(get_text("supported_formats"))
                else:
                    # Logic to select a video
                    folder_list = list(st.session_state.project_structure.keys())
                    if folder_list:
                        folder = st.selectbox(
                            get_text("select_folder"),
                            options=[""] + folder_list,
                            format_func=lambda x: get_text("please_select_folder") if x == "" else f"{get_display_folder_name(x)} ({len(st.session_state.project_structure[x])} {get_text('videos_count')})" if x else ""
                        )
                        
                        if folder and folder in st.session_state.project_structure:
                            video_list = st.session_state.project_structure[folder]
                            if video_list:
                                # 为视频文件添加收藏状态显示
                                def format_video_name(video_name):
                                    if video_name == "":
                                        return get_text("please_select_video")
                                    
                                    # 构建完整的视频路径用于检查收藏状态
                                    if folder == "__ROOT__":
                                        video_path = os.path.join(st.session_state.project_path, video_name)
                                    else:
                                        video_path = os.path.join(st.session_state.project_path, folder, video_name)
                                    
                                    # 检查是否已收藏
                                    if is_favorited(video_path, st.session_state.favorites):
                                        return f"⭐ {video_name}"
                                    else:
                                        return video_name
                                
                                video_file = st.selectbox(
                                    get_text("select_video"),
                                    options=[""] + video_list,
                                    format_func=format_video_name
                                )
                                
                                if video_file and video_file != "":
                                    # 构建视频路径
                                    if folder == "__ROOT__":
                                        video_path = os.path.join(st.session_state.project_path, video_file)
                                    else:
                                        video_path = os.path.join(st.session_state.project_path, folder, video_file)
                                    
                                    # 验证文件是否存在
                                    if os.path.exists(video_path):
                                        # 只有当选择的视频与当前视频不同时才更新和重新运行
                                        if st.session_state.current_video != video_path:
                                            st.session_state.current_video = video_path
                                            st.success(f"{get_text('video_selected')} {video_file}")
                                            
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
                                        st.error(f"{get_text('video_not_exist')} {video_path}")
                            else:
                                st.warning(f"{get_text('no_video_in_folder').format(folder=folder)}")
                    else:
                        st.warning(get_text("no_folder_found"))
            else:
                st.info(get_text("data_loaded_prompt"))


if __name__ == "__main__":
    main()