global K
import sys
import copy
def solve(W, items):
    global K
    # print(K)
    n = len(items)
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif items[i-1]["weight"] <= w: 
                # print(items[i-1]["value"])
                # print(K[i-1][w-items[i-1]["weight"]])
                K[i][w] = max(items[i-1]["value"] + K[i-1][w-items[i-1]["weight"]],  K[i-1][w])
            else: 
                K[i][w] = K[i-1][w] 
    return K[n][W] 
  

while(True):
    global K
    try:
        max_weight, num_items = map(int, input().split())
    except:
        break
    items = []
    K = [[0 for i in range(max_weight + 1)] for i in range(num_items + 1)]
    for i in range(num_items):
        value, weight = map(int, input().split())
        items.append({"value": value, "weight": weight, "item_num":i})
    # done inputing values
    max_value = solve(max_weight, items)
    if max_value == 0:
        print(0)
        print("\n")
    else:
        num_items = 1
        current_weight = max_weight
        current_value = max_value
        n = len(items)
        items_chosen = []
        while current_value != 0:
            if current_weight >= items[n - 1]["weight"]:
                if K[n - 1][current_weight] == current_value:
                    n = n - 1
                elif K[n - 1][current_weight - items[n - 1]["weight"]] == current_value - items[n - 1]["value"]:
                    items_chosen.append(n - 1)
                    current_weight -= items[n - 1]["weight"]
                    current_value -= items[n - 1]["value"]
                    n = n - 1
            else:
                n = n -1
    print(len(items_chosen))
    string = ""
    for item in items_chosen:
        string += str(item) + " "
    print(string[:-1])
