# Group Homomorphism

*Definition*: Let $G_1, G_2$ be two groups.

- **Homomorphism (同态)**: a map $f: G_1 \to G_2$ such that

    $$
    \forall x, y \in G_1 \quad 
    f(xy)  = f(x) f(y) 
    $$

    - **Endomorphism (自同态)**: a homomorphism from a group to *itself*.

- **Isomorphism (同构)**: an homomorphism from one group to another which is *also injective (one-to-one)*, and therefore preserves group structure.

    - **Isomorphic Groups**: Two groups between which exists an isomorphism (and therefore are essentially the *same* group), denoted by

        $$
        G_1 \cong G_2
        $$
    
    - **Automorphism (自同构)**: an isomorphism from a group to *itself* ("symmetries" of a group)
        
        - **Automorphism group** $\Aut(G)$: the group consisting of all automorphisms of a group $G$.

## Theorems on Group Homomorphisms

<div class="result">

*Theorem*: (**Group homomorphism lemma**)

Let $f: G_1 \to G_2$ be a group homomorphism. Then

- $\ker{f} = \{x|x\in G_1, f(x) = 0\}$ is a subgroup of $G_1$
- $\im{f} = \{y|y \in f(G_1) \subset G_2\}$ is a subgroup of $G_2$

</div>

----
*Proof*:

----

<div class="result">

*Theorem*: (**Fundamental theorem of homomorphism**)

Let $f: G_1 \to G_2$ be a group homomorphism. Then

$$G_1 / \ker{f} \cong \im{f}$$

</div>
----