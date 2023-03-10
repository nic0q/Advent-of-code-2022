f = open("aoc7.txt", "r")
lines = f.readlines()
f.close()
lines = list(map(lambda line : line.replace("\n", ""), lines))

TOTAL = 70000000
UNUSED = 30000000

# Sum a filesize in all the tree of directories
def add_size(arr, index, size):
  for i in range(index + 1):
    arr[i] += int(size)
  return arr

# i: Console commands
# o: array of disks
def explore(l):
  li = [0] # "/" root directory
  index = 0
  for i in l:
    c = i.split(" ")
    if i == "$ cd ..":
      index -= 1
    elif c[0] != "$" and c[0] != "dir":
      add_size(li, index, c[0])
    elif c[1] == "cd":
      index += 1
      li.insert(index, 0)      
  return li

# AOC Part 1
# i: array of disks
# o: Sum of all the directories with a total size of at most 100000
def size(li):
  return sum(list(filter(lambda line : line < 100000, li)))

print(size(explore(lines)))

# AOC Part 2

# i: array of disks
# o: smallest directory for freeup space
def to_be_deleted(li):
  required = UNUSED - (TOTAL - li[0])
  return min(list(filter(lambda s : s > required, li)))

print(to_be_deleted(explore(lines)))