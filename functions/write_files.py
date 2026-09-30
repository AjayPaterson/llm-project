import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    
        valid_file_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    
        if valid_file_path == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        elif os.path.isdir(target_path) == True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
        with open(target_path, "w")  as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)' 
        
    except Exception as e:
        return f"Error: {e}"
    
    
# schema

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to the file specified in the file path.",
        "parameters": {
            "type": "object",
            "required": ["content", "file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to use when writing content, which must be supplied in the call.",
                },
                "content": {
                    "type": "string",
                    "description": "Text or content to use and add to file provided in file path, which must be supplied in the call.",
                }
            },
        },
    },
}