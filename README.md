# Output Checking
For comparing your console outputs from the sample outputs.

## Dependencies
Python >= 3.7

## Usage
- Paste the sample output into `sample_output.txt`
- Paste your output into `my_output.txt`
- Run `check.py`

## How It Works
- All results are printed on the console
- It shows the **first** line that the two texts differ
- You should then fix that line, update `my_output.txt`, and rerun the script

## Interpret Results
:point_down: This means on line 12 of your output, you typed `hello`, but the sample output expected `Hello`.
```
Line 12
Your output:
hello

Expected:
Hello
```

:point_down: This means the sample output has line 78 which says `Bye`, but your output ended at line 77 and missing line 78 (and beyond).
```
Your output is missing line 78
Expected:
Bye
```

:point_down: This means the sample output only has 44 lines, whereas your output has 3 extra lines from 45 to 48.
```
Your output has 3 extra lines at the end,
from line 45 - 48.
```
