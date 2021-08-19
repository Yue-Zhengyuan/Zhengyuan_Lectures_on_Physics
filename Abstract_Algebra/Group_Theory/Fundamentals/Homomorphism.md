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

- $\Hom(G, H)$: The set of all homomorphisms between $G, H$.
    
    This set is always nonempty, since it contains the **zero homomorphism**, sending all elements in $G$ to the identity of $H$:

    $$
    0: G \to H \quad g \mapsto 1_H
    $$

- **Endomorphism**: a homomorphism from a group to *itself*.

- $\End(G)$: The set of all endomorphisms of $G$
    
    This set is also always nonempty, since it contains the identity mapping.

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

*First Isomorphism Theorem*:

Let $f: G \to H$ be a group homomorphism. Then 

$$
G / \ker{f} \cong \im{f}
$$

</div>

----

*Proof*: Since $\im f \le H$, we may directly redefine $H = \im f$, making $f$ an epimorphism. 

Let $K = \ker f$. Its left cosets $xK$ ($x \in G$) are mapped by $f$ to

$$
f(xK) = f(x) f(K) = f(x)
$$

which is *independent* of the representative element: if we change $x$ to $xh$ ($h \in K$), we still obtain

$$
f(xh) = f(x)f(h) = f(x) \cdot 1_H = f(x)
$$

Thus we can define the isomorphism between $G/K$ and $H$ as

$$
\boxed{
    \phi: G/K \to H, \quad xK \mapsto f(x)
}
$$

Let us verify that $\phi$ is indeed an isomorphism:

- $\phi$ is well-defined, independent of the choice of the representative element of $xK$. 

- $\phi$ is a homomorphism, since

    $$
    \begin{align*}
        \phi(xK) \phi(x'K) &= f(x)f(x') = f(xx')
        \\
        \phi(xK \cdot x'K) &= \phi(xx'K) = f(xx')
    \end{align*}
    $$

- $\ker \phi = \{K\} = \{1_{G/K}\}$.
    
    Obviously $\phi(K) = f(1_G) = 1$. Suppose there is another coset $xK \in \ker \phi \ (x \notin K)$. Then

    $$
    \phi(xK) = f(x) = 1 \Rightarrow x \in K
    $$

    which contradicts the hypothesis. 

- $\im \phi = H$. For any $y \in H$, since we can always find $x \in G$ such that $y = f(x)$, we can also use this $x$ so that $y = \phi(xK)$

The last two properties implies that $\phi$ is an isomorphism. $\blacksquare$

----

<div class="result">

*Second Isomorphism Theorem*:

Let $H$ be a subgroup of $G$, and $N$ a *normal* subgroup of $G$. Then

- $NH \le G$
- $N \cap H \lhd H$
- $NH/N \cong H/(N \cap H)$

</div>

----

*Proof*: 

----

<div class="result">

*Third Isomorphism Theorem*:

Let $M,N$ be *normal* subgroups of $G$, and $N \le M$. Then

- $M/N \lhd G/N$
- $(G/N)/(M/N) \cong G/M$

</div>

----

*Proof*: 

----