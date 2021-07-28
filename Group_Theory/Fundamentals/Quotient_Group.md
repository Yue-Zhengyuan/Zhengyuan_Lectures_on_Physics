# Quotient Group

## Quotient Set and Quotient Group

*Definition*: From Lagrange's theorem, if we find a subgroup $H$ of a (finite) group $G$, we can divide $G$ into cosets of $H$. This motivates us to define:

- **Quotient set** $G/H$: the set of all (left) cosets of $H$ in $G$.

We next try to promote the quotient set to a group with a non-trivial and reasonable multiplication, defined by

$$
(g_1 H) (g_2 H) \overset{?}{=} g_1 g_2 H
$$

But we know that the notation $gH$ is ambiguous: we can pick any $h \in H$, and $gH = (gh)H$. We must check if the above multiplication is well-defined, i.e. if we can really bring $g_2$ to the left of the first $H$. 

Suppose we change $g_1 \to g_1 h$ ($h$ is arbitrarily chosen from $H$). Then

$$
(g_1 h H)(g_2 H) \equiv g_1 h g_2 H \overset{!}{=} g_1 g_2 H
$$

We demand that we should always be able to find an $h' \in H$ such that

$$
g_1 h g_2 = g_1 g_2 h'
$$

In other words, we want

$$
\forall g_1, g_2 \in G, \forall h \in H, 
\exist h' \in H \Rightarrow h g_2 = g_2 h'
$$

which can be briefly written as $\forall g \in G \Rightarrow Hg = gH$. This leads to the following definition.

*Definition*: 

- **Normal (invariant) subgroup**: a subgroup $H \in G$ which is invariant under *conjugation* by any elements in $G$:

    $$
    (H \triangleleft G) := 
    \forall \, h \in H, g \in G : g^{-1} h g \in H
    $$

    Or briefly $g H g^{-1} = H$. 

- **Action of a group $G$ on its subgroup $H$**:

## Equivalence Relations

*Definition*:

- **Equivalence relation**: Two elements $g, g' \in G$ are **equivalent** if 
    
    $$
    \exist h \in H: g' = gh 
    \quad (\text{i.e.} \quad g^{-1} g' \in H)
    $$
    
    Since $H$ is also a group, this is also equivalent to saying $g' g^{-1} \in H$. In Abelian notation

    $$
    g' - g \in H
    $$

- **Equivalence class** $[g]$: the set of all elements in $G$ that are equivalent to $g$
    
    $$
    [g] = \{gh \mid h \in H\}
    $$

    which is just the *left coset* $gH$. 
    
- **The quotient group** $G/H$: The set of all equivalence classes (left cosets of $H$) (defined only when $H$ is a *normal* subgroup of $G$)

    $$
    G/H = \{ [g] \mid g \in G\}
    $$

    The multiplication is defined as

    $$
    [g] [g'] = [g g']
    $$

    *Verification of unambiguity*: Since $g^{-1} H g = H$, we obtain

    $$
    [g][g'] = (g H) (g' H)
    = g g' (g'^{-1} H g') H 
    = g g' H = [g g']
    $$

- **Center** of a group $G$: the set of elements that commute with every element of $G$, denoted by
    
    $$
    Z(G) = \{z \in G \mid \forall g \in G, \ zg = gz\}
    $$

    - **Centerless group**: a group with $Z(G) = 1$ (trivial, containing only the identity element of $G$)

<div class="result">

*Theorem*: (On the center of a group)

- $Z(G)$ is a normal subgroup of $G$
- A group $G$ is abelian *if and only if* $Z(G) = G$

</div><br>

## Example
