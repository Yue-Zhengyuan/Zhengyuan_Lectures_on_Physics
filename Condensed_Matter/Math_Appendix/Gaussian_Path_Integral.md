# Gaussian Path Integral

## Continuous Label of Integration Variables

We start with the real Gaussian integral with many variables (the complex case will be treated later):

$$
Z(J) = \int du_1 ... du_N \exp \left(
    - \frac{1}{2} u_i A_{ij} u_j + J_i u_i
\right)
$$

Note that we may finally take the $N \to \infty$ limit. We imagine that $u_n$ is the value of a physical quantity $u(x)$ (e.g. mass, oscillation displacement) at position $x_n$:

$$
u_n = u(x_n)
$$

where $x_n$ are positions on a $d$-dimensional, $N$-site square lattice (possibly of finite or infinite size, determined by $N$) with site spacing $a$, i.e.

$$
x_n = (n_1 a, ..., n_d a) \quad
n_1,...,n_d \in \mathbb{Z}
$$

Let us now take the continuum limit $a \to 0$ of the lattice (while keeping its volume $V = a^{Nd}$ unchanged). It is expected that the quantity $u(x_n)$ will scale as $a^d$, i.e. the volume per site; thus we set

<div class="result">

**Scaling of integration variables $u$:**

$$
u_i \to u_{\text{lattice}}(x_i)
= u_{\text{continuum}}(x_i) a^d
$$

</div><br>

Then, the integration measure of $Z$ is scaled to

$$
a^{Nd} \int \bigg[\prod_n du_n \bigg]
= V \int \bigg[\prod_n du_n \bigg]
$$

To get reasonable expression inside the exponent, we also require the matrix $A$ and the source $J$ *not* to scale with $a$:

$$
\begin{align*}
    A_{ij} \to A_{\text{lattice}}(x_i, x_j)
    &= A_{\text{continuum}}(x_i, x_j)
    \\
    J_i \to J_{\text{lattice}}(x_i)
    &= J_{\text{continuum}}(x_i)
\end{align*}
$$

Then in terms of the continuum variables, the integral becomes

$$
\begin{align*}
    Z(J) &= \lim_{a \to 0}
    V \int \bigg[\prod_n du(x_n) \bigg] 
    \\ &\quad \times \exp \bigg[
        - \frac{1}{2} a^{2d} \sum_{ij} 
        u(x_i) A(x_i,x_j) u(x_j) 
        + a^d \sum_{i} J(x_i) u(x_i)
    \bigg]
\end{align*}
$$

Note that in the exponential function, as $a \to 0$, the volume $a^d$ just serves as the *integration measure* over $x$:

$$
a^d \sum_i \to \int d^dx
$$

Define the integration measure (omitting unimportant constant normalization factors, such as the total volume $V$ of the parameter $x$ space)

$$
Du \equiv \prod_n du(x_n)
$$

we obtain

<div class="result">

**Real Gaussian path integral:**

$$
\begin{align*}
    Z(J) &\propto \int Du \,
    \exp \bigg[
        -\frac{1}{2} \int d^dx \, d^dy \,
        u(x) A(x,y) u(y)
        \\ &\qquad \qquad \qquad \qquad
        + \int d^dx \, J(x) u(x)
    \bigg]
\end{align*}
$$

</div><br>

In the path integral case, we are usually not interested in the overall constant normalization factor, and use the normalized integral

$$
\begin{align*}
    \mathcal{Z}(J) &\equiv \frac{Z(J)}{Z(0)} 
    = \exp \bigg[
        \frac{1}{2} J_i [A^{-1}]_{i j}J_j
    \bigg]
\end{align*}
$$

In the continuum limit, we obtain

<div class="result">

**Normalized real Gaussian path integral:**

$$
\mathcal{Z}(J)
= \exp \bigg[
    \frac{1}{2} \int d^dx \, d^dy \, 
    J(x) A^{-1}(x,y) J(y)
\bigg]
$$

</div><br>

## Example 1: Scalar Field Theory

## Example 2: Electromagnetism in Vacuum
