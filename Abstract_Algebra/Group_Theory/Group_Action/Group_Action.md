# Group Action

*Definition*: Let $X$ be a set; $G$ be a group.

- **Left Action** of $G$ on $X$: a map

    $$
    \phi: G \times X \to X \quad
    \phi(g,x) = g * x
    $$

    satisfying the following intuitive requirements:

    $$
    \begin{array}{r|c}
        \begin{aligned}
            \text{Compatibility with} \\
            \text{group multiplication} 
        \end{aligned} & 
        (gh) * x = g * (h * x)
        \\[6pt] \hline \\[-6pt]
        \text{Identity action} &
        1 * x = x
    \end{array}
    $$

    Usually we simply write $g * x$ as $g(x)$. 

- **Right action** of $G$ on $X$: a map

    $$
    \phi: X \times G \to X \quad
    \phi(x,g) = x * g
    $$

    satisfying the following intuitive requirements:

    $$
    \begin{array}{r|c}
        \begin{aligned}
            \text{Compatibility with} \\
            \text{group multiplication} 
        \end{aligned} & 
        x * (gh) = (x * g) * h
        \\[6pt] \hline \\[-6pt]
        \text{Identity action} &
        x * 1 = x
    \end{array}
    $$

### Action of A Group on Itself

Common definitions of the action of $G$ on itself ($X = G$) are: 

$$
\begin{array}{c|cc}
    \text{Name} & \text{Left action} & \text{Right action}
    \\[3pt] \hline \\[-6pt]
    \text{Trivial} & x\ (\forall g) & x\ (\forall g)
    \\[0.4em]
    \text{Translation} & gx & xg 
    \\[0.4em]
    \text{Conjugation} & gxg^{-1} & g^{-1}xg
\end{array}
$$

Let us verify that the conjugation is a valid group action.

----
*Proof*: 

- For the left adjoint: obviously $1 x 1^{-1} = x$. We only need to check

    $$
    \begin{align*}
        gh * x &= gh x (gh)^{-1}
        = g (h x h^{-1}) g^{-1}
        \\
        &= g (h * x) g^{-1} = g * (h * x)
    \end{align*}
    $$

- For the right adjoint: obviously $1^{-1} x 1 = x$. We only need to check
    $$
    \begin{align*}
        gh * x &= (gh)^{-1} x gh
        = h^{-1} (g^{-1} x g) h
        \\
        &= h^{-1} (x * g) h = (x*g) * h 
        \quad \blacksquare
    \end{align*}
    $$
----

## Permutation Representation of Group Action

The action of group $G$ on set $X$ is closely related to the permutation groups of $X$.

*Definition*:

- **Permutation representations** of $G$: group *homomorphisms*

    $$
    \gamma: G \to \Sym(X), \quad g \mapsto \gamma_g
    $$

<div class="result">

*Theorem*: There is a bijection between left/right actions of $G$ on $X$ and permutation representations $\gamma:G \to \Sym(X)$.

$$
\begin{align*}
    \text{Left action} \ g*x 
    \ &\Leftrightarrow \ 
    \text{Permutation} \ \gamma_g(x) = g * x
    \\
    \text{Right action} \ x*g
    \ &\Leftrightarrow \ 
    \text{Permutation} \ \gamma_g(x) = x * g^{-1}
\end{align*}
$$

</div>

----

*Proof*: We verify that $\gamma$ is indeed a homomorphism. For $g,h \in G$

$$
\begin{align*}
    \text{Left:} &&
    \gamma_{g} \gamma_{h}(x) 
    &= g * (h * x)
    \\
    &&&= (gh) * x
    = \gamma_{gh}(x)
    \\
    \text{Right:} &&
    \gamma_{g} \gamma_{h}(x) 
    &= (x * h^{-1}) * g^{-1}
    \\
    &&&= x * (h^{-1} g^{-1})
    \\
    &&&= x * (gh)^{-1}
    = \gamma_{gh}(x)
    & \blacksquare
\end{align*}
$$

----

The terminologies for special permutation groups can be applied to the group action or permutation representations as well.

## Cayley's Theorem

Every abstractly defined group can be realized as the group of symmetries of some set, at least itself.

<div class="result">

*Theorem*: (Cayley) Every group $G$ is *isomorphic* to a subgroup of $\Sym(G)$, i.e. a permutation group of $G$ itself.

</div><br>
