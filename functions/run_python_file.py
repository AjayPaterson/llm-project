import os, subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    
        valid_file_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
    
        if valid_file_path == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif os.path.isfile(target_path) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif file_path.endswith(".py")  == False:
            return f'Error: "{file_path}" is not a Python file'
    
        command = ["python", target_path]
    
        if args:
            command.extend(args)
        
        result = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)
    
        # output string creation
        output = []
    
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        
        if result.stdout == "" and result.stderr == "":
            output.append(f"No output produced")
        else:
            if result.stdout:
                output.append(f"STDOUT: {result.stdout}")
            if result.stderr:
                output.append(f"STDERR: {result.stderr}")
    
        return "\n".join(output)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    

# schema

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Takes file path and optional args and returns stdout, stderr or exit code.",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to use when running code",
                },
                "args": {
                    "type": "array",
                    "description": "If args is provided they are to be added to the command list.",
                    "items": {
                        "type": "string"
                    }
                }
            },
        },
    },
}