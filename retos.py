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

def max_depth(s: str) -> int:
  # Code here
    actual: int = 0
    maximo: int = 0
    for ch in s:
        if ch == '[':
            actual += 1
            maximo = max(maximo, actual)
        if ch == ']':
            actual -= 1
            if actual < 0:
                return -1
    
    return maximo if actual == 0 else -1 

def find_unsafe_gifts(warehouse: list[str]) -> int:
    count:int = 0
    rows: int = len(warehouse)
    cols:int = len(warehouse[0])

    for r, row in enumerate(warehouse):
        for c, cell in enumerate(row):

            if cell != '*':
                continue

            flags = False

            if r>0 and warehouse[r-1][c] == '#':
                flags = True
            if r<rows-1 and warehouse[r+1][c] == "#":
                flags = True
            if c>0 and warehouse[r][c-1] == '#':
                flags = True
            if c<cols-1 and warehouse[r][c+1] == '#':
                flags = True
            
            if not flags:
                count +=1
    
    return count

def elf_battle(elf1: str, elf2: str) -> int:
    # Code here
    live_elf1 = 3
    live_elf2 = 3

    for ch, ch2 in zip(elf1, elf2):
        if ch == 'A':
            if ch2 != 'B':
                live_elf2 -=1
        elif ch == 'F':
            live_elf2 -=2
        
        if ch2 == 'A':
            if ch != 'B':
                live_elf1 -=1
        elif ch2 == 'F':
            live_elf1 -=2

        if live_elf1 <= 0 or live_elf2<=0:
            break

    if live_elf1<=0 and live_elf2<=0:
        return 0
    
    if live_elf1>live_elf2:
        return 1
    if live_elf1<live_elf2:
        return 2
    
    return 0

def run_factory(factory: list[str]) -> str:
    # Code here
    rows:int = len(factory)
    colms: int = len(factory[0])
    r, c = 0, 0
    visited = set()

    while True:
        if r<0 or r >= rows or c<0 or c>= colms:
            return 'broken'
        if (r,c) in visited:
            return 'loop'
        
        visited.add(r,c)

        cell = factory[r][c]

        if cell == ".":
            return 'completed'
        
        if cell == '>':
            c+=1
        elif cell == '<':
            c-=1
        elif cell == '^':
            r-=1
        elif cell == "v":
            r+=1

def find_gift_path(workshop: dict[any], gift: str | int | bool) -> list[str]:
    # Code here
    for k, v in workshop.items():
        if v == gift:
            return [k]
        if isinstance(v, dict):
            agame = find_gift_path(v, gift)
            if agame:
                return [k]+agame
            
    return []

def draw_table(data: list[dict[str, str | int]], sortBy: str) -> str:
    columns = list(data[0].keys())

    sorted_data = sorted(data, key=lambda x: x[sortBy])

    widths = []
    for i, col in enumerate(columns):
        header = chr(65 + i) 
        max_len = max(
            len(header),
            max(len(str(row[col])) for row in sorted_data)
        )
        widths.append(max_len + 2)

    def horizontal_line():
        return '+' + '+'.join('-' * w for w in widths) + '+'

    header_row = (
        '|' +
        '|'.join(
            ' ' + chr(65 + i).ljust(widths[i] - 1)
            for i in range(len(widths))
        ) +
        '|'
    )

    rows = []
    for row in sorted_data:
        rows.append(
            '|' +
            '|'.join(
                ' ' + str(row[col]).ljust(widths[i] - 1)
                for i, col in enumerate(columns)
            ) +
            '|'
        )

    return '\n'.join(
        [horizontal_line(), header_row, horizontal_line(), *rows, horizontal_line()]
    )


def pack_gifts(gifts: list[int], maxWeight: int) -> int | None:
    # Code here
    sleighs: int = 1
    currentWeight: int = 0
    if len(gifts) == 0:
        return 0
    for gift in gifts:
        if gift > maxWeight:
            return None
        if currentWeight+gift <= maxWeight:
            currentWeight += gift
        
        else:
            sleighs += 1
            currentWeight = gift
            
    return sleighs


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
    print(max_depth(']'))
    print(max_depth('[[[]]]'))

    print(
        draw_table(
        [
            { "gift": 'Book', "quantity": 5 },
            { "gift": 'Music CD', "quantity": 1 },
            { "gift": 'Doll', "quantity": 10 }
        ],
        'quantity'
        )
    )