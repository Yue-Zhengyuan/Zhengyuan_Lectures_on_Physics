# Lie Groups and Lie Algebra

## Lie Groups

*Definition*:

- **Lie group $G$**: a *differential manifold* endowed with a **group structure** such that the operation of *multiplication* and *inverse* are *differentiable* (with respect to some parameter determining the elements in $G$).
    
    - **Dimension of $G$**: the dimension of $G$ as a manifold

----

*Theorem*: (**Subgroups of Lie groups**)

Every closed subgroup $H$ of a Lie group $G$ is also a Lie group.

----

## Lie Algebra

*Definition*:

- **Left/right-translation of $g \in G$ by $a \in G$**:
    
    $$
    L_a g \equiv a g, \quad R_a g \equiv g a
    $$

    *Remark*: 
    
    - By definition, $L_a, R_a$ are diffeomorphisms from $G$ to itself.
    - In the following we shall mainly focus on $L_a$.

- **Left-invariant vector field $X$**: a vector field $X$ defined on the Lie group $G$ satisfying
    
    $$
    L_{a*} X|_g = X|_{ag}
    $$

    where $L_{a*}: T_g G \to T_{ag} G$ is the pushforward induced by $L_a$.

    In component form, we have (from the general definition of pushforward)

    $$
    (L_{a*} X)^\nu
    = X^\mu(g) \frac{\partial x^\nu(ag)}{\partial x^\mu(g)}
    = X(ag)^\nu
    $$

    Here, instead of $y$, we use $x(ag)$ to denote the coordinate at $ag$.

    *Remark*:

    - A vector $V \in T_e G$ can uniquely define a left-invariant vector field $X_V$ throughout $G$:

        $$
        X_V |_g = L_{g*} V, \quad g \in G
        $$

        Conversely, a left-invariant vector field $X$ can uniquely determine

        $$
        V = X|_e \in T_e G
        $$

    - The **set of all left-invariant vector fields** defined on $G$ is denoted by $\frak{g}$. Since each $X_V \in \frak{g}$ is determined by $V \in T_e G$, we have 
        
        $$ \dim{\frak{g}} = \dim{T_e G} = \dim{G} $$
    
- **Lie algebra $\frak{g}$ of Lie group $G$**: the set $\frak{g}$ defined on $G$ together with the *Lie bracket*: $[\ , \ ]: \frak{g} \times \frak{g} \to \frak{g}$.

    ----

    *Proof of closure of $\frak{g}$ under Lie bracket*:

    For a general pushforward $f: M \to N$, we have shown that

    $$
    f_* [X,Y] = [f_* X, f_* Y]
    $$

    Then

    $$
    \begin{align*}
        L_{a*} [X, Y]|_g &= [L_{a*} X|g, L_{a*} Y|g] \\
        &= [X|_{ag}, Y|_{ag}] = [X, Y]|_{ag}
    \end{align*}
    $$

    Thus $[X, Y] \in \frak{g}$. $\blacksquare$

    ----
