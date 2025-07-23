# -*- coding: utf-8 -*-
import streamlit as st
from config.word_bank import DRIVING_CONTROL_STYLE, VISUAL_ATTENTION_STYLE, INTEGRATED_STYLE, SUGGESTION
from config.word_bank_translations import (
    get_translated_options,
    DRIVING_CONTROL_STYLE_TRANS,
    VISUAL_ATTENTION_STYLE_TRANS,
    INTEGRATED_STYLE_TRANS,
    SUGGESTION_TRANS
)
from modules.data_storage import save_annotation
from modules.favorites_manager import add_to_favorites, remove_from_favorites, is_favorited, save_favorites
from modules.language_manager import get_text

def get_original_values(selected_translated, option_list, translation_dict, language):
    """将翻译后的选项值转换回原始中文值以便保存"""
    if language == 'zh':
        return selected_translated
    
    # 创建反向映射
    reverse_map = {}
    for original in option_list:
        if original in translation_dict:
            translated = translation_dict[original].get(language, original)
            reverse_map[translated] = original
    
    # 转换选中的值
    return [reverse_map.get(val, val) for val in selected_translated]

def get_translated_values(selected_original, translation_dict, language):
    """将原始中文值转换为当前语言的翻译值以便显示"""
    if language == 'zh':
        return selected_original
    
    return [translation_dict.get(val, {}).get(language, val) for val in selected_original]

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
                if st.button(get_text("unfavorite"), key="unfavorite_btn", help=get_text("unfavorite_help"), use_container_width=True):
                    new_favorites = remove_from_favorites(current_video, favorites)
                    st.session_state.favorites = new_favorites
                    if save_favorites(new_favorites):
                        st.toast(get_text("unfavorited_success"), icon="💔")
                        st.rerun()
                    else:
                        st.error(get_text("unfavorite_failed"))
            else:
                if st.button(get_text("favorite"), key="favorite_btn", help=get_text("favorite_help"), use_container_width=True):
                    new_favorites = add_to_favorites(current_video, favorites)
                    st.session_state.favorites = new_favorites
                    if save_favorites(new_favorites):
                        st.toast(get_text("favorited_success"), icon="❤️")
                        st.rerun()
                    else:
                        st.error(get_text("favorite_failed"))
        
        with col2:
            # 使用容器确保垂直居中对齐，与按钮在同一水平线上
            status_container = st.container()
            with status_container:
                # 添加一些垂直间距，确保状态文字与按钮垂直居中对齐
                st.markdown("<div style='margin-top: 8px;'>", unsafe_allow_html=True)
                if is_fav:
                    st.markdown(get_text("favorited_status"))
                else:
                    st.markdown(get_text("unfavorited_status"))
                st.markdown("</div>", unsafe_allow_html=True)
    
    st.divider()
    st.subheader(get_text("required_fields"))

    # --- Top half of the form (mandatory) ---
    autonomous_mode = st.text_input(
        get_text("autonomous_mode"), 
        value=annotations.get('autonomous_mode', ''),
        help=get_text("autonomous_mode_help")
    )
    
    # Get current language
    current_lang = st.session_state.get('language', 'zh')
    
    # 获取已保存的原始值并转换为当前语言
    saved_driving_style = annotations.get('driving_control_style', [])
    default_driving_style = get_translated_values(saved_driving_style, DRIVING_CONTROL_STYLE_TRANS, current_lang)
    
    driving_control_style = st.multiselect(
        get_text("driving_control_style"),
        options=get_translated_options(DRIVING_CONTROL_STYLE, DRIVING_CONTROL_STYLE_TRANS, current_lang),
        default=default_driving_style,
        max_selections=3
    )

    # 获取已保存的原始值并转换为当前语言
    saved_visual_style = annotations.get('visual_attention_style', [])
    default_visual_style = get_translated_values(saved_visual_style, VISUAL_ATTENTION_STYLE_TRANS, current_lang)
    
    visual_attention_style = st.multiselect(
        get_text("visual_attention_style"),
        options=get_translated_options(VISUAL_ATTENTION_STYLE, VISUAL_ATTENTION_STYLE_TRANS, current_lang),
        default=default_visual_style,
        max_selections=3
    )

    # 获取已保存的原始值并转换为当前语言
    saved_integrated_style = annotations.get('integrated_style', [])
    default_integrated_style = get_translated_values(saved_integrated_style, INTEGRATED_STYLE_TRANS, current_lang)
    
    integrated_style = st.multiselect(
        get_text("integrated_style"),
        options=get_translated_options(INTEGRATED_STYLE, INTEGRATED_STYLE_TRANS, current_lang),
        default=default_integrated_style,
        max_selections=3
    )

    # 获取已保存的原始值并转换为当前语言
    saved_suggestion = annotations.get('suggestion', [])
    default_suggestion = get_translated_values(saved_suggestion, SUGGESTION_TRANS, current_lang)
    
    suggestion = st.multiselect(
        get_text("suggestion"),
        options=get_translated_options(SUGGESTION, SUGGESTION_TRANS, current_lang),
        default=default_suggestion,
        max_selections=3
    )

    st.divider()
    st.subheader(get_text("optional_descriptions"))

    # --- Bottom half of the form (optional) ---
    scene_description = st.text_area(
        get_text("scene_description_field"),
        value=annotations.get('scene_description', ''),
        height=100
    )

    drivers_attention = st.text_area(
        get_text("drivers_attention_field"),
        value=annotations.get('drivers_attention', ''),
        height=100
    )

    human_machine_interaction = st.text_area(
        get_text("human_machine_interaction_field"),
        value=annotations.get('human_machine_interaction', ''),
        height=100
    )

    evaluation_suggestions = st.text_area(
        get_text("evaluation_suggestions_field"),
        value=annotations.get('evaluation_suggestions', ''),
        height=100
    )

    # --- Real-time saving logic ---
    # 将翻译后的选项值转换回原始中文值以便保存
    updated_annotations = {
        'autonomous_mode': autonomous_mode,
        'driving_control_style': get_original_values(driving_control_style, DRIVING_CONTROL_STYLE, DRIVING_CONTROL_STYLE_TRANS, current_lang),
        'visual_attention_style': get_original_values(visual_attention_style, VISUAL_ATTENTION_STYLE, VISUAL_ATTENTION_STYLE_TRANS, current_lang),
        'integrated_style': get_original_values(integrated_style, INTEGRATED_STYLE, INTEGRATED_STYLE_TRANS, current_lang),
        'suggestion': get_original_values(suggestion, SUGGESTION, SUGGESTION_TRANS, current_lang),
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
                st.toast(get_text("annotation_saved"), icon="✅")
                # Return the updated annotations to the main app
                return updated_annotations
            else:
                st.error(get_text("save_failed"))
    
    return None