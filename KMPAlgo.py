"""
Knuth–Morris–Pratt algorithm
looks for instances of a "pattern" inpPattern inside a main "text string" inpText, based on the observation that when a mismatch occurs, the word itself has enough information to indicate where the next match could begin, avoiding the need to re-examine previously matched letters.  
The total Time Complexity is reduced to O(length of string(n)+length of pattern(n)) compared to normal approach with runtime O(n*n).
"""

class KMPAlgo:
    
    def __init__(self, input_string):
        self.inpText = input_string
        self.length = len(input_string)
        
    def PrefixIndexTable(self):
        """
		return prefix table with index postion values for inout string
        """
        tbl_prefix_index = [0]*self.length
        input_string = list(self.inpText)
        k,l=0,1
        while k<self.length and l<self.length:
            if input_string[k]==input_string[l]:  # case 1: if character found then add value in prefix table and increment value of both input string and given pattern 
                tbl_prefix_index[l]=k+1
                k+=1
                l+=1
            else:  # case 2: if no match found then start from beginning index and add 0 in prefix table
                if k==0:
                    tbl_prefix_index[l]=0
                    l+=1
                else:
                    k = tbl_prefix_index[k-1]
        return tbl_prefix_index
    
    def search_pattern_KMPAlgo(self, inpPattern):
        """
		return index position where pattern found
        """
        n = 0  # the beginning of the current match in inpText
        k = 0  # the position of the current character in inpPattern
        PrefixIndexTable=self.PrefixIndexTable()


        while n + k < self.length:
            if inpPattern[k] == self.inpText[n+k]:
                if k == len(inpPattern) - 1:
                    return n
                k += 1
            else:
                if PrefixIndexTable[k] > 0:
                    n = n + k - PrefixIndexTable[k]
                    k = PrefixIndexTable[k]
                else:
                    n += 1
                    k = 0
        return None  #if pattern not found return index value as None
		

#Enter input string and check if pattern found in given string.        
input_string = input("Enter the input string:")
strPat1 = input("Enter the Pattern 1:")
strPat2 = input("Enter the Pattern 2:")

KMPAlgo = KMPAlgo(input_string)

print("Prefix Index Table of input string: ",KMPAlgo.PrefixIndexTable()) 
print("Pattern 1 found at index position:",KMPAlgo.search_pattern_KMPAlgo(strPat1)) 
print("Pattern 2 found at index position:",KMPAlgo.search_pattern_KMPAlgo(strPat2)) 
