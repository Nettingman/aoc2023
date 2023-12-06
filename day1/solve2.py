def main():
    final_value = 0
    text_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    with open("input", "r") as f:
        for line in f:
            line_strip = line.strip()
            calibration_value = ""

            text_digit_pos_first = -1
            text_digit_value_first = None
            for elem in text_digits.keys():
                pos = line_strip.find(elem)
                if pos >= 0:
                    if text_digit_pos_first == -1 or pos < text_digit_pos_first:
                        text_digit_pos_first = pos
                        text_digit_value_first = text_digits[elem]

            text_digit_pos_last = -1
            text_digit_value_last = None
            for elem in text_digits.keys():
                pos = line_strip.rfind(elem)
                if pos >= 0:
                    if pos > text_digit_pos_last:
                        text_digit_pos_last = pos
                        text_digit_value_last = text_digits[elem]

            for index, char in enumerate(line_strip):
                if text_digit_pos_first != -1 and index >= text_digit_pos_first:
                    calibration_value += text_digit_value_first
                    break

                if char.isdigit():
                    calibration_value += char
                    break

            index = len(line_strip)
            for char in reversed(line_strip):
                index -= 1

                if text_digit_pos_last != -1 and index <= text_digit_pos_last:
                    calibration_value += text_digit_value_last
                    break

                if char.isdigit():
                    calibration_value += char
                    break

            final_value += int(calibration_value)

    print(final_value)


if __name__ == '__main__':
    main()
