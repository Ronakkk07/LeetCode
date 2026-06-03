class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        # intervals.sort(key=lambda x: x[0])
        if n <= 1:
            return intervals
        merge = True
        while merge:
            merge = False
            i = 0
            while i < len(intervals) and not merge:
                j = i + 1
                while j < len(intervals):
                    # suppose (1,3), (2,4)
                    a1 = intervals[i][0] # this gives start --> 1
                    b1 = intervals[i][1] # this gives end --> 3
                    a2 = intervals[j][0] # this gives start --> 2
                    b2 = intervals[j][1] # this gives end --> 4

                    if not (b1 < a2 or b2 < a1):
                        ns = min(a1, a2)
                        ne = max(b1, b2)
                        intervals[i][0], intervals[i][1] = ns, ne # this formed the new interval
                        del intervals[j] # removing (2,4) as it got merged
                        merge = True
                        break
                    j += 1
                i += 1
        return intervals