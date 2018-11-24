#fraction.py
#Script By jiho2007

class frac:
    def __init__(self, n=1, m=1):
        self.n = n #분자
        self.m = m #분모
        if type(n) != int and n % 1 == 0: #int화
            self.n = int(n)
        if type(m) != int and m % 1 == 0:
            self.m = int(m)

    def __repr__(self): #str로 변환
        return 'frac(n={}, m={})'.format(self.n, self.m)

    def __str__(self):
        return '{}/{}'.format(self.n, self.m)

    def __format__(self, s):
        return self.__str__()

    def __add__(self, f): #덧셈
        if type(f) == frac:
            return frac(self.n*f.m + self.m*f.n, self.m * f.m)
        return frac(self.n + f*self.m, self.m)

    def __sub__(self, f): # 뺄셈
        if type(f) == frac:
            if self.n * f.m > self.m * f.n:
                rn = self.n*f.m - self.m*f.n
            elif self.n * f.m < self.m * f.n:
                rn = self.m*f.n - self.n*f.m
            else:
                return 0
            return frac(rn, self.m*f.m).reduc()
        return self.__sub__(frac())

    def __mul__(self, f): #곱셈
        if type(f) == frac:
            return frac(self.n*f.n, self.m) / f.m
        return frac(self.n*f, self.m).reduc()

    def __truediv__(self, f): #나눗셈
        if type(f) == frac:
            return self.__mul__(frac(f.m, f.n))
        return frac(self.n, self.m*f).reduc()

    def __radd__(self, f): #순서반대 덧셈
        return self.__add__(f)

    def __rsub__(self, f): #순서반대 뺄셈
        if type(f) == frac:
            return f.__sub__(self)
        return self.__sub__(frac(self.m*f, self.m))

    def __rmul__(self, f): #순서반대 곱셈
        return self._mul__(f)

    def __rtruediv__(self, f): #순서반대 나눗셈
        if type(f) == frac:
            return f.__truediv__(self)
        return frac(self.m, self.n).__mul__(f)

    def toFloat(self): #소수로 반환
        return float(self.n) / float(self.m)

    def reduc(self): #약분
        if self.m<self.n:
            c=self.m
        elif self.n<self.m:
            c=self.n
        else:
            return frac()
        for i in range(c, 0, -1):
            if self.n%i == 0 and self.m%i == 0:
                return frac(self.n/i, self.m/i)
        return frac(self.n, self.m)

if __name__ == '__main__': #Test
    half = frac(1, 2) #1/2
    div3 = frac(m=3, n=1) #1/3
    fds = frac(4, 6) #4/6
    opf = frac(1.5, 3) #1.5/3
    print('TEST: __repr__ for Fraction 1/3 is: {}'.format(repr(div3))) #frac(n=1, m=3)
    print('TEST: __str__ for Fraction 1/2 is: {}'.format(half)) #1/2
    print('TEST: 1/2 equals: {}'.format(half.toFloat())) #0.5
    print('TEST: {} + {} = {}'.format(half, div3, half + div3)) #5/6
    print('TEST: {} - {} = {}'.format(half, div3, half - div3)) #1/6
    print('TEST: 1 - {} = {}'.format(div3, 1 - div3)) #2/3
    print('TEST: {} * {} = {}'.format(half, div3, div3 * half)) #1/6
    print('TEST: 2 * {} = {}'.format(div3, div3 * 2)) #2/3
    print('TEST: {} / 2 = {}'.format(half, half / 2)) #1/4
    print('TEST: reduc() of {} is: {}'.format(fds, fds.reduc())) #2/3
    print('TEST: 1.5 / 3 is: {}'.format(opf)) #1.5/3
    print('TEST: {} / {} = {}'.format(half, div3*2, half / (div3*2))) #3/4
    print('TEST: 1 / {} = {}'.format(div3*2, 1 / (div3*2))) #3/4
