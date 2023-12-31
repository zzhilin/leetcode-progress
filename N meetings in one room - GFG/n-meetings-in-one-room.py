#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        times = sorted([(s, e, e - s) for s, e in zip(start, end)], key=lambda x: x[1])
        res = 0 # alwayes 1
        last_end_time = -1
        
        for meeting in times:
            st, en, duration = meeting
            if last_end_time < st:
                res += 1
                last_end_time = en
            
        
        # print(times)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends