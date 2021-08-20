# Lattice and Space Group

*Definition*:

- **$n$-dimensional (Bravais) lattice**: a subset (subgroup) of $\R^n$ construct by linear combinations of $n$ linearly-independent (basis) vectors $t_1,...,t_n$ with *integer* coefficients

    $$
    T = \{m_1 t_1 + \cdots m_n t_n \mid
    m_1,...,m_n \in \mathbb{Z}\}
    $$

- **Lattice vectors**: linear combinations of $t_1,...,t_n$ with integer coefficients.

    $$
    t = m_1 t_1 + \cdots m_n t_n, \quad
    m_1,...,m_n \in \mathbb{Z}
    $$

A lattice is isomorphic to its own translation group, which is a subgroup of the full translation group $\mathbb{T}$ of $\R^n$.

The lattice has other symmetry operations (involving rotations and reflections) that leave the origin invariant. The collection of all symmetries of the lattice form a **space group** in $\R^n$.

Space groups in 2D are called **wallpaper groups**.

## Point Group of A Lattice

*Definition*: Let $G$ be a space group.

- **Point group** $P$: the group of the *linear parts* of all elements in $G$, which is a subgroup of $\O(n)$.

    $$
    P = \{R \in \O(n) \mid \exist a \in \R^n, \ (a,R) \in G\}
    $$

    <div class="remark">
    
    *Remark*: 

    - $a$ is *not necessarily* in the translation subgroup $T$. 
    - The origin-preserving subgroup $G_0 \le P$

    </div>

    ----

    *Verifying group structure of $P$*:

    - $R, R' \in P \Rightarrow RR' \in P$, since group multiplication of $G$ gives

        $$
        (a, R) (a', R') = (a+Ra', RR')
        $$

    - The identity matrix $1 \in P$, since $(0,1) \in G$ (the identity of $G$)
    
    - $R \in P \Rightarrow R^{-1} \in P$, since

        $$
        (a,R)^{-1} = (-R^{-1}a, R^{-1})
        $$

    ----

<div class="result">

*Theorem*: For any space group $G$

- $P \cong G/T$.
- $P$ is a *finite* group.

</div>

----

*Proof*: 

- We shall use the first theorem of isomorphism. The desired isomorphism is simply

    $$
    \phi: \Isom(\R^n) \to \O(n) \quad (a,R) \mapsto R
    $$

    which can be restricted to $\phi|_G: G \to P$. Obviously $\ker \phi = T$. Then by the first theorem of isomorphism

    $$
    \im \phi|_G \cong G / \ker \phi|_G
    \Rightarrow P \cong G/T 
    \quad \blacksquare
    $$

- Let $\{t_1,...,t_n\}$ be the basis vectors of $T$, and $C$ a (hyper-)sphere centered at the origin that contains $t_1,...,t_n$ inside it. 

----

<div class="remark">

*Remark*: Now that $P$ is a finite subgroup of $\O(n)$, it can only be one of the following groups:

- 2D: Cyclic groups $C_n$ or dihedral groups $D_n$ ($n \in \N_+$)
- 3D: Cyclic groups $C_n$, dihedral groups $D_n$ ($n \in \N_+$) or symmetry groups of regular (Platonic) polyhedrons

</div><br>

## Crystallographic Restriction

In addition to the finiteness of the point group $P$, the geometry of lattices imposes a stronger restriction on the allowed rotations in $P$.

<div class="result">

*Theorem*: The rotations in the point group of any space group can only be of order 2,3,4,6.

</div><br>

----

*Proof*: Without loss of generality, assume that the rotation is in the 2D plane spanned by the translation basis vectors $t_1, t_2$ (otherwise we can always rename the basis vectors). We also choose two orthonormal basis vectors $e_1, e_2$ in this plane. Other dimensions are irrelevant in the following proof. 

The rotation by an angle $\theta$ (denoted by $R_\theta$) is represented by the matrices (omitting other dimensions, which are not affected)

$$
\begin{align*}
    \text{In basis} \ \{t_1,t_2\} &: \begin{pmatrix}
        a & b \\ c & d
    \end{pmatrix} \\
    \text{In basis} \ \{e_1,e_2\} &: \begin{pmatrix}
        \cos \theta & -\sin \theta \\ 
        \sin \theta & \cos \theta
    \end{pmatrix}
\end{align*}
$$

- Since the point group is finite, $\theta$ cannot be arbitrary. We take the minimal allowed value
    
    $$
    \boxed{
        \theta = 2\pi/n \quad (n \in \N_+)
    }
    $$

- The two matrices are related by a change of basis; thus they have the same trace:

    $$
    a + d = 2 \cos \theta
    $$

- If $(\tau, R_\theta)$ is a symmetry of the lattice (possibly $\tau \ne 0$), the new lattice basis $\{t'_1, t'_2\}$ must still be lattice vectors:

    $$
    \left. \begin{align*}
        t_1' = at_1 + ct_2 & \in T
        \\
        t_2' = bt_1 + dt_2 & \in T
    \end{align*} \right\} \Rightarrow \ 
    a,b,c,d \in \mathbb{Z} \ \Rightarrow \ 
    \boxed{2 \cos \theta \in \mathbb{Z}}
    $$
    
Thus the allowed $n$'s satisfying the boxed requirement are

$$
\begin{array}{c|c|c|c|c|c}
    n & 1 & 2 & 3 & 4 & 6
    \\[3pt] \hline \\[-6pt]
    2 \cos \frac{2\pi}{n} &
    2 & -2 & -1 & 0 & 1
\end{array} \quad \blacksquare
$$

----

## Isomorphic Space Groups

The point group $P$ is *uniquely* determined (up to isomorphism) by the space group $G$ producing it. 

<div class="result">

*Theorem*: Two isomorphic space groups $G,G'$ have isomorphic point groups $P,P'$.

</div>

----

*Proof*:

- We first prove a lemma.

    *Lemma*: Let $G, T$ be a space group and its translation subgroup. Define the set

    $$
    G_n = \{x \in G \mid \forall g \in G, \ x g^n = g^n x\}
    $$

----

If we restrict to 2D planes, we can prove a stronger statement on the isomorphism between two wallpaper groups and their point groups.

<div class="result">

*Theorem*: Let $G,G'$ be two isomorphic wallpaper groups with isomorphism $\phi:G \to G'$. Also, let $T,P$ and $T',P'$ be the translation subgroup and the point group of $G$ and  $G'$ respectively

</div>

----

*Proof*:

----
