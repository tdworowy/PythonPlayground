
# def count_consecutive_ones(n):
#     binary = bin(n)
#     elements = [x for x in list(binary)[2:]]
#     s_elements = "".join(elements)
#     sub_lists = s_elements.split("0")
#     return max([len(ele) for ele in sub_lists])
#
# def count_consecutive_ones(n):
#     return max([len(ele) for ele in "".join([x for x in list(bin(n))[2:]]).split("0")])

def count_consecutive_ones(n):
    return max([len(ele) for ele in (bin(n))[2:].split("0")])
if __name__ == "__main__":
    print(count_consecutive_ones(5))
    print(count_consecutive_ones(6))
    print(count_consecutive_ones(439))



