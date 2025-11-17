def permuted_choice_1(key_binary_table):

    # removing bits in the position which are multiples of 8(8,16..64)
    for i in range(1, 9):
        j = (8 * i) - (i * 1)
        key_binary_table.pop(j)

    # mapping with a permutation table
    pc1_permutation_result = mapping(permuted_choice_1_ptable, key_binary_table)

    # splitting result into two 28 bit lists
    pc1_result_1 = pc1_permutation_result[:28]
    pc1_result_2 = pc1_permutation_result[28:]

    return pc1_result_1, pc1_result_2  # this returns a tuple (pc1_result_1,pc1_result_2)
