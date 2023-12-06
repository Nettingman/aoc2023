def main():
    final_value = 0

    with open("input", "r") as f:
        for line in f:
            line_strip = line.strip()
            calibration_value = ""
            for char in line_strip:
                if char.isdigit():
                    calibration_value += char
                    break

            for char in reversed(line_strip):
                if char.isdigit():
                    calibration_value += char
                    break

            final_value += int(calibration_value)

    print(final_value)


if __name__ == '__main__':
    main()
