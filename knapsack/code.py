global previous_answers
import sys
import copy
sys.setrecursionlimit(150000)
def solve(first_n, max_weight, items):
    global previous_answers
    if previous_answers[first_n][max_weight] != None:
        return previous_answers[first_n][max_weight]
    item_to_consider = items[first_n - 1]
    if first_n == 1:
        if max_weight >= item_to_consider["weight"]:
            previous_answers[first_n][max_weight] = [item_to_consider["value"], [item_to_consider]]
            return [item_to_consider["value"], [item_to_consider]]
        else:
            previous_answers[first_n - 1][max_weight] = [0,[]]
            return [0,[]]
    if max_weight >= item_to_consider["weight"]:
        a = solve(first_n - 1, max_weight - item_to_consider["weight"], items)
        a_value = a[0] + item_to_consider["value"]
        a_items = a[1]
        a_items.append(item_to_consider)
        b = solve(first_n - 1, max_weight, items)
        b_value = b[0]
        b_items = b[1]
        max_value = max(a_value, b_value)
        if max_value == a_value:
            previous_answers[first_n][max_weight] = copy.deepcopy([a_value, a_items])
            return [a_value, a_items]
        else:
            previous_answers[first_n][max_weight] = copy.deepcopy([b_value, b_items])
            return [b_value, b_items]
    else:
        previous_answers[first_n - 1][max_weight] = [0,[]]
        return [0,[]]
        # a = solve(first_n - 1, max_weight, items)
        # previous_answers[first_n][max_weight] = copy.deepcopy(a)
        # return a

while(True):
    global previous_answers
    try:
        max_weight, num_items = map(int, input().split())
    except:
        break
    items = []
    previous_answers = [[None for i in range(max_weight + 1)] for i in range(num_items + 1)]
    for i in range(num_items):
        value, weight = map(int, input().split())
        items.append({"value": value, "weight": weight, "item_num":i})
    items.sort(key=lambda x: x["weight"], reverse=True)
    items = solve(num_items, max_weight, items)[1]
    print(len(items))
    string = ""
    for item in items:
        string += str(item["item_num"]) + " "
    print(string[:-1])