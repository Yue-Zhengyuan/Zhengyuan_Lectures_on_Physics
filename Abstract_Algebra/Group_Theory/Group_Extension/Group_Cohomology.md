# Group Cohomology

## Group Extension with Abelian Kernel

Consider the special case of extension of an *Abelian* group $A$

$$
1 \to A \xrightarrow{\mu} G 
\xrightarrow{\pi} B \to 1
$$

## *G*-Modules

*Definition*: Let $G$ be a group.

- **Left $G$-module**: an *Abelian* group $M$ (written additively) together with a (left) action of $G$ on $M$ which is *compatible* with the Abelian structure of $M$

    $$
    \forall g\in G,\ \forall a,b \in M \quad 
    g(a+b) = g(a) + g(b)
    $$

- **Right $G$-module**: defined similarly as the left $G$-module, but with a compatible right action of $G$ on $M$:

    $$
    \forall g\in G,\ \forall a,b \in M \quad 
    (a+b)g = (a)g + (b)g
    $$

## Cochain

*Definition*: Let $G$ be a group, $M$ a $G$-module (in additive notation), and $n$ a non-negative integer. 

- **$n$-Cochain**: any function of $n$ elements of $G$, whose values are in $M$

    $$
    \omega_n(g_1,...,g_n): G^n \to M
    $$

    $G^0$ is defined as $\{1_G\}$.

- $C^n(G,M)$: the *Abelian group* of all $n$-cochains; the group multiplication is given by


    ----

    *Verifying group structure*:

    ----

## Cocycle and Coboundary

*Definition*:

- **Coboundary homomorphism**: a group homomorphism $d^{n+1}: C^n(G,M) \to C^{n+1}(G,M)$ calculated as

    $$
    \begin{align*}
        & d^{n+1}\omega_{n+1}(g_1,...,g_{n+1})
        \\
        &= g_1 \omega_n (g_2,...,g_{n+1})
        + (-1)^{n+1} \omega_n(g_1,...,g_n)
        \\ &\quad 
        + \sum_{j=1}^n (-1)^j 
        \omega_n(g_1,...,g_{j-1},g_j g_{j+1},...,g_{n+1})
    \end{align*}
    $$

- **$n$-Cocycle group**: 

    $$
    Z^n(G,M) \equiv \ker d^{n+1}
    $$

    Elements in this group are called **$n$-cocycles**.

- **$n$-Coboundary group**: 

    $$
    B^n(G,M) \equiv \begin{cases}
        \{0\} & n = 0 \\
        \im d^n & n \ge 1
    \end{cases}
    $$

    Elements in this group are called **$n$-cocycles**.

<div class="result">

*Theorem*: 

- $d^{n+1} \circ d^n = 0$
- *Corollary*: $B^n(G,M) \lhd Z^n(G,M)$

</div><br>

The theorem allows the following definition:

- **$n$-Cohomology group**:

    $$
    H^n(G,M) \equiv Z^n(G,M) / B^n(G,M)
    $$
