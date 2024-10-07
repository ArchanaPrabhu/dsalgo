class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        endWordSet = set()
        for i in endWord:
            endWordSet.add(i)
        
        begin_dict = {c: 0 for c in beginWord}

        for i in beginWord:
            begin_dict[i] += 1
        visited = [0] * len(wordList)
        ans = []
        
        minAns = float("-infinity")
        listAns = []
        # check if there is a diff of 1 in the word
        # if yes, check if the diff word is present in endWord
        # if yes, explore in a dfs way. remove the word in a new list and send it to the dfs or have a visited array. also send the characters visited.
        # if we've reached a place where there are no matches in the list, we end the search
        def isWordDiffOne(a, b):
            count = 0
            for i in a:
                if i not in b:
                    count = count + 1
            if (count == 1):
                # print("word diff", a, b, count)
                return True
            # print("word diff", a, b, count)
            return False
        
        def search(visited, beginWord, endWordSet, endWord, ans):
            print("search", visited, beginWord, endWordSet, wordList, ans)
            nonlocal minAns
            nonlocal listAns
            if (beginWord == endWord):
                # print("return 1", ans)
                return True, ans
                
            if (min(visited) == 1): # all are visited
                # print("return 2")
                return False, ans

            for i in range(len(wordList)):
                if (visited[i] == 0):
                    visited[i] = 1
                    # for every unvisited word that has a character from endWordSet,
                    # check if it is compatible to switch, this is just a possibility
                    if (isWordDiffOne(beginWord, wordList[i])):
                        updatedWordSet = False
                        for c in endWordSet:
                            # print("for", c, wordList[i])
                            if c in wordList[i]:
                                # print("if", c, wordList[i])
                                endWordSet.remove(c)
                                updatedWordSet = True
                                break
                        
                        ans.append(wordList[i])
                        # print(beginWord, ans)
                        found = False
                        found, ans = search(visited, wordList[i], endWordSet, endWord, ans[:])
                        if (found):
                            minAns = max(len(ans), minAns)
                            listAns = ans[:]
                            
                                
                        # recursion over, reset states
                        ans.remove(wordList[i])
                        if (updatedWordSet):
                            endWordSet.add(c)
                    
            return minAns, listAns
        
        return search(visited, beginWord, endWordSet, endWord, ans)
                    
solution = Solution()
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# hit -> hot -> dot -> dog -> log -> cog



