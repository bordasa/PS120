def join_or(my_list, separator=', ', conjunction='or'):
    my_str_list = [str(num) for num in my_list]

    if len(my_list) == 1:
        return my_str_list[0]
    if len(my_list) == 2:
        return f"{my_str_list[0]} {conjunction} {my_str_list[1]}"
    else:
        part1 = separator.join(my_str_list[: -1])
        part2 = f"{conjunction} {my_str_list[-1]}"
        return f"{part1}{separator}{part2}"

print(join_or([1, 2]))                   # => "1 or 2"
print(join_or([1, 2, 3]))                # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))          # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))   # => "1, 2, and 3"
