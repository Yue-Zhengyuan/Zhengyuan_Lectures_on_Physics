# Isometries

*Definition*: Let $X, Y$ be two metric spaces with metrics $d_X, d_Y$. 

- **Isometry**: a *distance-preserving* map $f:X \to Y$ such that

$$
d_X(a,b) = d_Y(f(a), f(b)) \quad
\forall a,b \in X
$$

## General Properties of Isometries

1. $f$ is *injective*, i.e. 

    $$
    \forall a, b \in X, \quad
    (a \ne b) \Rightarrow (f(a) \ne f(b))
    $$

    Otherwise the distance between $a, b$ cannot be preserved.

2. The composition of two isometries, and the inverse of an isometry (if it is also bijective) are still isometries.

3. Isometries from a metric space $X$ to *itself* are automatically bijective; thus they form a *group* (denoted by $\Isom(X)$) under the composition of mappings.