###条件を整理するにはどうしたらいいのか、事前に紙とかに書き出すのが良い？


# time: O(N)
# space: O(1)
class Solution:
    def myAtoi(self, s: str) -> int:

        if len(s) == 0:
            return 0

        digit_num_list = [str(i) for i in range(0, 10)]
        atoi_start_idx = 0
        atoi_end_idx = 0
        int_sign = ""

        s_index = 0
        while s_index < len(s) and s[s_index] == " ":
            s_index += 1

        if s_index + 1 == len(s):
            return int(s[s_index]) if s[s_index] in digit_num_list else 0
        elif s_index == len(s):
            return 0

        if s[s_index] == "+" or s[s_index] == "-":
            int_sign = s[s_index]
            s_index += 1
            atoi_start_index = s_index
        elif s[s_index] in digit_num_list:
            int_sign = "+"
            atoi_start_index = s_index
            s_index += 1
        else:
            return 0

        while s_index < len(s) and s[s_index] in digit_num_list:
            s_index += 1

        atoi_end_index = s_index - 1

        if atoi_start_index == atoi_end_index + 1:
            return 0

        atoi_num = (
            int(s[atoi_start_index : atoi_end_index + 1])
            if int_sign == "+"
            else -int(s[atoi_start_index : atoi_end_index + 1])
        )

        if atoi_end_index - atoi_start_index + 1 >= 10:
            if 2**31 - 1 < atoi_num:
                return 2**31 - 1
            elif -(2**31) > atoi_num:
                return -(2**31)

        return atoi_num
