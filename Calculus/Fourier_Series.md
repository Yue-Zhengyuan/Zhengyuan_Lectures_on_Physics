# Fourier Series

The **continuous Fourier transform in finite space** (usually called **Fourier series**) is obtained from DFT by taking the continuum limit

$$
(L = Na \ \text{is fixed}) \quad \text{and} \quad (a \to 0)
$$

- The site position $x_n = na$ becomes a *continuous* variable $x$. 
- The continuous function $f(x)$ inherits periodicity $f(x+L) = f(x)$ from the discrete sequence ($f_{n+N} = f_n$)
- The momentum $k_m = 2m\pi/L$ *remains discrete*, but now $m$ takes value from all $\mathbb{Z}$.

For two consecutive values of $x$, their difference is

$$
\Delta x = a
$$

The DFT formulas become (assuming finite convention for labelling of $x$, so that $x \in [0,L)$)

$$
\begin{align*}
    f(k_m) &= \sum_n f(x_n) e^{-ik_m x_n} 
    = \sum_n \frac{\Delta x}{a} \,f(x_n) e^{-ik_m x_n}
    \\
    &\to \frac{1}{a} \int_0^L dx \, f(x) e^{-ik x}
    
    \\[1.5em]

    f(x) &= \frac{1}{N} \sum_{m=-\infty}^{\infty} 
    f(k_m) e^{ik_m x}
\end{align*}
$$

However, from physical considerations, function $f(x)$ should be *rescaled*. As $a \to 0$, the amount of any physical quantity $f$ (e.g. mass, charge, displacement from equilibrium) assigned to each single site ("averaging" over the whole chain) approaches 0 as $O(a)$. Thus we redefine the function $f(x)$ as

<div class="result">

**Rescaling in the limit of continuous space:**

$$
f_{\text{lattice}}(x)
= f_{\text{continuum}}(x) \, \Delta x 
\quad (\Delta x = a)
$$

</div><br>

This rescaling is analog of the relation between *probability distributions* of discrete and continuous random variables. For discrete variables, we talk about the probability $P(x)$ that $x$ takes a certain value; but for continuous variables, we can only describe the probability $p(x) dx$ that $x$ is in the range $(x, x+dx)$ (where $p(x)$ is the probability density).

Thus, replace $f(x)$ by $a f(x)$ in the above transformation (keep $f(k)$ unchanged), we obtain

<div class="result">

**Fourier series of function $f(x)$**

$$
f(x) = \frac{1}{L} \sum_{m=-\infty}^{\infty} 
f(k_m) e^{ik_m x}, \quad
f(k_m) = \int_0^L dx \, f(x) e^{-ik_m x}
$$

</div><br>

<div class="remark">

*Remark*: 

- Since $f(x) = f(x+L)$, the Fourier series can be evaluated on any interval $[x_0, x_0 + L)$ (in particular, when $x_0 = -L/2$).

    $$
    f(k_m) = \int_{x_0}^{x_0+L} dx \, f(x) e^{-ik_m x}
    $$

- An alternative, more symmetric definition of Fourier series is

    $$
    f(x) = \frac{1}{\sqrt{L}} \sum_{m=-\infty}^{\infty} 
    f(k_m) e^{ik_m x}, \quad
    f(k_m) = \frac{1}{\sqrt{L}} \int_0^L dx \, f(x) e^{-ik_m x}
    $$

</div><br>

## Unitary Conditions

For Fourier series, the unitary conditions are slightly different:

- $k$-Orthogonality

    $$
    \begin{align*}
        \frac{1}{N} \sum_{n=0}^{N-1} e^{i (k_m - k_{m'}) x_n} 
        = \frac{1}{L} \sum_{n=0}^{N-1} 
        \Delta x \, e^{i (k_m - k_{m'}) x_n} 
        &= \delta_{m,m'}
    \end{align*}
    $$

    In the $N \to \infty$ limit, we obtain

    <div class="result">

    **$k$-Orthogonality (Fourier series):**

    $$
    \frac{1}{L} \int_0^L dx \, e^{i(k_m - k_{m'}) x} = \delta_{m,m'}
    $$

    </div><br>

    <div class="remark">

    *Remark*: Since the range of $n$ can be arbitrarily shifted, the momentum orthogonality also holds on any interval $[x_0, x_0+L)$ (in particular, when $x_0 = -L/2$).

    $$
    \frac{1}{L} \int_{x_0}^{x_0+L} dx \, e^{i(k_m - k_{m'}) x} 
    = \delta_{m,m'}
    $$

    </div><br>

- $x$-Orthogonality

    Without loss of generality, assume $N$ is odd. Then

    $$
    \sum_{m=-(N-1)/2}^{(N-1)/2} e^{ik_m (x' - x)} = N \delta_{x x'}
    $$

    This relation is more subtle: as $N \to \infty$, both sides are *infinite* when $x = x'$. It turns out that this divergent behavior is proportional to the **Dirac delta function**:

    <div class="result">

    **$x$-Orthogonality (Fourier series):**

    $$
    \frac{1}{L} \sum_{m=-\infty}^{\infty} e^{ik_m (x' - x)} 
    = \delta(x - x')
    $$

    </div><br>

    *Proof*: This relation actually means that for *any* function $f(x)$

    $$
    \int_{x_0}^{x_0+L} dx \, f(x) \sum_{m=-\infty}^{\infty} 
    e^{ik_m (x' - x)} = L f(x')
    $$

    To show this, we return to the discrete case: the LHS is then

    $$
    \begin{align*}
        &\sum_n \Delta x \, f(x_n) 
        \sum_m e^{ik_m (x_{n'} - x_n)}
        \quad (\Delta x = L/N = a)
        \\
        &= \sum_n \Delta x \, f(x_n) N \delta_{nn'}
        = (N \Delta x) f(x_{n'}) 
        \\
        &= L f(x_{n'}) \to L f(x') 
        \qquad \blacksquare
    \end{align*}
    $$
