def count(target, position):
    count = 0
    v = abs(position - target)
    count += (v // 3) + (v % 3)
    position = target

    return count, position


def solution(numbers, hand):
    answer = ''

    # initial
    left_position = 10
    right_position = 12

    for i in numbers:
        if i == 0:
            i = 11

        if i == 1 or i == 4 or i == 7:
            left_position = i
            answer = answer + "L"

        elif i == 3 or i == 6 or i == 9:
            right_position = i
            answer = answer + "R"

        else:
            l_count, left_change = count(i, left_position)
            r_count, right_change = count(i, right_position)
            if hand == "left":
                if l_count > r_count:
                    right_position = right_change
                    answer = answer + "R"
                else:
                    left_position = left_change
                    answer = answer + "L"

            elif hand == "right":
                if r_count > l_count:
                    left_position = left_change
                    answer = answer + "L"
                else:
                    right_position = right_change
                    answer = answer + "R"


    return answer