# /usr/bin/python

# usage of generators
# shawn 2018/1/12

def generator_function(n):
    i = 0
    while i < n:    
        print('before yield %d' %i)
        yield i
        i = i + 1
        print('after yield %d' % i)

def fibon(n):
    """caculate Fibonacci
    """
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


def test1():
    """Test the generator_function()
    """
    gen = generator_function(3)
    print('-'*10)
    print(gen.__next__())

    print('-'*10)
    print(gen.__next__())

    print('-'*10)
    print(gen.__next__())

def testFibon():
    for x in fibon(100):
        print(x)

if __name__ == '__main__':
    #test1()

    testFibon()
