# Determinant and Inverse Transformation


## Determinant of a Matrix

### 2D Determinant

<center>

![](images/2d_det.svg)   
*Geometric meaning of 2D determinant*

</center>

Let $a, b$ be the two columns of a $2 \times 2$ matrix $A$ (**under an orthonormal basis**, but it need not to be the standard one; this is important)

$$
A = \begin{bmatrix}
    a_1 & b_1 \\
    a_2 & b_2
\end{bmatrix}
$$

We can use the two vectors to construct a **parallelogram** $ABCD$ (see figure), whose *area* is given by the formula (see Appendix; try to prove it by yourself):

$$
\text{Area} = 
|a_1 b_2 - a_2 b_1|
$$

If we are not using the components along an orthonormal basis, the result will be more complicated. The expression inside the absolute value sign $| \, |$ is defined as the **determinant** of matrix $A$, denoted by

$$
\det A \equiv a_1 b_2 - a_2 b_1
$$

The determinant can be a negative number. When $\det A > 0$, we say that the two vectors $a, b$ form a **right-hand basis** of the 2D vector space. Thus the standard basis itself 

$$
e_1 = (1,0)^\mathsf{T}, \quad
e_2 = (0,1)^\mathsf{T}
$$ 

is a right-hand basis.

When $\det A = 0$, it means that $a$ and $b$ are *on the same line*.

### 3D Determinant

<center>

![](images/3d_det.png)   
*Geometric meaning of 3D determinant*

</center>

Similar to the 2D case, let $a, b, c$ be the three columns of a $3 \times 3$ matrix $A$ (**under orthonormal basis**)

$$
A = \begin{bmatrix}
    a_1 & b_1 & c_1 \\
    a_2 & b_2 & c_2 \\
    a_3 & b_3 & c_3
\end{bmatrix}
$$

We can use the three vectors to construct a **parallelepiped** (see figure), whose *volume* is given by the formula (see Appendix):

$$
\begin{align*}
    \text{Volume} = 
    | &a_1 b_2 c_3 + a_2 b_3 c_1 + a_3 b_1 c_2 \\
    &- a_3 b_2 c_1 - a_2 b_1 c_3 - a_1 b_3 c_2|
\end{align*}
$$

The expression inside the absolute value sign $| \, |$ is defined as the **determinant** of matrix $A$, still denoted by $\det A$. It can be rewritten in terms of 2D determinants:

$$
\det A = a_1 \det \begin{bmatrix}
    b_2 & c_2 \\
    b_3 & c_3 
\end{bmatrix}
- a_2 \det \begin{bmatrix}
    b_1 & c_1 \\
    b_3 & c_3 
\end{bmatrix}
+ a_3 \det \begin{bmatrix}
    b_1 & c_1 \\
    b_2 & c_2 
\end{bmatrix}
$$

When $\det A > 0$, we say that the two vectors $a, b$ form a **right-hand basis** of the 3D vector space. Thus the standard basis itself

$$
e_1 = (1,0,0)^\mathsf{T}, \quad 
e_2 = (0,1,0)^\mathsf{T}, \quad
e_3 = (0,0,1)^\mathsf{T}
$$ 

is a right-hand basis.

When $\det A = 0$, it means that $a, b, c$ are *on the same plane*.

## Inverse of Linear Transformation and Matrix

For a given linear transformation $A$, *if we can find* another transformation $B$ that completely *cancels* the effect of $A$, *and* $A$ completely cancels the effect of $B$, then we say that $A$ and $B$ are the **inverse of each other**. 

The matrix representation of $B$ is called the **inverse** of the matrix $A$. We shall use the notation $A^{-1}$ to denote both the inverse transformation and the inverse matrix.

Mathematically, "completely cancel" means

$$
A A^{-1} = A^{-1} A = 1
$$

where $1$ is the **identity transformation**, whose effect is no effect at all. Its matrix representation is called the **identity matrix**, the same under any choice of basis vectors:

$$
(1)_{ij} = \delta_{ij}
= \begin{bmatrix}
    1 & & \\
    & \ddots & \\
    & & 1
\end{bmatrix}
= \operatorname{diag}(1,...,1)
$$

*Remark*:

- Do *not* use $1/A$ to denote the inverse of $A$.

