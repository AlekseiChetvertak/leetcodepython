class Solution(object):
    def addTwoNumbers(self, l1, l2):
        #reversing
        lis1reversed=[]
        lis2reversed=[]
        finresult=[]
        int1 = 0
        int2 = 0
        for value in l1:
            lis1reversed = [value] + lis1reversed
        for value in l2:
            lis2reversed = [value] + lis2reversed
        #converting
        for digit in lis1reversed: 
            int1 = int1 * 10 + digit
        for digit in lis2reversed:
            int2 = int2 * 10 + digit
        
        resultlist = [int(char) for char in (str(int1+int2))]
        print(resultlist)
        # reversing a list
        for value in resultlist:
            finresult=[value] + finresult
        return[finresult]
    lis1 = [1,1,1]
    lis2 = [1,1,2]
    print(addTwoNumbers(0,lis1,lis2))