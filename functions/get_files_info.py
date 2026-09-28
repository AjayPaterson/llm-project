import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        # will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        
        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        
            
        if os.path.isdir(target_dir):
            file_details = []
            for filename in os.listdir(target_dir):
                full_path = os.path.join(target_dir, filename)
                size = os.path.getsize(full_path)
                is_dir = os.path.isdir(full_path)
                file_details.append(f"- {filename}: file_size={size} bytes, is_dir={is_dir}")
            return "\n".join(file_details)
        else:
            return f'Error: "{directory}" is not a directory'
        
    except Exception as e:
        return f"Error: {e}"