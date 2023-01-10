f = open("aoc7.txt", "r")
lines = f.readlines()
f.close()
lines = list(map (lambda line : line.replace("\n", ""), lines))

# Sum a filesize in all the tree of directories
def add_size(arr, index, size):
  for i in range(index + 1):
    arr[i] += int(size)
  return arr

def explore(l):
  li = [0]
  index = 0
  for i in range(len(l)):
    c = l[i].split(" ")
    if c[1] == "cd":
      if c[2] == "..":
        index -= 1
      else:
        index += 1
        li.insert(index, 0)
    elif c[0] != "dir" and c[0] != "$":
      add_size(li, index, c[0])
  return sum(list(filter(lambda line : line < 100000, li)))

print(explore(lines))
