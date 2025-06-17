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
    计算并显示标注进度
    """
    if not project_structure:
        return

    total_videos = sum(len(videos) for videos in project_structure.values())
    annotated_videos = 0
    
    for folder, videos in project_structure.items():
        for video_file in videos:
            # 处理根目录的特殊情况
            if folder == "根目录":
                video_path = os.path.join(project_path, video_file)
            else:
                video_path = os.path.join(project_path, folder, video_file)
            annotation_path = get_annotation_path(video_path)
            if is_annotation_complete(annotation_path):
                annotated_videos += 1

    if total_videos > 0:
        progress_percentage = annotated_videos / total_videos
        
        # 总进度显示
        st.sidebar.markdown("#### 📈 总体进度")
        st.sidebar.progress(progress_percentage)
        
        # 进度状态显示
        if progress_percentage == 1.0:
            status_color = "#28a745"  # 绿色
            status_icon = "✅"
            status_text = "已完成"
        elif progress_percentage >= 0.5:
            status_color = "#ffc107"  # 黄色
            status_icon = "🟡"
            status_text = "进行中"
        else:
            status_color = "#dc3545"  # 红色
            status_icon = "🔴"
            status_text = "待完成"
        
        st.sidebar.markdown(f"""
        <div style="
            background-color: {status_color}15;
            border-left: 4px solid {status_color};
            padding: 0.5rem;
            border-radius: 3px;
            margin: 0.5rem 0;
        ">
            <strong>{status_icon} {status_text}</strong><br>
            已完成: {annotated_videos} / {total_videos} 个视频<br>
            完成率: {progress_percentage:.1%}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.sidebar.markdown("""
        <div style="
            background-color: #f8d7da;
            border-left: 4px solid #dc3545;
            padding: 0.5rem;
            border-radius: 3px;
            margin: 0.5rem 0;
        ">
            <strong>⚠️ 提示</strong><br>
            未找到视频文件
        </div>
        """, unsafe_allow_html=True)

    # 各文件夹详细进度
    if project_structure:
        st.sidebar.markdown("#### 📂 文件夹详情")
        for folder, videos in project_structure.items():
            folder_total = len(videos)
            folder_annotated = 0
            for video_file in videos:
                # 处理根目录的特殊情况
                if folder == "根目录":
                    video_path = os.path.join(project_path, video_file)
                else:
                    video_path = os.path.join(project_path, folder, video_file)
                annotation_path = get_annotation_path(video_path)
                if is_annotation_complete(annotation_path):
                    folder_annotated += 1
            
            if folder_total > 0:
                folder_progress = folder_annotated / folder_total
                
                # 文件夹进度条颜色
                if folder_progress == 1.0:
                    bar_color = "#28a745"
                elif folder_progress >= 0.5:
                    bar_color = "#ffc107"
                else:
                    bar_color = "#dc3545"
                
                st.sidebar.markdown(f"""
                <div style="
                    background-color: #f8f9fa;
                    padding: 0.4rem;
                    border-radius: 5px;
                    margin: 0.3rem 0;
                    border: 1px solid #e9ecef;
                ">
                    <strong>{folder}</strong><br>
                    <div style="
                        background-color: #e9ecef;
                        border-radius: 10px;
                        height: 6px;
                        margin: 0.2rem 0;
                    ">
                        <div style="
                            background-color: {bar_color};
                            width: {folder_progress:.1%};
                            height: 6px;
                            border-radius: 10px;
                        "></div>
                    </div>
                    <small>{folder_annotated}/{folder_total} ({folder_progress:.0%})</small>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.sidebar.markdown(f"""
                <div style="
                    background-color: #f8f9fa;
                    padding: 0.4rem;
                    border-radius: 5px;
                    margin: 0.3rem 0;
                    border: 1px solid #e9ecef;
                ">
                    <strong>{folder}</strong><br>
                    <small>0/0 (无视频)</small>
                </div>
                """, unsafe_allow_html=True)