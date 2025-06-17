# -*- coding: utf-8 -*-
import os

def get_project_structure(project_path):
    """
    Scans the project path and returns a dictionary with the folder structure.
    Only includes folders that contain video files.
    """
    project_structure = {}
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv']

    for root, dirs, files in os.walk(project_path):
        # We only care about the immediate subdirectories of the project_path
        if root == project_path:
            for d in dirs:
                folder_path = os.path.join(project_path, d)
                video_files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in video_extensions]
                if video_files:
                    project_structure[d] = sorted(video_files)
    
    return project_structure