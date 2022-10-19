def accumulative_percentage(amount: float, percentage: int, period):
    for _ in range(period):
        amount += (amount * percentage) / 100
    return amount
