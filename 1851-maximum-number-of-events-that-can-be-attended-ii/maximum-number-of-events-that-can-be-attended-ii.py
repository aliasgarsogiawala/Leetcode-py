from bisect import bisect_right
from functools import lru_cache

class Solution(object):
    def maxValue(self, events, k):
        events.sort()
        start_days = [event[0] for event in events]
        n = len(events)

        @lru_cache(None)
        def dp(i, k):
            if i == n or k == 0:
                return 0

            skip = dp(i + 1, k)
            _, end, value = events[i]
            next_i = bisect_right(start_days, end)
            take = value + dp(next_i, k - 1)

            return max(skip, take)

        return dp(0, k)
