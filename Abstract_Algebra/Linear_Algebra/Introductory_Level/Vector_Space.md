# Vector Spaces and Basis Vectors

## Vector Spaces

For the purpose of an introductory physics course, **vectors** can be imagined as arrows in the plane (2D), the space (3D) or in higher dimensional spaces, and a **vector space** (denoted by $V$) is the collection (set) of all vectors in that space. 

We can perform the following operations on vectors in the vector space:

- **Addition** of vectors

- **Scalar multiplication** on a vector (by *real* numbers)

    (Later in your life you will have to deal with *complex* numbers, but now we restrict ourselves to the real world.)


[vec_space]: https://en.wikipedia.org/wiki/Vector_space

## Linear Independence

First we introduce an commonly encountered concept in linear algebra. Consider a set of vectors $e_1, e_2, ..., e_n \in V$. Since we have vector addition and scalar multiplication in the vector space $V$, we can construct a *linear combination* of them, with (real) coefficients $v_1, ..., v_n$: 

$$
v = v_1 e_1 + \cdots + v_n e_n
= \sum_{i=1}^n v_i e_i \in V
$$

Then the vectors $e_1, ..., e_n$ are said to be **linearly independent** if

$$
v = \sum_{i=1}^n v_i e_i = 0 
\, \Leftrightarrow \,
v_1 = \cdots = v_n = 0
$$

i.e. the zero vector can *only* be obtained by setting *all* combination coefficients to zero. 

*Remark*: The set of all vectors obtained from linear combinations is called the **span** of the vectors $e_1, ..., e_n$, denoted by

$$
\span (e_1, ..., e_n)
= \left\{
    \sum_{i=1}^n v_i e_i \mid
    v_1, ..., v_n \in \mathbb{R}
\right\}
$$

## Basis Vectors

Given a set of *linearly independent* vectors $\{e_1,...,e_n\}$, if *any* vector $v\in V$ can be *uniquely* represented as a linear combination of $e_1, ..., e_n$

$$
v = \sum_{i=1}^{n} v_i e_i
\qquad v_1,...,v_n\in \mathbb{R}
$$

Then the vectors $e_1, ..., e_n$ are called **basis vectors** of $V$. The number of these vectors $n$ is called the **dimension** of $V$ (denoted by $\dim V$). 

The number $v_i$ is called the **components** of the vector $v$ along the basis vector $e_i$. Then the vector $v$ can be also written as a **column vector** (without explicit reference to the basis we are using)

$$
v = \begin{bmatrix}
    v_1 \\ \vdots \\ v_n
\end{bmatrix}
$$

*Remarks*:

- Usually we choose an **orthonormal basis**, i.e. each basis vector is of length 1, and is orthogonal to other basis vectors (i.e. **inner product** is zero). 
    
    An example is the usual $x, y, ...$ unit vectors (let us call them the **standard basis**). In this case, the components of a vector *coincides* with the coordinates of the end point of the vector. 

- The choice of basis vectors is *not unique*, since there are *infinitely many* sets of $n$ linearly-independent vectors in the vector space $V$. For example (say $n = 2$), if $e_1, e_2$ are basis vectors of $V$, then we can also use

    $$
    e'_1 = e_1 + 3e_2, \quad
    e'_2 = 2e_1 - e_2
    $$

- In the expansion of basis vectors themselves
    
    $$
    e_i = \sum_{a=1}^n (e_i)_a e_a
    $$

    The $a$th component of the $i$th basis vector is simply 

    $$
    (e_i)_a = \delta_{ia}
    = \begin{cases}
        0, & a \ne i \\
        1, & a = i
    \end{cases}
    $$

    The notation $\delta_{ia}$ is called the **Kronecker delta**. For example, when $\dim{V} = 2$, we have

    $$
    e_1 = \begin{bmatrix}
        1 \\ 0
    \end{bmatrix}, \quad
    e_2 = \begin{bmatrix}
        0 \\ 1
    \end{bmatrix}
    $$

    You must be aware that **this does not mean that they are the standard basis**. 

- Two vectors of the same components will be different if the sets of basis vectors used to construct them are not the same. 

    <center>

    ![](images/different_basis.svg)   
    *Two different vectors can have the same components (2, 3) <br>under different basis; the figures are drawn to the same scale*

    </center>

## Einstein Summation Rule

People are tired of always writing the summation sign $\sum$ in linear algebra calculations. Thus the genius Einstein invented the following rule: 

<center>

**If an index appears twice, then sum over it.**

</center>

which allows people to throw away the summation signs. For example:

$$
\sum_i v_i e_i \to v_i e_i
$$

The index $i$ appears twice, thus we should sum over $i$. Unless there might be some ambiguity, we shall always adopt the Einstein summation rule in the following. 

In addition, we are free to choose which letter represents the index to be summed over:

$$
\sum_i v_i e_i = \sum_j v_j e_j  = \cdots
\, \Rightarrow \,
v_i e_i = v_j e_j = \cdots
$$
