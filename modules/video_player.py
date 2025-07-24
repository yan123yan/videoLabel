# -*- coding: utf-8 -*-
import streamlit as st
import os
from modules.report_rating import display_report_rating
from modules.data_storage import load_annotation, load_json_annotation
from modules.language_manager import get_text

def display_video(video_path):
    """
    Displays the video player in the Streamlit app.
    Also shows the video timestamp and rating panel below.
    """
    if os.path.exists(video_path):
        # 视频播放器
        st.video(video_path)
        # Streamlit's st.video doesn't directly expose a timestamp.
        # This is a placeholder for where we might add more complex
        # timestamp handling if a suitable component is found.
        st.caption(f"{get_text('playing')} {os.path.basename(video_path)}")
        
        # 分隔线
        st.markdown("---")
        
        # 加载当前视频的标注数据
        annotation_data = load_annotation(video_path)
        
        # 加载已保存的JSON数据（如果存在）
        existing_json_data = load_json_annotation(video_path)
        existing_ratings = None
        
        # 如果JSON文件存在，提取评分数据
        if existing_json_data:
            existing_ratings = {
                'factuality': existing_json_data.get('factuality', ''),
                'relevance': existing_json_data.get('relevance', ''),
                'coherence': existing_json_data.get('coherence', ''),
                'usefulness': existing_json_data.get('usefulness', '')
            }
        
        # 显示评分面板，传递已存在的评分数据
        rating_result = display_report_rating(annotation_data, existing_ratings)
        
        # 如果有评分结果返回，可以在这里处理
        if rating_result:
            # 未来可以在这里添加保存评分的逻辑
            pass
    else:
        st.error(get_text("video_not_exist"))