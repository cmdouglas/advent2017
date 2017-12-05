from util import advent_input
from collections import Counter, defaultdict

def valid(passphrase):
    words = passphrase.split(' ')
    c = Counter(words)
    
    # check that the phrase has at most 1 of any word
    return c.most_common(1)[0][1] == 1
    
def anagrams(words):
    """finds all sets of anagrams in words"""
    def key(word):
        return ''.join(sorted(word))
    
    anagram_registry = defaultdict(list)
    
    for word in words:
        anagram_registry[key(word)].append(word)
    
    return anagram_registry.values()
    
def valid2(passphrase):
    words = passphrase.split(' ')
    return len(max(anagrams(words), key=len)) == 1
    
def part1():
    total = 0
    
    with advent_input(4) as f:
        for line in f:
            line = line.strip()
            if valid(line):
                total += 1
        
    print(total)
    
def part2():
    total = 0
    
    with advent_input(4) as f:
        for line in f:
            line = line.strip()
            if valid2(line):
                total += 1
        
    print(total)
    
if __name__ == '__main__':
    part1()
    part2()
                