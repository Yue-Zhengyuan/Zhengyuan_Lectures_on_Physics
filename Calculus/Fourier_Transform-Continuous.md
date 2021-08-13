# Continuous Fourier Transform

The **continuous Fourier transform (in infinite space)** is obtained from the Fourier series by taking the limit 

$$ L \to \infty $$ 

(or equivalently from DFT by taking a *two-step* limit: *first* $a \to 0$, *then* $N \to \infty$). Now both $x, k$ will become continuous labels. Define the increment in $x, k$:

$$
\Delta x = a, \quad \Delta k = \frac{2\pi}{L} = \frac{2\pi}{Na}
$$

For infinite space, we *have to* use the symmetric labelling of $x$:

$$
n \in \bigg[-\frac{N}{2}, \frac{N}{2} \bigg) \cap \mathbb{Z} 
\ \Rightarrow \ 
x_n \in \bigg[-\frac{L}{2}, \frac{L}{2} \bigg)
$$

Physically, this means that the system does not have asymmetry between both sides of the origin $x = 0$. Then the Fourier series formulas become

$$
\begin{align*}
    \text{Fourier Series:} &\quad
    f(x) = \frac{1}{L} \sum_{m=-\infty}^{\infty} f(k_m) e^{ik_m x}
    \\
    \text{Series Coefficient:} &\quad
    f(k_m) = \int_{-L/2}^{L/2} dx \, f(x) e^{-ik_m x}
    \\
    k \text{-Orthogonality:} &\quad
    \int_{-L/2}^{L/2} dx \, e^{i(k_m - k_{m'}) x} 
    = L \delta_{m,m'}
    \\
    x \text{-Orthogonality:} &\quad
    \frac{1}{L} \sum_{m=-\infty}^{\infty} e^{ik_m (x' - x)} 
    = \delta(x - x')
\end{align*}
$$

In the $L\to \infty$ limit, we have the replacement

$$
\frac{1}{L} \sum_m = \sum_m \frac{\Delta k}{2\pi}
\to \int_{-\infty}^\infty \frac{dk}{2\pi}
$$

Then

<div class="result">

**Continuous Fourier transform:**

$$
f(x) = \int_{-\infty}^{\infty} \frac{dk}{2\pi} f(k) e^{ikx}, \quad 
f(k) = \int_{-\infty}^{\infty} dx \, f(x) e^{-ikx}
$$

</div><br>

An alternative, more symmetric definition is

$$
f(x) = \int_{-\infty}^{\infty} \frac{dk}{\sqrt{2\pi}} f(k) e^{ikx}, \quad 
f(k) = \int_{-\infty}^{\infty} \frac{dx}{\sqrt{2\pi}} \, f(x) e^{-ikx}
$$

## Unitary Relations

The generalization of $x$-orthogonality is straightforward:

<div class="result">

**$x$-Orthogonality (continuous Fourier transform):**

$$
\int_{-\infty}^{\infty} \frac{dk}{2\pi} e^{ik(x' - x)} 
= \delta(x - x')
$$

</div><br>

But the $k$-orthogonality is more subtle, since both sides are infinite as $L \to \infty$. Again, this leads to the appearance of Dirac delta function:

<div class="result">

**$k$-Orthogonality (continuous Fourier transform):**

$$
\int_{-\infty}^{\infty} dx \, e^{i(k-k')x} 
= 2\pi \delta(k - k')
$$

</div><br>

*Proof*: The easiest proof is to switch $x$ and $k$ in the $x$-orthogonality. Nevertheless, let us prove from the Fourier series formula. The delta function actually means for any function $f(k)$

$$
\int_{-\infty}^\infty \frac{dk}{2\pi} f(k) 
\int_{-\infty}^\infty dx \, e^{i(k-k')x} 
= f(k')
$$

In the finite-$L$ case, we have

$$
\begin{align*}
    &\frac{1}{L} \sum_m f(k_m) 
    \int_{-L/2}^{L/2} dx \, e^{i(k_m - k_{m'}) x} 
    \\
    &= \sum_m f(k_m) \delta_{mm'} = f(k_{m'})
    \to f(k') \quad \blacksquare
\end{align*}
$$

## Application in Quantum Mechanics

### Resolution of Identity

The position-space wave function of the momentum eigenstate $\ket{k}$ is (not normalized)

$$
\braket{x}{k} = e^{ikx}
$$

which can be verified by plugging in the operator $\hat{p} = -i\partial_x$ 

$$
\amp{x}{\hat{p}}{k} = -i\partial_x e^{ikx} = k e^{ikx} = \amp{x}{k}{k}
$$

The orthogonality relations for Fourier transform then becomes

$$
\begin{alignat*}{3}
    \int \frac{dk}{2\pi} e^{ik(x' - x)} 
    &= \int \frac{dk}{2\pi} \braket{x'}{k} \braket{k}{x}
    &&= \delta(x - x')
    \\
    \int dx \, e^{i(k-k')x} 
    &= \int dx \, \braket{k'}{x} \braket{x}{k}
    &&= 2\pi \delta(k - k')
\end{alignat*}
$$

Regarding $f(x), f(k)$ as the wave function in position/momentum space of the state $\ket{f}$, we have (by inserting an identity)

$$
\begin{align*}
    f(x) &= \braket{x}{f} 
    = \int \frac{dk}{2\pi} \braket{x}{k} \braket{k}{f}
    = \int \frac{dk}{2\pi} e^{ikx} f(k)
    \\
    f(k) &= \braket{k}{f}
    = \int dx\, \braket{k}{x} \braket{x}{f}
    = \int dx\, e^{-ikx} f(x)
\end{align*}
$$
