"""

Remake by đặc vụ Ân 2k8
p/s dont make this is idiot

Note:
    P : Quân tốt   (Pawn)                   w(White) Trắng
    N : Quân mã    (Knight)                 b(Black) Đen
    B : Quân tượng (Bishop)
    R : Quân xe    (Rock)
    Q : Quân hậu   (Queen)
    K : Quân vua   (King)
    ♔ ♕ ♖ ♗ ♘ ♙ ♚ ♛ ♜ ♝ ♞ ♟
"""
import re

BLACK = '\033[30m'
WHITE = '\033[0m'

class Chess():
    def __init__(self) -> None:
        self.board: list[list[str]] = [
            ['Rb', 'Nb', 'Bb', 'Qb', 'Kb', 'Bb', 'Nb', 'Rb'],
            ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
            ['--', '--', '--', '--', '--', '--', '--', '--'], 
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'], 
            ['--', '--', '--', '--', '--', '--', '--', '--'], 
            ['Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw'], 
            ['Rw', 'Nw', 'Bw', 'Qw', 'Kw', 'Bw', 'Nw', 'Rw'], 
        ]
    
    def printBoard(self):
        #this function use for debug!
        pieces = {
            'Pw': f'{WHITE}♟', 'Pb': f'{BLACK}♟',
            'Nw': f'{WHITE}♞', 'Nb': f'{BLACK}♞',
            'Bw': f'{WHITE}♝', 'Bb': f'{BLACK}♝',
            'Rw': f'{WHITE}♜', 'Rb': f'{BLACK}♜',
            'Qw': f'{WHITE}♛', 'Qb': f'{BLACK}♛',
            'Kw': f'{WHITE}♚', 'Kb': f'{BLACK}♚',
            '--': ' '
        }
        i = 0
        for _ in self.board:
            i+=1
            print(*[pieces[piece] for piece in _],f'{WHITE} {9-i}')
        print(*[WHITE + _ for _ in 'abcdefgh'.upper()], sep = ' ')

class Pawn():
    ...

if __name__ == '__main__':
    Chess = Chess()
    Chess.printBoard()