# Euclidean Group

The group $\Isom(\R^n)$ of isometries between $\R^n$ and itself is called the **Euclidean group** $\mathbb{E}$. 

The set $\R^n$ as a vector space can be endowed with an *inner product* defined as

$$
u \cdot v = \sum_{j=1}^n u_j v_j
$$

where $u_j, v_j$ are components of $u, v$ along the $j$th vector $e_j$ of an *orthonormal* basis. Based on the inner product, the metric on $\R^n$ is:

$$
d(x,y) = \sqrt{(x-y)\cdot(x-y)} = |x - y|
$$

The angle $\theta$ between two vectors $u,v$ is then defined as

$$
u \cdot v = |u||v| \cos \theta
$$

## Important Subgroups

Two types of isometries of $\R^n$ are of special importance; they form subgroups of $\mathbb{E}$ respectively. 

### Origin-Preserving Isometries

Such an isometry $R$ keeps the origin (the zero vector) invariant: 

$$
R(0) = 0
$$

All origin-preserving isometries form a *subgroup* $G_0$ of $\mathbb{E}$:

$$
G_0 \equiv \{R \in \Sym(\R^n) \mid R(0) = 0\}
$$

<div class="result">

*Theorem*: $G_0 \cong \O(n)$.

</div>

----

*Proof*: Let $R \in G_0$. 

- An important observation is that *$R$ preserves the inner product*: for any $u,v \in \R^n$

    $$
    u \cdot v = R(u) \cdot R(v)
    $$

    To show this, first note that $R$ preserves the norm of any vector:

    $$
    |v - 0| = |R(v) - R(0)| \Rightarrow 
    |v| = |R(v)|
    $$

    Then

    $$
    \begin{align*}
        2u \cdot v &= |u|^2 + |v|^2 - |u - v|^2
        \\
        2h(u) \cdot R(v)
        &= |R(u)|^2 + |R(v)|^2 - |R(u) - R(v)|^2
        \\
        &= |u|^2 + |v|^2 - |u - v|^2 = 2u \cdot v
    \end{align*}
    $$

