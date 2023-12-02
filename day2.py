def solve_a():
    def possible_sample(sample):
        for category in sample:
                number, color = category[1:].split(" ")
                number = int(number)
                match color:
                    case 'red':
                        if number > 12:
                            return False
                    case 'green':
                        if number > 13:
                            return False
                    case 'blue':
                        if number > 14:
                            return False
        return True

    res = 0
    while line := input():
        game, data = line.split(":")
        id = int(game.split(" ")[1])

        if all(possible_sample(sample.split(",")) for sample in data.split(";")):
            res += id
    
    return res

def solve_b():
    res = 0
    while line := input():
        _, data = line.split(":")

        num_red = num_green = num_blue = -1
        for sample in data.split(";"):
            for category in sample.split(","):
                number, color = category[1:].split(" ")
                number = int(number)
                match color:
                    case 'red':
                        if number > num_red:
                            num_red = number
                    case 'green':
                        if number > num_green:
                            num_green = number
                    case 'blue':
                        if number > num_blue:
                            num_blue = number

        res += num_red * num_green * num_blue
    return res
