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
- **report_rating.py**: Handles rating report functionality for annotation quality assessment
- **language_manager.py**: Manages internationalization and language switching

## Key Implementation Details

1. **Session State Management**: The application heavily relies on Streamlit's session state for maintaining user data across reruns. Key session state variables include:
   - `folder_path`: Current working directory
   - `selected_file`: Currently selected video
   - `annotation_data`: Current annotation form data
   - `favorites`: List of bookmarked videos
   - `selected_language`: Current UI language preference
   - `report_ratings`: Rating scores for annotation quality

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
5. Language translations are stored in the `translations/` directory
6. User preferences (favorites, history, language) are persisted in JSON files

## Known Issues and Bugs

### 🐛 Critical Bugs

1. **Inconsistent Sorting** (file_manager.py):
   - Root directory uses `sorted()` while subdirectories use `natsorted()`
   - **Impact**: Confusing file ordering between directories
   - **Fix**: Use `natsorted()` consistently throughout

2. **Type Inconsistency** (report_rating.py):
   - Rating values use integers in UI but may be stored as strings
   - **Impact**: Potential matching issues when loading saved ratings
   - **Fix**: Ensure consistent string type for all rating values

3. **Incomplete Error Handling** (data_storage.py):
   - IOError returns empty dict without distinguishing file-not-found vs read-error
   - JSON parse errors are printed but not reported to user
   - **Impact**: Users unaware of actual failure reasons
   - **Fix**: Add specific error types and user notifications

### ⚠️ Security Concerns

1. **Path Traversal Risk** (app.py):
   - User input paths are not validated
   - **Impact**: Potential unauthorized file access
   - **Fix**: Implement path normalization and validation

2. **Concurrent Access Issues**:
   - No file locking mechanism for multi-user scenarios
   - **Impact**: Potential data corruption
   - **Fix**: Implement file locking or database storage

### 🔧 Performance Issues

1. **Memory Leak Risk** (history_manager.py):
   - `os.path.getmtime()` may fail on files being written
   - **Impact**: Unexpected exceptions
   - **Fix**: Add try-catch with fallback behavior

2. **Session State Race Conditions** (app.py):
   - Fast video switching may cause state inconsistencies
   - **Impact**: Mismatched video and annotation data
   - **Fix**: Implement state locking during updates

### 📝 Best Practices

1. **Testing**: Always test with various file structures and edge cases
2. **Validation**: Validate all user inputs before processing
3. **Logging**: Add comprehensive logging for debugging
4. **Documentation**: Keep inline comments minimal, focus on complex logic
5. **Error Recovery**: Implement graceful degradation for all features

## Development Guidelines

### Adding New Features
1. Create module in `modules/` directory
2. Follow existing naming conventions
3. Use type hints for function parameters
4. Handle errors with user-friendly messages
5. Update this documentation

### Code Style
- Follow PEP 8 guidelines
- Use descriptive variable names
- Keep functions focused and small
- Avoid global variables
- Use session state for persistence

### Testing Checklist
- [ ] Test with empty directories
- [ ] Test with large video files
- [ ] Test with special characters in filenames
- [ ] Test concurrent access
- [ ] Test language switching
- [ ] Test data persistence across sessions