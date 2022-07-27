
# @param s string字符串
# @return int整型
#
class Solution:
    def romanToInt(self, s):
        # write code here

        result = 0

        roman_int_mapper = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


        break_poll = 0
        for index, single_s in enumerate(s):
            print(index, single_s)

            if break_poll == 1:
                break_poll = 0
                continue

            if index + 1 == len(s):
                single_s_int = roman_int_mapper[single_s]
                result += single_s_int
                break

            next_index_single_s = s[index + 1]

            if single_s is "I":
                if next_index_single_s is "V":
                    break_poll=1
                    single_s_int = 4
                elif next_index_single_s is "X":
                    break_poll = 1
                    single_s_int = 9
                else:
                    single_s_int = roman_int_mapper[single_s]

            elif single_s is "X":
                if next_index_single_s is "L":
                    break_poll = 1
                    single_s_int = 40
                elif next_index_single_s is "C":
                    break_poll = 1
                    single_s_int = 90
                else:
                    single_s_int = roman_int_mapper[single_s]

            elif single_s is "C":
                if next_index_single_s is "D":
                    break_poll = 1
                    single_s_int = 400
                elif next_index_single_s is "M":
                    break_poll = 1
                    single_s_int = 900
                else:
                    single_s_int = roman_int_mapper[single_s]

            else:
                single_s_int = roman_int_mapper[single_s]

            result += single_s_int

        return result


# solution = Solution()
# result = solution.romanToInt("LVIII")
# print(result)