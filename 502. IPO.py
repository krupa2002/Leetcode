class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capitalHeap = []
        profitHeap = []

        for i,c in enumerate(capital):
            heappush(capitalHeap,(c,profits[i]))

        while k:
            while capitalHeap and capitalHeap[0][0]<=w:
                cap,profit = heappop(capitalHeap)
                heappush(profitHeap,(-profit,cap))

            if profitHeap:
                w+=-heappop(profitHeap)[0]
            k-=1
        return w


        
