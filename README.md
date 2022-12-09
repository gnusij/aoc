# AOC

Set an environment variable for your advent-of-code [session id](docs/how-to-get-session-id.md)
```sh
# put this in your ~/.bashrc file
export AOC_SESSION='53616c7465645f5fa8fc...'
```

Get puzzles:
```py
# from today (2022 12 02)
>>> from aoc import data
>>> data
'B Y\nA Y\nB Z\nA Z\nA Y\nB Z\nC X\nC X\nC X\nC Y\nC Z\nB Y\nC Y\nC...'

# from specific date
>>> import aoc
>>> aoc.get(year=2022, day=2)
'B Y\nA Y\nB Z\nA Z\nA Y\nB Z\nC X\nC X\nC X\nC Y\nC Z\nB Y\nC Y\nC...'
```

Get examples:
```py
# from today (2022 12 02)
>>> aoc.ex  
'A Y\nB X\nC Z\n'

# from specific date
>>> aoc.get_ex(2022,2)
'A Y\nB X\nC Z\n'
```