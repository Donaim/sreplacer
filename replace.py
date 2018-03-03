
''' READING '''

text = ""
with open("replace.txt", "r", encoding="utf-8") as file:
    text = file.read()

lines = text.split('\n')
# print(lines)

''' PARSING '''

every = []
sep   = []

def first_part(line): return line.split()[0]
def second_part(line): return line.split()[1]
def append_separated(line):
    p1 = first_part(line)
    p2 = second_part(line)
    
    def app(l1, l2, r1, r2):
        sep.append( ( l1 + p1 + r1 , l2 + p2 + r2) )

    app(' ', ' ', ' ', ' ')
    app(' ', '\n', ' ', '\n')

SEPARATED_MODE = "#SEPARATED"
EVERY_MODE     = "#EVERY"
parse_mode = EVERY_MODE


for l in lines:
    if len(l.split()) < 1: continue # l is empty
    if l[0] == '#':
        if first_part(l) == SEPARATED_MODE: parse_mode = l
        else: continue # ignoring lines that starts with '#'

    if len(l.split()) < 2: continue
    
    if parse_mode == EVERY_MODE:
        every.append( (first_part(l), second_part(l)) )
    elif parse_mode == SEPARATED_MODE:
        append_separated(l)

# print(repl)

every = sorted(every, key= lambda tup: -len(tup[0])) # od największego, żeby nie było konflików przy replacement
repl = every + sep

''' WRITING '''


raw = ""

with open("wy-raw.md", "r", encoding="utf-8") as fin:
    for line in fin:
        raw += line

for (s, v) in repl:
    raw = raw.replace(s, v)

with open("wy.md", "w+", encoding="utf-8") as fout:
    fout.write(raw)

