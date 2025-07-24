# -*- coding: utf-8 -*-
import os
import re
import json

def get_annotation_path(video_path):
    """Generates the path for the annotation file based on the video path."""
    return os.path.splitext(video_path)[0] + '.txt'

def get_json_annotation_path(video_path):
    """Generates the path for the JSON annotation file based on the video path."""
    return os.path.splitext(video_path)[0] + '.json'

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

# 固定的raw_response模板文本
TEMPLATE_RAW_RESPONSE = """### Step 1: Style Interpretation as Hypothesis

#### Driving Control Style: Smooth Driving
- **Behavioral Implication**: Indicates a stable and consistent driving rhythm with steady acceleration and low steering variability.
- **Expected Observations**: Smooth speed changes, minimal braking, and consistent steering angles.

#### Visual Attention Style: Focused on Forward Road
- **Behavioral Implication**: Indicates strong attention on the forward road area.
- **Expected Observations**: Gaze focused on the road ahead, minimal distraction.

#### Integrated Style: Focused
- **Behavioral Implication**: High task focus and sustained attention to road and traffic dynamics.
- **Expected Observations**: Consistent attention to the road, minimal distraction, and engagement with the driving environment.

### Step 2: Cross-Modal Consistency Verification

#### Driving Signals:
- **Speed**: The speed fluctuates but remains relatively stable around 20-25 m/s, with a slight decrease and then a sharp drop to 1.7 m/s and 1.1 m/s, followed by a recovery to 3.1 m/s and 6.6 m/s.
- **Acceleration**: The acceleration is generally smooth with some fluctuations, peaking at 4.4 m/s² and 3.7 m/s².
- **Steering Angle**: The steering angle is minimal and mostly stable, with slight changes indicating minor steering adjustments.
- **Braking Signal**: The braking signal is low and mostly absent, with a brief increase to 0.4 and 0.3, indicating light braking.

#### Object Fixations:
- The driver's gaze is primarily on the dashboard and autonomous information, with occasional shifts to vehicles and the rearview mirror.

#### Autonomous Mode:
- The vehicle is in manual mode throughout the segment.

### Step 3: Final Structured Report

#### Scene Description:
The video depicts a driving scenario on a multi-lane road with a clear view of the road ahead. The road is surrounded by trees and open fields, with a few other vehicles visible in the distance. The weather appears clear, and the road conditions are dry.

#### Driver's Attention:
The driver's gaze is predominantly focused on the dashboard and autonomous information, with occasional glances at the vehicles and rearview mirror. This suggests a high level of engagement with the driving environment and the vehicle's systems. The driver appears to be paying attention to the road ahead and the vehicle's status, which aligns with the "Focused on Forward Road" and "Focused" styles.

#### Human-Machine Interaction:
The driver is in manual mode, and the vehicle's autonomous systems are not actively engaged. The driver's steering and braking actions are smooth, with minimal steering adjustments and light braking. The driver's attention to the dashboard and autonomous information suggests a level of trust in the vehicle's systems, which is consistent with the "Smooth Driving" and "Focused" styles.

#### Evaluation & Suggestions:
The driver's behavior is generally smooth and focused, with minimal distractions and consistent attention to the road and the vehicle's systems. The driver's actions are in line with the "Smooth Driving" and "Focused" styles, indicating a stable and controlled driving pattern. However, the occasional glances at the rearview mirror and vehicles suggest a need for further situational awareness.

#### Recommended Actions:
1. **Observe system prompts**: The driver should continue to pay attention to the vehicle's autonomous systems and prompts to ensure optimal interaction and safety.
2. **Check mirrors**: The driver should periodically check the rearview mirror to maintain situational awareness and ensure no blind spots.
3. **Focus on traffic**: The driver should remain focused on the road and traffic conditions to maintain a safe and controlled driving environment."""

def load_json_annotation(video_path):
    """
    Loads the JSON annotation file if it exists.
    
    Args:
        video_path: Path to the video file
    
    Returns:
        Dictionary containing the JSON data if file exists, None otherwise
    """
    json_path = get_json_annotation_path(video_path)
    
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading JSON annotation file: {e}")
            return None
    return None

def save_json_annotation(video_path, annotation_data, rating_data):
    """
    Saves the complete annotation data including ratings to a JSON file.
    
    Args:
        video_path: Path to the video file
        annotation_data: Dictionary containing annotation data from txt file
        rating_data: Dictionary containing rating scores (factuality, relevance, coherence, usefulness)
    
    Returns:
        True if successful, False otherwise
    """
    json_path = get_json_annotation_path(video_path)
    
    try:
        # 准备JSON数据结构，基于模板格式
        json_data = {
            "raw_response": TEMPLATE_RAW_RESPONSE,
            "extracted_sections": {
                "scene_description": annotation_data.get('scene_description', ''),
                "driver_attention": annotation_data.get('drivers_attention', ''),
                "human_machine_interaction": annotation_data.get('human_machine_interaction', ''),
                "evaluation_suggestions": annotation_data.get('evaluation_suggestions', ''),
                "recommended_actions": annotation_data.get('suggestion', [])
            },
            "video_path": video_path,
            "factuality": rating_data.get('factuality', ''),
            "relevance": rating_data.get('relevance', ''),
            "coherence": rating_data.get('coherence', ''),
            "usefulness": rating_data.get('usefulness', '')
        }
        
        # 保存JSON文件
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        
        return True
    except Exception as e:
        print(f"Error saving JSON annotation file: {e}")
        return False