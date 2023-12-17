class Solution:
    def rotate(self, A, K):
        # Implement your solution here

        i = K % len(A)
        to_rotate = A[(len(A)-i):]
        left = A[:(len(A)-i)]
        res = [0] * len(A)
        for i in range(len(A)):
            res[(i+K)%len(A)] = A[i]
        A[:] = res