#reverse함수
def reverse(xs) :
         if xs == [] :
                  return[]
         else :
                  return reverse(xs[1:])+[xs[0]]


def is_list(x) :
         return isinstance(x,list)

#복습 1번
def deep_reverse(xs) :
         if xs==[] :
                  return []
         elif is_list(xs[0]) == True :
                  return deep_reverse(xs[1:])+[deep_reverse(xs[0])]
         else :
                  return deep_reverse(xs[1:])+[xs[0]]
print(deep_reverse([1,[2,3,[4,[5,6]]]]))
         
#복습 2번
def symmetric_square_matrix(xs) :
         for i in range(0,(len(xs)-1)) :
                  for j in range(1+i,(len(xs)-1)) :  
                           if not xs[i][j]==xs[j][i] :
                                    return False
         return True

print(symmetric_square_matrix([[1,9,5,11],[9,4,7,3],[5,7,-7,8],[11,3,8,6]]))


#복습 3번
def check_sudok(xs) :
         for i in range(0,(len(xs)-2)) :
                  for j in range(0,(len(xs)-1)) :
                           if i!=j :
                                    if xs[i][i] == xs[i][j] or xs[i][i] == xs[j][i] :
                                             return False
         return True
print(check_sudok([[1,2,3],[4,5,6],[7,8,9]]))
         

#복습 4번
def list_product(xs) :
         product = 1
         if not xs == [] :
                  for i in range(0,(len(xs))) :
                           product = product*xs[i]
         return product
print(list_product([3,5,2,8]))


#복습 5번
def greatest(xs) :
         if xs == [] :
                  return None
         a = xs[0]
         for i in range(1,(len(xs)-1)) :
                  if a < xs[i] :
                           a = xs[i]
         return a
print(greatest([5,2,3,6,4,3,7,5,8,2]))
def total(xs,b) :
         a = 0
         for i in range(0,b+1) :
                  a = a + xs[i]
         return a
         


b = []
#복습 6번
def longest_repetition(xs) :
         if xs==[] :
                  return None
         a = 1
         for i in range(0,len(xs)-1) :
                  if xs[i]==xs[i+1] :
                           a+=1
                  else :
                           b.append(a)
                           return longest_repetition(xs[i+1:])
         print(b,total(b,b.index(greatest(b))))
         print(xs[total(b,b.index(greatest(b)))],greatest(b))


print(longest_repetition([5,5,4,4,4,4,4,2,2,2,2,7,8,4,4,3,3,3]))                           
                  
#def deep_count(xs) :
         
         
         
         

         
