# Cosets

*Definition*: Let $H \le G$. Pick $g \in G$.

- **Coset**: The set of group elements obtained by 

    $$
    \begin{align*}
        \text{Left coset} &: gH = \{gh \mid h \in H\}
        \\
        \text{Right coset}&: Hg = \{hg \mid h \in H\}
    \end{align*}
    $$

    <div class="remark">

    *Remark*: The element $g$ is called the **representative element** of the coset. Obviously it is not unique, for we can pick any $h \in H$ and use $gh$ as the representative element, i.e. $gH = (gh)H$. 

    </div><br>

## The Underlying Equivalence Relation

The left coset $gH$ is in fact an equivalent class $[g]$ under the equivalence relation: for $x, y \in G$

$$
(x \sim y) \Leftrightarrow (\exists h \in H, \ x = yh)
$$

Similarly, the right coset $Hg$ is an equivalent class $[g]$ under the equivalence relation

$$
(x \sim y) \Leftrightarrow (\exists h \in H, \ x = hy)
$$

The general theory of equivalence classes implies:

<div class="result">

*Theorem*: Let $H$ be a subgroup of group $G$.

- Two cosets $g_1 H, g_2 H$ ($g_1, g_2 \in G$) are *either disjoint or the same*;
- (Lagrange) If $G$ is a finite group, the order $|H|$ divides $|G|$.

</div><br>

## Normal Subgroups and Quotient Group

*Definition*: Based on partition of $G$ by its cosets

- **Index** of a subgroup $H$: the number of left/right cosets of $H$ in $G$, denoted by $|G:H|$.
- **Quotient set** $G/H$: the set of all left/right cosets of $H$ in $G$.

It is possible to promote the quotient set to a group (the **quotient (factor) group**) under certain conditions. But first we introduce some terminologies.

### Permutable Subgroups and Normal Subgroups

*Definition*: Let $G$ be a group, and $H \le G$. 

- **Permutable subgroup**: $H$ is *permutable* if it permutes with all *subgroups* of $G$.

    $$
    HK = KH \quad \forall K \le G
    $$

- **Normal subgroup**: $H$ is *normal* (denoted by $H \lhd G$) if it is commutes with all *elements* of $G$, i.e. its left coset is the same as its right coset.

    $$
    g H = H g \quad \forall g \in G
    $$

    which is a special case of permutable subgroup.

### Quotient Group

Now we are ready to determine when a quotient set can be promoted to a group. 

<div class="result">

*Theorem*: The quotient set $G/H$ is a *group* under the multiplication rule 

$$
(g_1 H) (g_2 H) = g_1 g_2 H
$$

*if and only if* $H$ is a normal subgroup of $G$.

</div>

----

*Proof of Necessity* $\Rightarrow$: We need to check if the multiplication rule is well-defined, since notation $gH$ is ambiguous. For any $g, g' \in G$ and $h \in H$

$$
(g' h H)(g H) \equiv g' h g H \overset{!}{=} g' g H
$$

Cancelling $g'$ on both sides, we demand that 

$$
hgH = gH \Rightarrow g^{-1} h g H = H \Rightarrow
g^{-1} h g \in H
$$

Arbitrariness of $g, h$ then implies $g^{-1} H g = H$ for all $g \in G$.

*Proof of Sufficiency* $\Leftarrow$: The group axioms can then be verified straightforwardly. $\blacksquare$

----

