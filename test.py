print(ord("a"))
from openpyxl.utils import get_column_letter
print(get_column_letter(ord("H")))

print(chr(97+(ord("c")-97)))
print((int(ord("c")-97)))
print(((26*(int(ord("a")-97)+1))+int(ord("p")-97))) # AP

from app import getcolumns

print(getcolumns("a","B"))
print(ord("b"))