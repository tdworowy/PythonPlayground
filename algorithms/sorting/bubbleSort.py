from random import randint


class bubbleSort:


    def sort(self,list_):
      list = list_[:]
      resoult = []
      i =1
      while len(resoult) < len(list_):
          for j in range(len(list)-1):
              if list[j] > list[i]:
                 list[j],list[i] = list[i],list[j]
              i +=1
          i =1
          resoult.append(list[-1])
          list = list[:-1]
      return  resoult[::-1]

if __name__ == '__main__':
    list = [randint(0, 1000) for x in range(1000)]
    bs = bubbleSort()
    sortedList = bs.sort(list)
    print(sortedList)

    list.sort()
    print(list)
    assert sortedList == list
