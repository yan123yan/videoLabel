# -*- coding: utf-8 -*-
import os

def get_project_structure(project_path):
    """
    Scans the project path and returns a dictionary with the folder structure.
    Includes both subfolders with video files and direct video files in the root path.
    """
    project_structure = {}
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v']

    try:
        # 首先检查根目录下是否有视频文件
        root_video_files = []
        for file in os.listdir(project_path):
            file_path = os.path.join(project_path, file)
            if os.path.isfile(file_path) and os.path.splitext(file)[1].lower() in video_extensions:
                root_video_files.append(file)
        
        if root_video_files:
            project_structure["根目录"] = sorted(root_video_files)

        # 然后检查子文件夹
        for root, dirs, files in os.walk(project_path):
            # 只检查直接子目录，避免过深的嵌套
            if root == project_path:
                for d in dirs:
                    folder_path = os.path.join(project_path, d)
                    try:
                        video_files = []
                        for f in os.listdir(folder_path):
                            if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f)[1].lower() in video_extensions:
                                video_files.append(f)
                        if video_files:
                            project_structure[d] = sorted(video_files)
                    except (PermissionError, FileNotFoundError):
                        # 跳过无法访问的文件夹
                        continue
                        
    except Exception as e:
        print(f"扫描项目路径时出错: {e}")
    
    return project_structure