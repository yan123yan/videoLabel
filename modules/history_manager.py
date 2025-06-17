# -*- coding: utf-8 -*-
import os
import json
from typing import List

# 历史记录配置文件路径
HISTORY_FILE = "data/path_history.json"

def ensure_data_directory():
    """确保data目录存在"""
    os.makedirs("data", exist_ok=True)

def load_path_history() -> List[str]:
    """从本地文件加载路径历史记录"""
    ensure_data_directory()
    
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                history_data = json.load(f)
                return history_data.get('paths', [])
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading path history: {e}")
            return []
    return []

def save_path_history(paths: List[str]) -> bool:
    """保存路径历史记录到本地文件"""
    ensure_data_directory()
    
    try:
        history_data = {
            'paths': paths[:10],  # 只保留最近10个路径
            'last_updated': str(os.path.getmtime(HISTORY_FILE)) if os.path.exists(HISTORY_FILE) else str(0)
        }
        
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history_data, f, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"Error saving path history: {e}")
        return False

def add_path_to_history(new_path: str, current_history: List[str]) -> List[str]:
    """添加新路径到历史记录"""
    # 如果路径已存在，先移除
    if new_path in current_history:
        current_history.remove(new_path)
    
    # 将新路径添加到开头
    current_history.insert(0, new_path)
    
    # 只保留最近10个路径
    return current_history[:10]

def clear_path_history() -> bool:
    """清空路径历史记录"""
    try:
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
        return True
    except IOError as e:
        print(f"Error clearing path history: {e}")
        return False

def get_history_file_info() -> dict:
    """获取历史记录文件信息"""
    if os.path.exists(HISTORY_FILE):
        stat = os.stat(HISTORY_FILE)
        return {
            'exists': True,
            'size': stat.st_size,
            'modified': stat.st_mtime,
            'path': os.path.abspath(HISTORY_FILE)
        }
    else:
        return {
            'exists': False,
            'path': os.path.abspath(HISTORY_FILE)
        }