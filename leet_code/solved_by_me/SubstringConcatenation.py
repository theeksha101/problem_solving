from typing import List
import collections


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        string_len = len(s)
        words_len = len(words)
        len_word = len(words[0])
        substring_size = len_word * words_len
        word_count = collections.Counter(words)

        def check(i):
            remaining = word_count
            words_used = 0
