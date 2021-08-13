# Isometries of $\R^n$

## General Properties of Isometries

In general, given two metric spaces $X, Y$ with metrics (distances) $d_X, d_Y$, an **isometry** is a *distance-preserving* map between them:

$$
f: X \to Y \quad 
\forall a,b \in X, \quad
d_X(a,b) = d_Y(f(a), f(b))
$$

Below we list some general properties of isometries that follow immediately from the definition, without giving a rigorous proof.

- $f$ is *injective*, i.e. 

    $$
    \forall a, b \in X, \quad
    (a \ne b) \Rightarrow (f(a) \ne f(b))
    $$

    Otherwise the distance between $a, b$ cannot be preserved.

- The composition of two isometries, and the inverse of an isometry (if it is also bijective) are still isometries.

From these properties, all isometries from a metric space $X$ to *itself* are automatically bijective; thus they form a *group* under the composition of mappings.

## Classification of Isometries of $\mathbb{R}^n$

From now on we consider isometries between $\R^n$ and itself, which are required to be globally defined (i.e. are *bijective*). The set of all such isometries (denoted by $\Isom(\R^n)$) is a *group* under the usual composition of mappings. 

We first make $\R^n$ into a vector space with an *inner product*; then the metric $d(x,y)$ on $\R^n$ is directly chosen as the square root the inner product of $x - y$ and itself. Isometries of $\R^n$ can be divided into two types:

- **Origin-preserving isometries**: such an isometry $h$ satisfies

    $$
    h(0) = 0
    $$

    One can show that the set of all origin-preserving isometries is a *subgroup* of $\Isom(\R^n)$. It turns out that these isometries are *linear transformations* of $\R^n$, and furthermore

    <div class="result">

    *Theorem*: The subgroup of origin-preserving isometries of $\R^n$ is *isomorphic* to the orthogonal group $O(\R^n)$.

    </div><br>

- **Non-origin-preserving isometries**: $g(0) \ne 0$

    Among the isometries that do not preserve the origin, **translations** are of special importance. A translation by a vector $a \in \R^n$ is denoted by $\tau_a$: 

    $$
    \tau_a: \R^n \to \R^n \quad 
    \forall x\in R^n, \quad \tau_a(x) = a + x
    $$

    Intuitively, the composition and the inverse of translations are given by

    $$
    \tau_a \circ \tau_b = \tau_b \circ \tau_a = \tau_{a+b}, \quad
    \tau_a^{-1} = \tau_{-a}
    $$

    Thus the set of all translations form a *Abelian* (all translations commute with each other) subgroup $T$ of $\Isom(\R^n)$. 

    <div class="result">

    *Theorem*: An isometry $g$ that does not preserve the origin can always be related to an origin-preserving one $h$ by a translation $\tau_a$:

    $$
    g(x) = a + h(x) = (\tau_a \circ h)(x), \quad a \equiv g(0)
    $$

    </div><br>

## Building $\Isom(\R^n)$ from Subgroups

The whole isometry group $G \equiv \Isom(\R^n)$ can be built from the origin-preserving subgroup $H \cong O(\R^n)$ and the translation subgroup $T$ by semi-direct product.


## Composition of Isometries
