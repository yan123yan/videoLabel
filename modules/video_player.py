# -*- coding: utf-8 -*-
import streamlit as st
import os
from modules.report_rating import display_report_rating
from modules.data_storage import load_annotation
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
        
        # 显示评分面板
        rating_result = display_report_rating(annotation_data)
        
        # 如果有评分结果返回，可以在这里处理
        if rating_result:
            # 未来可以在这里添加保存评分的逻辑
            pass
    else:
        st.error(get_text("video_not_exist"))