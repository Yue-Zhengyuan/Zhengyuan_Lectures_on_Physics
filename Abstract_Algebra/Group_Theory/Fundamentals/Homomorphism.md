# Group Homomorphism

*Definition*: Let $G, H$ be two groups, and $f: G \to H$ a map between them.

- **Homomorphism (同态)**: the map $f$ with the property

    $$
    \forall x, y \in G \quad 
    f(xy)  = f(x) f(y) 
    $$

    The set of all homomorphisms between $G, H$ is denoted by $\Hom(G, H)$.

- **Endomorphism (自同态)**: a homomorphism from a group to *itself*.

    The set of all endomorphisms of $G$ is denoted by $\End(G)$.

## Kernel and Image of A Group Homomorphism

<div class="result">

*Theorem*: Let $f: G \to H$ be a group homomorphism.

- $\ker{f} = \{x \mid x\in G, f(x) = 1_H\}$ is a *normal* subgroup of $G$
- $\im{f} = \{y \mid y \in f(G) \subset H\}$ is a subgroup of $H$

</div>

----

*Proof*:

----

The kernel and the image can be used to classify homomorphisms. We first give some definitions, which are group theory versions of corresponding concepts in general theory of maps.

*Definition*:

- **Monomorphism (单同态)**: an *injective* homomorphism
- **Epimorphism (满同态)**: a *surjective* homomorphism $\im f = H$
- **Isomorphism (同构)**: a *bijective* homomorphism, which preserves group structure.
    - **Isomorphic Groups**: Two groups between which exists an isomorphism (and therefore are essentially the *same* group), denoted by $G \cong H$

<div class="result">

*Theorem*: For a group homomorphism $f: G \to H$

- $f$ is a monomorphism $\Leftrightarrow$ $\ker f = \{1_G\}$
- $f$ is an epimorphism $\Leftrightarrow$ $\im f = H$
- $f$ is an isomorphism $\Leftrightarrow$ $\ker f = \{1_G\}$ *and* $\im f = H$

</div><br>

## Isomorphism Theorems

<div class="result">

*Theorem*: (Fundamental theorem of homomorphism)

Let $f: G \to H$ be a group homomorphism. Then

$$G / \ker{f} \cong \im{f}$$

</div>

----

*Proof*:

----

## Automorphism

*Definition*:

- **Automorphism (自同构)**: an isomorphism from a group to *itself* ("symmetries" of a group)
    
- **Automorphism group** $\Aut(G)$: the group consisting of all automorphisms of a group $G$.

### Conjugation and Inner Automorphism

