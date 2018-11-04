#!/usr/bin/python3
import sys

def main(argv):
  mode = None
  user_args = sys.argv[1:]
  if len(user_args) != 2 and len(user_args) != 3:
    raise IndexError("price.txt and gift card value must be supplied on the command line.")
  if len(user_args) == 3:
    mode = user_args.pop()
  target, file_name = int(user_args.pop()), user_args.pop()
  price_dict, price_list = getPrices(file_name)
  
  if mode:
    result = threeSumClosest(price_list, target)
    if isinstance(result, str):
      print(result)
    else:
      print("{0} {1}, {2} {3}, {4} {5}".format(
        price_dict[result[0]].pop(),result[0], 
        price_dict[result[1]].pop(), result[1],
        price_dict[result[2]].pop(), result[2]))
  else:
    result = twoSumClosest(price_list, target)
    if isinstance(result, str):
      print(result)
    else:
      print("{0} {1}, {2} {3}".format(
        price_dict[result[0]].pop(),result[0], 
        price_dict[result[1]].pop(), result[1]))

def getPrices(file_name):
  price_dict, price_list = {}, []
  with open(file_name, "r") as f:
    for line in f:
      line = line.rstrip().split(',')
      item = line[0]
      value = int(line[1])
      if value in price_dict:
        price_dict[value].append(item)
      else:
        price_dict[value] = [item]
      price_list.append(value)
  return price_dict, price_list

def twoSumClosest(prices, target):
  if not prices or len(prices) <2:
      return "Not possible"
  l, r = 0, len(prices) - 1
  diff = float('inf')
  result = "Not possible"
  while l < r:
      sum_price = prices[l] + prices[r]
      if sum_price == target:
          return [prices[l],prices[r]]
      if sum_price < target and target - sum_price < diff:
          diff = target -  sum_price
          result = [prices[l],prices[r]]
      if sum_price < target:
          l+=1
      elif sum_price > target:
          r -= 1
  return result

def threeSumClosest(prices, target):
    result = "Not possible"
    diff = float('inf')
    for i in range(len(prices) - 2):
        j, k = i+1, len(prices) - 1
        while j < k:
            sum1 = prices[i] + prices[j] + prices[k]
            if sum1 == target:
                return [prices[i], prices[j], prices[k]]
            if sum1 < target and target - sum1 < diff:
                diff = target - sum1
                result = [prices[i], prices[j], prices[k]]
            if sum1 < target:
                j += 1
            elif sum1 > target:
                k -= 1
    return result

if __name__ == "__main__":
   main(sys.argv[1:])