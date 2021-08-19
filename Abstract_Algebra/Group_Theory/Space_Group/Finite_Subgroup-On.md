# Finite Subgroups of $\O(n)$

<div class="remark">
<center>

*In this section we restrict to 2D and 3D spaces.*

</center>
</div><br>

The symmetry groups of many bounded shapes (which must leave at least one point on this object invariant) and the point group of any space group are finite subgroups of the full linear isometry group $\O(n)$, motivating the following discussions. 

## Finite Subgroups of $\O(2)$

The full group $\O(2)$ contains an important subgroup: the **special orthogonal group**, consisting solely of rotations

$$
\SO(2) = \{R \in \O(2) \mid \det R = +1\}
$$

Let $G$ be a non-trivial finite subgroup of $\O(2)$. 

- If $G \le \SO(2)$, all of its elements are rotations. Let $R_\theta \in G$ be the element of rotation by an angle $\theta \in [0,2\pi)$. Since $G$ is finite, there must be a smallest finite order $n \in \N_+$ such that

    $$
    R_\theta^n = 1 \Rightarrow 
    n\theta = 0 \ \text{mod}\ {2\pi}
    $$

    Then we can choose from the cyclic subgroup $\{1, R_\theta, R_\theta^2,..., R_\theta^{n-1}\}$ the element which gives the smallest positive angle after modulo $2\pi$. Suppose that this element is

    $$
    R_\varphi \equiv R_\theta^m \quad 1 \le m \le n-1
    $$

    This means that there exists $k \in \N_+$ such that $m\theta = 2k\pi + \varphi$. However, this $R_\varphi$ also has order $n$, because

    $$
    n \varphi = n(m\theta - 2k\pi)
    $$

- If $G$ contains reflections (elements with determinant $-1$),

To summarize:

<div class="result">

*Theorem*: A finite subgroup of $\O(2)$ must be one of the following:

- The cyclic group $C_n$ ($n \in \N_+$)
- The dihedral group $D_n$ ($n \in \N_+$)

</div><br>

## Finite Subgroups of $\O(3)$

<div class="result">

*Theorem*: A finite subgroup of $\O(3)$ must be one of the following:

- The cyclic group $C_n$ ($n \in \N_+$)
- The dihedral group $D_n$ ($n \in \N_+$)
- The symmetry group of Platonic solids (tetrahedral $A_4$, cube/octahedral $S_4$, dodecahedral/icosahedral $A_5$)

</div><br>
