# Group Axioms

*Definition*:

- **Group**: a set $G$ endowed with a binary relation (**group multiplication**) 

    $$
    \circ: G \times G \to G \quad
    (a, b) \mapsto a \circ b \equiv ab \in G
    $$
    
    that has the following properties: for all $a,b,c \in G$

    1. *Associativity*: $a(bc) = (ab)c$
    2. *Existence of (left) identity*: $\exists\ 1 \in G, \ 1a = a$
    3. *Existence of (left) inverse*: $\exists\ a^{-1} \in G, \ a^{-1}a = 1$

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


