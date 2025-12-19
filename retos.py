def manufacture_gifts(gifts_to_produce: list[dict[str, int]]) -> list[str]:
    toys: list[str] = []
    for elm in gifts_to_produce:
        toy, quantity = elm.get("toy"), elm.get("quantity")
        if not isinstance(quantity, int) or quantity <=0:
            continue
        toys.extend([toy]*quantity)

    return toys

from datetime import datetime
import math

def time_until_take_off(from_time:str, take_off_time:str)->int:
    from_timestamp = time_cleaning_elf(from_time)
    take_off_timestamp = time_cleaning_elf(take_off_time)
    return take_off_timestamp - from_timestamp

def time_cleaning_elf(time_raw:str):
    time_not_np = time_raw.replace(" NP", "")
    date_day, dtae_time = time_not_np.split("@")
    year, month, day = map(int,date_day.split("*"))
    hour, minut, secound = map(int,dtae_time.split("|"))
    dt = datetime(year,month,day,hour,minut,secound)
    return math.floor(dt.timestamp())

def match_gloves(gloves: list[dict[str, str]]) -> list[str]:
    left_glove:dict[str,int] = {}
    right_glove:dict[str,int] = {}
    pair: list[dict[str, str]]= []
    for glove in gloves:
        hand = glove['hand']
        color = glove['color']
    
        if hand == "L":
            if color in right_glove and right_glove.get(color)>0:
                pair.append(color)
                right_glove[color] -=1
            else:
                left_glove[color] = left_glove.get(color, 0) + 1
        elif hand == "R":
            if color in left_glove and left_glove.get(color)>0:
                pair.append(color)
                left_glove[color] -=1
            else:
                right_glove[color] = right_glove.get(color, 0) + 1

    return pair

def draw_tree(height:int, 
              ornament:str, 
              frequency:int)->str:
    elem:list[str] = []
    posicion:int = 1
    for i in range(height):
        fila = " "*(height-i-1)

        for j in range(2*i+1):
            if posicion % frequency == 0:
                fila += ornament
            else:
                fila +="*"
            posicion += 1
        elem.append(fila)

    trunk = " " * (height - 1) + "#"
    elem.append(trunk)
    
    return "\n".join(elem)

def find_unique_toy(toy: str) -> str:
  # Code here
  toy_lower = toy.lower()
  for i, char in enumerate(toy_lower):
      if toy_lower.count(char) == 1:
          return toy[i]
  return ''

from typing import Literal

def move_reno(board: str, moves: str) -> Literal['fail', 'crash', 'success']:
    lines = board.strip().split('\n')
    for r, row in enumerate(lines):
        for c, cell in enumerate(row):
            if cell == '@':
                fiel, colm = r, c
                
    recoger = False
    rows = len(lines)
    cols = len(lines[0])
    for move in  moves:
        new_row, new_coll = fiel, colm
        if move == "L":
            new_coll -= 1
        if move == "R":
            new_coll += 1
        if move == "U":
            new_row -= 1
        if move == "D":
            new_row += 1
        if not (0 <= new_row < rows and 0 <= new_coll < cols):
            return 'success' if recoger else 'crash'

        if lines[new_row][new_coll] == '#':
            return 'success' if recoger else 'crash'

        fila, col = new_row, new_coll

        if lines[fila][col] == '*':
            recoger = True

    return 'success' if recoger else 'fail'

if __name__ == "__main__":
    toys_for_qa = [{'toy': "doll", 'quantity': 3},
                   {'toy': "robot", 'quantity': 5},
                   {'toy': "dron", 'quantity': 0}]
    
    print(manufacture_gifts(toys_for_qa))

    takeoff = '2025*12*25@00|00|00 NP'
    print('30 segundos antes:', time_until_take_off('2025*12*24@23|59|30 NP', takeoff))

    gloves = [
                {'hand': 'L', 'color': 'red'},
                {'hand': 'R', 'color': 'red'},
                {'hand': 'R', 'color': 'green'},
                {'hand': 'L', 'color': 'blue'},
                {'hand': 'L', 'color': 'green'}
            ]
    print(match_gloves(gloves))
    print(draw_tree(5,"@", 2))
    print(find_unique_toy("Todos"))
    board = """
    .....
    .*#.*
    .@...
    .....
    """
    print(move_reno(board, "LURD"))