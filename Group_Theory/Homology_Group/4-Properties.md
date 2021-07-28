# General Properties of Homology Groups

## Connectedness and Homology Groups

----

*Theorem*: (**Decomposition of homology group of union of disjoint pieces**)

Let the simplicial complex $K$ be a *disjoint* union of $N$ *connected* components, i.e.

$$
K = K_1 \cup K_2 \cup \cdots \cup K_N, \quad
K_i \cap K_j = \varnothing
$$

Then

$$
H_r(K) = H_r(K_1) \oplus H_r(K_2) \oplus \cdots \oplus H_r(K_N)
$$

*Corollary*: 

- $H_0(K) \cong \mathbb{Z}^N$

- $K \ \text{is connected} \Leftrightarrow H_0(K) \cong \mathbb{Z}$

----

## Structure of Homology Groups

*Definition*:

- **Torsion subgroup of $H_r(K)$**: we decompose $H_r(K)$ to 

    $$
    H_r(K) = \mathbb{Z}^f \oplus 
    \mathbb{Z}_{k_1} \oplus \cdots \oplus \mathbb{Z}_{k_p}
    $$

    The *finite part* ($\mathbb{Z}_{k_1} \oplus \cdots \oplus \mathbb{Z}_{k_p}$) is called the **torsion subgroup of $H_r(K)$**

    *Remark*: If we use $H_r(K;\mathbb{Z}_2)$ or $H_r(K;\mathbb{R})$, the torsion subgroup will not be recognized:

    $$
    H_r(K;\mathbb{R}) = \mathbb{R}^ f
    $$

## Betti Numbers and the Euler-Poincaré Theorem

*Definition*: Let $K$ be a $n$-dimensional simplicial complex. 

- **The $r$-th Betti number $b_r(K)$**:
    
    $$
    b_r(K) \equiv \text{rank }{H_r(K)} 
    = \dim{H_r(K;\mathbb{R})}
    $$

    *Remark*: Since the homology groups are topological invariants, so are the Betti numbers

- **Euler characteristic of $K$**:

    $$
    \chi(K) \equiv \sum_{r=0}^n (-1)^r I_r
    $$

----

*Theorem*: (**Euler-Poincaré theorem: relation between $b_r$ and $\chi$**)

$$
\chi(K) = \sum_{r=0}^n (-1)^r b_r(K)
$$

*Remark*: The theorem shows that Euler characteristic is also a topological invariant.

----
