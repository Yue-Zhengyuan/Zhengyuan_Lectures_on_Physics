# *G*-Modules

## Group Ring

*Definition*: Let $G$ be a group, and $R$ a ring.

- **Group ring** $RG$: the *ring* of all *formal* linear combinations of elements in $G$ with coefficients in $R$

    $$
    RG \equiv \bigg\{
        \alpha = \sum_{g \in G} \alpha_g g \ \bigg|\ 
        \alpha_g \in R,\ g \in G
    \bigg\}
    $$

    If $G$ is infinite, we require that only a finite number of coefficients $\alpha_g$ to is nonzero. 

<div class="remark">

*Remark*: The group ring can also be regarded as a collection of all mappings of coefficients $\alpha: G \to R$ with values $g \mapsto \alpha_g$

</div><br>
    
- **Addition and multiplication in $RG$**: For any two elements in $RG$

    $$
    \alpha = \sum_{g \in G} \alpha_g g, \quad
    \beta = \sum_{g \in G} \beta_g g
    $$

    define addition and multiplication on $RG$ as

    $$
    \begin{align*}
        \alpha + \beta
        &= \sum_{g\in G} (\alpha_g + \beta_g) g
        \\
        \alpha \beta
        &= \sum_{h,k \in G} (\alpha_h \beta_k) h k
        = \sum_{g\in G} \bigg(
            \sum_{h \in G} \alpha_h \beta_{h^{-1}g}
        \bigg) g
    \end{align*}
    $$

    The ring axioms can be verified easily. 

### Addition Identity (Zero)

Let $0_R$ be the zero of $R$. The zero of $RG$ is evidently

$$
0_{RG} = \sum_{g \in G} 0_R g
$$

### Multiplication Identity (One)

When the ring $R$ has the one $1_R$, we can define the one for the group ring $RG$. Let $\gamma = 1_{RG}$, then

- Left identity requirement

    $$
    \begin{align*}
        \gamma \alpha &= \sum_{g\in G} \bigg(
            \sum_{h \in G} \gamma_h \alpha_{h^{-1}g}
        \bigg) g \overset{!}{=} 
        \sum_{g\in G} \alpha_g g
        \\ &\Downarrow \\
        \alpha_g &= \sum_{h \in G} \gamma_h \alpha_{h^{-1}g}
        \quad \forall g \in G
    \end{align*}
    $$

- Right identity requirement

    $$
    \begin{align*}
        \alpha \gamma &= \sum_{g\in G} \bigg(
            \sum_{h \in G} \alpha_h \gamma_{h^{-1}g}
        \bigg) g \overset{!}{=} 
        \sum_{g\in G} \alpha_g g
        \\ &\Downarrow \\
        \alpha_g &= \sum_{h \in G} \alpha_h \gamma_{h^{-1}g}
        \quad \forall g \in G
    \end{align*}
    $$

Both are satisfied by choosing

$$
\gamma_g = \begin{cases}
    1_R & g = 1_G \\
    0_R & \text{otherwise}
\end{cases} \Rightarrow
\boxed{1_{RG} = 1_R 1_G}
$$

## *G*-Module

A common choice of $R$ is the ring of integers $\Z$, which has $1$ (in the usual sense) as its multiplication identity. 

*Definition*: Let $G$ be a group.

- **Left $G$-module**: the left $\Z G$-module. 
- **Right $G$-module**: the right $\Z G$-module. 

### Scalar Multiplication of the $G$-Module

As for generic modules over rings, we can define a scalar multiplication $\_ \cdot \_: \Z G \times M \to M$ on the $G$-module. 

First consider the left $G$-module. Let the underlying Abelian group be $M$ (written additively). For $\alpha\in \Z G$ and $v \in M$, the scalar multiplication is defined as

$$
\begin{align*}
    \alpha \cdot v &= \sum_{g \in G} \alpha_g g(v)
    &\ &(\alpha_g \in \Z)
    \\
    &= \prod_{g \in G} [g(v)]^{\alpha_g} 
    &\ & (\text{In multiplicative notation})
\end{align*}
$$

where $g(v) \in M$ is the *left action* of $g \in G$ on $v$. 

<div class="result">

*Theorem*: To make the scalar multiplication well-defined, *the group action cannot be arbitrarily chosen*: it should be **compatible** with the Abelian structure of $M$, i.e.

$$
\forall g\in G,\ \forall u,v \in M : \quad 
g(u+v) = g(u) + g(v)
$$

</div>

----

*Verifying axioms of scalar multiplication*: From the compatibility with the Abelian structure of $M$, we immediately obtain a useful result ("linearity" of the action of $G$ on $M$)

$$
g\bigg(
    \sum_{v\in M} a_v v
\bigg) = \sum_{v \in M} a_v g(v) \quad
(a_v \in \Z)
$$

Then, for any $\alpha,\beta \in \Z G$ and $u,v \in M$, the following 2 axioms needs the compatibility with $M$ (the corresponding step is marked with $\overset{!}{=}$):

- Compatibility with ring multiplication

    $$
    \begin{align*}
        \alpha \cdot (\beta \cdot v) 
        &= \sum_{g\in G} \alpha_g g \bigg(
            \sum_{h \in G} \beta_h h (v)
        \bigg)
        \\
        &\overset{!}{=} \sum_{g\in G} \alpha_g 
        \sum_{h \in G} \beta_h g(h(v))
        \\
        &= \sum_{g,h \in G}(\alpha_g \beta_h) gh(v)
        = (\alpha \beta) \cdot v
    \end{align*}
    $$

- Distributivity over vectors

    $$
    \begin{align*}
        \alpha \cdot (u+v) 
        &= \sum_{g\in G} \alpha_g g(u+v)
        \overset{!}{=} \sum_{g\in G} \alpha_g [g(u) + g(v)]
        \\
        &= \sum_{g\in G} \alpha_g g(u)
        + \sum_{g\in G} \alpha_g g(v)
        = \alpha \cdot u + \alpha \cdot v
    \end{align*}
    $$

The rest 2 axioms can be verified without the requirement on the group action of $G$.

- Identity of $\Z G$

    $$
    1_{\Z G} \cdot v = 1_{\Z} 1_G(v) = 1_{\Z} v = v
    $$
    
    In the second step, we used the fact that the identity of any group must act trivially. 

- Distributivity over scalars

    $$
    \begin{align*}
        (\alpha + \beta) \cdot v
        &= \sum_{g \in G} (\alpha_g + \beta_g) g(v)
        \\
        &= \sum_{g\in G} \alpha_g g(v)
        + \sum_{g\in G} \beta_g g(v)
        = \alpha \cdot v + \beta \cdot v
        \quad \blacksquare
    \end{align*}
    $$

----

<div class="remark">

*Remark*: 

- For the right $G$-module, we have a similar compatibility requirement on the right action of $G$ on $M$.

$$
\forall g\in G,\ \forall u,v \in M : \quad 
(u+v)g = (u)g + (v)g
$$

- A (left or right) $G$-module is called **trivial** if the group action is trivial, i.e. (e.g. for left $G$-module)

    $$
    \forall g\in G,\ \forall v \in M : \quad 
    g(v) = v
    $$

</div><br>
