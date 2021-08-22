# Matrix Representations of A Group

## Unitarity Theorem

Finite groups always have **unitary representations**, i.e. there exist a representation $D(g)$ so that for all group elements $g$,

$$
D^{\dagger}(g)D(g) = 1
$$

## Reducible and Irreducible Representations

*Definition*: Let $D(g)$ be a matrix representation of group $G$.

- **Reducible representation**: can be put into *the same block-diagonal form* via the *same* similarity transformation for *all* group elements.
- **Irreducible representation**: representations that cannot be put into the same block diagonal form for all elements.

### Schur Lemma

<div class="result">

*Theorem*: (Schur) Let $D(g)$ be an $n$-dimensional *irrep* of a *finite* group $G$, and $A$ an $n \times n$ matrix.

$$
\begin{align*}
    \forall g \in G: A D(g) = D(g) A 
    \ \Rightarrow \ 
    A = \lambda 1 \quad (\lambda \in \C)
\end{align*}
$$

</div><br>

### Irreducible Representation Orthogonality

<div class="result">

*Theorem*: Let $r,s$ label two irreps with dimension $d_r,d_s$. Then

$$
\sum_g [D_{ij}^{(r)}(g)]^* D_{kl}^{(s)}(g)
= \frac{|G|}{d_r} \delta_{rs} \delta_{ik} \delta_{jl}
$$

</div><br>

## Conjugation Class and Character

A equivalence class of conjugation of elements in a group $G$ (denoted by $c$) is defined as follows: let $g_c\in c$, then

$c=\left\{g\in G\left|g_c\right.=f^{-1}g f \text{for} \text{some} f\in G\right\}$

Due to the invariance of matrix trace under similarity transformations, we can define the **character** of the equivalence class as

$$
\chi^{(r)}(c)\equiv \Tr D^{(r)}(c)
$$

### Character Orthogonality

<div class="result">

*Theorem*: Let $n_c$ be the number of group elements in the $c$ equivalence class. Then

$$
\sum_c n_c [\chi^{(r)}(c)]^* \chi^{(s)}(c)=|G|\delta_{r s}
$$

</div>

----

*Proof*:

From the representation orthogonality, we trace over $(i,j)$ and $(k,l)$:

$\sum_g \sum_{i, k} \left[D_{i i}^{(r)}(g)\right]{}^*D_{k k}^{(s)}(g)=\frac{|G|}{d_r}\delta_{r s}\sum_{i, k} \delta_{i k}\delta_{i k}=|G|\delta
_{r s}$

The summation over $g$ can be changed to summation over equivalence
classes:

$\sum_c n_c \chi^{(r)*}(c)\chi^{(s)}(g)=|G|d_r\delta^{r s}\quad \blacksquare$

----

### Test for Irreducibility

In a general representation, suppose that the $r$th irrep occurs $n_r$ times in the block-diagonal form. Then

$$
\chi (c)=\sum_r  n_r\chi^{(r)}(c)
$$

Therefore

$$
\begin{align*}
    \sum_c n_c\chi^*(c)\chi (c) &= |G|\sum_r  n_r^2
    \\
    \sum_c n_c\chi^{(r)*}(c)\chi (c) &= |G| n_r
\end{align*}
$$



By setting $n_r=1$ for only one irrep, we easily obtain the criterion for a representation to be irreducible:

$$
\sum_c  n_c\chi^*(c)\chi (c)=|G|
$$

### Dimension of Irreducible Representations

$\sum_r  d_r^2=|G|$

*Proof*:

To prove this theorem, we need the . Any finite group $G$ is isomorphic
to a subgroup of the permutation group $S_{|G|}$. But $S_{|G|}$ has a
representation obtained by permuting the rows of the $|G|$-dimensional
identity matrix. This representation restricted to group $G$ is the
regular representation of $G$.

Regular representation has the following property: except the matrix for
identity (which is an equivalence class of *itself*), all diagonal
elements of the representation matrices are zero (since all rows are
moved away from the original place). Then

$\sum_c  n_c\chi^{(\text{reg})*}(c)\chi^{(\text{reg})}(c)=n_e\chi^{(\text{reg})*}(e)\chi^{(\text{reg})}(e)\\
=d_{\text{reg}}^2=|G|^2=|G|\sum_r  n_r^2$

$\Longrightarrow \text{ }\sum_r  n_r^2=|G|$

Besides

$\sum_c  n_c\chi^{(r)*}(c)\chi^{(\text{reg})}(c)=n_e\chi^{(r)*}(e)\chi^{(\text{reg})}(e)\\
=d_rd_{\text{reg}}=d_rN(G)=|G| n_r$

$\Longrightarrow \text{ }d_r=n_r$

( *all* irreps appear in the regular representation) and

$\sum_r  n_r^2=\sum_r  d_r^2=|G|\quad \blacksquare$

### Irreducible Representation of Abelian Groups

For an Abelian group, *all elements are an equivalence class of their
own*. According to

Therefore, *all irreps of an Abelian group are one-dimensional*.

Then, since

$\sum_r  d_r^2=|G|$

we conclude that *the Abelian group has $|G|$ irreps*.

### Character Table

A **character table** lists all equivalence classes in the group and the corresponding values of characters.

Example: Character table of $A_4$

In the table $\omega =\exp (2\pi i / 3)$. 

$$
\begin{array}{ccccccc}
    A_4 & n_c & c & 1 & 1' & 1'' & 3 
    \\[4pt] \hline \\[-6pt]
    1 & 1 & I & 1 & 1 & 1 & 3
    \\[4pt] \hline \\[-6pt]
    Z_2 & 3 & (12)(34) & 1 & 1 & 1 & -1
    \\[4pt] \hline \\[-6pt]
    Z_3 & 4 & (123) & 1 & \omega  & \omega^* & 0
    \\[4pt] \hline \\[-6pt]
    Z_3 & 4 & (132) & 1 & \omega^* & \omega  & 0
\end{array}
$$

### Orthogonality of Character Table

Column Orthogonality (different irrep.)

$\sum_c  n_c\chi^{(r)*}(c)\chi^{(s)}(c)=|G|\delta^{r s}$

Row Orthogonality (different equivalence class)

$\sum_r \chi^{(r)*}(c)\chi^{(r)}\left(c'\right)=\frac{|G|}{n_c}\delta^{r s}$

Character Table is Square

$N_C=N_R$

Here $N_C$ is the number of equivalence classes in the group, and
$N_R$ is the number of all irreps of the group.

## Reality of Representations

Real: The representation matrices are real

Complex: The representation matrices are complex, and is not equivalent
with their complex conjugate (they have complex-conjugate characters)

Pseudo-real: The representation matrices are complex, but is equivalent
with their complex conjugate (they have equal real characters)

$$
\frac{1}{|G|} \sum_g \chi^{(r)}(g^2)
= \eta^{(r)} = \begin{cases}
    1 & \text{Real} \\
    0 & \text{Complex} \\
    -1 & \text{Pseudo-real} \\
\end{cases}
$$
