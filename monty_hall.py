not_switching_wins = sum(monty_hall(randrange(3), switch=False) for _ in range(iterations))
switching_wins = sum(monty_hall(randrange(3), switch=True) for _ in range(iterations))
