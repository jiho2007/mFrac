#frac.py
#Script By jiho2007

class frac:
    def __init__(self, n, m=1):
        if type(n) == str or type(m) == str:
            raise TypeError
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

    def __sub__(self, f): #뺄셈
        if type(f) == frac:
            if self.n * f.m > self.m * f.n:
                rn = self.n*f.m - self.m*f.n
            elif self.n * f.m < self.m * f.n:
                rn = self.m*f.n - self.n*f.m
            else:
                return 0
            return frac(rn, self.m*f.m).reduc()
        return self.__sub__(frac(1))

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

    def __eq__(self, f): #같은지 비교
        if type(f) == frac:
            a = self.common(f)
            b = f.common(self)
            return a.n == b.n and a.m == b.m
        return self.__eq__(frac(1))

    def __ne__(self, f): #같지 않은지 비교
        return not self.__eq__(f)

    def __lt__(self, f): #작은지 비교
        if type(f) == frac:
            a = self.common(f)
            b = f.common(self)
            return a.n < b.n and a.m == b.m
        return self.__lt__(frac(1))

    def __le__(self, f): #작거나 같은지 비교
        if type(f) == frac:
            a = self.common(f)
            b = f.common(self)
            return a.n <= b.n and a.m == b.m
        return self.__le__(frac(1))

    def __gt__(self, f): #큰지 비교
        if type(f) == frac:
            a = self.common(f)
            b = f.common(self)
            return a.n > b.n and a.m == b.m
        return self.__lt__(frac(1))

    def __ge__(self, f): #크거나 같은지 비교
        if type(f) == frac:
            a = self.common(f)
            b = f.common(self)
            return a.n >= b.n and a.m == b.m
        return self.__le__(frac(1))

    def toFloat(self): #소수로 반환
        return float(self.n) / float(self.m)

    def reduc(self): #약분
        if self.m<self.n:
            c=self.m
        elif self.n<self.m:
            c=self.n
        else:
            return frac(1)
        for i in range(c, 0, -1):
            if self.n%i == 0 and self.m%i == 0:
                return frac(self.n/i, self.m/i)
        return frac(self.n, self.m)

    def common(self, f): #통분
        if type(f) == frac:
            return frac(self.n*f.m, self.m*f.m)
        return frac(self.n*f, self.m*f)
    
    def clean(self): #int화
        x = 1
        while True:
            if (self.n * x) % 1 == 0:
                return frac(self.n * x, self.m * x).reduc()
            x += 1

    def be(self, f):
        if type(f) == frac:
            self.n = f.n
            self.m = f.m
        else:
            self.n = f
            self.m = 1
