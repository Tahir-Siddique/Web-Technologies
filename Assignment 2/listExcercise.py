list = [1,2,3,4,5,6,7,8,9,0]
list_sum = sum(list)
print(f"Sum : {list_sum}")
average = list_sum/len(list)
print(f"Average : {average}")
list.reverse()
print(f"Reversed => {list}")
print(f"Minimum : {min(list)}\nMaximum : {max(list)}")