- Next, we prove that $R$ is a linear map, i.e. for any $u,v  \in \R^n$ and $a \in \R$

    $$
    R(u+v) = R(u) + R(v), \quad R(av) = ah(v)
    $$

    Introduce an orthonormal set of basis vectors $\{e_1,...,e_n\}$. Then $v$ can be expressed as

    $$
    v = (v \cdot e_j) e_j \equiv v_j e_j
    $$

    Since $R$ preserves the inner product:
    
    - $\{e'_1,...,e'_n\}$ (with $e'_j \equiv R(e_j)$) is also an orthonormal basis, allowing us to write

    $$
    v = (v \cdot e'_j) e'_j \equiv v'_j e'_j
    $$

    - The components of $R(v)$ along the new basis are the same as those of $v$ along the old basis:

        $$
        R(v) = \underbrace{[R(v) \cdot e'_j]}_{v \cdot e_j} e'_j = v_j e'_j
        $$

    Then

    $$
    \begin{align*}
        R(u+v) &= (u + v)_j e'_j 
        = (u_j + v_j) e'_j \\
        &= u_j e'_j + v_j e'_j = R(u) + R(v)
        \\
        R(av) &= (av)_j e'_j 
        = a v_j e'_j = a R(v)
    \end{align*}
    $$

- Obviously linear maps preserving the inner product are orthogonal maps. They are represented by $n \times n$ orthogonal matrices (in the group $\O(n)$) under any orthonormal basis. $\blacksquare$

----

Due to this isomorphism, we simply use the orthogonal matrix $R \in \O(n)$ to denote the linear map $A$. The action of $R \in G_0$ on any $x \in \R^n$ is directly given by the matrix multiplication

$$
R(x) = R x
$$

### Translation Group

Among isometries that does not preserve the origin, **translations** are of special importance. A translation by a vector $a \in \R^n$ is denoted by $\tau_a$: 

$$
\tau_a: \R^n \to \R^n \quad 
\forall x\in \R^n, \ \tau_a(x) = a + x
$$

Intuitively, the composition and the inverse of translations are given by

$$
\tau_a \tau_b = \tau_b \tau_a = \tau_{a+b}, \quad
\tau_a^{-1} = \tau_{-a}
$$

Thus all translations form an *Abelian* subgroup $\mathbb{T}$ of $\mathbb{E}$. Obviously:

<div class="result">

*Theorem*: $\mathbb{T} \cong \R^n$ 

Here $\R^n$ is understood as a group with the usual vector addition as group multiplication). The isomorphism is simply

$$
\tau_a \in \mathbb{T} \mapsto a \in \R^n
$$

</div><br>

Due to this isomorphism, we simply use the translation vector $a$ to denote the translation. The groups multiplication in $\mathbb{T}$ will be written additively:

$$
\tau_a \tau_b \to a + b, \quad
1_\mathbb{T} = \tau_0 \to 0
$$

The action of $a \in \mathbb{T}$ on $x \in \R^n$ is 

$$
a(x) = a + x
$$

<div class="remark">

*Remark*: Although $\mathbb{T}$ is an Abelian subgroup, this does not mean that its elements also commute with other elements in $\mathbb{E}$ (often they do not). 

</div><br>

## Group Structure of $\mathbb{E}$

The following theorem is now obvious:

<div class="result">

*Theorem*: Any isometry $g \in \mathbb{E}$ can be expressed as the composition of an origin-preserving one $R \in G_0$ and a translation $a \in \mathbb{T}$, i.e.

$$
\mathbb{E} = \mathbb{T} G_0 
= \{aR \mid a \in \mathbb{T}, R \in G_0\}
$$

</div>

----

*Proof*: For each $g$, simply choose the translation $a = g(0)$. $\blacksquare$

----

The group multiplication in $\mathbb{E}$ is defined based on the action on a vector $x \in \R^n$: for an arbitrary $g = \tau_a R$

$$
g(x) = (aR)(x) = a + Rx
$$

Then the action of the composition of two elements in $\mathbb{E}$ is

$$
\begin{align*}
    (a R) (a' R')(x)
    &= (a, R)(a' + R'x)
    \\
    &= a + R(a' + R'x)
    \\
    &= (a + Ra') + RR'x
\end{align*}
$$

From this result:

<div class="result">

**Multiplication and inverse in $\mathbb{E}$:**

$$
(a R) (a' R') 
= (a+Ra')(R R'), \quad
(a R)^{-1} = (-R^{-1}a) R^{-1}
$$

</div>

----

*Verifying the inverse*:

$$
\begin{align*}
    (a R)[(-R^{-1}a) R^{-1}]
    &= (a - RR^{-1}a) (RR^{-1})
    \\
    &= (a - a)1 = 0 \cdot 1 = 1_G
    & \blacksquare
\end{align*}
$$

----

With this multiplication, we can show that

<div class="result">

*Theorem*: $\mathbb{T} \lhd \mathbb{E}$ (the translation group is a *normal* subgroup of $\mathbb{E}$).

</div>

----

*Proof*: For any $\tau_a \in \mathbb{T}$ and any $\tau_b R \in \mathbb{E}$

$$
\begin{align*}
    &(b R)^{-1} a (b R)
    = [(-R^{-1}b) R^{-1}] [(a+b)R] \\
    &= [-R^{-1}b + R^{-1}(a+b)](R^{-1} R) \\
    &= (R^{-1}a)1
    & \blacksquare
\end{align*}
$$

----

From the above analysis, we find that $\mathbb{E}$ is (isomorphic to) the *semi-direct product* of the translation group $\mathbb{T}$ and the point group $G_0$:

$$
\left. \begin{aligned}
    \mathbb{E} &= \mathbb{T} G_0 \\
    \mathbb{T} &\lhd \mathbb{E} \\
    \mathbb{T} \cap G_0 &= \{1\} \\
\end{aligned} \right\} \Rightarrow
\mathbb{E} \cong \mathbb{T} \rtimes G_0 \cong \R^n \rtimes \O(n)
$$

The isomorphism is simply $\tau_a R \mapsto (\tau_a,R)$. The homomorphism $\phi: G_0 \to \Aut(\mathbb{T})$ in the semi-direct product can be found by comparing with the general definition:

$$
\begin{gather*}
    (a, R) (a', R')
    \overset{\text{def}}{=} (a'+\phi_R(a'), R R')
    = (a+Ra', hh')
    \\ \Downarrow \\
    \boxed{
        \phi_R: a \mapsto Ra
    }
\end{gather*}
$$
