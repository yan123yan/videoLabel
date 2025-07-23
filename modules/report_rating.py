# -*- coding: utf-8 -*-
import streamlit as st

def display_report_rating(annotation_data):
    """
    显示Co-driving Report Rating面板
    包含标题、报告内容和四个评分下拉框
    """
    # 面板容器
    with st.container():
        # 标题
        st.markdown("### Co-driving Report Rating")
        
        # 报告输出框
        report_content = format_report_content(annotation_data)
        st.text_area(
            "Report:",
            value=report_content,
            height=300,
            disabled=True,
            key="report_display"
        )
        
        # 评分下拉框容器
        st.markdown("#### Rating Criteria")
        
        # 使用列布局放置四个下拉框
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            factuality_score = st.selectbox(
                "Factuality",
                options=[1, 2, 3, 4, 5],
                key="factuality_rating",
                help="Rate the factual accuracy of the report"
            )
        
        with col2:
            relevance_score = st.selectbox(
                "Relevance",
                options=[1, 2, 3, 4, 5],
                key="relevance_rating",
                help="Rate the relevance of the report content"
            )
        
        with col3:
            coherence_score = st.selectbox(
                "Coherence",
                options=[1, 2, 3, 4, 5],
                key="coherence_rating",
                help="Rate the logical flow and coherence"
            )
        
        with col4:
            usefulness_score = st.selectbox(
                "Usefulness",
                options=[1, 2, 3, 4, 5],
                key="usefulness_rating",
                help="Rate the practical usefulness"
            )
        
        # Save按钮 - 使用列布局让按钮更宽
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Save Rating", type="primary", key="save_rating", use_container_width=True):
                # 保存评分的逻辑将在后续添加
                st.success("Rating saved successfully! (Function to be implemented)")
                
                # 返回评分数据
                rating_data = {
                    "factuality": factuality_score,
                    "relevance": relevance_score,
                    "coherence": coherence_score,
                    "usefulness": usefulness_score
                }
                return rating_data
    
    return None


def format_report_content(annotation_data):
    """
    格式化报告内容，从annotation_data中提取extracted sections信息
    """
    sections = []
    
    # Scene Description
    scene_desc = annotation_data.get('scene_description', '')
    if scene_desc:
        sections.append(f"Scene Description: {scene_desc}")
    
    # Driver's Attention
    drivers_attention = annotation_data.get('drivers_attention', '')
    if drivers_attention:
        sections.append(f"\n\nDriver's Attention: {drivers_attention}")
    
    # Human-Machine Interaction
    human_machine = annotation_data.get('human_machine_interaction', '')
    if human_machine:
        sections.append(f"\n\nHuman-Machine Interaction: {human_machine}")
    
    # Evaluation & Suggestions
    eval_suggestions = annotation_data.get('evaluation_suggestions', '')
    if eval_suggestions:
        sections.append(f"\n\nEvaluation & Suggestions: {eval_suggestions}")
    
    # Recommended Actions (从suggestions字段获取)
    suggestions = annotation_data.get('suggestion', [])
    if suggestions:
        sections.append(f"\n\nRecommended Actions: {', '.join(suggestions)}")
    
    # 如果没有任何数据，返回提示信息
    if not sections:
        return "No report data available. Please complete the annotation first."
    
    return ''.join(sections)