# Inner Product

## Defining Properties

For two vectors $u,v\in V$, we can define an operation called the **inner product** (denoted by $u \cdot v$), which send two vectors *to a real number*: 

$$
\_ \cdot \_ : V \times V \to \mathbb{R}
$$

Inner product is *defined to have* the following properties:

- **Symmetry**: $\forall \, u,v \in V$

    $$
    u \cdot v = v \cdot u
    $$

- **Linearity in the second argument**: $\forall \, u,v,w \in V ;\, \alpha,\beta \in \mathbb{R}$
    
    $$
    u \cdot (\alpha v + \beta w) 
    = \alpha (u \cdot v) + \beta(u \cdot w)
    $$

The two properties combined gives linearity in the first argument, too (show this by yourself; thus we say that the inner product is a **bi-linear** function):

$$
(\alpha v + \beta w) \cdot u
= \alpha (v \cdot u) + \beta(w \cdot u)
$$

Up to now we have not really define how to *calculate* the inner product. It turns out that there are many ways to define the calculation that satisfy the two properties above. We can then also generalize the concept of inner product to more abstract vector spaces.

*Remark*: Some concepts derived from the inner product

- Two vectors are **orthogonal** to each other if their inner product is 0.
- The **length** of a vector $v$ is defined as $|v| \equiv \sqrt{v \cdot v}$. 

## Orthonormal Basis Vectors

Until now we have not described how to really calculate the inner product. For two vectors $u,v \in V$

$$
u = u_i e_i, \quad v = v_i e_i
$$

Due to bi-linearity of inner product, $u \cdot v$ can be reduced to the linear combination of the inner product of basis vectors:

$$
u \cdot v = u_i v_j (e_i \cdot e_j)
$$

The numbers $e_i \cdot e_j$ are still not determined, and depend on both the choice of basis vectors, which is *not unique*. Now we pick a *special* choice of basis vectors such that

$$
e_i \cdot e_j = \delta_{ij} 
= \begin{cases}
    1 & i = j \\
    0 & i \ne j
\end{cases}
$$

i.e. each basis vector has length 1, and is orthogonal to all other basis vectors. You can just imagine them as the familiar unit vectors along the coordinate axes. Such a set of basis vectors is called an **orthonormal basis** (orthogonal and normalized).

Then we recover something you already know:

$$
u \cdot v = u_i v_j \delta_{ij} = u_i v_i
$$

We emphasize that **this formula is valid only when we are using the components of $u,v$ along an orthonormal basis**.

From this relation, we can choose $v = e_j$ and express the $j$th components of $u$ along $e_j$ as the inner product of $u$ and $e_j$:

$$
u \cdot e_j = u_i \delta_{ij} = u_j
$$

*Remark*: Even the choice of orthonormal basis is *not unique*. For example, you can easily *rotate* the basis to obtain a new one. This is easy to understand intuitively, but a rigorous mathematical proof of this statement is not very trivial.

## Inner Product under Linear Map

After the linear map $A$, the inner product $u \cdot v$ is transformed to 

$$
\begin{align*}
    (Au) \cdot (Av)
    &= (Au)_i (Av)_j (e_i \cdot e_j)
    \\
    &= (A_{ik} u_k) (A_{jl} v_l) (e_i \cdot e_j)
\end{align*}
$$

If we are using an orthonormal basis, then

$$
\begin{align*}
    (Au) \cdot (Av)
    &= (A_{ik} u_k) (A_{jl} v_l) \delta_{ij}
    \\
    &= A_{ik} u_k A_{il} v_l
    \\
    &= u_k (A^\mathsf{T})_{ki} A_{il} v_l
    \\
    &= u_k (A^\mathsf{T} A)_{kl} v_l
\end{align*}
$$

## Orthogonal Matrix

Let us consider a special case: if 

$$
A^\mathsf{T} A = 1 \quad
\text{or equivalently $A A^\mathsf{T}$ = 1}
$$

where $1$ is the **identity matrix** (we will talk more about it later)

$$
(1)_{ij} = \delta_{ij}
$$

then

$$
\begin{align*}
    (Au) \cdot (Av)
    &= u_k \delta_{il} v_l
    \\
    &= u_k v_k = u \cdot v
\end{align*}
$$

i.e. the inner product is invariant under $A$. We call such a representation matrix an **orthogonal matrix**. 
