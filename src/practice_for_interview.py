from collections import deque


def test():
    # arr = [0 for _ in range(100)]
    # arr.append(10)
    # arr.insert(1, 100)
    # arr.extend([5, 6])
    # arr.remove(10)
    # arr.pop()
    # arr.pop(1)
    # len(arr)

    # list_tuples = [(1, "apple"), (2, "banana")]
    # for num, fruit in list_tuples:
    #     print(num, fruit)
    #
    # for index, (num, fruit) in enumerate(list_tuples):
    #     print(index, num, fruit)
    #
    # pairs = [(1, 'a'), (3, 'c'), (2, 'b')]
    # sorted_pairs = sorted(pairs)
    #
    # graph = {'A': [('B', 5), ('C', 10)],
    #          'B':[('D', 10), ('E', 90)]}
    #
    # list_dict_practice = [
    #     {"carrot", 320},
    #     {"banana", 200},
    #     {"apple", 20}
    # ]
    # for item in list_dict_practice:
    #     print(list(item))
    #
    # # list_dict_practice.sort(key=lambda x: list(x)[0])
    # print(list_dict_practice)
    #
    # temp_set =  {"pineapple", 120}
    # temp_set.add(130)
    #
    # if 120 in temp_set:
    #     return 100

    my_dict = {1: 300, 2: 400}
    for key, values  in my_dict.items():
        print(key, values)


    # create a map for every alphabet

    alpha_freq = { i: 0 for i in range(26)}
    print(alpha_freq)

    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    q.pop()
    print(q)
    q[0] = 100
    print(q)

    for i in range(len(q)):
        q[i] = i * 10

    print(q)

    # initialize a 2D matrix with 0s.
    maze = []

if __name__ == "__main__":
    test()