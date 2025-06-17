# -*- coding: utf-8 -*-
import streamlit as st
import os
from modules.file_manager import get_project_structure
from modules.video_player import display_video
from modules.annotation_form import display_annotation_form
from modules.data_storage import save_annotation, load_annotation
from modules.progress_manager import display_progress

def main():
    st.set_page_config(layout="wide", page_title="视频标注工具")

    st.title("视频标注应用")

    if 'project_path' not in st.session_state:
        st.session_state.project_path = None
    if 'project_structure' not in st.session_state:
        st.session_state.project_structure = None
    if 'current_video' not in st.session_state:
        st.session_state.current_video = None
    if 'annotations' not in st.session_state:
        st.session_state.annotations = {}

    # Sidebar for project configuration
    with st.sidebar:
        st.header("项目配置")
        project_path_input = st.text_input("输入视频文件夹路径", st.session_state.project_path or "")

        if st.button("确认路径"):
            if os.path.isdir(project_path_input):
                st.session_state.project_path = project_path_input
                st.session_state.project_structure = get_project_structure(project_path_input)
                st.success("项目加载成功！")
            else:
                st.error("路径不存在，请检查！")

        if st.button("重置"):
            st.session_state.project_path = None
            st.session_state.project_structure = None
            st.session_state.current_video = None
            st.session_state.annotations = {}
            st.rerun()

        if st.session_state.project_path and st.session_state.project_structure:
            display_progress(st.session_state.project_structure, st.session_state.project_path)

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