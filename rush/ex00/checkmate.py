def checkmate(board):
    #ฟังก์ชันตรวจสอบการโจมตีของ King
    rows = board.splitlines()
    size = len(rows)
    king_position = None

    #ค้นหาตำแหน่งของ King ('K')
    for i in range(size):
        for j in range(size):
            if rows[i][j] == 'K':
                king_position = (i, j)
                break
        if king_position:
            break

    if not king_position:
        print("Error: No King found")
        return

    #ตรวจสอบตำแหน่งว่าถูกโจมตีหรือไม่
    def is_attacked(x, y):
        # ตรวจสอบ Pawn (P) ที่โจมตีในแนวทแยง
        if (x > 0 and y > 0 and rows[x - 1][y - 1] == 'P') or \
           (x > 0 and y < size - 1 and rows[x - 1][y + 1] == 'P'):
            return True

        #การตรวจสอบ Bishop (B) และ Queen (Q) ที่โจมตีในแนวทแยง
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x, y
            while 0 <= nx + dx < size and 0 <= ny + dy < size:
                nx += dx
                ny += dy
                if rows[nx][ny] in ['B', 'Q']:
                    return True
                if rows[nx][ny] != '.':
                    break

        #การตรวจสอบ Rook (R) และ Queen (Q) ที่โจมตีในแนวนอนและแนวตั้ง
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x, y
            while 0 <= nx + dx < size and 0 <= ny + dy < size:
                nx += dx
                ny += dy
                if rows[nx][ny] in ['R', 'Q']:
                    return True
                if rows[nx][ny] != '.':
                    break

        return False

    # ตรวจสอบว่ากษัตริย์ถูกโจมตีหรือไม่
    if is_attacked(*king_position):
        print("Success")
    else:
        print("Fail")

def main():
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()
