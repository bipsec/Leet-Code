class Solution:
  def bestHand(self, ranks, suits) -> str:

    rank = {}
    card = {}
    for i in range(len(ranks)):
      if ranks[i] not in rank:
        rank[ranks[i]] = 1
      else:
        rank[ranks[i]] += 1

    for i in range(len(suits)):
      if suits[i] not in card:
        card[suits[i]] = 1
      else:
        card[suits[i]] += 1
    # print(rank, card)
    result = ["Flush", "Three of a Kind", "Pair", "High Card"]
    vals = list(rank.values())
    suit_val = list(card.values())

    for val in range(len(vals)):
      if 5 in suit_val:
        res = result[0]
      elif 3 in vals or 4 in vals:
        res = result[1]
      elif 2 in vals and 3 not in vals:
        res = result[2]
      else:
        res = result[3]
    return res


s = Solution()
print(s.bestHand(ranks=[13, 2, 3, 1, 9], suits=["a", "a", "a", "a", "a"]))
print(s.bestHand(ranks=[4, 4, 2, 4, 4], suits=["d", "a", "a", "b", "c"]))
print(s.bestHand([10, 10, 2, 12, 9], suits=["a", "b", "c", "a", "d"]))
print(s.bestHand([13, 12, 3, 4, 7], suits=["a", "d", "c", "b", "c"]))
