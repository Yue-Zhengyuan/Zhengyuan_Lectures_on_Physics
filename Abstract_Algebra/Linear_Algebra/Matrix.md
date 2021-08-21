# Matrix Representation of Linear Maps 

Let $A: V \to W$ be a linear map. Let us choose a set of basis vectors in $V, W$:

$$
\begin{align*}
    \text{Basis of}\ V &: \{e_1,...,e_n\} 
    &\ (n = \dim V)
    \\
    \text{Basis of}\ W &: \{\epsilon_1,...,\epsilon_m\} 
    &\ (m = \dim W)
\end{align*}
$$

Due to the linearity, $A$ can be *fully* described by specifying its action on *each* basis vector of $V$:

$$
e_i \mapsto A e_i \quad (i = 1, ..., n)
$$

Then for any vector $v$, we have

$$
\begin{align*}
    v' 
    &\equiv A v 
    \\
    &= A (v_i e_i) 
    &\quad &\text{(Expand $v$ using $\{e_i\}$)}
    \\
    &= v_i (A e_i) 
    &\quad &\text{(Use linearity of $A$)}
\end{align*}
$$

Nothing prevents us to expand $A e_i$ as linear combination of the basis vectors of $W$: 

$$
A e_i = \sum_{j=1}^m \epsilon_j A_{j i} \qquad (i = 1, ..., n)
$$

The numbers $A_{j i}$ are linear combination coefficients. We do not write $A_{i j} \epsilon_j$, which is just a matter of convention. The collection of all the coefficients $A_{ji}$ form a **matrix** that represents the linear map $A$, in which $A_{i j}$ is at the $i$th row and the $j$th column:

$$
[A_{ji}] = \begin{bmatrix}
    A_{11} & \cdots & A_{1n} \\
    \vdots & & \vdots \\
    A_{m1} & \cdots & A_{mn}
\end{bmatrix} \in F^{m \times n}
$$

Remember the meaning of each column of the transformation matrix: **the $i$th column is the transformation result of the $i$th basis vector of $V$**. 

<div class="remark">

*Remark*: **Translation** ($T: v \in V \mapsto v + t \in V$, where $t$ is the translation vector) is not a linear map on $V$. One can easily verify, for two vectors $v, w \in V$

$$
\left.
\begin{align*}
    T (v + w) &= (v + w) + t
    \\
    T v + T w &= (v + w) + 2t
\end{align*}
\right\} \Rightarrow
T(v + w) \ne Tv + Tw
$$

However, it is possible to use matrices *in $(d+1)$ dimension* to represent $d$-dimensional translations (see [this Wikipedia article][affine_trans]). 

[affine_trans]: https://en.wikipedia.org/wiki/Affine_transformation#Representation

</div><br>

## Matrix-Vector Multiplication

Using the linearity $A$, we can find the new vector $A v \in W$ to which the vector $v \in V$ is sent by the linear map $A$: 

$$
\begin{align*}
    v' &= v_j (A e_j)
    \\
    &= v_j (\epsilon_i A_{i j}) 
    &\quad &\text{(Expand $A e_j$ using $\{\epsilon_i\}$)}
    \\
    &= (A_{i j} v_j) \epsilon_i
    &\quad &\text{(Rearrange)}
\end{align*}
$$

Therefore, the component of $A v$ along the basis $\epsilon_i$ of $W$ is given by

$$
(A v)_i = A_{i j} v_j
$$

This is *defined* as the rule of the multiplication of matrix $A$ and column vector $v$.

## Composition of Linear Map

Suppose we have two linear maps 

$$
B: V \to W, \quad A: W \to X
$$ 

We first apply $B$ onto a vector $v$, then apply $A$. The result of the combined transformation is denoted by $A B v \in X$ (the transformations are written from right to left according to the order).

Now let us find its components under a basis of $X$: 

$$
\begin{align*}
    [A (B v)]_{i}
    = A_{i j} (B v)_{j}
    = A_{i j} (B_{j k} v_k)
    = A_{i j} B_{j k} v_k
\end{align*}
$$

We discover that if we define a new matrix $C$ by

$$
C_{i k} \equiv A_{i j} B_{j k}
$$

We obtain

$$
[A(B v)]_i = C_{ik} v_k
$$

This means that *$C$ is the representation matrix of the composite transformation $AB: V \to X$*. Thus we define that the **product** of the matrices $A, B$ is 

$$
(AB)_{i k} \equiv A_{i j} B_{j k}
$$

so that

$$
[A(B v)]_i = [(AB) v]_i
$$

The matrix product defined in this way has the following properties:

- **Associativity**: $(AB)C = A(BC)$

- **Non-commutativity**: In general $AB \ne BA$
