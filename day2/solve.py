def main():
    max_seen_colors = []
    id_sum = 0

    with open("input", "r") as f:
        for line in f:
            current_game = {"red": 0, "green": 0, "blue": 0}
            line_relevant = line.strip()[line.find(":") + 2:]
            for grab in line_relevant.split("; "):
                for items_saw in grab.split(", "):
                    count_and_color = items_saw.split(" ")
                    current_game[count_and_color[1]] = max(current_game[count_and_color[1]], int(count_and_color[0]))

            max_seen_colors.append(current_game)

    for ii, elem in enumerate(max_seen_colors):
        if elem["red"] <= 12 and elem["green"] <= 13 and elem["blue"] <= 14:
            id_sum += ii + 1

    print(id_sum)


if __name__ == '__main__':
    main()
