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
>>> n = frac(1, 2) #create fraction 1/2
>>> m = frac(m=3, n=2) #you can set numerator to n, denominator to m
```

**Reduction And Reversing**  
```python
>>> x = frac(2, 8)   #create fraction 2/8
>>> print(x.reduc()) #reduction of 2/8
'1/4'
>>> f = frac(1, 2)     #create fraction 1/2
>>> print(f.common(3)) #common fraction of 1/2
'3/6'
>>> e = frac(3, 4)     #create fraction 3/4
>>> print(reversed(f)) #reverse 母 and 子
'4/3'
```

**Calculation**  
```python
>>> n = frac(1, 2)
>>> m = frac(2, 3)
>>> print(n+m) #Add
'5/6'
>>> print(1-m) #Subtract
'1/3'
>>> print(m*2) #Multiplication
'4/3'
>>> print(n/2) #Division
'1/4'
```

**Comparing**
```python
>>> frac(1, 2) == frac(2, 4) #Equals
True
>>> frac(1, 2) < frac(1, 3)  #Less than
False
>>> frac(1, 2) <= frac(3, 6) #Less than and Equals
True
>>> frac(2, 4) > frac(3, 9)  #Greater than
True
>>> frac(3, 6) >= frac(6, 9) #Greater than and Equals
False
```