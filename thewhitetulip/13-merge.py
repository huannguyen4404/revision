even_file = open("even.txt")
odd_file = open("odd.txt")

even_lines = even_file.readlines()
odd_lines = odd_file.readlines()

even_lines = [line.strip() for line in even_lines]
odd_lines = [line.strip() for line in odd_lines]
final_lines = {}


def _transform_dup_lines(lines):
    for line in lines:
        if line not in final_lines.keys():
            final_lines[line] = 0
        else:
            final_lines[line] += 1


_transform_dup_lines(even_lines)
_transform_dup_lines(odd_lines)

lines = "\n".join(list(final_lines.keys()))
file = open("merged.txt", "w")
file.write(lines + "\n")
file.close()
