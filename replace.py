
''' READING '''

text = ""
with open("replace.txt", "r", encoding="utf-8") as file:
    text = file.read()

lines = text.split('\n')
# print(lines)


''' PARSING '''

repl = []

def first_part(line): return line.split()[0]
def second_part(line): return line.split()[1]

SEPARATED_MODE = "#EXACT"
EVERY_MODE     = "#EVERY"
parse_mode = EVERY_MODE

for l in lines:
    if len(l.split()) < 1: continue # l is empty
    if l[0] == '#':
        if first_part(l) == SEPARATED_MODE: parse_mode = l
        else: continue # ignoring lines that starts with '#'

    if len(l.split()) < 2: continue
    
    if parse_mode == EVERY_MODE:
        repl.append( (first_part(l), second_part(l)) )
    elif parse_mode == SEPARATED_MODE:
        repl.append( (' ' + first_part(l) + ' ', ' ' + second_part(l) + ' ') )
        repl.append( ('\t' + first_part(l) + '\t', '\t' + second_part(l) + '\t') )
        # print(repl[-1])

# print(e_codes, e_values)


''' WRITING '''

# fin  = open("replace.txt", "r", encoding="utf-8")
fin  = open("wy-raw.md", "r", encoding="utf-8")
fout = open("wy.md", "w+", encoding="utf-8")

class mem(object):
    def __init__(self):
        self.data = ""
    def add(self, c):
        self.data += c
    def clear(self): self.data = ""
    def write(self, file): file.write(self.data)
    def parse_char(self, c):
        self.add(c)
        for (s, v) in repl:
            if self.data == s: 
                fout.write(v)
                return True
            if self.data in s: return True

ememory = mem()
for l in fin:  
    for ch in l: 
        if not ememory.parse_char(ch): 
            ememory.write(fout)
            ememory.clear()

fin.close()
fout.close()

