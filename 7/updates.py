
from sys import stdin

class File:
  def __init__(self, name, size, parent) -> None:
    self.name = name
    self._size = size
    self.parent = parent

  def size(self):
    return self._size

  def print(self, indent = 0):
    print("  " * indent, "-", self.name, "(file, size =", self.size(), ")")

  name = ""
  _size = 0
  parent = None


class Dir(File):
  def __init__(self, name, parent) -> None:
    super().__init__(name, 0, parent)
    self.content = []
  
  def size(self):
    sum = 0
    for item in self.content:
      sum += item.size()
    self._size = sum
    return sum

  def print(self, indent = 0):
    print("  " * indent, "-", self.name, "(dir, size =", self.size(), ")")
    
    for item in self.content:
      item.print(indent + 1)

  def add_content(self, file):
    self.content.append(file)
  
  def cd(self, dest):
    if dest == "/":
      return root
    elif dest == "..":
      return self.parent
    else:
      content_names = [item.name for item in self.content]
      
      if dest not in content_names:
        self.add_content(Dir(name, self))
      
      return self.content[content_names.index(dest)]
  
  
  def sum_dirs_lt(self, size):
    sum = 0
    if self._size < size:
      sum += self._size
    
    subdirs = [item for item in self.content if type(item) == Dir]
    for dir in subdirs:
      sum += dir.sum_dirs_lt(size)
    
    return sum
  
  def find_dir_gt(self, size):
    res = -1
    if self.size() > size:
      res = self.size()
    
    subdirs = [item for item in self.content if type(item) == Dir]
    for dir in subdirs:
      dir_res = dir.find_dir_gt(size) 
      res = min(dir_res, res) if dir_res > 0 else res

    return res

  content = []

## Global variables
root = Dir("/", None)

## Read file system structure
wd = root
line = stdin.readline().strip()
while line:
  _, cmd = line.split(" ", 1)

  if (cmd == "ls"):
    line = stdin.readline().strip()
    while line and line[0] != '$':
      info, name = line.split()  
      if info == "dir":        
        wd.add_content(Dir(name, wd))
      else:
        wd.add_content(File(name, int(info), wd))

      line = stdin.readline().strip()

  else:
    _ , dest = cmd.split()
    wd = wd.cd(dest)

    line = stdin.readline().strip()


## Find directories with size < 100'000
root.size()
print(root.sum_dirs_lt(100000))


## Find size of smallest directory that should be deleted
total_space = 70000000
required_space = 30000000
used_space = root.size()

print(root.find_dir_gt(required_space - (total_space - used_space)))

