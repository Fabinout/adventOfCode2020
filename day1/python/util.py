def readFile(py :str) -> str:
    file_object = open(py, "r")
    a = (file_object.read())
    file_object.close()
    return a
