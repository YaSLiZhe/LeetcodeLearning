## 最常考的算法与数据结构知识点

## 排序类（Sort）：

基础知识：快速排序（Quick Sort）， 归并排序（Merge Sort）的原理与代码实现。需要能讲明白代码中每一行的目的。快速排序时间复杂度平均状态下 O（NlogN），空间复杂度 O（1），归并排序最坏情况下时间复杂度 O（NlogN），空间复杂度 O（N）

入门题目：
Leetcode 148. Sort List
Leetcode 56. Merge Intervals
Leetcode 27. Remove elements



进阶题目：
Leetcode 179. Largest Number
Leetcode 75. Sort Colors
Leetcode 215. Kth Largest Element （可以用堆的解法替代）
Leetcode 4. Median of Two Sorted Arrays
注意：后两题是与快速排序非常相似的快速选择（Quick Select）算法，面试中很常考



## 链表类（Linked List）：

基础知识：链表如何实现，如何遍历链表。链表可以保证头部尾部插入删除操作都是 O（1），查找任意元素位置 O（N）

基础题目：
Leetcode 206. Reverse Linked List
Leetcode 876. Middle of the Linked List
注意：快慢指针和链表反转几乎是所有链表类问题的基础，尤其是反转链表，代码很短，建议直接背熟。



进阶题目:
Leetcode 160. Intersection of Two Linked Lists
Leetcode 141. Linked List Cycle (Linked List Cycle II)
Leetcode 92. Reverse Linked List II
Leetcode 328. Odd Even Linked List

堆（Heap or Priority Queue）、栈（Stack）、队列（Queue）、哈希表类（Hashmap、Hashset）：



### 基础知识：各个数据结构的基本原理，增删查改复杂度。



## Queue 题目：

Leetcode 225. Implement Stack using Queues
Leetcode 346. Moving Average from Data Stream
Leetcode 281. Zigzag Iterator
Leetcode 1429. First Unique Number
Leetcode 54. Spiral Matrix
Leetcode 362. Design Hit Counter



## Stack 题目：

Leetcode 155. Min Stack (follow up Leetcode 716 Max Stack)
Leetcode 232. Implement Queue using Stacks
Leetcode 150. Evaluate Reverse Polish Notation
Leetcode 224. Basic Calculator II (I, II, III, IV)
Leetcode 20. Valid Parentheses
Leetcode 1472. Design Browser History
Leetcode 1209. Remove All Adjacent Duplicates in String II
Leetcode 1249. Minimum Remove to Make Valid Parentheses
Leetcode 735. Asteroid Collision



## Hashmap/ Hashset 题目：

Leetcode 1. Two Sum
Leetcode 146. LRU Cache (Python 中可以使用 OrderedDict 来代替)
Leetcode 128. Longest Consecutive Sequence
Leetcode 73. Set Matrix Zeroes
Leetcode 380. Insert Delete GetRandom O(1)
Leetcode 49. Group Anagrams
Leetcode 350. Intersection of Two Arrays II
Leetcode 299. Bulls and Cows
Leetcode 348 Design Tic-Tac-Toe



## Heap／Priority Queue 题目：

Leetcode 973. K Closest Points
Leetcode 347. Top k Largest Elements
Leetcode 23. Merge K Sorted Lists
Leetcode 264. Ugly Number II
Leetcode 1086. High Five
Leetcode 88. Merge Sorted Arrays
Leetcode 692. Top K Frequent Words
Leetcode 378. Kth Smallest Element in a Sorted Matrix
Leetcode 295. Find Median from Data Stream （标准解法是双 heap，但是 SortedDict 会非常容易）
Leetcode 767. Reorganize String
Leetcode 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit (这个题用单调双端队列、TreeMap、双 heap 都可以)
Leetcode 895. Maximum Frequency Stack



## 二分法（Binary Search）：

基础知识：二分法是用来解法基本模板，时间复杂度 logN；常见的二分法题目可以分为两大类，显式与隐式，即是否能从字面上一眼看出二分法的特点：要查找的数据是否可以分为两部分，前半部分为 X，后半部分为 O



