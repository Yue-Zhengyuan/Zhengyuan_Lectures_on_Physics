# Group Axioms

A **group** is a set $G$ endowed with a binary relation (**group multiplication**) that has the following properties: for all $a,b,c \in G$

- **Associativity**: $a(bc) = (ab)c$
- **Existence of (left) identity**: $\exist\ 1 \in G \Rightarrow 1a = a$
- **Existence of (left) inverse**: $\exist\ a^{-1} \in G \Rightarrow a^{-1}a = 1$

<div class="remark">

*Remark*: The left identity is the same as the right identity; the left inverse is also the same as the right inverse, i.e.

$$
\forall g \in G, \quad g1 = g, \quad gg^{-1} = 1
$$

</div>

----

*Proof*: For any $g \in G$

$$
g g^{-1} = (g^{-1})^{-1} g^{-1} g g^{-1}
= (g^{-1})^{-1} g^{-1} = 1
$$

Thus left inverse = right inverse. Then

$$
g 1 = g g^{-1} g = 1g = g
$$

Thus left identity = right identity. $\blacksquare$

----


