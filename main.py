

# s = aaaabcca

# a: 5, b: 1, c: 2



# def strcounter(s):
#     for sym in s:
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)
#
# s = 'cccccc' N ** 2


# def strcounter(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)
# s = 'aaabc'
# # O(N) = M * N
# # N * N - худший случай, если все символы уникальны
# strcounter(s)



def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    print('hello!')
    print(syms_counter)

#O(N) = N

strcounter('aaaabca')