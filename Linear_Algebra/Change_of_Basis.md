# Change of Basis


Sometimes the standard basis may not be very convenient. Thus we naturally face the question of how to describe things using another set of basis vectors. It is expected that if we change to a new set of basis vectors:

- A vector will have different components 
- A linear transformation will be represented by a different matrix

In this section we shall show, in two dimensions, how to find the components of vectors and representation matrices of linear transformations under a new set of basis vectors. The generalization to higher dimensions is straightforward.

## Description of the New Basis

The new basis $e'_1, e'_2$ can always be described by their components along the old basis $e_1, e_2$ (which need not be the standard basis). In other words, the new basis is related to the old basis by a linear transformation $\mathcal{D}$:

$$
e'_1 = \mathcal{D} e_1 
= \begin{bmatrix}
    \mathcal{D}_{11} \\ \mathcal{D}_{21}
\end{bmatrix}, 
\quad
e'_2 = \mathcal{D} e_2
= \begin{bmatrix}
    \mathcal{D}_{12} \\ \mathcal{D}_{22}
\end{bmatrix}
$$

Thus the change from the old basis to the new basis is described by the matrix (under the old basis)

$$
\mathcal{D} = \begin{bmatrix}
    \mathcal{D}_{11} & \mathcal{D}_{12} \\
    \mathcal{D}_{21} & \mathcal{D}_{22}
\end{bmatrix}
$$

*Remark*: The inverse operation, i.e. change from the new basis to the old basis, is described by the inverse matrix $\mathcal{D}^{-1}$ (**under the new basis**).

### Components of Vectors along the New Basis

For an arbitrary vector, its components along the new and the old basis vectors are related by

$$
\begin{align*}
    v 
    &= v_1 e_1 + v_2 e_2 
    &\quad &\text{(in old basis)}
    \\
    &= v'_1 e'_1 + v'_2 e'_2 
    &\quad &\text{(in new basis)}
    \\
    &= v'_1 \mathcal{D}e_1 + v'_2 \mathcal{D} e_2 
    \\
    &= \mathcal{D} (v'_1 e_1 + v'_2 e_2)
    &\quad &\text{(using linearity of $\mathcal{D}$)}
\end{align*}
$$

Using the matrix notation to make the expression more clear:

$$
\begin{bmatrix}
    v_1 \\ v_2
\end{bmatrix}
= \mathcal{D} \begin{bmatrix}
    v'_1 \\ v'_2
\end{bmatrix}
$$

Thus the components of $v$ along the new basis are given by

$$
\begin{bmatrix}
    v'_1 \\ v'_2
\end{bmatrix} = \mathcal{D}^{-1}
\begin{bmatrix}
    v_1 \\ v_2
\end{bmatrix} 
\quad \text{or} \quad
v' = \mathcal{D}^{-1} v
$$

where $v' \equiv v'_1 e_1 + v'_2 e_2$ is the vector constructed using the *new* components and the *old* basis vectors.

## Matrix of Linear Transformation under the New Basis

In the *basis-free* language, for an arbitrary vector $v \in V$, a linear transformation $A$ sends it to another vector $w \in V$:

$$
w = A v
$$

In the old basis ("un-primed"), we have the matrix form

$$
\begin{bmatrix}
    w_1 \\
    w_2
\end{bmatrix} 
= \begin{bmatrix}
    A_{11} & A_{12} \\
    A_{21} & A_{22}
\end{bmatrix}
\begin{bmatrix}
    v_1 \\
    v_2
\end{bmatrix} 
\quad \text{or} \quad 
w = A v
$$

In the new basis, we have a similar expression (with all elements "primed")

$$
\begin{bmatrix}
    w'_1 \\
    w'_2
\end{bmatrix} 
= \begin{bmatrix}
    A'_{11} & A'_{12} \\
    A'_{21} & A'_{22}
\end{bmatrix}
\begin{bmatrix}
    v'_1 \\
    v'_2
\end{bmatrix}
\quad \text{or} \quad 
w' = A' v'
$$

The matrix $A'$ is exactly the representation of the transformation $A$ under the new basis. Remember that

$$
w' = \mathcal{D}^{-1} w , \quad
v' = \mathcal{D}^{-1} v
$$

Then we obtain

