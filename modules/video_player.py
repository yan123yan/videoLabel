# -*- coding: utf-8 -*-
import streamlit as st
import os

def display_video(video_path):
    """
    Displays the video player in the Streamlit app.
    Also shows the video timestamp.
    """
    if os.path.exists(video_path):
        st.video(video_path)
        # Streamlit's st.video doesn't directly expose a timestamp.
        # This is a placeholder for where we might add more complex
        # timestamp handling if a suitable component is found.
        st.caption(f"正在播放: {os.path.basename(video_path)}")
    else:
        st.error("视频文件不存在！")