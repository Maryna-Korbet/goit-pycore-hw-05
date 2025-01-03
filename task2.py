import re
from typing import Callable

def generator_numbers(text: str):
  position = 0
  text_slice = text
  
  while True:
    if position >= len(text_slice) - 1:
      break

    text_slice = text_slice[position:]
    match = re.search(r'(^|\s)(\d+(?:\.\d+)?)(\s|$)', text_slice)
    
    if match == None:
      break
    
    position = match.end() - 1
    result = float(match.group().strip())
    yield result


def sum_profit(string: str, func: Callable[[str], float]) -> float:
  sum = 0
  for res in func(string):
    sum += res
    print(res, sum)

  return round(sum, 2)


text = "The total income of the employee consists of several parts: 1000.01 as the main income, supplemented by additional income of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")