$$
\begin{align*}
    \mathcal{D}^{-1} w 
    &= A' \mathcal{D}^{-1} v
    \\
    &= \mathcal{D}^{-1} A v \qquad (w = A v)
\end{align*}
$$

Since $v$ is arbitrary, we must have

$$
A' \mathcal{D}^{-1} = \mathcal{D}^{-1} A
$$

Multiply both sides by $\mathcal{D}$ *on the right*, we obtain the new representation matrix $A'$:

$$
A' = \mathcal{D}^{-1} A \mathcal{D}
$$

*Remark*: If two matrices $A,B$ are related by a change of basis, i.e.

$$
B=\mathcal{D}^{-1}A \mathcal{D}
$$

we say that $A$ and $B$ are **similar** to each other (the word "similar" is chosen for obvious reasons). The "sandwich" operation $\mathcal{D}^{-1}A \mathcal{D}$ is called a **similarity transformation**.

### EXERCISE

<center>

![](images/change_of_basis.svg)   
*An example of change of basis*

</center>

From the information of the figure above:

- Write down the matrix $\mathcal{D}$ representing the change of basis from the standard $e_x, e_y$ to $e_1, e_2$.

- Calculate the new components of the vector $v$. You may find $\mathcal{D}^{-1}$ using a computer. Check if your result agrees with the figure.

## Inner Product under the New Basis

Geometrically, the inner product $u, v$ depends only on the length of $u, v$ and the angle $\theta$ between them:

$$
u \cdot v = |u| |v| \cos \theta
$$

Thus intuitively, inner product should be *invariant* under change of basis, which does not change the vectors at all. Now let us verify it (this is a good exercise of matrix multiplication and Einstein summation rule; do it by yourself before looking at the answer below).

Under the old basis:

$$
u \cdot v = u_i v_j (e_i \cdot e_j)
$$

Under the new basis:

$$
\begin{align*}
    u \cdot v 
    &= u'_i v'_j (e'_i \cdot e'_j)
    \\
    &= (\mathcal{D}^{-1} u)_i (\mathcal{D}^{-1} v)_j
    \times
    ((\mathcal{D} e_i) \cdot (\mathcal{D} e_j))
    \\
    &= (\mathcal{D}^{-1})_{ik} u_k
    (\mathcal{D}^{-1})_{jl} v_l
    \times
    (\mathcal{D} e_i)_m (\mathcal{D} e_j)_n
    (e_m \cdot e_n)
    \\
    &= (\mathcal{D}^{-1})_{ik} u_k
    (\mathcal{D}^{-1})_{jl} v_l
    \times
    \mathcal{D}_{ma} (e_i)_a
    \mathcal{D}_{nb} (e_j)_b
    (e_m \cdot e_n)
\end{align*}
$$

However, we know that the $a$th component of $e_i$ along the basis itself is

$$
(e_i)_a = \delta_{i a}
$$

Similarly $(e_j)_b = \delta_{jb}$. Therefore

$$
\begin{align*}
    u \cdot v 
    &= (\mathcal{D}^{-1})_{ik} u_k
    (\mathcal{D}^{-1})_{jl} v_l
    \times
    \mathcal{D}_{ma} \delta_{ia}
    \mathcal{D}_{nb} \delta_{jb}
    (e_m \cdot e_n)
    \\
    &= (\mathcal{D}^{-1})_{ik} u_k
    (\mathcal{D}^{-1})_{jl} v_l
    \times
    \mathcal{D}_{mi} \mathcal{D}_{nj} 
    (e_m \cdot e_n)
    \\
    &= [\mathcal{D}_{mi} (\mathcal{D}^{-1})_{ik}]
    [\mathcal{D}_{nj} (\mathcal{D}^{-1})_{jl}]
    u_k v_l (e_m \cdot e_n)
    \\
    &= (\mathcal{D}\mathcal{D}^{-1})_{mk}
    (\mathcal{D}\mathcal{D}^{-1})_{nl}
    u_k v_l (e_m \cdot e_n)
    \\
    &= \delta_{mk} \delta_{nl} u_k v_l (e_m \cdot e_n)
    \\
    &= u_m v_n (e_m \cdot e_n)
\end{align*}
$$

Renaming $m,n$ to $i,j$, we have verified the result of $u \cdot v$ is unchanged if we calculate using the components along the new basis.
