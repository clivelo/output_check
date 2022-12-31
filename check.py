import os


def read_output(fpath: str) -> list[str]:
    output = []
    with open(fpath, "r") as f:
        for row in f:
            output.append(row.strip("\n"))
    return output


def show_difference(t1, t2):
    for i in range(len(t2)):
        try:
            if t1[i] != t2[i]:
                print(f'Line {i + 1}\n'
                      f'Your output:\n{t1[i]}\n\n'
                      f'Expected:\n{t2[i]}\n')
                print("Please fix this line, update the output file, and rerun this script.")
                return
        except IndexError:
            print(f"Your output is missing line {i + 1}\n"
                  f"Expected:\n"
                  f"{t2[i]}\n")
            print("Please fix this line, update the output file, and rerun this script.")
            return

    if len(t1) > len(t2):
        print(f"Your output has {len(t1) - len(t2)} extra lines at the end,\n"
              f"from line {len(t2) + 1} to {len(t1)}.")
        return

    print("Everything looks good!")


def main():
    t1 = read_output(p1)
    t2 = read_output(p2)
    show_difference(t1, t2)


if __name__ == "__main__":
    dirpath = os.path.dirname(__file__)
    p1 = os.path.join(dirpath, "my_output.txt")
    p2 = os.path.join(dirpath, "sample_output.txt")
    main()
