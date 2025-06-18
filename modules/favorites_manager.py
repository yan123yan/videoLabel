# -*- coding: utf-8 -*-
import os
import json
from typing import List, Set

# 收藏记录配置文件路径
FAVORITES_FILE = "data/favorites.json"

def ensure_data_directory():
    """确保data目录存在"""
    os.makedirs("data", exist_ok=True)

def load_favorites() -> Set[str]:
    """从本地文件加载收藏记录"""
    ensure_data_directory()
    
    if os.path.exists(FAVORITES_FILE):
        try:
            with open(FAVORITES_FILE, 'r', encoding='utf-8') as f:
                favorites_data = json.load(f)
                return set(favorites_data.get('favorites', []))
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading favorites: {e}")
            return set()
    return set()

def save_favorites(favorites: Set[str]) -> bool:
    """保存收藏记录到本地文件"""
    ensure_data_directory()
    
    try:
        favorites_data = {
            'favorites': list(favorites),
            'last_updated': str(os.path.getmtime(FAVORITES_FILE)) if os.path.exists(FAVORITES_FILE) else str(0)
        }
        
        with open(FAVORITES_FILE, 'w', encoding='utf-8') as f:
            json.dump(favorites_data, f, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"Error saving favorites: {e}")
        return False

def add_to_favorites(video_path: str, current_favorites: Set[str]) -> Set[str]:
    """添加视频到收藏"""
    new_favorites = current_favorites.copy()
    new_favorites.add(video_path)
    return new_favorites

def remove_from_favorites(video_path: str, current_favorites: Set[str]) -> Set[str]:
    """从收藏中移除视频"""
    new_favorites = current_favorites.copy()
    new_favorites.discard(video_path)
    return new_favorites

def is_favorited(video_path: str, favorites: Set[str]) -> bool:
    """检查视频是否已收藏"""
    return video_path in favorites

def clear_favorites() -> bool:
    """清空收藏记录"""
    try:
        if os.path.exists(FAVORITES_FILE):
            os.remove(FAVORITES_FILE)
        return True
    except IOError as e:
        print(f"Error clearing favorites: {e}")
        return False

def get_favorites_file_info() -> dict:
    """获取收藏记录文件信息"""
    if os.path.exists(FAVORITES_FILE):
        stat = os.stat(FAVORITES_FILE)
        return {
            'exists': True,
            'size': stat.st_size,
            'modified': stat.st_mtime,
            'path': os.path.abspath(FAVORITES_FILE)
        }
    else:
        return {
            'exists': False,
            'path': os.path.abspath(FAVORITES_FILE)
        }