#### 显式二分法：

Leetcode 34. Find First and Last Position of Element in Sorted Array
Leetcode 33. Search in Rotated Sorted Array
Leetcode 1095. Find in Mountain Array
Leetcode 162. Find Peak Element
Leetcode 278. First Bad Version
Leetcode 74. Search a 2D Matrix
Leetcode 240. Search a 2D Matrix II



#### 隐式二分法：

Leetcode 69. Sqrt(x)
Leetcode 540. Single Element in a Sorted Array
Leetcode 644. Maximum Average Subarray II
Leetcode 528. Random Pick with Weight
Leetcode 1300. Sum of Mutated Array Closest to Target
Leetcode 1060. Missing Element in Sorted Array
Leetcode 1062. Longest Repeating Substring
Leetcode 1891. Cutting Ribbons
Leetcode 410. Split Array Largest Sum (与 1891 类似)



## 双指针（2 Pointer）：

基础知识：常见双指针算法分为三类，同向（即两个指针都相同一个方向移动），背向（两个指针从相同或者相邻的位置出发，背向移动直到其中一根指针到达边界为止），相向（两个指针从两边出发一起向中间移动直到两个指针相遇）



#### 背向双指针：(基本上全是回文串的题)

Leetcode 409. Longest Palindrome
Leetcode 125. Valid Palindrome (I、II)
Leetcode 5. Longest Palindromic Substring
Leetcode 647. Palindromic Substrings



#### 相向双指针：(以 two sum 为基础的一系列题)

Leetcode 1. Two Sum (这里使用的是先排序的双指针算法，不同于 hashmap 做法)
Leetcode 167. Two Sum II - Input array is sorted
Leetcode 15. 3Sum
Leetcode 16. 3Sum Closest
Leetcode 18. 4Sum
Leetcode 454. 4Sum II
Leetcode 277. Find the Celebrity
Leetcode 11. Container With Most Water
Leetcode 186 Reverse Words in a String II



#### 同向双指针：（个人觉得最难的一类题，可以参考下这里 TimothyL：Leetcode 同向双指针/滑动窗口类代码模板）

Leetcode 283. Move Zeroes
Leetcode 26. Remove Duplicate Numbers in Array
Leetcode 395. Longest Substring with At Least K Repeating Characters
Leetcode 340. Longest Substring with At Most K Distinct Characters
Leetcode 424. Longest Repeating Character Replacement
Leetcode 76. Minimum Window Substring
Leetcode 3. Longest Substring Without Repeating Characters
Leetcode 1004 Max Consecutive Ones III
Leetcode 1658 Minimum Operations to Reduce X to Zero



## 宽度优先搜索（BFS）：面试中最常考的

基础知识：
常见的 BFS 用来解决什么问题？(1) 简单图（有向无向皆可）的最短路径长度，注意是长度而不是具体的路径（2）拓扑排序 （3） 遍历一个图（或者树）
BFS 基本模板（需要记录层数或者不需要记录层数）
多数情况下时间复杂度空间复杂度都是 O（N+M），N 为节点个数，M 为边的个数



#### 基于树的 BFS：不需要专门一个 set 来记录访问过的节点

Leetcode 102 Binary Tree Level Order Traversal
Leetcode 103 Binary Tree Zigzag Level Order Traversal
Leetcode 297 Serialize and Deserialize Binary Tree （很好的 BFS 和双指针结合的题）
Leetcode 314 Binary Tree Vertical Order Traversal



#### 基于图的 BFS：（一般需要一个 set 来记录访问过的节点）

Leetcode 200. Number of Islands
Leetcode 133. Clone Graph
Leetcode 127. Word Ladder
Leetcode 490. The Maze
Leetcode 323. Connected Component in Undirected Graph
Leetcode 130. Surrounded Regions
Leetcode 752. Open the Lock
Leetcode 815. Bus Routes
Leetcode 1091. Shortest Path in Binary Matrix
Leetcode 542. 01 Matrix
Leetcode 1293. Shortest Path in a Grid with Obstacles Elimination
Leetcode 417. Pacific Atlantic Water Flow



