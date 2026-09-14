class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([(beginWord, 1)])
        st = set(wordList)
        if endWord not in st:
            return 0
        st.discard(beginWord)
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                original = word[i]
                for ch in range(ord('a'), ord('z') + 1):
                    word = word[:i] + chr(ch) + word[i+1:]

                    if word in st:
                        st.remove(word)
                        q.append((word, steps + 1))
                word = word[:i] + original + word[i+1:]
        return 0