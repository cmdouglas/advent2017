from util import advent_input

def checksum(rows):
    return sum(max(row) - min(row) for row in rows)
    
def checksum2(rows):
    total = 0
    for (i, row) in enumerate(rows):
        for item1 in row:
            for item2 in row:
                if item1 != item2 and item1 % item2 == 0:
                    print(f"row {i} - {item1}, {item2}")
                    total += item1 // item2
    
    return total
        
    
if __name__ == '__main__':
    with advent_input(2) as f:
        txt = f.read()
        rows = txt.split('\n')
        rows = [[int(num) for num in row.split('\t')] for row in rows]
        print(checksum(rows))
        print(checksum2(rows))
        