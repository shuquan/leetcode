class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        # Use recursion to resolve the problem
        # The algorithm complexity is high due to it has to iterate from one
        # for each call given k, n. Another optimization is passing another
        # parameter in mycombinationSum3(self, k, n, start) for tracking.
        if k < 0 or k > 0 and ((10 - k) + 9)*k/2 < n:
            return []
        elif k == 1 and n < 10:
			return [[n]]
        # Check the worst recursion sitiation and try to avoid it.
        elif (1 + k)*k/2 == n:
            return [range(1, k + 1)]
        # Check the worst recursion sitiation and try to avoid it.
        elif ((10 - k) + 9)*k/2 == n:
            return [range(9, 9 - k, -1)]
        else:
            l = []
            for i in range(n):
                if i > 0 and i <= n/2 and i < 10:
                    for j in self.combinationSum3(k - 1, n - i):
                        # If the number is not unique, then skip it.
                        # If the return list is empty, then skip it.
                        if i not in j and len(j) != 0:
                            j.append(i)
                            l.append(sorted(j))
            # If the length of final list is less than 2, then return it.
            if len(l) < 2:
                return l
            else:
                # Drop any duplicated element.
                c = []
                for i in l:
                    if i not in c:
                        c.append(i);
                return c
