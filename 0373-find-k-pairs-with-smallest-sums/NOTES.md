failed 15 + 50
O(klogk) time, O(k) space
The idea is to use a min heap to keep track of the sum of each pair and the indices of the elements in `nums1` and `nums2` that make up the sum. The heap is ordered by the sum, so the smallest sum (and its indices) is always at the top of the heap.

We start by adding the first `k` pairs in the heap. Then, we pop the smallest pair from the heap, add it to the result, and push the next pair in the sequence (i.e., the pair formed by the next element in `nums2` and the same element in `nums1`) into the heap. We repeat this process until we have found `k` pairs or the heap is empty.​
