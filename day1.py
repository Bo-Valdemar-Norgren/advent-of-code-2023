def solve_a():
    res = 0
    while line := input():
        digits = [x for x in line if x.isdigit()]
        res += int(digits[0] + digits[-1])
    
    return res

def solve_b():
    letter_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6', 
        'seven': '7',
        'eight': '8', 
        'nine': '9'
    }

    res = 0
    while line := input():
        digits = []
        i = 0
        while i < len(line):
            if line[i].isdigit():
                digits.append(line[i])
                i += 1
            else:
                curr = line[i:]
                match = False
                for key in letter_map.keys():
                    if curr.startswith(key):
                        digits.append(letter_map[key])
                        i += len(key) - 1
                        match = True
                        break
                i += not match
        res += int(digits[0] + digits[-1])

    return res
