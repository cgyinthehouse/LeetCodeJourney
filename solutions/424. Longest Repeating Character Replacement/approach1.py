import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = collections.defaultdict(int)
        slow, fast = 0, 0
        max_length = 0
        while fast < len(s):
            freq_map[s[fast]] += 1
            while (fast - slow + 1 - max(freq_map.values())) > k:
                freq_map[s[slow]] -= 1
                slow += 1
            max_length = max(max_length, fast - slow + 1)
            fast += 1
        return max_length