## [拓扑排序](https://zh.wikipedia.org/wiki/%E6%8B%93%E6%92%B2%E6%8E%92%E5%BA%8F)

Leetcode 207 Course Schedule （I, II）
Leetcode 444 Sequence Reconstruction
Leetcode 269 Alien Dictionary
Leetcode 310 Minimum Height Trees
Leetcode 366 Find Leaves of Binary Tree



## 深度优先搜索（DFS）：

#### 面试中最常考的（分类的稍微有点粗糙了，没有细分出回溯/分治来，准备找个时间给每个 DFS 的题标记下是哪种 DFS）

基础知识：
常见的 DFS 用来解决什么问题？(1) 图中（有向无向皆可）的符合某种特征（比如最长）的路径以及长度（2）排列组合（3） 遍历一个图（或者树）（4）找出图或者树中符合题目要求的全部方案
DFS 基本模板（需要记录路径，不需要返回值 and 不需要记录路径，但需要记录某些特征的返回值）
除了遍历之外多数情况下时间复杂度是指数级别，一般是 O(方案数 × 找到每个方案的时间复杂度)
递归题目都可以用非递归迭代的方法写，但一般实现起来非常麻烦



#### 基于树的 DFS：需要记住递归写前序中序后序遍历二叉树的模板

Leetcode 543 Diameter of Binary Tree (分治)
Leetcode 124 Binary Tree Maximum Path Sum (分治)
Leetcode 226 Invert Binary Tree (分治)
Leetcode 101 Symmetric Tree (回溯 or 分治)
Leetcode 951 Flip Equivalent Binary Trees (分治)
Leetcode 236 Lowest Common Ancestor of a Binary Tree (相似题：235、1650) (回溯 or 分治)
Leetcode 105 Construct Binary Tree from Preorder and Inorder Traversal (分治)
Leetcode 104 Maximum Depth of Binary Tree (回溯 or 分治)
Leetcode 987 Vertical Order Traversal of a Binary Tree
Leetcode 1485 Clone Binary Tree With Random Pointer
Leetcode 572 Subtree of Another Tree (分治)
Leetcode 863 All Nodes Distance K in Binary Tree
Leetcode 1110 Delete Nodes And Return Forest (分治)



## 二叉搜索树（BST）：

#### BST 特征：中序遍历为单调递增的二叉树，换句话说，根节点的值比左子树任意节点值都大，比右子树任意节点值都小，增删查改均为 O（h）复杂度，h 为树的高度；注意不是所有的 BST 题目都需要递归，有的题目只需要 while 循环即可

Leetcode 230 Kth Smallest element in a BST
Leetcode 98 Validate Binary Search Tree
Leetcode 270 Cloest Binary Search Tree Value
Leetcode 235 Lowest Common Ancestor of a Binary Search Tree
Leetcode 669 Trim a Binary Search Tree (分治)
Leetcode 700 Search in a Binary Search Tree
Leetcode 108 Convert Sorted Array to Binary Search Tree (分治)
Leetcode 333 Largest BST Subtree (与 98 类似) (分治)
Leetcode 285 Inorder Successor in BST (I, II)





## 基于图的 DFS: 

#### 和 BFS 一样一般需要一个 set 来记录访问过的节点，避免重复访问造成死循环; Word XXX 系列面试中非常常见，例如 word break，word ladder，word pattern，word search。

Leetcode 341 Flatten Nested List Iterator (339 364)
Leetcode 394 Decode String
Leetcode 51 N-Queens (I II 基本相同)
Leetcode 291 Word Pattern II (I 为简单的 Hashmap 题)
Leetcode 126 Word Ladder II （I 为 BFS 题目）
Leetcode 93 Restore IP Addresses
Leetcode 22 Generate Parentheses
Leetcode 856 Score of Parentheses
Leetcode 301 Remove Invalid Parentheses
Leetcode 37 Sodoku Solver
Leetcode 212 Word Search II （I, II）
Leetcode 1087 Brace Expansion
Leetcode 399 Evaluate Division
Leetcode 1274 Number of Ships in a Rectangle
Leetcode 1376 Time Needed to Inform All Employees
Leetcode 694 Number of Distinct Islands
Leetcode 131 Palindrome Partitioning



