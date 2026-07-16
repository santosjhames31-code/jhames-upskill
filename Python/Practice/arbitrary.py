"""
Write a function summarize(*args, **kwargs) that takes any numbers and optional 
formatting flags (like round_to=2) and returns stats (mean, max, min)
"""
import statistics

def summarize(*args, **num):
    MAX = max(args)
    MIN = min(args)
    MEAN = statistics.mean(args)
    round = num.get('round')

    print(f"MAX  : {MAX : .{round}f}")
    print(f"MIN  : {MIN : .{round}f}")
    print(f"MEAN : {MEAN : .{round}f}")


summarize(1, 2, 3, round="2")
    