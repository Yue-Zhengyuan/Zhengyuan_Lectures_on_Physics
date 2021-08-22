# Lattice and Space Group

*Definition*:

- **$n$-dimensional (Bravais) lattice**: a subset (subgroup) of $\R^n$ construct by linear combinations of $n$ linearly-independent (basis) vectors $t_1,...,t_n$ with *integer* coefficients

    $$
    T = \{m_1 t_1 + \cdots m_n t_n \mid
    m_1,...,m_n \in \Z\}
    $$

    <div class="remark">

    *Remark*: A lattice is isomorphic to its own translation group, which is a discrete subgroup of the full translation group $\mathbb{T}$ of $\R^n$.

    </div><br>

- **Lattice vectors**: linear combinations of $t_1,...,t_n$ with integer coefficients.

    $$
    t = m_1 t_1 + \cdots m_n t_n, \quad
    m_1,...,m_n \in \Z
    $$

- **Space group**: The group of all symmetries (translations, linear maps and their combinations) of the lattice.

    Space groups in 2D are called **wallpaper groups**.

## Point Group of A Lattice

*Definition*: Let $G$ be a space group.

- **Point group** $P$: the group of the *linear parts* of all elements in $G$, which is a subgroup of $\O(n)$.

    $$
    P = \{R \in \O(n) \mid \exist a \in \R^n, \ (a,R) \in G\}
    $$

    <div class="remark">
    
    *Remark*: 

    - $a$ is *not necessarily* a lattice vector in $T$. 
    - The origin-preserving subgroup $G_0 \le P$
    - $P$ sends lattice vectors to lattice vectors; thus, under the lattice basis vectors, elements in $P$ are represented by matrices with *integer entries*, i.e. $P \le \GL(n,\Z)$. 

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
    a,b,c,d \in \Z \ \Rightarrow \ 
    \boxed{2 \cos \theta \in \Z}
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

## Alternative Expression of The Translation Group

Although the translation group is an Abelian group, its elements in general does not commute with elements outside the subgroup. However, we have the following result:

<div class="result">

*Theorem*: Let $G$ be a space group and $T$ its translation subgroup. Define the group

$$
G_n = \{x \in G \mid \forall g \in G, \ x g^n = g^n x\}
\quad (n \in \N_+)
$$

Then $T = G_n$ whenever $n$ is a multiple of $|P|$ (or $|G/T|$).

</div>

----

*Proof*: First observe that $g^n \in T$ for all $g \in G$ if $n$ is a multiple of $|P|$. It suffices to show this for $g \in P$; recall that the order of each element must divides $|P|$, otherwise the cyclic subgroup generated by this element will violate Lagrange's theorem. Thus for $g \in P$, we have $g^n = 1 \in T$. 

- Obviously $T \subset G_n$, since $T$ is an Abelian group:

    $$
    \forall t \in T: \ g^n \in T \Rightarrow tg^n = g^n t
    $$

- Now we only need to prove $G_n \subset T$. Let $x \equiv (\tau,R) \in G_n$:
    
    $$
    x g^n = g^n x \Rightarrow g^n = x g^n x^{-1}
    $$

    Suppose that $g^n = (t,1)$. Then the group multiplication in the space group gives

    $$
    \begin{align*}
        x g^n x^{-1} 
        &= (\tau,R) (t,1) (-R^{-1}\tau, R^{-1}) \\
        &= (\tau,R) (t-R^{-1}\tau, R^{-1}) \\
        &= (Rt, 1)
        \overset{!}{=} (t, 1) = g^n
    \end{align*}
    $$

    This means that

    $$
    \forall t \in T: Rt = t
    \Rightarrow R = 1 \Rightarrow x \in T
    \quad \blacksquare
    $$

----

## Isomorphic Space Groups

The point group $P$ is *uniquely* determined (up to isomorphism) by the space group $G$ producing it. 

<div class="result">

*Theorem*: Two isomorphic space groups $G,G'$ have isomorphic point groups $P,P'$.

</div>

----

*Proof*: It suffices to show that $G, G'$ have isomorphic translation subgroups $T, T'$. This turns out to be true. 

Let $\phi$ be the isomorphism between $G, G'$. Note that the relation $x g^n = g^n x$ is mapped to $\phi(x) \phi^n(g) = \phi^n(g) \phi(x)$ for any $x,g \in G$, thus $\phi(G_n) = G'_n$. 

Then we can choose $n = |P||P'|$ and obtain $\phi(T) = T'$ (i.e. the isomorphism $\phi$ *maps translations to translations*). Thus the desired isomorphism between $T, T'$ is just the restricted map $\phi|_T$. $\blacksquare$

----

We can say more about the isomorphism $\phi$:

<div class="result">

*Theorem*: Let $\phi: G \to G'$ be an isomorphism between two space groups $G, G'$.

- The restricted isomorphism $\phi|_T: T \to T'$ between the translation subgroups is a *linear* map, represented by a matrix $U_{\phi} \in \GL(n,\Z)$.

- The induced isomorphism $\tilde{\phi}: P \to P'$ between the point groups is conjugation by $U_{\phi}$:

    $$
    R \in P \mapsto U_{\phi} R U_{\phi}^{-1} \in P'
    $$

</div>

----

*Proof*:

- On the restricted isomorphism $\phi|_T$:

    The identity element in $T$ is translation by the zero vector. Since $\phi|_T$ is an isomorphism, it must preserve this element, i.e. "preserve the origin" (recall that $T$ is isomorphic to the corresponding subset of $\R^n$). Thus it must be a linear map. 
    
    The representation matrix $U_\phi$ of $\phi|_T$ is defined by

    $$
    \phi|_T(t_j) = \sum_{i} t'_i (U_\phi)_{ij}
    $$

    where $\{t_i\}, \{t'_i\}$ are lattice basis vectors of $T, T'$ respectively. Since $\phi|_T$ map translations in $T$ to translations in $T'$, the matrix entries must be integers (i.e. $(U_\phi)_{ij} \in \Z$). 
    
    Furthermore, the matrix of the inverse mapping $\phi^{-1}|_{T'}$ (which is just $U_\phi^{-1}$) should also have integer entries. Thus $U_\phi \in \GL(n,\Z)$.

- On the induced isomorphism $\tilde{\phi}$:

    For a translation element $(t,1)$, it is mapped by $\phi$ to 

    $$
    \phi(t,1) = (U_\phi t, 1)
    $$

    Suppose $(a,A) \in G$; it is mapped by $\phi$ to

    $$
    \phi(a,A) = (b,B) \in G' \quad 
    (A \in P, B \in P')
    $$

    We want to know what $B$ is. Consider the conjugation of $(t,1)$ by $(a,A)$

    $$
    \begin{align*}
        & (a,A)(t,1)(a,A)^{-1} \\
        &= (a,A)(t,1)(-A^{-1}a, A^{-1}) \\
        &= (a,A)(t-A^{-1}a, A^{-1})
        = (At, 1)
    \end{align*}
    $$

    which is a "rotated" translation. Thus, it is sent by $\phi$ to

    $$
    \begin{align*}
        & \phi((a,A)(t,1)(a,A)^{-1}) = (U_\phi At, 1)
        \\
        &\overset{!}{=} (b,B)(U_\phi t,1)(b,B)^{-1}
        = (BU_\phi t,1)
    \end{align*}
    $$

    This implies that

    $$
    U_\phi A = B U_\phi \Rightarrow 
    B = U_\phi A U_\phi^{-1} 
    \quad \blacksquare
    $$

----