## 基于排列组合的 DFS: 其实与图类 DFS 方法一致，但是排列组合的特征更明显

Leetcode 17 Letter Combinations of a Phone Number
Leetcode 39 Combination Sum（I, II, III 相似， IV 为动态规划题目）
Leetcode 78 Subsets （I, II 重点在于如何去重）
Leetcode 46 Permutation (I, II 重点在于如何去重)
Leetcode 77 Combinations (I, II 重点在于如何去重)
Leetcode 698 Partition to K Equal Sum Subsets
Leetcode 526 Beautiful Arrangement (similar to 46)





## 记忆化搜索（DFS + Memoization Search）：

#### 算是用递归的方式实现动态规划，递归每次返回时同时记录下已访问过的节点特征，避免重复访问同一个节点，可以有效的把指数级别的 DFS 时间复杂度降为多项式级别; 注意这一类的 DFS 必须在最后有返回值（分治法），不可以用回溯法; for 循环的 dp 题目都可以用记忆化搜索的方式写，但是不是所有的记忆化搜索题目都可以用 for 循环的 dp 方式写。

Leetcode 139 Word Break II
Leetcode 72 Edit Distance
Leetcode 377 Combination Sum IV
Leetcode 1235 Maximum Profit in Job Scheduling
Leetcode 1335 Minimum Difficulty of a Job Schedule
Leetcode 1216 Valid Palindrome III
Leetcode 97 Interleaving String
Leetcode 472 Concatenated Words
Leetcode 403 Frog Jump
Leetcode 329 Longest Increasing Path in a Matrix



## 前缀和（Prefix Sum）

基础知识：前缀和本质上是在一个 list 当中，用 O（N）的时间提前算好从第 0 个数字到第 i 个数字之和，在后续使用中可以在 O（1）时间内计算出第 i 到第 j 个数字之和，一般很少单独作为一道题出现，而是很多题目中的用到的一个小技巧

常见题目：
Leetcode 53 Maximum Subarray
Leetcode 1423 Maximum Points You Can Obtain from Cards
Leetcode 1031 Maximum Sum of Two Non-Overlapping Subarrays
Leetcode 523 Continuous Subarray Sum
Leetcode 304 Range Sum Query 2D - Immutable
以上内容皆为面试中高频的知识点，以下知识点和题目在面试中属于中等频率（大概面 10 道题会遇到一次），时间不足的情况下，请以准备上面的知识点为主。



## 并查集（Union Find）：把两个或者多个集合合并为一个集合

基础知识：如果数据不是实时变化，本类问题可以用 BFS 或者 DFS 的方式遍历，如果数据实时变化（data stream）则并查集每次的时间复杂度可以视为 O（1）；需要牢记合并与查找两个操作的模板

常见题目：
Leetcode 721 Accounts Merge
Leetcode 547 Number of Provinces
Leetcode 737 Sentence Similarity II
Leetcode 305 Number of Islands II





## 字典树（Trie）

基础知识：（https://zh.wikipedia.org/wiki/Trie）；多数情况下可以通过用一个set来记录所有单词的prefix来替代，时间复杂度不变，但空间复杂度略高

常见题目：
Leetcode 208 Implement Trie (Prefix Tree)
Leetcode 211 Design Add and Search Words Data Structure
Leetcode 1268 Search Suggestions System
Leetcode 212 Word Search II
Leetcode 1166 Design File System



## 单调栈与单调队列（Monotone Stack／Queue）

基础知识：单调栈一般用于解决数组中找出每个数字的第一个大于／小于该数字的位置或者数字；单调队列只见过一道题需要使用；不论单调栈还是单调队列，单调的意思是保留在栈或者队列中的数字是单调递增或者单调递减的

常见题目：
Leetcode 85 Maximum Rectangle
Leetcode 84 Largest Rectangle in Histogram
Leetcode 907 Sum of Subarray Minimums (与 84 类似)
Leetcode 739 Daily Temperatures
Leetcode 901 Online Stock Span
Leetcode 503 Next Greater Element II
Leetcode 239 Sliding Window Maximum （唯一的单调队列题）

