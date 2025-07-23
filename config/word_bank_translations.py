# -*- coding: utf-8 -*-
"""
选项值的多语言翻译
"""

# 驾驶操控风格选项翻译
DRIVING_CONTROL_STYLE_TRANS = {
    "谨慎驾驶": {
        "zh": "谨慎驾驶",
        "en": "Cautious Driving"
    },
    "平稳驾驶": {
        "zh": "平稳驾驶", 
        "en": "Smooth Driving"
    },
    "激进驾驶": {
        "zh": "激进驾驶",
        "en": "Aggressive Driving"
    },
    "反应迟缓": {
        "zh": "反应迟缓",
        "en": "Slow Response"
    },
    "反应迅速": {
        "zh": "反应迅速",
        "en": "Quick Response"
    },
    "动态操控": {
        "zh": "动态操控",
        "en": "Dynamic Control"
    },
    "冒险驾驶": {
        "zh": "冒险驾驶",
        "en": "Risk-Taking Driving"
    },
    "粗心马虎驾驶": {
        "zh": "粗心马虎驾驶",
        "en": "Careless Driving"
    }
}

# 视觉注意风格选项翻译
VISUAL_ATTENTION_STYLE_TRANS = {
    "专注前方": {
        "zh": "专注前方",
        "en": "Focus Forward"
    },
    "忽视前方": {
        "zh": "忽视前方",
        "en": "Ignore Forward"
    },
    "观察四周": {
        "zh": "观察四周",
        "en": "Observe Surroundings"
    },
    "忽视四周": {
        "zh": "忽视四周",
        "en": "Ignore Surroundings"
    },
    "关注行人": {
        "zh": "关注行人",
        "en": "Focus on Pedestrians"
    },
    "忽视行人": {
        "zh": "忽视行人",
        "en": "Ignore Pedestrians"
    },
    "关注旁车": {
        "zh": "关注旁车",
        "en": "Focus on Adjacent Vehicles"
    },
    "忽视旁车": {
        "zh": "忽视旁车",
        "en": "Ignore Adjacent Vehicles"
    },
    "查看后视": {
        "zh": "查看后视",
        "en": "Check Rear View"
    },
    "忽视后视": {
        "zh": "忽视后视",
        "en": "Ignore Rear View"
    },
    "注视狭窄": {
        "zh": "注视狭窄",
        "en": "Narrow Focus"
    },
    "适度扫视": {
        "zh": "适度扫视",
        "en": "Moderate Scanning"
    },
    "频繁转移": {
        "zh": "频繁转移",
        "en": "Frequent Shifting"
    },
    "观察仪表": {
        "zh": "观察仪表",
        "en": "Check Dashboard"
    },
    "忽略仪表": {
        "zh": "忽略仪表",
        "en": "Ignore Dashboard"
    },
    "观察系统提示": {
        "zh": "观察系统提示",
        "en": "Check System Alerts"
    },
    "忽略系统提示": {
        "zh": "忽略系统提示",
        "en": "Ignore System Alerts"
    }
}

# 综合风格选项翻译
INTEGRATED_STYLE_TRANS = {
    "谨慎": {
        "zh": "谨慎",
        "en": "Cautious"
    },
    "稳定": {
        "zh": "稳定",
        "en": "Stable"
    },
    "激进": {
        "zh": "激进",
        "en": "Aggressive"
    },
    "粗心": {
        "zh": "粗心",
        "en": "Careless"
    },
    "分心": {
        "zh": "分心",
        "en": "Distracted"
    },
    "专注": {
        "zh": "专注",
        "en": "Focused"
    }
}

# 建议选项翻译
SUGGESTION_TRANS = {
    "减速": {
        "zh": "减速",
        "en": "Slow Down"
    },
    "适当加速": {
        "zh": "适当加速",
        "en": "Speed Up Appropriately"
    },
    "变道": {
        "zh": "变道",
        "en": "Change Lane"
    },
    "超车": {
        "zh": "超车",
        "en": "Overtake"
    },
    "观察行人": {
        "zh": "观察行人",
        "en": "Watch for Pedestrians"
    },
    "检查后视镜": {
        "zh": "检查后视镜",
        "en": "Check Rear Mirror"
    },
    "增加车距": {
        "zh": "增加车距",
        "en": "Increase Following Distance"
    },
    "使用转向灯": {
        "zh": "使用转向灯",
        "en": "Use Turn Signal"
    },
    "关注周围交通": {
        "zh": "关注周围交通",
        "en": "Monitor Surrounding Traffic"
    },
    "手动驾驶": {
        "zh": "手动驾驶",
        "en": "Manual Driving"
    },
    "自动驾驶": {
        "zh": "自动驾驶",
        "en": "Autonomous Driving"
    },
    "继续保持": {
        "zh": "继续保持",
        "en": "Maintain Current State"
    },
    "准备接管": {
        "zh": "准备接管",
        "en": "Prepare to Take Over"
    },
    "观察信号灯": {
        "zh": "观察信号灯",
        "en": "Watch Traffic Lights"
    },
    "观察系统提示": {
        "zh": "观察系统提示",
        "en": "Check System Alerts"
    }
}

def get_option_text(option_value, translation_dict, language='zh'):
    """
    获取选项值的翻译文本
    
    :param option_value: 选项的原始值（中文）
    :param translation_dict: 对应的翻译字典
    :param language: 目标语言
    :return: 翻译后的文本
    """
    if option_value in translation_dict:
        return translation_dict[option_value].get(language, option_value)
    return option_value

def get_translated_options(option_list, translation_dict, language='zh'):
    """
    获取整个选项列表的翻译
    
    :param option_list: 原始选项列表
    :param translation_dict: 对应的翻译字典
    :param language: 目标语言
    :return: 翻译后的选项列表
    """
    return [get_option_text(option, translation_dict, language) for option in option_list]