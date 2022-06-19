G_map = ["...", "...", "..."]
#region checking
#region service
def get_vertical(_map, vert): 
    result = ''
    for row in _map:
        result += row[vert]
    return result

def get_diagonal(_map, _dir):
    result = ''
    if _dir: i =  0
    else:    i = -1
    for row in _map:
        result += row[i] 
        if _dir:     i += 1
        if not _dir: i -= 1          
    return result
#endregion

#region main_logic
def check(line):
    i = 1 
    while i < len(line):
        if line[0] == line[i] and line[i] != '.':
            result = line[i]
        else:
            result = ''
            break 
        i += 1
    return result

# Если result == '' тогда проверяем наличие точек, если точки есть, то игра еще не закончена, иначе ничья
def check_all_lines(lines):
    result = ''
    for line in lines:
        result += check(line)
    if result != '':
        result = result[0]
    else:  
        for line in lines:
            if '.' in line:
                return 'C'
        result = 'D'
    return result      
#endregion
def main_check(_map):
    #initialization of possible combinations: 3 - horizontal, 3 - vertical, 2 - diagonal
    lines = []
    lines.append(_map[0])  
    lines.append(_map[1])
    lines.append(_map[2])
    lines.append(get_vertical(_map,0))
    lines.append(get_vertical(_map,1))
    lines.append(get_vertical(_map,2))
    lines.append(get_diagonal(_map, True))
    lines.append(get_diagonal(_map, False))
    
    return check_all_lines(lines)
#endregion
#region gameplay
#region services
def replace_ind(string, index, sub):
    if string[index] != '.':
        return string
    string = list(string)
    string[index] = sub    
    return ''.join(string)
def place(x, y, isX):
    if isX:
        sym = 'X' 
    else:
        sym = 'O'
    G_map[x] = replace_ind(G_map[x], y, sym)
#endregion
def main_loop():
    cont_game = True
    isX_turn = True
    while cont_game:
        print("\n" * 3)  
        for line in G_map:
            print(line)
        if isX_turn:
            print('Ходит X')
        else:
            print('Ходит O')
        x = int(input('Введите строку '))
        y = int(input('Введите столбик '))
        if (x in range(1,4) and y in range(1, 4)) and (G_map[x-1][y-1] == '.'):
            place(x-1, y-1, isX_turn)   
            state = main_check(G_map) 
        else:
            state = 'X' if not isX_turn else 'O'
            print("\n" * 3) 
            print('Неправильно походил')
        if state != 'C':
            print('Победил: ' + state)
            cont_game = False
        else:
            isX_turn = not isX_turn 
#endregion
main_loop()
