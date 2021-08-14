# General Properties of Higher Homotopy Groups

## Abelian Nature

----

*Theorem*: **Higher homotopy groups are always Abelian**.

----

## Properties Generalized from Fundamental Group $\pi_1$

----

*Theorem*: (**Homotopy groups for arcwise connected spaces**)

If a topological space $X$ is arcwise connected, then

$$ 
\forall x_0, x_1 \in X \quad \pi_n(X, x_0) \cong \pi_n(X, x_1)
$$

----

*Theorem*: (**Homotopy groups are topological invariants**)

Let $X, Y$ be topological spaces of the same homotopy type, with $f: X \to Y$ being the homotopic equivalence. Then

$$
\pi_n(X, x_0) \cong \pi_n(Y, f(x_0))
$$

----

*Theorem*: (**Homotopy groups of a contractible space are trivial**)

Let $X$ be a contractible topological space, then

$$
\pi_n(X, x_0) \cong \{e\}
$$

----

*Theorem*: (**Homotopy groups of product of topological spaces**)

Let $X, Y$ be two *arcwise connected* topological spaces, and $x_0 \in X, y_0 \in Y$ be two base points. Then

$$
\pi_n(X \times Y, (x_0,y_0)) \cong
\pi_n(X, x_0) \oplus \pi_n(Y, y_0)
$$

----

## (Universal) Covering Spaces

*Definition*:

- **Covering space of topological space $X$**: another topological space $\tilde{X}$ which can "cover" $X$ via some continuous *surjective* map $p: \tilde{X} \to X$.
    
    Mathematically, "cover" means that for each $x \in X$, we can find a *connected open neighborhood* $U \subset X$, such that $p^{-1}(U)$ is a *disjoint union* of open sets in $\tilde{X}$, each of which is mapped *homeomorphically* to $U$ by $p$ (i.e. $p$ restricted to one of these open sets is a homeomorphism)

    *Remark*: By $p^{-1}(U)$ we just mean the *pre-image* of $U$ under $p$; since $p$ is only guaranteed to be surjective, it may not have a well-defined inverse on its *full* domain $\tilde{X}$.

    - **Universal covering space of $X$**: a *simply connected* covering space of $X$

*Example*: 

- $\mathbb{R}$ is the universal covering space of $S^1$ with the map $p: x \to e^{2\pi i x}$. 

----

*Theorem*: 

Let $\tilde{X}$ be the universal covering space of a *connected* topological space $X$ under the map $p$. If $x_0 \in X, \tilde{x}_0 \in \tilde{X}$ are base points such that $p(\tilde{x}_0) = x_0$, then the *induced* homomorphism

$$
p_*: \pi_n(\tilde{X}, \tilde{x_0})
\to \pi_n(X, x_0)
$$

is an *isomorphism* when $n \ge 2$ (*not applicable* to the case $n = 1$). 

----

## (Universal) Covering Groups

- **Topological group**: a group which is also a topological space

    - **(Universal) Covering group**: a (universal) covering space of the topological group which is also a topological group (in this case, $p$ is a *group homomorphism*)

