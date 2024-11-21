from checkmate import checkmate  # นำเข้าฟังก์ชัน checkmate จากไฟล์ checkmate.py

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

