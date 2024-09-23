# First solution 9/22/2024 - 30 mins:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grams = defaultdict(list)

        for i in strs:
            count = [0] * 26
            for letter in i:
                count[ord(letter) - ord('a')] += 1
            grams[tuple(count)].append(i)

        return grams.values()

            

"""
Time: O(m * n)
Attempts: Had to watch video

Mistakes made:

Learned:
defaultdict() - defaultdict is a subclass of Python's built-in dict (dictionary) that provides a 
default value for keys that have not been set yet. This means you don't need to check if a key exists 
before trying to access or modify its value, which can simplify your code.

Using a tuple as the key for a dictionary

dictname.values() returns a list of all the values in the dictionary.

"""