- Note that we used the expression "if we can find". This means that some linear transformation does *not* have its inverse.

- We state without proof that if a linear transformation is invertible, then *its inverse is unique*. 

Here we shall not teach you how to calculate the inverse of an arbitrary invertible matrix, which can be done by computers. 

### Determinant and Matrix Invertibility

Consider a linear transformation $A$.

<center>

![](images/non_invertible_trans.png)   
*A non-invertible 2D linear transformation*   
*(Screenshot from the linear transformation demo)*

</center>

First suppose $A$ is in 2D, it is not difficult to understand if $A$ transforms the two basis vectors to the *same line* (see figure), then we *lost the information in one dimension*, since any linear combination of $A e_1, A e_2$ gives vectors on that same line. Thus the transformation will *not* be invertible. 

Similarly, for $A$ in 3D, if $A$ transforms the two basis vectors to the *same plane* (including the case when all basis vectors are transformed to the same line), then we lost the information in one (or even two) dimension(s). Then the transformation will *not* be invertible. 

These cases happen when $\det A = 0$. Thus we obtain the following criteria for $A$ to be invertible.

<center>

**A (square) matrix $A$ is invertible if and only if $\det{A} \ne 0$.**

</center>

This holds for any dimensions. 

### Inverse of Product of Matrices

When you invert a product of matrices, the order of the product sequence should be *reversed*, i.e.

$$
\left(A_1A_2 \cdots A_n\right){}^{-1}
= A_n^{-1} \cdots A_2^{-1} A_1^{-1}
$$

This is easy to understand if you think in terms of the transformations they represent. For example, consider the problem of putting an elephant into a refrigerator with closed doors. We need to do it in 3 steps:

<center>

|Operation|Represented by|
|-:|:-|
|Open the door|$A_1$|
|Move the elephant in|$A_2$|
|Close the door|$A_3$|

</center>

Is it obvious to you that $A_1, A_3$ are inverse of each other? Net effect: 

$$
\begin{align*}
    &|\text{elephant in refrigerator} \rangle
    \\
    & \quad = 
    A_3 A_2 A_1 | \text{elephant out of refrigerator} \rangle
\end{align*}
$$

The inverse operation is evidently

<center>

|Operation|Represented by|
|-:|:-|
|Open the door|$A_3^{-1}$|
|Move the elephant out|$A_2^{-1}$|
|Close the door|$A_1^{-1}$|

</center>

Net effect: 

$$
\begin{align*}
    &|\text{elephant out of refrigerator} \rangle
    \\
    & \quad = 
    A_1^{-1} A_2^{-1} A_3^{-1} | \text{elephant in refrigerator} \rangle
\end{align*}
$$

### EXERCISE

- Calculate $\det 1$. What does it mean?

- For a general $2 \times 2$ matrix
    
    $$
    A = \begin{bmatrix}
        a & b \\
        c & d
    \end{bmatrix}
    $$

    - When will $A$ be invertible?
    
    - Explicitly calculate $A^{-1}$. Verify your answer for the last question. 


## Appendix A: Geometrical Meaning of Determinant

### 2D Determinant = Parallelogram Area

<center>

![](images/2d_det-solution.svg)   
*Calculation of area of parallelogram ABCD*

</center>

We draw a line through point D parallel to the $x$ axis. Cut off the triangle DPC and move it to AQB. Now we obtain a new parallelogram AQPD, which has the same area as ABCD. 

However, since its base AQ is on the $x$ axis, the formula $A = ah$ can now be applied directly. The height of AQPD is obviously equal to $b_{y}$. It remains to find the base AQ.

Since BQ is parallel to $\boldsymbol{b}$, we can set

$$\overrightarrow{BQ} = \alpha\boldsymbol{b}$$

Then, from $\overrightarrow{OQ} = \overrightarrow{AB} + \overrightarrow{BQ} = \boldsymbol{a} + \alpha\boldsymbol{b}$, we obtain (for the $x,y$ components respectively)

$$
\left.
\begin{align*}
    x_{Q} = a_{x} + \alpha b_{x} \\
    0 = a_{y} + \alpha b_{y}
