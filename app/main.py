def copy_file(command: str) -> None:
    params = command.split()
    if len(params) < 3 or params[1] == params[2]:
        return
    file1 = open(params[1], "r")
    content = file1.read()
    file1.close()
    file2 = open(params[2], "w")
    file2.write(content)
