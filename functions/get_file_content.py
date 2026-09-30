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
    
    
    
# schema

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Return the content of a file in a specifed file path.",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Will return content from provided file path, which must be supplied in the call.",
                },
            },
        },
    },
}