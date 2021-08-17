# Group Homomorphism

*Definition*: Let $G, H$ be two groups, and $f: G \to H$ a map between them.

- **Homomorphism**: the map $f$ with the property

    $$
    \forall x, y \in G \quad 
    f(xy)  = f(x) f(y) 
    $$

    <div class="remark">

    *Remark*: Sometimes the group homomorphism is written in power notation $x^f \equiv f(x)$ due to the property $(xy)^f = x^f y^f$.

    </div><br>

    The set of all homomorphisms between $G, H$ is denoted by $\Hom(G, H)$, which is always nonempty, since it contains the **zero homomorphism**

    $$
    0: G \to H \quad g \mapsto 1_H
    $$

- **Endomorphism**: a homomorphism from a group to *itself*.

    The set of all endomorphisms of $G$ is denoted by $\End(G)$, which is also nonempty, since it contains the identity mapping.

## Kernel and Image of Group Homomorphism

<div class="result">

*Theorem*: Let $f: G \to H$ be a group homomorphism.

$$
\begin{align*}
    \ker{f} &\equiv \{x \mid x\in G, f(x) = 1_H\} \lhd G
    \\
    \im{f} &\equiv \{y \mid y \in f(G) \subset H\} \le H
\end{align*}
$$

</div>

----

*Proof*: 

- First verify that $\ker f$ is closed under the group multiplication of $G$. Let $x_1, x_2 \in \ker f$; then

    $$
    f(x_1 x_2) = f(x_1) f(x_2) = 1_H \cdot 1_H = 1_H
    \Rightarrow x_1 x_2 \in \ker f
    $$

    And obviously $1_G \in \ker f$; the inverse of any $x \in \ker f$ is $x^{-1} \in \ker f$. Thus $\ker f \le G$.

    Next we verify $\ker f \lhd G$. For any $x \in \ker f$ and $g \in G$

    $$
    \begin{align*}
        f(g^{-1} x g) &= f(g^{-1}) f(x) f(g) \\
        &= f(g^{-1}) \cdot 1_H \cdot f(g) \\
        &= f(g^{-1}) f(g) \\
        &= f(g^{-1} g) = f(1_G) = 1_H
        & \Rightarrow
        g^{-1} x g \in \ker f
    \end{align*}
    $$

- First verify that $\im f$ is closed under the group multiplication of $H$. For any $y_1, y_2 \in \im f$, we can find $x_1, x_2 \in G$ such that $y_1 = f(x_1), y_2 = f(x_2)$. Then

    $$
    y_1 y_2 = f(x_1)f(x_2) = f(x_1 x_2) 
    \Rightarrow y_1 y_2 \in \im f
    $$

    And obviously $1_H \in \im f$ (since $1_H = f(1_G)$); the inverse of any $y = f(x) \in \im f$ is $f(x^{-1})$. Thus $\im f \le H$.

----

## Special Homomorphisms

A special normal subgroup of $G$ is $\{1\}$, and a special subgroup of $H$ is $H$ itself. These lead to important special cases of group homomorphisms.

*Definition*:

- **Monomorphism**: an *injective* homomorphism, i.e.

    $$
    \forall x_1, x_2 \in G \quad x_1 \ne x_2 \Rightarrow f(x_1) \ne f(x_2)
    $$

- **Epimorphism**: a *surjective* homomorphism, i.e.

    $$
    \forall y \in H,\ \exists x \in G \quad y = f(x)
    $$

- **Isomorphism**: a *bijective* homomorphism, preserving group structure.

    $$
    $$

    - **Isomorphic Groups**: Two groups between which exists an isomorphism (and therefore are essentially the *same* group), denoted by $G \cong H$

<div class="result">

*Theorem*: For a group homomorphism $f: G \to H$

- $f$ is a monomorphism $\Leftrightarrow$ $\ker f = \{1_G\}$
- $f$ is an epimorphism $\Leftrightarrow$ $\im f = H$
- $f$ is an isomorphism $\Leftrightarrow$ $\ker f = \{1_G\}$ *and* $\im f = H$

