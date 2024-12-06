def is_odd(n: int):
    return (n%2 == 1)

def is_delimiter_closed(splitted_list: list):
    return is_odd(len(splitted_list))
