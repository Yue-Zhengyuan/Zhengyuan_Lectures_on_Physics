# Symmetry Group

*Definition*: Let $X$ be a metric space, and $W$ a subset of $X$. 

- **Symmetry** of $W$: isometries of $X$ that leave the set $W$ invariant, i.e.

    $$
    u(W) = \{u(x) \mid x \in W\} = W
    $$

- **Symmetry group** of $W$: the group of all symmetries of $W$
    
    $$
    \Sym(W) = \{
        u \in \Isom(X) \mid
        u(W) = W
    \}
    $$

<div class="remark">

*Remark*: In the following, we choose $X = \R^n$.

</div><br>

In considering the wallpaper group (2D space group), we do not only want $\R^2$ to be invariant under the action of the group elemets, but also some of its subsets (e.g. a set of discrete points on a lattice ).

For a subset $W$ of $\R^2$, its **symmetry group** is the set of all isometries of $\R^2$ that leave $W$ invariant, which is also a subgroup of $\Isom(\R^2)$:



Its **point group** is the collection of all isometries that keeps one point of $W$ invariant (this point will be placed at the origin), which is a subgroup of $O(2)$.

## Finite Subgroups of $O(2)$

For many subsets of $\R^2$ (except, for example, a circle centered at the origin), the point group is a *finite* subgroup of $\R^2$. It turns out that the classification of these groups is straightforward.

<div class="result">

*Theorem*: Any *finite* subgroup of $O(2)$ is *isomorphic* to either $C_n$ or $D_n$ for some $n \in \mathbb{N}_+$.

</div><br>

## Bounded Objects

A subset $W$ of $\R^2$ is said to be **bounded** if it can be entirely contained in (i.e. is a subset of) a closed disk of finite radius centered at the origin:

$$
W \in \{x \in \R^2 \mid |x| \le r < \infty\}
$$

Casually speaking, $W$ is just some finite shape in the plane. 

<div class="result">

*Theorem*: (Symmetry group of a finite planar shape)

Let $W$ be a bounded subset of $\R^2$. Its symmetry group $\Sym(W)$ is a subgroup of $O(2)$, and contains no non-trivial translations (i.e. translation by a nonzero vector).

</div><br>
