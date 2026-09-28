from config import MAX_CHARS
import os

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    
        valid_file_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    
        if valid_file_path == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif os.path.isfile(target_path) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        
        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        return file_content_string
        
    except Exception as e:
        return f"Error: {e}"