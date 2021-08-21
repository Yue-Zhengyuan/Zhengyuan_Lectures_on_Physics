# Math Preliminary: Complex Analysis 

## Cauchy Integral Formula

For any function defined in a region on the complex plane, we have the **Laurent expansion** around a point $z_0$ in that region:

$$
f(z) = \sum_{n=-\infty}^{+\infty} 
a_n (z - z_0)^n
$$

The $n < 0$ part is called the **principal part**, and the usual $n \ge 0$ part is the **analytic part**. The coefficients can be found by: 

<div class="result">

**Cauchy integral formula**:

$$
a_n = \frac{1}{2\pi i}
\oint_C dz \,
\frac{f(z)}{(z - z_0)^{n+1}}, \quad
n \in \Z
$$

The integration path $C$ (counter-clockwise) must enclose $z_0$, and obviously in the region where $f(z)$ is defined.

</div><br>

*Explanation of the Cauchy Integral Formula:*

Since the complex integration is *independent of the shape* of the closed path $C$, we can take $C$ to be a circle of radius $r$ around the point $z_0$. Then $C$ can be parametrized as

$$
C = \{ z \mid z_0+r e^{i \theta}, \,
\theta \in [0,2\pi) \}
$$

The complex integral is then reduced to the real integral：

$$
\oint_C dz 
= i r\int_0^{2\pi} e^{i \theta} d\theta
$$

Plug in the Laurent expansion in the RHS of the Cauchy formula:

$$
\begin{align*}
    &\frac{1}{2 \pi i}
    \oint_C dz \frac{f(z)}{(z-z_0)^{n+1}}
    \\
    &=\frac{1}{2\pi i}
    \sum_{m=-\infty}^{\infty} 
    \oint_C dz \, a_m(z - z_0)^{m-(n+1)}
    \\
    &= \frac{1}{2 \pi i} \sum_{m=-\infty}^{\infty} i r a_m\int_0^{2\pi}d\theta \, e^{i \theta} (r e^{i \theta})^{m-(n+1)}
    \\
    &= \frac{1}{2\pi} \sum_{m=-\infty}^{\infty} r^{m-n}a_m\int_0^{2\pi}d\theta \, e^{i(m-n)\theta}
    \\
    &= \sum_{m=-\infty}^{\infty} r^{m-n}a_m \delta_{m n}
    = a_n \qquad \qquad \blacksquare
\end{align*}
$$

<div class="remark">

*Remark*: Comparing the analytic part with the usual Taylor series, we find:

1. for $n\ge 0$ (the derivatives)

    $$
    f^{(n)}(z_0)
    = \frac{n!}{2\pi i}
    \oint_C dz \frac{f(z)}{(z-z_0)^{n+1}}
    $$

2. for $n=0$ (the function itself)

    $$
    f(z_0)
    = \frac{1}{2\pi i}
    \oint_C dz \, \frac{f(z)}{z-z_0}
    $$

</div><br>

## The Residue Theorem

Suppose that

$$
f(z) = \sum_{n=-m}^{+\infty} a_n (z - z_0)^n
\quad (m\in \mathbb{N})
$$

and let $C$ be a closed path enclosing $z=z_0$ but no other singular points of $f(z)$. Then apply the Cauchy Integral Formula for $n=-1$, we have: 

<div class="result">

**The residue theorem:**

$$
\oint_C dz \, f(z) = 2 \pi i a_{-1}
$$

</div><br>
