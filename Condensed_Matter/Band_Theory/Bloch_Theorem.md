# The Translation Group

An $d$-dimensional **Bravais lattice** is an infinite array of discrete points described by $d$ linearly independent basis vectors $\{a_1,...,a_d\}$: the position of any point $R$ can be described by

$$
R = \sum_{j=1}^d n_j a_j, \quad 
n_1,...,n_d \in \Z
$$

The lattice is invariant under elementary translation operations along any one of the basis vectors. We write

$$
g_j = \text{Translation by the vector} \ a_j
$$

Obviously all these elementary translations $\{g_1,...,g_d\}$ commute with each other:

$$
g_i g_j = g_j g_i
$$

They generate the (Abelian) **translation group** of the lattice:

$$
G = \left\{ 
    \prod_{j=1}^n g_j^{n_j} \bigg| n_1,...,n_d \in \Z
\right\}
$$

The physical meaning of each element is

$$
\prod_{j=1}^n g_j^{n_j} = \text{Translation by the vector} \ 
\sum_{j=1}^n n_j a_j
$$

## Bloch Theorem

