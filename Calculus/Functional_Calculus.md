# Functional Calculus

## From Multi-variable Function to Functional

In functional calculus, the $i,j,...$ subscripts is replaced by the continuous label $x$, and sum over the subscript is replaced by integration over $x$.

## Functional Derivative

Recall that in ordinary multi-variable calculus, we have

$$
\frac{\partial}{\partial x_i} x_j = \delta_{ij}
\, \Rightarrow \,
\frac{\partial}{\partial x_i} \sum_{j} x_j k_j = k_i
$$

By replacing the subscripts by continuous labels $x,y,...$, and change the Kronecker delta to delta function, we naturally define the **functional derivative** as

$$
\frac{\delta}{\delta J(x)} J(y) = \delta(x - y)
$$

This also applies to higher dimensional coordinate label $x$. Therefore

$$
\begin{align*}
    &\frac{\delta}{\delta J(x)} \int dy \, J(y) \phi(y)
    \\
    &= \int dy \, \delta(x-y) \phi(y) = \phi(x)
\end{align*}
$$

For the derivative of a composite functional, we can still use the chain rule. For example

$$
\begin{align*}
    &\frac{\delta}{\delta J(x)} \exp \bigg[
        i \underbrace{\int dy \, J(y) \phi(y)}_{F}
    \bigg]
    \\
    &= \frac{\delta F}{\delta J(x)} \frac{\delta e^{iF}}{\delta F}
    = \phi(x) \times i e^{iF}
    \\
    &= i \phi(x) \exp \bigg[
        i \int dy \, J(y) \phi(y)
    \bigg]
\end{align*}
$$

If the variable to be differentiated appears in the functional as its derivative, then we first integrate by parts to restore it to itself, then take the derivative. For example (in 3+1D spacetime)

$$
\begin{align*}
    &\frac{\delta}{\delta J(x)} \int d^4y \,
    V^\mu(y) \partial_\mu J(y)
    \\
    &= \frac{\delta}{\delta J(x)} \left[
        -\int d^4y \, J(y) \partial_\mu V^\mu(y)
    \right]
    \\[1em]
    &= - \partial_\mu V^\mu(x)
\end{align*}
$$

## Functional Extrema and Euler-Lagrange Equation

