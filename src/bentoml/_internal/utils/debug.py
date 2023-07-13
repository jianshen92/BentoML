def print_call_stack():
    import inspect
    stack = inspect.stack()
    print("Call stack:")
    for frame_info in stack:
        filename = frame_info.filename
        lineno = frame_info.lineno
        function = frame_info.function
        print(f"  File '{filename}', line {lineno}, in {function}")