## 扫描线算法（Sweep Line）

基础知识：一个很巧妙的解决时间安排冲突的算法，本身比较容易些也很容易理解
常见题目：
Leetcode 253 Meeting Room II（Meeting Room I 也可以使用）
Leetcode 1094 Car Pooling
Leetcode 218 The Skyline Problem
Leetcode 759 Employee Free Time
TreeMap



## 基础知识：基于红黑树（平衡二叉搜索树）的一种树状 hashmap

增删查改、找求大最小均为 logN 复杂度，Python 当中可以使用 SortedDict 替代；SortedDict 继承了普通的 dict 全部的方法，除此之外还可以 peekitem(k)来找 key 里面第 k 大的元素，popitem(k)来删除掉第 k 大的元素，弥补了 Python 自带的 heapq 没法 logN 时间复杂度内删除某个元素的缺陷；最近又在刷一些 hard 题目时候突然发现 TreeMap 简直是个神技，很多用别的数据结构写起来非常麻烦的题目，TreeMap 解决起来易如反掌。

常见题目：
Leetcode 729 My Calendar I
Leetcode 981 Time Based Key-Value Store
Leetcode 846 Hand of Straights
Leetcode 218 The Skyline Problem
Leetcode 480. Sliding Window Median (这个题用 TreeMap 超级方便)
Leetcode 318 Count of Smaller Numbers After Self (这个题线段树、二分索引树、TreeMap 都可以)



## 动态规划（Dynamic Programming）

基础知识：这里指的是用 for 循环方式的动态规划，非 Memoization Search 方式。DP 可以在多项式时间复杂度内解决 DFS 需要指数级别的问题。常见的题目包括找最大最小，找可行性，找总方案数等，一般结果是一个 Integer 或者 Boolean。动态规划有很多分支，暂时还没想好怎么去写这部分，后面想好了再具体写吧。

常见题目：
Leetcode 674 Longest Continuous Increasing Subsequence (接龙型 dp)
Leetcode 62 Unique Paths II
Leetcode 70 Climbing Stairs
Leetcode 64 Minimum Path Sum
Leetcode 368 Largest Divisible Subset (接龙型 dp)
Leetcode 300 Longest Increasing Subsequence (接龙型 dp)
Leetcode 354 Russian Doll Envelopes (接龙型 dp， 300 的 2D 版)
Leetcode 256 Paint House
Leetcode 121 Best Time to Buy and Sell Stock
Leetcode 55 Jump Game
Leetcode 45 Jump Game II
Leetcode 132 Palindrome Partitioning II
Leetcode 312 Burst Balloons (区间型 dp)
Leetcode 1143 Longest Common Subsequence (前缀型 dp)
Leetcode 1062 Longest Repeating Substring (dp 方法与 longest common substring 一致)
Leetcode 718 Maximum Length of Repeated Subarray (和 1062 本质上一样)
Leetcode 174 Dungeon Game
Leetcode 115 Distinct Subsequences
Leetcode 72 Edit Distance
Leetcode 91 Decode Ways
Leetcode 639 Decode Ways II
Leetcode 712 Minimum ASCII Delete Sum for Two Strings
Leetcode 221 Maximal Square
Leetcode 1277 Count Square Submatrices with All Ones (可以使用 221 一样的解法)
Leetcode 198 House Robber
Leetcode 213 House Robber II
Leetcode 740 Delete and Earn
Leetcode 87 Scramble String
Leetcode 1140 Stone Game II
Leetcode 322 Coin Change
Leetcode 518 Coin Change II (01 背包型)
Leetcode 1048 Longest String Chain
Leetcode 44 Wildcard Matching
Leetcode 10 Regular Expression Matching
Leetcode 32 Longest Valid Parentheses
Leetcode 1235 Maximum Profit in Job Scheduling (DP + binary search)
Leetcode 1043 Partition Array for Maximum Sum
Leetcode 926 Flip String to Monotone Increasing