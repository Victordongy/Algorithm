from heapq import heappush, heappop
from functools import total_ordering


def huffman(a_list):
    pq = []
    for i in a_list:
        heappush(pq, SymbolNode(i))

    while len(pq) > 1:
        x = heappop(pq)
        y = heappop(pq)
        z = SymbolNode(x.weight + y.weight, y, x)
        heappush(pq, z)
    result = get_codeword(pq[0])
    return result

# helper function to output codeword from tree
def get_codeword(node, string=None, result=None):
    if not string:
        string = ''
    if not result:
        result = set()
    # base case
    if node.is_leaf():
        result.add(string)
        return result
    result = get_codeword(node.left, string+'0', result)
    result = get_codeword(node.right, string+'1', result)
    return result




def alg(a_file):
    in_file = open(a_file)
    n = int(in_file.readline())
    content = [int(x) for x in in_file.readlines()]

    in_file.close()
    return len(max(huffman(content), key=len)), len(min(huffman(content), key=len))


@total_ordering
class SymbolNode:
    def __init__(self, weight, left=None, right=None):
        self.weight = weight
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def is_leaf(self):
        return not self.left and not self.right


if __name__ == '__main__':
    #print(alg('/home/joel/Documents/Python/Algorithms/stanford_algs/stanford-algs/testCases/course3/assignment3HuffmanAndMWIS/question1And2/input_random_1_10.txt'))
    print(alg('week3/huffman.txt'))