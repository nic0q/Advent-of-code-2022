f = open("aoc7.txt", "r")
lines = f.readlines()
f.close()

lines = list(map (lambda line : line.replace("\n", ""), lines))

def sumDir(stack, index, size):
  for i in range(index + 1):
    stack[i] += int(size)
  return stack

def explore(l):
  stack = [0]
  nivel = 0
  for i in range(len(l)):
    c = l[i].split(" ")
    if c[0] == "$": 
      if c[1] == "cd":
        if c[2] == "..":
          nivel -= 1
        elif c[2] != "/":
          stack.insert(nivel + 1, 0)
          nivel+=1
    elif c[0] != "dir":
      sumDir(stack, nivel, c[0])
  return sum(list(filter(lambda line : line < 100000, stack)))

print(explore(lines))
