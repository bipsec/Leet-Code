class Solution:
    def findRestaurant(self, list1, list2):
        dupes = {}

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    dupes[list1[i]] = i + j

        val = min(list(dupes.values()))

        res = []
        for key, value in dupes.items():
            if val == value:
                res.append(key)

        return res


s = Solution()
print(s.findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
                       list2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
print(
    s.findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"], list2=["KFC", "Shogun", "Burger King"]))
print(s.findRestaurant(list1=["happy", "sad", "good"], list2=["sad", "happy", "good"]))
