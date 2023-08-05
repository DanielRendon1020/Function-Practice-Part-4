def max_num(x):
    return max(x)

# print(max_num([1, 2, 3, 4, 5]))


def mult_list(x):
    total = 1
    for i in x:
        total *= i
        # ^^^ Same as total = x * i
    return total

# print(mult_list([5, 2, 3]))


def rev_string(x):
    return x[::-1]
    # Slice notation [start:stop:step]

# print(rev_string('hello'))


def num_within(x, y, z):
    if x >= y and x <= z:
        return True
    else:
        return False
    
# print(num_within(5, 2, 8))
# print(num_within(10, 15, 3))


def pascal(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        triangle = [[1], [1, 1]]    #this is as far as I got on my own
        row_number = 2      #currently 2 rows in triangle
        while len(triangle) < n:
            row = []    #new row is a list
            row_prev = triangle[row_number - 1]     #get last list of list (last row in triangle)
            length = len(row_prev)+1    #length of new row (adding 1 more index)
            for i in range(length):     # assigning each index
                if i == 0:
                    row.append(1)   #first number in new row is 1
                elif i > 0 and i < length-1:    #between second index and second to last index...
                    row.append(triangle[row_number-1][i-1] + triangle[row_number-1][i])
                                        # ^^^ THIS IS THE CONFUSING PART!! ^^^ 😡
                else:
                    row.append(1)   #last number in new row is 1
            triangle.append(row)    #put the entire new row together
            row_number += 1     #increment row number

        for row in triangle:
            print(row)      #print each row

        # currently this function returns 'None' at the end of the last row because it never returns anything,
        # nesting a function to generate the triangle then return 'triangle' and making pascal(n) print 
        # each row is the solution!
        

print(pascal(10))



