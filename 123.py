#123.py

class Solution(object):
    def maxProfit(self, prices):

#        print(prices)
        if not prices: return 0
        plen = len(prices)
        
        prof1 = [0 for _ in range(plen)]
        prof2 = [0 for _ in range(plen)]
        print(prof2)
        minprices1 = prices[0]
        prof1[0] = 0
        for i in range(1,plen):
            minprices1 = min(minprices1,prices[i])
            prof1[i] = max(prof1[i-1],prices[i]- minprices1)
        maxprices2 = prices[-1]
        prof2[0] = 0
        for i in range(plen-2,-1,-1):
            maxprices2 = max(maxprices2,prices[i])
            prof2[i] = max(prof2[i+1],maxprices2 - prices[i])
        res = 0
        for i in range(plen):
            if prof1[i]+prof2[i]>res: res = prof1[i]+prof2[i]

        #print('prof1 is: ',prof1)
        #print('prof2 is: ',prof2)
        #print(res)

        return res 

if __name__ == '__main__':
    a = Solution()
    prices = [5,1,2,4,7,8]
    profit = a.maxProfit(prices)
    '''
        profit = 0
        for i in range(len(prices)-1):
            a = prices[:i]
            b = prices[i:]
            profa = self.prof(a)
            profb = self.prof(b)
            print('a is: ',a,'profit in a is: ',profa)
            print('b is: ',b,'profit in b is: ',profb)
            profit = max(profit,profa+profb)
        print(profit)
        return profit
    def prof(self,price):
        if not price:
            return 0
        minprice = price[0]
        maxprofit = 0
        for i in price:
            minprice = min(minprice,i)
            profit = i-minprice
            maxprofit = max(maxprofit,profit)
        return maxprofit
    '''

    