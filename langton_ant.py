from PIL import Image

size_x = 3000
size_y = 3000
img = Image.new('RGB', (size_x,size_y))
img_list = [[0 for i in range(size_y)] for j in range(size_x)]
instructions_list = ["L", "L", "R", "R"]
colors_list = [(0,0,0), (137, 49, 239), (242, 202, 25), (255, 0, 189)]
max_iterations = 1000000000
position = (1500,1500)
i=0
orientation = 0
is_in_canvas = True
while is_in_canvas and i <= max_iterations:
    if instructions_list[img_list[position[0]][position[1]]] == "L":
        if orientation == 270:
            orientation = 0
        else:
            orientation += 90
    else:
        if orientation == 0:
            orientation = 270
        else:
            orientation -= 90
    if img_list[position[0]][position[1]] == len(instructions_list) - 1:
        img_list[position[0]][position[1]] = 0
    else:
        img_list[position[0]][position[1]] += 1
    match orientation:
        case 0:
            if position[0] + 1 >= size_x:
                is_in_canvas = False
            position = (position[0] + 1, position[1])
        case 90:
            if position[1] - 1 < 0:
                is_in_canvas = False
            position = (position[0], position[1] - 1)
        case 180:
            if position[0] - 1 < 0:
                is_in_canvas = False
            position = (position[0] - 1, position[1])
        case 270:
            if position[1] + 1 >= size_y:
                is_in_canvas = False
            position = (position[0], position[1] + 1)
    i += 1
data = []
for i in img_list:
    for j in i:
        data.append(colors_list[j])
img.putdata(data)
img.save("ant.png")
