# -*- coding: utf-8 -*-
import streamlit as st
from modules.data_storage import save_json_annotation, load_annotation, load_json_annotation
from modules.language_manager import get_text

def display_report_rating(annotation_data, existing_ratings=None):
    """
    显示Co-driving Report Rating面板
    包含标题、报告内容和四个评分下拉框
    """
    # 面板容器
    with st.container():
        # 标题
        st.markdown(f"### {get_text('co_driving_report_rating')}")
        
        # 报告输出框
        report_content = format_report_content(annotation_data)
        st.text_area(
            get_text("report") + ":",
            value=report_content,
            height=300,
            disabled=True,
            key="report_display"
        )
        
        # 评分下拉框容器
        st.markdown(f"#### {get_text('rating_criteria')}")
        
        # 使用列布局放置四个下拉框
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            # 从existing_ratings获取factuality的默认值
            factuality_default = existing_ratings.get('factuality', '') if existing_ratings else ''
            factuality_index = 0 if factuality_default == '' else ([""] + list(range(1, 6))).index(factuality_default)
            
            factuality_score = st.selectbox(
                get_text("factuality"),
                options=[""] + list(range(1, 6)),
                format_func=lambda x: get_text("please_select_rating") if x == "" else str(x),
                index=factuality_index,
                key="factuality_rating",
                help=get_text("factuality_help")
            )
        
        with col2:
            # 从existing_ratings获取relevance的默认值
            relevance_default = existing_ratings.get('relevance', '') if existing_ratings else ''
            relevance_index = 0 if relevance_default == '' else ([""] + list(range(1, 6))).index(relevance_default)
            
            relevance_score = st.selectbox(
                get_text("relevance"),
                options=[""] + list(range(1, 6)),
                format_func=lambda x: get_text("please_select_rating") if x == "" else str(x),
                index=relevance_index,
                key="relevance_rating",
                help=get_text("relevance_help")
            )
        
        with col3:
            # 从existing_ratings获取coherence的默认值
            coherence_default = existing_ratings.get('coherence', '') if existing_ratings else ''
            coherence_index = 0 if coherence_default == '' else ([""] + list(range(1, 6))).index(coherence_default)
            
            coherence_score = st.selectbox(
                get_text("coherence"),
                options=[""] + list(range(1, 6)),
                format_func=lambda x: get_text("please_select_rating") if x == "" else str(x),
                index=coherence_index,
                key="coherence_rating",
                help=get_text("coherence_help")
            )
        
        with col4:
            # 从existing_ratings获取usefulness的默认值
            usefulness_default = existing_ratings.get('usefulness', '') if existing_ratings else ''
            usefulness_index = 0 if usefulness_default == '' else ([""] + list(range(1, 6))).index(usefulness_default)
            
            usefulness_score = st.selectbox(
                get_text("usefulness"),
                options=[""] + list(range(1, 6)),
                format_func=lambda x: get_text("please_select_rating") if x == "" else str(x),
                index=usefulness_index,
                key="usefulness_rating",
                help=get_text("usefulness_help")
            )
        
        # Save按钮 - 使用列布局让按钮更宽
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(get_text("save_json"), type="primary", key="save_rating", use_container_width=True):
                # 验证所有评分字段是否都有值
                missing_fields = []
                
                if factuality_score == "":
                    missing_fields.append("Factuality")
                if relevance_score == "":
                    missing_fields.append("Relevance")
                if coherence_score == "":
                    missing_fields.append("Coherence")
                if usefulness_score == "":
                    missing_fields.append("Usefulness")
                
                # 验证必填的annotation字段
                required_annotation_fields = {
                    'autonomous_mode': 'Autonomous Mode',
                    'driving_control_style': 'Driving Control Style',
                    'visual_attention_style': 'Visual Attention Style',
                    'integrated_style': 'Integrated Style',
                    'suggestion': 'Suggestions'
                }
                
                for field_key, field_name in required_annotation_fields.items():
                    field_value = annotation_data.get(field_key)
                    if not field_value or (isinstance(field_value, list) and len(field_value) == 0):
                        missing_fields.append(field_name)
                
                # 如果有缺失字段，显示错误消息
                if missing_fields:
                    st.error(get_text("fill_fields_before_save").format(fields=', '.join(missing_fields)))
                else:
                    # 获取当前视频路径
                    video_path = st.session_state.get('current_video')
                    
                    if video_path:
                        # 从txt文件重新加载最新的annotation数据
                        latest_annotation_data = load_annotation(video_path)
                        
                        # 准备评分数据
                        rating_data = {
                            "factuality": factuality_score,
                            "relevance": relevance_score,
                            "coherence": coherence_score,
                            "usefulness": usefulness_score
                        }
                        
                        # 保存JSON文件
                        if save_json_annotation(video_path, latest_annotation_data, rating_data):
                            st.success(get_text("json_saved_success"))
                            return rating_data
                        else:
                            st.error(get_text("json_save_failed"))
                    else:
                        st.error(get_text("no_video_selected"))
    
    return None


def format_report_content(annotation_data):
    """
    格式化报告内容，从annotation_data中提取extracted sections信息
    以JSON格式显示
    """
    import json
    
    # 构建extracted_sections字典
    extracted_sections = {
        "scene_description": annotation_data.get('scene_description', ''),
        "driver_attention": annotation_data.get('drivers_attention', ''),
        "human_machine_interaction": annotation_data.get('human_machine_interaction', ''),
        "evaluation_suggestions": annotation_data.get('evaluation_suggestions', ''),
        "recommended_actions": annotation_data.get('suggestion', [])
    }
    
    # 创建包含extracted_sections的JSON对象
    json_output = {
        "extracted_sections": extracted_sections
    }
    
    # 如果没有任何数据，返回提示信息
    if all(not v for v in extracted_sections.values()):
        return "No report data available. Please complete the annotation first."
    
    # 返回格式化的JSON字符串
    return json.dumps(json_output, ensure_ascii=False, indent=2)