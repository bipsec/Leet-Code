class Solution:
    def fun1(self, nums):
        subjects = ["math", "science","biology", "stat"]
        code = [101.000924, 102.27672442, 103.428734555555555554, 104.4285789]

        subjects_dict = dict(zip(subjects, code))
        # return subjects_dict
        # i = 0
        # for subject in subjects:
        #     # print(i, subject)
        #     i += 1

        # for subject in enumerate(subjects):
        #     print(subject)

        # for i in range(0, len(subjects)-1):
        #     subjects[i]= subjects[i].upper()
        # print(subjects)

        subjects = list(map(str.upper, subjects))
        code_1 = list(map(round, code, range(1,3)))

        result = list(map(lambda x,y: (x,y), code, subjects, ))
        return result

s = Solution()
print(s.fun1([4, 3, 2, 7, 8, 2, 3, 1]))
