from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_files import schema_write_file
from collections.abc import Callable

available_functions = [
    schema_get_files_info,
    schema_run_python_file,
    schema_write_file,
    schema_get_file_content,
]


def call_function(tool_call, verbose: bool=False) -> dict:
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")
    
    if verbose == True:
        print(f" - Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")
        
    function_map: dict[str, Callable[..., str]] = {
        "get_file_content": get_file_content,
        # etc.
    }