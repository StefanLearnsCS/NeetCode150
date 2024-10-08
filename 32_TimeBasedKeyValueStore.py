# First solution 10/7/2024 - 20 mins

class TimeMap:

    def __init__(self):
        self.timemap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.timemap[key]) - 1
        timelist = self.timemap[key]

        if not timelist:
            return ""

        if timestamp < timelist[0][-1]:
            return ""

        while l <= r:
            m = (l + r) // 2

            if timelist[m][-1] < timestamp:
                l = m + 1
            elif timelist[m][-1] > timestamp:
                r = m - 1
            else:
                return timelist[m][0]

        return self.get(key, timestamp - 1)
        
"""
Time: O(log n)
Space: O(n)

Attempts: 2, No video!
Mistakes made:
- First attempt I did not set a basecase for the recursion

Learned:
- Recognized recursion correctly.
- when defining init variables, still put self.
- when calling function like in the recursion, use self.
"""