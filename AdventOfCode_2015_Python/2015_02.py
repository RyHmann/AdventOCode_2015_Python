FILEPATH = "../data/2015/02.txt"


def main():
    all_presents = get_data(FILEPATH)
    total_paper_required = calculate_paper_required(all_presents)
    total_ribbon_required = calculate_ribbon_required(all_presents)
    print(f"Total paper required: {total_paper_required}.")
    print(f"Total ribbon required: {total_ribbon_required}.")


def get_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def calculate_paper_required(presents):
    total_paper_required = 0
    for present in presents:
        box_dims = format_line_into_dims(present)
        present_area = get_paper_area(box_dims)
        total_paper_required += present_area
    return total_paper_required


def calculate_ribbon_required(presents):
    total_ribbon_required = 0
    for present in presents:
        box_dims = format_line_into_dims(present)
        ribbon_length = get_total_ribbon(box_dims)
        total_ribbon_required += ribbon_length
    return total_ribbon_required


def get_paper_area(dims):
    length = get_length(dims)
    width = get_width(dims)
    height = get_height(dims)
    face_one_area = length * width
    face_two_area = width * height
    face_three_area = height * length
    area_list = [face_one_area, face_two_area, face_three_area]
    smallest_face = min(area_list)
    total_box_area = sum(area_list) * 2
    total_paper_required = total_box_area + smallest_face
    return total_paper_required


def get_total_ribbon(dims):
    length = get_length(dims)
    width = get_width(dims)
    height = get_height(dims)
    box_dims = [length, width, height]
    ribbon_bow = get_ribbon_bow(box_dims)
    ribbon_perim = get_ribbon_perimter(box_dims)
    total_ribbon = ribbon_perim + ribbon_bow
    return total_ribbon


def get_ribbon_perimter(dims):
    largest_side = dims.index(max(dims))
    small_side_list = dims
    small_side_list.pop(largest_side)
    ribbon_perimeter = 2 * sum(small_side_list)
    return (ribbon_perimeter) 


def get_ribbon_bow(dims):
    ribbon_length = 1
    for side in dims:
        ribbon_length = ribbon_length * side
    return ribbon_length


def format_line_into_dims(item):
    box_dims = item.split("x")
    return box_dims


def get_length(dims):
    return int(dims[0])


def get_width(dims):
    return int(dims[1])


def get_height(dims):
    return int(dims[2])


if __name__ == "__main__":
    main()