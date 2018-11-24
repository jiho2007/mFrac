# mFrac
**A Simple Fraction Python Library**

**Feature:**  
This Library implements 'frac' class.  
You can add, subtract, multiplicate, divide Fractions.

**How to Install:** *pip install -i https://test.pypi.org/simple/ mfrac*  
**How to Upgrade:** *pip install -i https://test.pypi.org/simple/ mfrac --upgrade*

**[Download ZIP](https://github.com/jiho2007/mfrac/archive/master.zip)**  
**[Download TAR.GZ](https://github.com/jiho2007/mfrac/archive/master.tar.gz)**  



**Import Code:**  
import code is simple. Just use this:  
```python
from mfrac import frac
```

**Creating Fraction Object**  
```python
#create 1/2
n = frac(1, 2)
#you can set numerator to n, denominator to m
m = frac(m=3, n=2)
```

**Reduction**  
```python
x = frac(2, 8)
#reduction of 2/8 (=1/4)
print(x.reduc())
```

**Calculation**  
```python
n = frac(1, 2)
m = frac(2, 3)
print(n+m) #Add             (=5/6)
print(1-m) #Subtract        (=1/3)
print(m*2) #Multiplication  (=4/3)
print(n/2) #Division        (=1/4)
```
