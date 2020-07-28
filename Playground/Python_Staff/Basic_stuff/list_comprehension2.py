def create_multipliers():
     return [lambda x, i=i: i * x for i in range(5)]

if __name__ == "__main__":

     M = [[1,2,3],[4,5,6],[7,8,9]]
     N = [[2,2,2],[3,3,3],[4,4,4]]

     test1 = [row[1] for row in M]
     test2 = [M[row][1] for row in (0,1,2)]
     test3 = [M[i][i] for i in range(len(M))]
     print(test1)
     print(test2)
     print(test3)


     test4 = [M[row][col] * N[row][col] for row in range(3) for col in range(3)]

     print(test4)



     for multiplier in create_multipliers():
          print( multiplier(2))

