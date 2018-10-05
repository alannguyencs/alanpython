import math

def get_list_color(num_color):
    list_color = [255]
    if num_color > 1:
        num_color -= 1
        step_color = 255 / num_color
        for i in range(num_color):
            list_color.append(int(i * step_color))
    return list_color


def generate_color_code(num_colors=5):
    assert (num_colors > 0)
    #given number of color code, generate reasonable RGB code
    #step 1: because RGB has 3 channels --> find a cube root
    num_R = int(math.ceil(num_colors ** (1./3.)))
    num_B = int(math.ceil((num_colors / num_R) ** (1./2.)))
    num_G = int (math.ceil(num_colors / (num_R * num_B)))
    print (num_R, num_B, num_G)

    list_R = get_list_color(num_R)
    list_B = get_list_color(num_B)
    list_G = get_list_color(num_G)

    color_code_list = []
    for r in list_R:
        for g in list_G:
            for b in list_B:
                color_code_list.append((r, g, b))


    print (color_code_list)
    return color_code_list[:num_colors]



generate_color_code(10)
