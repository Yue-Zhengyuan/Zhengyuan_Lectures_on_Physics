# Group Action

## Symmetric Group

The group axioms are inspired by the set of all operations that *permutes* elements in a set, i.e. leave the set invariant. More mathematically, given a set $X$, the set of all *bijections* from $X$ to itself is a group, called the **symmetric group** of $X$: 

$$
\Sym(X) = \{
    g: X\to X \mid 
    g\ \text{is bijective}
\}
$$

Comparing with the group axioms, in the group $\Sym(X)$:

- *Multiplication*: *composition* of mappings
- *Identity*: the *identity map*
- *Inverse*: the *inverse map* (which exists since all $g \in \Sym(X)$ are bijective)

### Examples

- **Permutation group $S_n$**

    The underlying set contains $n$ labels (say 1 to $n$); mapping one label to another means the same as permuting the labels. Thus this group has order $n!$.

## Group Action

Elements in $G \equiv \Sym(X)$ are said to **act** on the set $X$. The set $X$ will then be called a **$G$-set**. In general, the **action** of $G$ on $X$ can be defined in *various* ways, but it should satisfy the following requirements: for all $g \in G, x \in X$

- **Left action**:

    $$
    \phi: G \times X \to X \quad
    (g,x) \mapsto g*x
    $$

    - *Compatibility*: $(gh)*x = g*(h*x)$
    - *Action of identity*: $1*x = x$

- **Right action**:

    $$
    \phi: X \times G \to X \quad
    (x,g) \mapsto x*g
    $$

    - *Compatibility*: $x*(gh) = (x*g)*h$
    - *Action of identity*: $x*1 = x$

<div class="remark">

*Remark*: The group action (to be concrete, consider left actions) induces a *homomorphism* to the symmetric group $\Sym(X)$: 

$$
\phi: G \to \Sym(X), \quad
g \mapsto \phi_g: \phi_g(x) = g * x
$$

Conversely, each homomorphism $\phi: G \to \Sym(X)$ defines a group action. 

</div><br>

### Action of A Group on Itself

When $X = G$, common definitions of the action of $G$ on itself are: 

$$
\begin{array}{ccc}
    \text{Name} & \text{Left action} & \text{Right action}
    \\[3pt] \hline \\[-6pt]
    \text{Trivial} & x\ (\forall g) & x\ (\forall g)
    \\[0.4em]
    \text{Translation} & gx & xg 
    \\[0.4em]
    \text{Adjoint} & gxg^{-1} & g^{-1}xg
\end{array}
$$

Let us verify that the adjoint (conjugate) action is a valid definition.

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

## Cayley'x Theorem

It turns out that every abstractly defined group can be realized as the group of symmetries of some set, at least itself.

<div class="result">

*Theorem*: (Cayley) Every group $G$ is *isomorphic* to a subgroup of its own group of symmetries $\Sym(G)$.

$$
G \le \Sym(G)
$$

</div><br>
