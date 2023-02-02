def solution(numbers, hand):
    left_hand = [1, 4, 7]
    right_hand = [3, 6, 9]
    
    # numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    # hand = "right"
    # numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    # hand = "left"
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # hand = "right"

    key = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
    dic = {"left" : "*", "right" : "#"}
    global result
    result = ""
    right_check = []
    left_check = []
    hand_check = []
    def check(x):
        global result
        global right_check
        global left_check
        global hand_check
        global result
        right_check = []
        left_check = []
        hand_check = []
        if dic["left"] == "*" and dic["right"] == "#":
            left_check = [3, 0]
            right_check = [3, 2]
        elif dic["left"] == "*" and dic["right"] != "#":
            left_check = [3, 0]
            num2 = dic["right"] - 1
            right_check.append(num2 // 3)
            right_check.append(num2 % 3)
        elif dic["left"] != "*" and dic["right"] == "#":
            right_check = [3, 2]
            num1 = dic["left"] - 1
            left_check.append(num1 // 3)
            left_check.append(num1 % 3)
        elif dic["left"] == 0 and dic["right"] != 0:
            left_check = [3, 1]
            num2 = dic["right"] - 1
            right_check.append(num2 // 3)
            right_check.append(num2 % 3)
        elif dic["left"] != 0 and dic["right"] == 0:
            right_check = [3, 1]
            num1 = dic["left"] - 1
            left_check.append(num1 // 3)
            left_check.append(num1 % 3)
        else:
            num1 = dic["left"] - 1
            left_check.append(num1 // 3)
            left_check.append(num1 % 3)
            num2 = dic["right"] - 1
            right_check.append(num2 // 3)
            right_check.append(num2 % 3)
        if x == 0:
            hand_check = [3, 1]
        else:
            hand_check.append((x - 1) // 3)
            hand_check.append((x - 1) % 3)
        # print(x, dic["left"], dic["right"])
        # print(hand_check,left_check, right_check)
        left_sum = abs(left_check[0] - hand_check[0]) + abs(left_check[1] - hand_check[1])
        right_sum = abs(right_check[0] - hand_check[0]) + abs(right_check[1] - hand_check[1])
        # print(left_sum, right_sum)
        if left_sum > right_sum:
            dic["right"] = x
            result += "R"
        elif left_sum < right_sum:
            dic["left"] = x
            result += "L"
        else:
            # print(hand)
            if hand == "right":
                dic["right"] = x
                result += "R"
            else:
                dic["left"] = x
                result += "L"
                
    for x in numbers:
        if x in left_hand:
            result += "L"
            dic["left"] = x
           # print(x, dic["left"], dic["right"])
        elif x in right_hand:
            result += "R"
            dic["right"] = x
            # print(x, dic["left"], dic["right"])
        else:
            check(x)
            
    return result