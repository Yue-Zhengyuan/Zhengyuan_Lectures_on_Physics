# Integration of Differential Forms

## Orientation

*Definition*:

- **Orientation of basis vectors**: two sets of basis vectors (at the same point)

    $$
    e_\mu \equiv \frac{\partial}{\partial x^\mu}, \quad
    \tilde{e}_\mu \equiv \frac{\partial}{\partial y^\mu}
    $$

    **define the same orientation** if the transformation matrix (Jacobian) from one set to the other has *positive determinant*:

    $$
    \det \left( 
        \frac{\partial x}{\partial y} 
    \right) > 0
    $$

    if the determinant of the Jacobian is *negative*, the two sets **define the opposite direction**

- **Orientable manifold**: a manifold with a cover $\{U_i\}$, the sets of basis vectors from *any overlapping* charts in the overlapping region defining the same direction.

- **Volume element $\omega$**: a non-vanishing differential form defined on an *orientable* manifold; its order is *the same* as the manifold dimension

    - **Equivalent volume elements**: two volume elements related by a *positive-definite* function $h \in \mathcal{F}(M)$ such that $\omega' = h \omega$

### Change of Basis (Coordinates)

Take an $m$-form from $m$-dimensional manifold $M$

$$
\omega = h(p) \, dx^1 \wedge \cdots \wedge dx^m
$$

If we change the coordinates from $x$ to $y$, the volume element transforms to

$$
\begin{align*}
    \omega &= h(p) \,
    \frac{\partial x^1}{\partial y^{\mu_1}} dy^{\mu_1}
    \wedge \cdots \wedge
    \frac{\partial x^m}{\partial y^{\mu_m}} dy^{\mu_m}
    \\
    &= h(p) \, 
    \det \left(\frac{\partial x}{\partial y} \right)
    dy^1 \wedge \cdots \wedge dy^m
\end{align*}
$$

Here we used the definition of the matrix determinant.

Since $\omega$ is defined on an orientable manifold, the determinant should either be always positive or always negative. 

## Integration of Forms

Let $f: M \to \mathbb{R}$ be a function defined on $m$-dimensional manifold $M$; $\omega$ is a volume element. 

### On One Chart

In one chart $(U, \varphi)$ with coordinates $x$, we define the integration in $U$ simply as the ordinary integration in the coordinate space $\varphi(U)$:

$$
\int_{U} f \omega \equiv
\int_{\varphi(U)} f(\varphi^{-1}(x)) \, h(\varphi^{-1}(x))
\, dx^1 \cdots dx^m
$$

Here we used $dx^1 \cdots dx^m = dx^1 \wedge \cdots dx^m$. 

### On the Whole Manifold

*Definition*: Take an *open* covering $\{U_i\}$ of $M$ such that each point in $M$ is covered with *a finite number of $U_i$* (we assume that this is possible).

- **Partition of unity**: a family of differentiable functions $\varepsilon_i: M \to \mathbb{R}$ satisfying:
    
    > - $0 \le \varepsilon_i(p) \le 1$
    >
    > - $\varepsilon_i$ *vanishes* outside $U_i$
    >
    > - $(\forall p \in M) \, \sum_i \varepsilon_i(p) = 1$ (hence the name "partition of unity")

The partition of unity allows us to write

$$
f(p) = \sum_i f_i(p), \quad f_i(p) \equiv f(p) \varepsilon_i(p)
$$

where $f_i(p)$ also vanishes outside $U_i$. Then we can generalize the integration to the whole manifold:

$$
\int_M f \omega \equiv \sum_i \int_{U_i} f_i \omega
$$

i.e. as the sum of integral from each chart. 