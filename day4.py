from queue import Queue

def solve_a():
    score = 0
    while line := input():
        _, numbers = line.split(': ')
        winning, holdings = numbers.split('|')
        winning = {int(num) for num in winning.split(' ') if num}
        holdings = {int(num) for num in holdings.split(' ') if num}

        count = len(winning.intersection(holdings))
        score += 2 ** (count - 1) if count > 0 else 0
    return score

def solve_b():
    scratchcards = 0
    
    lines = []
    q = Queue()
    while line := input():
        lines.append(line)
        q.put(line)
    
    while not q.empty():
        curr = q.get()
        scratchcards += 1

        card, numbers = curr.split(': ')
        _, card_id = card.split()

        winning, holdings = numbers.split('|')
        winning = {int(num) for num in winning.split(' ') if num}
        holdings = {int(num) for num in holdings.split(' ') if num}

        count = len(winning.intersection(holdings))

        for i in range(count):
            q.put(lines[int(card_id) + i])
        
    return scratchcards