</div>

----

*Proof*: 

- Monomorphism

    *Necessity* $\Rightarrow$: Suppose there exists $x \ne 1_G \in \ker f$. But by definition of monomorphism

    $$
    x \ne 1_G \Rightarrow f(x) \ne f(1_G) = 1_H
    $$

    *Sufficiency* $\Leftarrow$: When $\ker f = \{1_G\}$, suppose for $x_1, x_2 \in G$

    $$
    f(x_1) = f(x_2) \Rightarrow f(x_1 x_2^{-1}) = f(1_G) = 1_H
    $$

    Thus $x_1 x_2^{-1} = 1 \in \ker f$, i.e. $x_1 = x_2$. $\blacksquare$

- Epimorphism: Obvious by definition. $\blacksquare$

- Isomorphism

    *Necessity* $\Rightarrow$: Obvious by definition, since an isomorphism is a monomorphism and an epimorphism at the same time. 

    *Sufficiency* $\Leftarrow$:

----

## Isomorphism Theorems

<div class="result">

*Theorem*: (First isomorphism theorem)

Let $f: G \to I$ be a group homomorphism. Then

$$G / \ker{f} \cong \im{f}$$

</div>

----

*Proof*: Since $\im f$ is a subgroup of $I$, we may directly restrict $f$ as a mapping to $U = \im f$ (i.e. $f: G \to U$), which is then an epimorphism. 

Let $H = \ker f$. Its left cosets $xH$ ($x \in G$) are mapped by $f$ to

$$
f(xH) = f(x) f(H) = f(x)
$$

which is *independent* of the representative element: if we change $x$ to $xh$ ($h \in H$), we still obtain

$$
f(xh) = f(x)f(h) = f(x) \cdot 1_U = f(x)
$$

Thus we can define the isomorphism between $G/H$ and $U$ as

$$
\phi: G/H \to U \quad 
\phi(xH) \mapsto f(x)
$$

Let us verify that $\phi$ is indeed an isomorphism:

- $\phi$ is well-defined, independent of the choice of the representative element of $xH$. 

- $\phi$ is a homomorphism, since

    $$
    \begin{align*}
        \phi(xH) \phi(x'H) &= f(x)f(x') = f(xx')
        \\
        \phi(xH \cdot x'H) &= \phi(xx'H) = f(xx')
    \end{align*}
    $$

- $\ker \phi = \{H\} = \{1_{G/H}\}$.
    
    Obviously $\phi(H) = f(1_G) = 1$. Suppose there is another coset $xH \in \ker \phi \ (x \notin H)$. Then

    $$
    \phi(xH) = f(x) = 1 \Rightarrow x \in H
    $$

    which contradicts the hypothesis. 

- $\im \phi = U$. For any $y \in U$, since we can always find $x \in G$ such that $y = f(x)$, we can also use this $x$ so that $y = \phi(xH)$

The last two properties implies that $\phi$ is an isomorphism. $\blacksquare$

----

## Automorphism

*Definition*: Let $G$ be a group.

- **Automorphism**: an *isomorphism* from a group to *itself* ("symmetries" of a group)
    
- **Automorphism group** $\Aut(G)$: the *group* of all automorphisms of $G$ (with mapping composition as group multiplication).

### Conjugation

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

### Inner Automorphism

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

- **Inner automorphism group** $\Inn(G)$: the *group* of all inner automorphisms (obtained by using different $g \in G$) of $G$ 

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

----

### Center of A Group

*Definition*: Let $G$ be a group.

- **Center** of $G$: the set of elements that commute with every element of $G$, denoted by
    
    $$
    Z(G) = \{z \in G \mid \forall g \in G, \ zg = gz\}
    $$

<div class="result">

*Theorem*: 

- $Z(G)$ is the largest *normal subgroup* of $G$
- $G / Z(G) \cong \Inn(G)$

</div>

----

*Proof*:

----

