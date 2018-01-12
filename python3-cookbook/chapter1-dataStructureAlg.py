# /usr/bin/env python

def sum(items):
    """use * to implement recursion algorithm
        items is a list
    """
    head, *tail = items
    return head + sum(tail) if tail else head

#### 1.1 & 1.2
def extractEle():
    """
        1. extract N elements in list(or tuple) and assign them to N variable
        2. usage of *, call function sum()
    """

    # 1.
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    # name, shares, price, date = data
    name, shares, price, (year, mon, day) = data
    print([name, shares, price, (year, mon, day)])

    s = 'Hello'
    # a, b, c, d = s    # Error
    a, b, c, d, e = s
    _, e, f, _, _ = s   # _ placeholder
    print([a, b, c, d, e])
    print([e, f])
    
    # 2. usage of *
    record = ('Dave', 'dave@ex.com', '777-555-1212', '876-232-2434')
    name, email, *phone = record    # phone is a list
    print(phone)

    *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
    print(trailing)

    # combine * and _ or ign to abondon some elements
    name, *_, (*ign, day) = data
    print([name, day])

### 1.3
def keepLastNEle():
    """keep the last n elements by collections.deque
        deque(maxlen=N): a queue with fixed size N. First in first out, and keep the new coming ones
    """
    from collections import deque
    q = deque(maxlen=4)
    for i in range(8):
        q.append(i)
    print("final q: ", q)
    q.appendleft(1)
    print("left append: ", q)
    q.popleft()
    q.pop()
    print("after pop: ", q)


## 1.4
def findMaxMin():
    """find the maximum and minimum in list
        heapq: function nlargest() nsmallest()
        heap[0]: always the smallest element
        heapq.heappop(): pop the first element, and replace it with the remained smallest one

        sometimes you need to sort firstly.
    """
    import heapq
    nums = [1, 4, 5, 0, 23, -12, 8, 37]
    print(heapq.nlargest(3, nums))   # find the largest 3 num
    print(heapq.nsmallest(2, nums))
     
    protfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, protfolio, key=lambda s : s['price'])
    expensive = heapq.nlargest(2, protfolio, key=lambda s : s['shares'])
    print(cheap)
    print(expensive)

    heap = list(nums)
    heapq.heapify(heap)   # convert list into heap
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))


if __name__ == '__main__':
    # extractEle()
    # keepLastNEle()
    findMaxMin()






