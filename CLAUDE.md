# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Video Annotation Tool built with Streamlit for annotating driving behavior videos. The application allows users to systematically label videos with driving control styles, visual attention styles, and provide detailed descriptions.

## Running the Application

```bash
# Run the Streamlit application
streamlit run app.py --server.port 8503

# The app will be available at http://localhost:8503
```

## Architecture

The codebase follows a modular architecture with clear separation of concerns:

- **app.py**: Main Streamlit application entry point that orchestrates all modules
- **file_manager.py**: Handles directory scanning and video file discovery
- **video_player.py**: Manages video playback functionality
- **annotation_form.py**: Contains all annotation UI components and form logic
- **data_storage.py**: Handles persistence of annotations to .txt files
- **progress_manager.py**: Tracks and displays annotation completion status
- **history_manager.py**: Manages recently used folder paths
- **favorites_manager.py**: Handles video bookmarking functionality
- **word_bank.py**: Configuration file containing predefined annotation options

## Key Implementation Details

1. **Session State Management**: The application heavily relies on Streamlit's session state for maintaining user data across reruns. Key session state variables include:
   - `folder_path`: Current working directory
   - `selected_file`: Currently selected video
   - `annotation_data`: Current annotation form data
   - `favorites`: List of bookmarked videos

2. **Data Storage Format**: Annotations are saved as .txt files alongside video files with the same base name. The format is JSON with the following structure:
   ```json
   {
     "autonomous_mode": "选项",
     "driving_control_style": "选项",
     "visual_attention_style": "选项",
     "integrated_style": "选项",
     "suggestions": ["建议1", "建议2"],
     "maneuver_description": "详细描述...",
     "visual_attention_description": "详细描述...",
     "driving_control_description": "详细描述...",
     "suggestions_description": "详细描述..."
   }
   ```

3. **File Organization**: The app supports both flat directory structures and nested folders. Video files are discovered recursively.

4. **Styling**: Custom CSS is embedded in app.py to provide a consistent UI experience. The app uses a wide layout optimized for video viewing.

## Common Development Tasks

When modifying the annotation options:
1. Update the lists in `word_bank.py`
2. The UI will automatically reflect the changes

When adding new features:
1. Create a new module in the project root
2. Import and integrate it in `app.py`
3. Follow the existing pattern of using Streamlit session state for data persistence

When debugging:
- Check the Streamlit session state using `st.write(st.session_state)`
- Annotations are saved in the same directory as video files with .txt extension
- Application data (favorites, history) is stored in the `/data` directory

## Important Conventions

1. All file I/O operations use UTF-8 encoding
2. Natural sorting (natsort) is used for file listings
3. Error handling includes user-friendly messages displayed via `st.error()`
4. The app assumes video files won't be moved after annotation (annotations are path-dependent)