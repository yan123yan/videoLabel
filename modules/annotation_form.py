# -*- coding: utf-8 -*-
import streamlit as st
from config.word_bank import DRIVING_CONTROL_STYLE, VISUAL_ATTENTION_STYLE, INTEGRATED_STYLE, SUGGESTION
from modules.data_storage import save_annotation
from modules.favorites_manager import add_to_favorites, remove_from_favorites, is_favorited, save_favorites

def display_annotation_form(annotations):
    """Displays the annotation form and handles user input."""
    
    # 收藏功能区域
    current_video = st.session_state.get('current_video')
    if current_video:
        favorites = st.session_state.get('favorites', set())
        is_fav = is_favorited(current_video, favorites)
        
        # 创建收藏按钮的网格布局，确保按钮和状态在同一水平线上
        # 调整列比例，给收藏按钮更多空间，确保"取消收藏"文字有足够宽度
        col1, col2 = st.columns([5, 2])
        with col1:
            if is_fav:
                if st.button("❤️ 取消收藏", key="unfavorite_btn", help="点击取消收藏此视频", use_container_width=True):
                    new_favorites = remove_from_favorites(current_video, favorites)
                    st.session_state.favorites = new_favorites
                    if save_favorites(new_favorites):
                        st.toast("已取消收藏！", icon="💔")
                        st.rerun()
                    else:
                        st.error("取消收藏失败！")
            else:
                if st.button("🤍 收藏", key="favorite_btn", help="点击收藏此视频", use_container_width=True):
                    new_favorites = add_to_favorites(current_video, favorites)
                    st.session_state.favorites = new_favorites
                    if save_favorites(new_favorites):
                        st.toast("收藏成功！", icon="❤️")
                        st.rerun()
                    else:
                        st.error("收藏失败！")
        
        with col2:
            # 使用容器确保垂直居中对齐，与按钮在同一水平线上
            status_container = st.container()
            with status_container:
                # 添加一些垂直间距，确保状态文字与按钮垂直居中对齐
                st.markdown("<div style='margin-top: 8px;'>", unsafe_allow_html=True)
                if is_fav:
                    st.markdown("**❤️ 已收藏**")
                else:
                    st.markdown("**🤍 未收藏**")
                st.markdown("</div>", unsafe_allow_html=True)
    
    st.divider()
    st.subheader("必须标注项")

    # --- Top half of the form (mandatory) ---
    autonomous_mode = st.text_input(
        "自动驾驶模式 (autonomous_mode)", 
        value=annotations.get('autonomous_mode', ''),
        help="0: 关闭, 1: 开启, 01: 先关后开, 10: 先开后关"
    )
    
    driving_control_style = st.multiselect(
        "驾驶操控风格 (driving_control_style)",
        options=DRIVING_CONTROL_STYLE,
        default=annotations.get('driving_control_style', []),
        max_selections=3
    )

    visual_attention_style = st.multiselect(
        "视觉注意风格 (visual_attention_style)",
        options=VISUAL_ATTENTION_STYLE,
        default=annotations.get('visual_attention_style', []),
        max_selections=3
    )

    integrated_style = st.multiselect(
        "综合风格 (integrated_style)",
        options=INTEGRATED_STYLE,
        default=annotations.get('integrated_style', []),
        max_selections=3
    )

    suggestion = st.multiselect(
        "建议 (suggestion)",
        options=SUGGESTION,
        default=annotations.get('suggestion', []),
        max_selections=3
    )

    st.divider()
    st.subheader("详细描述 (可选, 每文件夹至少5个)")

    # --- Bottom half of the form (optional) ---
    scene_description = st.text_area(
        "场景描述 (SceneDescription)",
        value=annotations.get('scene_description', ''),
        height=100
    )

    drivers_attention = st.text_area(
        "驾驶员注意力 (Driver’sAttention)",
        value=annotations.get('drivers_attention', ''),
        height=100
    )

    human_machine_interaction = st.text_area(
        "人机交互 (Human-MachineInteraction)",
        value=annotations.get('human_machine_interaction', ''),
        height=100
    )

    evaluation_suggestions = st.text_area(
        "评估与建议 (Evaluation&Suggestions)",
        value=annotations.get('evaluation_suggestions', ''),
        height=100
    )

    # --- Real-time saving logic ---
    updated_annotations = {
        'autonomous_mode': autonomous_mode,
        'driving_control_style': driving_control_style,
        'visual_attention_style': visual_attention_style,
        'integrated_style': integrated_style,
        'suggestion': suggestion,
        'scene_description': scene_description,
        'drivers_attention': drivers_attention,
        'human_machine_interaction': human_machine_interaction,
        'evaluation_suggestions': evaluation_suggestions
    }

    # If any value has changed, save the annotations
    if updated_annotations != annotations:
        video_path = st.session_state.get('current_video')
        if video_path:
            if save_annotation(video_path, updated_annotations):
                st.toast("标注已自动保存！", icon="✅")
                # Return the updated annotations to the main app
                return updated_annotations
            else:
                st.error("自动保存失败！")
    
    return None