# -*- coding: utf-8 -*-
import streamlit as st
import os
from modules.data_storage import get_annotation_path

def is_annotation_complete(annotation_path):
    """检查txt标注文件是否包含有效内容"""
    if not os.path.exists(annotation_path):
        return False
    
    try:
        with open(annotation_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            # 检查是否有基本的标注内容
            if len(content) < 50:  # 太短可能只是模板
                return False
            # 检查是否包含至少一个填写的字段
            lines = content.split('\n')
            for line in lines:
                if ':' in line and line.split(':', 1)[1].strip():
                    return True
        return False
    except:
        return False

def display_progress(project_structure, project_path):
    """
    Calculates and displays the annotation progress.
    """
    if not project_structure:
        return

    total_videos = sum(len(videos) for videos in project_structure.values())
    annotated_videos = 0
    
    for folder, videos in project_structure.items():
        for video_file in videos:
            video_path = os.path.join(project_path, folder, video_file)
            annotation_path = get_annotation_path(video_path)
            if is_annotation_complete(annotation_path):
                annotated_videos += 1

    if total_videos > 0:
        progress_percentage = annotated_videos / total_videos
        st.sidebar.progress(progress_percentage)
        st.sidebar.caption(f"已完成: {annotated_videos} / {total_videos} 个视频")
    else:
        st.sidebar.caption("未找到视频文件。")

    # Detailed progress per folder
    st.sidebar.subheader("各文件夹进度")
    for folder, videos in project_structure.items():
        folder_total = len(videos)
        folder_annotated = 0
        for video_file in videos:
            video_path = os.path.join(project_path, folder, video_file)
            annotation_path = get_annotation_path(video_path)
            if is_annotation_complete(annotation_path):
                folder_annotated += 1
        
        if folder_total > 0:
            st.sidebar.text(f"{folder}: {folder_annotated}/{folder_total}")
        else:
            st.sidebar.text(f"{folder}: 0/0")