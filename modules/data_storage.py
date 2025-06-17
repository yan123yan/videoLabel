# -*- coding: utf-8 -*-
import os
import re

def get_annotation_path(video_path):
    """Generates the path for the annotation file based on the video path."""
    return os.path.splitext(video_path)[0] + '.txt'

def parse_txt_annotation(content):
    """解析txt格式的标注内容"""
    lines = content.split('\n')
    data = {}
    
    # 解析基本标注字段
    for line in lines:
        if line.startswith('autonomous_mode:'):
            data['autonomous_mode'] = line.split(':', 1)[1].strip()
        elif line.startswith('driving_control_style:'):
            value = line.split(':', 1)[1].strip()
            data['driving_control_style'] = [v.strip() for v in value.split(',') if v.strip()]
        elif line.startswith('visual_attention_style:'):
            value = line.split(':', 1)[1].strip()
            data['visual_attention_style'] = [v.strip() for v in value.split(',') if v.strip()]
        elif line.startswith('integrated_style:'):
            value = line.split(':', 1)[1].strip()
            data['integrated_style'] = [v.strip() for v in value.split(',') if v.strip()]
        elif line.startswith('suggestions:'):
            value = line.split(':', 1)[1].strip()
            data['suggestion'] = [v.strip() for v in value.split(',') if v.strip()]
    
    # 解析详细描述字段
    content_parts = content.split('-------------------------')
    if len(content_parts) > 1:
        detail_section = content_parts[1]
        
        # 提取各个详细描述字段
        scene_match = re.search(r'\*\*Scene Description:\*\*(.*?)(?=\*\*|$)', detail_section, re.DOTALL)
        if scene_match:
            data['scene_description'] = scene_match.group(1).strip()
            
        attention_match = re.search(r'\*\*Driver\'s Attention:\*\*(.*?)(?=\*\*|$)', detail_section, re.DOTALL)
        if attention_match:
            data['drivers_attention'] = attention_match.group(1).strip()
            
        interaction_match = re.search(r'\*\*Human-Machine Interaction:\*\*(.*?)(?=\*\*|$)', detail_section, re.DOTALL)
        if interaction_match:
            data['human_machine_interaction'] = interaction_match.group(1).strip()
            
        evaluation_match = re.search(r'\*\*Evaluation & Suggestions:\*\*(.*?)(?=\*\*|$)', detail_section, re.DOTALL)
        if evaluation_match:
            data['evaluation_suggestions'] = evaluation_match.group(1).strip()
    
    return data

def format_txt_annotation(annotation_data):
    """将标注数据格式化为txt格式"""
    content = []
    
    # 基本标注字段
    content.append(f"autonomous_mode: {annotation_data.get('autonomous_mode', '')}")
    content.append(f"driving_control_style: {', '.join(annotation_data.get('driving_control_style', []))}")
    content.append(f"visual_attention_style: {', '.join(annotation_data.get('visual_attention_style', []))}")
    content.append(f"integrated_style: {', '.join(annotation_data.get('integrated_style', []))}")
    content.append(f"suggestions: {', '.join(annotation_data.get('suggestion', []))}")
    
    # 分隔线
    content.append("")
    content.append("-------------------------")
    content.append("")
    
    # 详细描述字段
    content.append("**Scene Description:**")
    content.append(annotation_data.get('scene_description', ''))
    content.append("")
    content.append("**Driver's Attention:**")
    content.append(annotation_data.get('drivers_attention', ''))
    content.append("")
    content.append("**Human-Machine Interaction:**")
    content.append(annotation_data.get('human_machine_interaction', ''))
    content.append("")
    content.append("**Evaluation & Suggestions:**")
    content.append(annotation_data.get('evaluation_suggestions', ''))
    
    return '\n'.join(content)

def save_annotation(video_path, annotation_data):
    """Saves the annotation data to a txt file."""
    annotation_path = get_annotation_path(video_path)
    try:
        content = format_txt_annotation(annotation_data)
        with open(annotation_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except IOError as e:
        print(f"Error saving annotation file: {e}")
        return False

def load_annotation(video_path):
    """Loads the annotation data from a txt file."""
    annotation_path = get_annotation_path(video_path)
    if os.path.exists(annotation_path):
        try:
            with open(annotation_path, 'r', encoding='utf-8') as f:
                content = f.read()
                return parse_txt_annotation(content)
        except IOError as e:
            print(f"Error loading annotation file: {e}")
            return {}
    return {}