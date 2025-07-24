# -*- coding: utf-8 -*-
"""
语言管理模块
处理多语言切换和文本获取
"""
import streamlit as st
from translations import TRANSLATIONS

def init_language():
    """初始化语言设置"""
    if 'language' not in st.session_state:
        st.session_state.language = 'zh'  # 默认中文

def get_text(key):
    """
    获取当前语言的文本
    :param key: 翻译键值
    :return: 对应语言的文本
    """
    # 确保语言已初始化
    if 'language' not in st.session_state:
        init_language()
    
    current_lang = st.session_state.language
    
    # 获取翻译
    if key in TRANSLATIONS:
        translation = TRANSLATIONS[key]
        if isinstance(translation, dict) and current_lang in translation:
            return translation[current_lang]
        else:
            # 如果找不到对应语言，返回中文或键值
            return translation.get('zh', key)
    else:
        # 如果键值不存在，返回键值本身
        return key

def display_language_selector_sidebar():
    """在侧边栏显示语言选择器"""
    # 获取当前语言
    current_lang = st.session_state.get('language', 'zh')
    
    # 语言选项
    languages = {
        'zh': '🇨🇳 简体中文',
        'en': '🇬🇧 English'
    }
    
    # 在侧边栏创建语言选择
    selected_lang = st.sidebar.selectbox(
        "🌐 " + get_text("language"),
        options=list(languages.keys()),
        format_func=lambda x: languages[x],
        index=0 if current_lang == 'zh' else 1,
        key="language_selector"
    )
    
    # 如果语言改变，更新并重新运行
    if selected_lang != current_lang:
        st.session_state.language = selected_lang
        # 清除当前视频和标注数据，确保重新选择
        if 'current_video' in st.session_state:
            st.session_state.current_video = None
        if 'annotations' in st.session_state:
            st.session_state.annotations = {}
        st.rerun()

def get_language_full_name():
    """获取当前语言的完整名称"""
    current_lang = st.session_state.get('language', 'zh')
    if current_lang == 'zh':
        return get_text('chinese')
    else:
        return get_text('english')