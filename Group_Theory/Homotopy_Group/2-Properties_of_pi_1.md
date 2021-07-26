# General Properties of Fundamental Groups

## Arcwise connectedness

----

*Theorem*: Let $x_0, x_1$ be two points in an *arcwise connected* topological space. Then

$$
\pi_1(X, x_0) \cong \pi_1(X, x_1)
$$

<center>
<img src="Fig_4-6.png" alt="change loop" width="300px">
</center>

*Proof*: Intuitively, this is true because we can always change a loop at $x_0$ to a loop at $x_1$ in an arcwise connected topological space using the trick shown in the figure above. $\blacksquare$

*Remark*: If $X$ is arcwise connected, the fundamental group is simply denoted by $\pi_1(X)$ without need to specify the base point $x_0$ of the loops. 

----

## Homotopic Invariance

*Definition*:

- **Homotopic maps**: two maps that can be *"continuously deformed"* to each other. 
    
    Mathematically, two maps $f, g: X \to Y$ are **homotopic** if we can find a *continuous* map $F: X \times I \to Y$ such that

    $$
        F(x, 0) = f(x), \quad
        F(x, 1) = g(x)
    $$

    Since this is an equivalence relation, it is denoted by $f \sim g$
    
    - **Homotopy**: the map $F$

- **Homotopy equivalent topological spaces**: two topological spaces $X,Y$ are **homotopy equivalent** (or **of the same homotopy type**) if we can find *continuous* maps
    
    $$f: X \to Y, \quad g: Y \to X$$

    such that

    $$
    (f \circ g \sim \text{id}_Y) \land
    (g \circ f \sim \text{id}_X) 
    $$

    denoted by $X \simeq Y$.

    - **Homotopic equivalence**: the maps $f, g$; they are called the **homotopy inverse** of each other.

    *Remark*: Recall the definition of *homeomorphism*, which requires

    $$
    (f \circ g = \text{id}_Y) \land
    (g \circ f = \text{id}_X) 
    $$

    Thus *homeomorphic spaces must be homotopy equivalent*, but the converse it not true. 

----

*Proposition*: **Homotopy equivalence (of topological spaces) is an equivalence relation**. 

----

*Theorem*: (**Fundamental group is a topological invariant**)

Let $X, Y$ be topological spaces of the same homotopy type, with $f: X \to Y$ being the homotopic equivalence. Then

$$
\pi_1(X, x_0) \cong \pi_1(Y, f(x_0))
$$

----

## Retraction

*Definition*:

- **Retract (收缩)**: a *subspace* $R$ of the whole topological space $X$, which can be obtained by a *continuous* map $f: X \to R$ such that $f|_R = \text{id}_R$ (i.e. the points on $R$ are kept unchanged).

    - **Retraction**: the continuous map $f$

- **Deformation retract (形变收缩)**: a *subspace* $R$ of the whole topological space $X$, which can be obtained by *deforming* $X$ while keeping the points in $R$ *unchanged*.
    
    Mathematically, there exist a *continuous* map $H: X \times I \to X$ such that

    $$
    \begin{align*}
        &\forall x \in X &\quad &H(x,0) = x, \quad H(x,1) \in R \\
        &\forall x \in R, t \in I &\quad &H(x,t) = x
    \end{align*}
    $$

    *Remark*: 
    - We note that $H(x,0) = \text{id}_X$, and $f(x) \equiv H(x,1)$ plays the role of retraction. Thus $H$ is a *homotopy* between $\text{id}_X$ and $f$. 
    - A retract is *not necessarily* a deformation retract. 

- **Contractible topological space**: a topological space whose deformation retract can be a *single point* in it.

    Mathematically, we can find a homotopy $H: X \times I \to X$ such that ($a \in X$ is a point)

    $$
    \begin{align*}
        &\forall \, x \in X &\quad &H(x,0) = x, \quad H(x,1) = a \equiv c_a(x)\\
        &\forall \, t \in I &\quad &H(a,t) = a
    \end{align*}
    $$
    
    - **Contraction**: the homotopy $H$

----

*Theorem*: **(Fundamental group of a contractible space is trivial)**

Let $X$ be a contractible topological space, then

$$
\pi_1(X, x_0) \cong \{e\}
$$

*Proof*: A contractible space has the same fundamental group as a point $\{p\}$, and a point has a trivial fundamental group. $\blacksquare$

----
