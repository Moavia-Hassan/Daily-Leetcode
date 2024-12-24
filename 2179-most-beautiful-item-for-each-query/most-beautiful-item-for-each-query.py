class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        # Sort items by price
        items.sort()

        # Pair each query with its index and sort queries by the query value
        queries = sorted([(q, i) for i, q in enumerate(queries)])

        max_bea = 0  # maximum beauty
        j = 0

        res = [0] * len(queries)

        for q, i in queries:
            # Update max_bea for all items with pr ice <= current query value
            while j < len(items) and items[j][0] <= q:
                max_bea = max(max_bea, items[j][1])
                j += 1

            # maximum beauty for the current query
            res[i] = max_bea

        return res