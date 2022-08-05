class Solution:
  def topKFrequent(self, words, k):
    seen = {}
    new_dict = {}
    dupes = []
    words = sorted(words)

    for i in range(len(words)):
      if words[i] not in seen:
        seen[words[i]] = 1
      else:
        seen[words[i]] += 1

    seen = dict(sorted(seen.items(), key=lambda kv: kv[1], reverse=True))

    for key, value in seen.items():
      dupes.append(key)
    return dupes[:k]


s = Solution()
print(s.topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2))
print(s.topKFrequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4))
print(s.topKFrequent(words=["the", "day", "day", "the"], k=1))
