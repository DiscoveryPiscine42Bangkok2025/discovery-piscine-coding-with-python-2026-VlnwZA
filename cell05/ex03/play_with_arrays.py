#!/usr/bin/env python3
arr = [2, 8, 9, 48, 8, 22, -12, 2]
print(arr)
new_arry = [x + 2 for x in arr]
new_arr_uper5 = [x for x in new_arry if x >= 5]
unique_arr = set(new_arr_uper5)
print(unique_arr)