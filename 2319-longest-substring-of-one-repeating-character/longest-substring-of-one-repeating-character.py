class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        
        # Segment tree structures to store segment properties
        max_len = [0] * (4 * n)
        pref_len = [0] * (4 * n)
        suff_len = [0] * (4 * n)
        pref_char = [''] * (4 * n)
        suff_char = [''] * (4 * n)

        def combine(node, l, r, mid):
            left_node = 2 * node
            right_node = 2 * node + 1
            left_size = mid - l + 1
            right_size = r - mid

            # Inherit basic state from child nodes
            pref_char[node] = pref_char[left_node]
            pref_len[node] = pref_len[left_node]
            suff_char[node] = suff_char[right_node]
            suff_len[node] = suff_len[right_node]
            max_len[node] = max(max_len[left_node], max_len[right_node])

            # Check boundary condition where left and right segments meet
            if suff_char[left_node] == pref_char[right_node]:
                merged_len = suff_len[left_node] + pref_len[right_node]
                if merged_len > max_len[node]:
                    max_len[node] = merged_len
                
                # If entire left child is a single repeating char, extend prefix length
                if pref_len[left_node] == left_size:
                    pref_len[node] = left_size + pref_len[right_node]

                # If entire right child is a single repeating char, extend suffix length
                if suff_len[right_node] == right_size:
                    suff_len[node] = right_size + suff_len[left_node]

        def build_tree(node, l, r):
            if l == r:
                max_len[node] = 1
                pref_len[node] = 1
                suff_len[node] = 1
                pref_char[node] = s[l]
                suff_char[node] = s[l]
                return

            mid = (l + r) // 2
            build_tree(2 * node, l, mid)
            build_tree(2 * node + 1, mid + 1, r)
            combine(node, l, r, mid)

        def update_tree(node, l, r, idx, ch):
            if l == r:
                pref_char[node] = ch
                suff_char[node] = ch
                return

            mid = (l + r) // 2
            if idx <= mid:
                update_tree(2 * node, l, mid, idx, ch)
            else:
                update_tree(2 * node + 1, mid + 1, r, idx, ch)
            combine(node, l, r, mid)

        # Step 1: Build the segment tree initially
        build_tree(1, 0, n - 1)

        # Step 2: Process all query updates
        result = []
        for idx, ch in zip(queryIndices, queryCharacters):
            update_tree(1, 0, n - 1, idx, ch)
            result.append(max_len[1])

        return result