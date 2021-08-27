# Inner Product

*Definition*: Let $V$ be a vector space over the field $F$ (usually $\R$ or $\C$).

- **Inner product**: a binary operation sending two vectors to the field $F$: 

    $$
    \la \_, \_ \ra: V \times V \to F,
    \quad (u,v) \mapsto \expect{u,v}
    $$

    which satisfied the following axioms: for all $u,v,w\in V$ and $\alpha \in F$

    $$
    \begin{array}{c|c}
        \text{Requirement} & \text{Description}
        \\[4pt] \hline \\[-8pt]
        \text{Conjugate symmetry} & 
        \expect{u,v} = \expect{v,u}^*
        \\[6pt]
        \text{Positivity} &
        \expect{v,v} \ge 0
        \\[6pt]
        \text{Definiteness} &
        \expect{v,v} = 0 \Leftrightarrow v = 0
        \\[6pt]
        \text{Additivity in 2nd slot} &
        \expect{u,v+w} = \expect{u,v} + \expect{u,w}
        \\[6pt]
        \text{Linearity in 2nd slot} &
        \expect{u,\alpha v} = \alpha \expect{u,v}
    \end{array}
    $$

<div class="remark">

*Remark*: A vector space endowed with an inner product is called an **inner product space**.

</div><br>

### Some Concepts Derived from the Inner Product

- Two vectors are **orthogonal** to each other if their inner product is 0.
- The **length** of a vector $v$ is defined as $|v| \equiv \sqrt{\expect{v,v}}$. 

## Orthonormal Basis Vectors

Until now we have not described how to really calculate the inner product. For two vectors $u,v \in V$

$$
u = u_i e_i, \quad v = v_i e_i
$$

Due to bi-linearity of inner product, $\expect{u,v}$ can be reduced to the linear combination of the inner product of basis vectors:

$$
\expect{u,v} = u_i^* v_j \expect{e_i, e_j}
$$

The numbers $\expect{e_i, e_j}$ are still not determined, and depend on both the choice of basis vectors, which is *not unique*. Now we pick a *special* choice of basis vectors such that

$$
\expect{e_i, e_j} = \delta_{ij} 
= \begin{cases}
    1 & i = j \\
    0 & i \ne j
\end{cases}
$$

i.e. each basis vector has length 1, and is orthogonal to all other basis vectors. You can just imagine them as the familiar unit vectors along the coordinate axes. Such a set of basis vectors is called an **orthonormal basis** (orthogonal and normalized).

Then we recover something you already know:

$$
\expect{u,v} = u_i^* v_j \delta_{ij} = u_i^* v_i
$$

We emphasize that **this formula is valid only when we are using the components of $u,v$ along an orthonormal basis**.

From this relation, we can choose $u = e_j$ and express the $j$th components of $v$ along $e_j$ as the inner product of $u$ and $e_j$:

$$
\expect{e_j, v} = \delta_{ij} v_i = v_j
$$

*Remark*: Even the choice of orthonormal basis is *not unique*. For example, you can easily *rotate* the basis to obtain a new one. This is easy to understand intuitively, but a rigorous mathematical proof of this statement is not very trivial.

## Inner Product under Linear Map

After the linear map $A$, the inner product $\expect{u,v}$ is transformed to 

$$
\begin{align*}
    \expect{Au, Av}
    &= (Au)_i^* (Av)_j \expect{e_i, e_j}
    \\
    &= (A_{ik} u_k)^* (A_{jl} v_l) \expect{e_i, e_j}
\end{align*}
$$

If we are using an orthonormal basis, then

$$
\begin{align*}
    \expect{Au, Av}
    &= (A_{ik} u_k)^* (A_{jl} v_l) \delta_{ij}
    \\
    &= A_{ik}^* u_k^* A_{il} v_l
    \\
    &= u_k^* (A^\dagger)_{ki} A_{il} v_l
    \\
    &= u_k^* (A^\dagger A)_{kl} v_l
\end{align*}
$$

## Unitary Matrix

Let us consider a special case: if 

$$
A^\dagger A = 1 
\quad \text{or equivalently} \quad
A A^\dagger = 1
$$

where $1$ is the **identity matrix** (we will talk more about it later)

$$
(1)_{ij} = \delta_{ij}
$$

then

$$
\begin{align*}
    \expect{Au, Av}
    &= u_k^* \delta_{il} v_l
    \\
    &= u_k^* v_k = \expect{u,v}
\end{align*}
$$

i.e. the inner product is invariant under $A$. We call such a representation matrix a **unitary matrix**. 
