
change_dict = {}

#recursive
def findMinCoins(coin_vals, change):
	min_coins = change
	if change in coin_vals:
		return 1
	elif change in change_dict:
		return change_dict[change]
	else:
		for coin in [c for c in coin_vals if c <=change]:
			poss_num_coins = 1+ findMinCoins(coin_vals,change-coin)
			min_coins = min(min_coins,poss_num_coins)
			change_dict[change] = min_coins

	return min_coins

#lookup table dp
def dpCoins(coin_vals, change, min_change):
	coins = {x:[0]*len(coin_vals) for x in range(change+1)}
	
	for num in range(change+1):
		poss_min = num
		for val in [c for c in coin_vals if c <= num]:
			if min_change[num-val] + 1 < poss_min:
				poss_min = min_change[num-val] + 1 
				coins[num] = [x for x in coins[num-val]]
				coins[num][coin_vals.index(val)]+=1
		min_change[num] = poss_min
	return coins[num]


# print(findMinCoins([1,5,10,25],78))
change = 78
min_change = [0 for i in range(change+1)]
print(dpCoins([1,5,10,21,25],change,min_change))
