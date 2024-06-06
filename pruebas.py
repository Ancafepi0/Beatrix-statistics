def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def print_color_table():
    for style in range(8):
        for fg in range(30, 38):
            for bg in range(40, 48):
                code = f"{style};{fg};{bg}"
                print_color(f"\033[{code}m {code} \033[0m", code)
            print()

print_color_table()
