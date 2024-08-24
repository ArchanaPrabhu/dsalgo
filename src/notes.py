# sets
my_set = set([1, 2, 3])
my_set.remove(1)
my_set.union([1, 2], [3, 4])
my_set.intersection([1, 2, 3], [4, 3, 2])
my_set.add(4)
if 1 in my_set:
    print("present")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)

my_dict = {'key1': 'val1', 'key2': 'val2'}
my_dict.get('key1')
my_dict['key1'] = 'new_val1'
if 'key1' in my_dict:
    print("present")
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()


my_list = [(1, 2)]
my_list.append((3, 4))

for i in range(1, 10):
    print(i)

arr = [1, 2, 3, 4]
for i in range(0, len(arr)):
    new_array = arr[0:i] + arr

array = [1, 2, 3, 4, 5]
    #    0  1  2  3  4
left = 1
right = 3
my_array = array[left:right + 1] # This is inclusive of left and right index element
# output: [2, 3, 4]