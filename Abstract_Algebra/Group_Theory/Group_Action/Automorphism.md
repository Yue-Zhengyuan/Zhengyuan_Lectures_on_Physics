# Automorphism

*Definition*: Let $G$ be a group.

- **Automorphism**: an *isomorphism* from a group to *itself* ("symmetries" of a group)
    
- $\Aut(G)$: the *group* of all automorphisms of $G$ (with mapping composition as group multiplication).

## Conjugation

*Definition*: Let $G$ be a group.

- **Conjugacy relation**: an *equivalence relation* defined as

    $$
    x \sim y \ \Leftrightarrow \ 
    \exists g \in G,\ y = gxg^{-1}
    $$

- **Conjugacy class**: equivalence class based on the conjugacy relation. The class represented by $x \in G$ is the set of all elements conjugate to $x$.

    $$
    [x] \equiv \{gxg^{-1} \mid g \in G\}
    $$

## Inner Automorphism

*Definition*: Let $G$ be a group.

- **Inner automorphism**: the conjugation mapping defined for a *fixed* $g \in G$

    $$
    f_g: G \to G \quad f_g(x) = gxg^{-1}
    $$

    ----

    *Verifying the homomorphism definition*: For any $x, y \in G$

    $$
    f_g(x) f_g(y) = gxg^{-1} gyg^{-1} 
    = g(xy)g^{-1} = f_g(xy)
    \quad \blacksquare
    $$

    ----

- $\Inn(G)$: the *group* of all inner automorphisms (obtained by using different $g \in G$) of $G$ 

<div class="result">

*Theorem*: $\Inn(G) \lhd \Aut(G)$

</div>

----

*Proof*: For any $f_g \in \Inn(G)$ and $\phi \in \Aut(G)$, consider the image of the composition mapping

$$
\begin{align*}
    &(\phi^{-1} f_g \phi)(x) 
    \\
    &= (\phi^{-1} f_g)(\phi(x))
    = \phi^{-1} (g \phi(x) g^{-1})
    \\
    &= \phi^{-1}(g) x \phi^{-1}(g^{-1})
    = f_{\phi^{-1}(g)}(x)
\end{align*}
$$

Therefore

$$
\phi^{-1} f_g \phi = f_{\phi^{-1}(g)} \in \Inn(G)
\quad \blacksquare
$$

<div class="remark">

*Remark*: Based on this theorem, we define the **outer automorphism group** as

$$
\Out(G) = \Aut(G) / \Inn(G)
$$

Its elements are not conjugation operations, and are called **outer automorphism**.

</div><br>

----

## Center of A Group

There exists a natural homomorphism (in fact, an epimorphism) between $G$ and $\Inn(G)$:

$$
\phi: G \to \Inn(G) \quad g \mapsto f_g,
\ f_g(x) = gxg^{-1}
$$

The kernel of $\phi$ is of special importance: for $z \in \ker \phi$, the inner automorphism $f_z$ is the identity mapping.

$$
f_z(x) = zxz^{-1} = x \Rightarrow
zx = xz \quad (\forall x \in G)
$$

i.e. $z$ commutes with all $x \in G$. This motivates the following definition.

*Definition*: Let $G$ be a group.

- **Center** of $G$: the set of elements that commute with every element of $G$, denoted by
    
    $$
    Z(G) = \{z \in G \mid \forall g \in G, \ zg = gz\}
    $$

Since $Z(G) = \ker \phi$, we obtain from the first isomorphism theorem:

<div class="result">

*Theorem*: $G / Z(G) \cong \Inn(G)$

</div>
