matrix: list[list[int]] = []


def set_size(width: int, height: int):
    global matrix

    if width < 0 or height < 0:
        return
    
    matrix = [[0 for _ in range(width)] for _ in range(height)]
    print(matrix)