class Queue:
  def __init__ (self, capacity):
    self.internalArray = [None] * capacity 
    self.start = 0
    self.end = capacity - 1
    self.size = 0

  def add (self, item):
    if (self.end != (len(self.array) - 1)):
      temp = self.end + 1

    else:
      temp = 0

    if (self.array[temp] == None):
      self.end = temp
      self.array [self.end] = value
      self.size += 1
      print ("{}has been added to the queue.".format(value))
    else:
      print ("Queue is full")

  def remove (self):
    print (self.array [self.start])
    self.arrary [self.start] = None
    self.size = 1
    if (self.start != (len(self.array) -1 )):
      self.start += 1
    else:
      self.start = 0

newQueue = Queue(8)
print(newQueue.array)
newQueue.add ('a')
print(newQueue.array)
newQueue.add ('c')
print(newQueue.array)
newQueue.remove ()
print(newQueue.array)




