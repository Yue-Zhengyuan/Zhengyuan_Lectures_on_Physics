# Subgroups and Cosets

*Definition*:

- **Subgroup**: a subset $H$ of $G$ which still forms a group under the same multiplication rule of $G$.
    
- **Coset**: The set of group elements obtained by multiplying $g \in G$ on the left (or right) of a subgroup $H$ of $G$

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

<div class="result">

*Theorem*: (**Lagrange**) Let $H$ be a subgroup of (a finite group) $G$.

- Two cosets $g_1 H, g_2 H$ ($g_1, g_2 \in G$) are *either disjoint or the same*;
- $|H|$ divides $|G|$.

</div><br>

- **Index** of a subgroup $H$: the number of left/right cosets of H in G.