\end{align*}
\right\}
\, \Rightarrow \,
\left\{
\begin{align*}
    &\alpha = - \frac{a_{y}}{b_{y}}
    \\
    &x_{Q} = a_{x} - \frac{a_{y}b_{x}}{b_{y}}
\end{align*}
\right.
$$

Finally

$$
A = |x_{Q}| |b_{y}| 
= |a_{x}b_{y} - a_{y}b_{x}|
$$

### 3D Determinant = Parallelepiped Volume

<center>

![](images/3d_det-solution.png)   
*Calculation of volume of parallelepiped*

</center>

Let CSTU be the cross-section through C of the parallelepiped parallel to the $xy$-plane. We observe that if we move the part above CSTU to the bottom of the parallelepiped, we will get a new parallelepiped OPQR-CSTU (notice that OPQR is *in the* $xy$*-plane*), which has the same volume as the original parallelepiped.

Let the coordinates of P and R be respectively

$$P:\left( x_{P},\ y_{P},\ 0 \right),\ \ R:\left( x_{R},\ y_{R},\ 0 \right)$$

The vectors $\overrightarrow{AP}$ and $\overrightarrow{BR}$ are parallel to $\boldsymbol{c}$. Therefore, they can be expressed as

$$\overrightarrow{AP} = \alpha\boldsymbol{c},\ \ \overrightarrow{BR} = \beta\boldsymbol{c}$$

And the coordinates of P and Q can be found from

$$\overrightarrow{OP} = \overrightarrow{OA} + \overrightarrow{AP} = \boldsymbol{a} + \alpha\boldsymbol{c},\ \ \overrightarrow{OR} = \overrightarrow{OB} + \overrightarrow{BR} = \boldsymbol{b} + \beta\boldsymbol{c}$$

Therefore, we write

$$
\left\{
\begin{align*}
    x_{P} = a_{x} + \alpha c_{x} \\
    y_{P} = a_{y} + \alpha c_{y} \\
    0 = a_{z} + \alpha c_{z} 
\end{align*}
\right. ,
\quad
\left\{
\begin{align*}
    x_{R} = b_{x} + \beta c_{x} \\
    y_{R} = b_{y} + \beta c_{y} \\
    0 = b_{z} + \alpha c_{z}
\end{align*}
\right.
$$

from which we obtain

$$
\alpha = - \frac{a_{z}}{c_{z}} ,\quad
\beta = - \frac{b_{z}}{c_{z}}
$$

Therefore

$$
\left\{
\begin{align*}
    x_{P} = a_{x} - \frac{a_{z}c_{x}}{c_{z}} \\
    y_{P} = a_{y} - \frac{a_{z}c_{y}}{c_{z}}
\end{align*}
\right. , 
\quad
\left\{
\begin{align*}
    x_{R} = b_{x} - \frac{b_{z}c_{x}}{c_{z}} \\
    y_{R} = b_{y} - \frac{b_{z}c_{y}}{c_{z}}
\end{align*}
\right.
$$

Using the results for 2D, we immediately get

$$
\begin{align*}
    &A_{\text{OPQR}} 
    = \det \begin{bmatrix}
        x_{P} & x_{R} \\
        y_{P} & y_{R}
    \end{bmatrix}
    \\
    &= \frac{1}{c_{z}}\left( a_{x}b_{y}c_{z} + a_{y}b_{z}c_{x} + a_{z}b_{x}c_{y} - a_{z}b_{y}c_{x} - a_{y}b_{x}c_{z} - a_{x}b_{z}c_{y} \right)
\end{align*}
$$

The height of the new parallelepiped is evidently equal to $c_{z}$. Then, the volume $V$ is simply

$$
\begin{align*}
    V &= A_{\text{OPQR}} \times c_{z} 
    \\
    &= a_{x}b_{y}c_{z} + a_{y}b_{z}c_{x} + a_{z}b_{x}c_{y} - a_{z}b_{y}c_{x} - a_{y}b_{x}c_{z} - a_{x}b_{z}c_{y}
\end{align*}
$$

This defines the determinant

$$
V = \det \begin{bmatrix}
    a_{x} & b_{x} & c_{x} \\
    a_{y} & b_{y} & c_{y} \\
    a_{z} & b_{z} & c_{z} \\
\end{bmatrix}
$$

### EXERCISE

Generalize the above procedure to derive the expression of the 4D determinant. Its absolute value defines the "volume" of a 4D parallelepiped.

