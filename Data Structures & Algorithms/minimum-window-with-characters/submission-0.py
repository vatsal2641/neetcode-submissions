class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # Characters and their required frequencies
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        # Current window frequencies
        count_window = {}

        left = 0
        formed = 0
        required = len(count_t)

        min_len = float("inf")
        ans = ""

        for right in range(len(s)):

            # Add s[right] to window
            c = s[right]
            count_window[c] = count_window.get(c, 0) + 1

            # This character has now satisfied its required frequency
            if c in count_t and count_window[c] == count_t[c]:
                formed += 1

            # Try shrinking the window
            while formed == required:

                # Current window is valid
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left:right + 1]

                # Remove s[left]
                c = s[left]
                count_window[c] -= 1

                # Window is no longer satisfying this character
                if c in count_t and count_window[c] < count_t[c]:
                    formed -= 1

                left += 1

        return ans

                    
