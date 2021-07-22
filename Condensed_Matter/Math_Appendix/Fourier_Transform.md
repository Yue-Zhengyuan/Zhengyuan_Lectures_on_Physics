# Fourier Transform

## One-Dimensional Chain

To motivate the discrete Fourier transform, we first construct a (periodic) 1D chain (let us call it $I$) of $N$ sites. The distance between two nearest neighbors is $a$; the length of the chain (period in space) is therefore $L = Na$.

```
    Example: N = 4

                 |<--a-->|
    ..-- + ----- + ----- + ----- + --..
         0       1       2       3
```

The $n$th site is at the position

$$
x_n = na, \quad x_{n + N} = x_n
\  (\text{Periodicity})
$$

Due to the periodicity, the sites on the chain can be labelled by any $N$ consecutive integers $n_0, n_0+1, ..., n_0+N-1$. Two conventional choices are:

- When the number of sites is finite, we usually use the "**finite convention**":
    
    $$
    n \in [0, N) \cap \mathbb{Z} 
    = \{0, 1, ..., N-1\}
    $$

- When the number of sites is infinite (e.g. an infinitely long chain, or when the lattice spacing tends to zero (the **continuum limit**)), we usually use the "**symmetric convention**":

$$
n \in \left[-\frac{N}{2}, \frac{N}{2} \right) \cap \mathbb{Z} 
= \begin{cases}
    \{ -\frac{N}{2}, ..., \frac{N}{2}-1 \}
    & N \, \text{even}
    \\
    \{ -\frac{N-1}{2}, ..., \frac{N-1}{2} \}
    & N \, \text{odd}
\end{cases}
$$

## Discrete Fourier Transform

Consider a function $f(x): I \to \mathbb{C}$ assigning a complex number to each site of the chain: 

$$
f_n \equiv f(x_n), \quad
$$

Obviously $f_n$ also has the periodicity $f_{n+N} = f_n$. We assemble these values $\{f_n\}$ into a column vector

$$
f = (f_0, ..., f_{N-1})^\mathsf{T} \ 
\text{or} \  (f_{-(N-1)/2}, ..., f_{(N-1)/2})^\mathsf{T}
$$

The **discrete Fourier transform** is a linear transformation on this vector $f$.

<div class="result">

**Discrete Fourier transform (DFT):**

$$
f(k_m) = \sum_n U_{mn} f(x_n) 
= \frac{1}{\sqrt{N}} \sum_n e^{-i k_m x_n} f(x_n)
$$

- The *unitary* transformation matrix $U_{mn}$ is given by

    $$
    U_{mn} = \frac{1}{\sqrt{N}} e^{-i k_m x_n}
    = \frac{1}{\sqrt{N}} e^{-2\pi i m n/N}, \quad
    k_m = \frac{2\pi m}{L}
    $$

- The momentum label $m$ is usually in the symmetric convention

    $$
    m \in \left[-\frac{N}{2}, \frac{N}{2} \right) \cap \mathbb{Z} 
    $$

    so that $k$ lies in the range $[-\pi/a, \pi/a)$ (the **1st Brillouin zone**). 

</div><br>

### Unitarity of Transformation $U$

We first prove the unitarity of the matrix $U$:

$$
\begin{align*}
    (U^\dagger U)_{nn'}
    &= \sum_m (U^\dagger)_{nm} U_{mn'}
    \\
    &= \frac{1}{N} \sum_m e^{2\pi imn/N} e^{-2\pi imn'/N}
    \\
    &= \frac{1}{N} \sum_m e^{2\pi im(n-n')/N} = \delta_{nn'}
    \\
    (U U^\dagger)_{mm'}
    &= \sum_m U_{mn} (U^\dagger)_{nm'}
    \\
    &= \frac{1}{N} \sum_n e^{-2\pi imn/N} e^{2\pi im'n/N}
    \\
    &= \frac{1}{N} \sum_n e^{2\pi i(m'-m)n/N} = \delta_{mm'}
    \quad \blacksquare
\end{align*}
$$

<div class="remark">

*Remark*: In term of $k_m, x_n$, these unitarity conditions can be written as

$$
\begin{align*}
    \frac{1}{N} \sum_m e^{ik_m (x_{n'} - x_n)} &= \delta_{nn'}
    &\quad &\text{(Position $x$ orthogonality)}
    \\
    \frac{1}{N} \sum_n e^{i(k_m - k_{m'}) x_n} &= \delta_{mm'}
    &\quad &\text{(Momentum $k$ orthogonality)}
\end{align*}
$$

which will give us the **Dirac delta function** when taking the continuum limit, as we will see later. 

</div><br>

### Periodicity in Momentum Space

The range of $m$ can also be chosen as any $N$ consecutive integers, due to the periodicity in momentum $k$ space:
    
$$
\begin{align*}
    f(k_{m+N})
    &= \sum_{n=0}^{N-1} 
    f(x_n) e^{-ik_{m+N} x_n} \\
    &= \sum_{n=0}^{N-1} 
    f(x_n) e^{-ik_m x_n} \underbrace{
        e^{-i(2\pi/a)na}
    }_{=\exp(-2\pi in) = 1} = f(k_m)
\end{align*}
$$

A shift of the range of $m$ corresponds to a cyclic permutation of rows of the matrix $U$, which does not affect its unitarity. 

### Inverse Transform

One can perform an *inverse* transform to recover $f(x_n)$ from $f(k_m)$. Since $U$ is unitary, we can easily find its inverse:

$$
(U^{-1})_{nm} = (U^\dagger)_{nm} = U_{mn}^*
= \frac{1}{\sqrt{N}} e^{ik_m x_n}
$$

Therefore

<div class="result">

**Inverse Discrete Fourier transform:**

$$
f(x_n) = \sum_m (U^{-1})_{nm} f(k_m) 
= \frac{1}{\sqrt{N}} \sum_m e^{i k_m x_n} f(k_m)
$$

</div><br>

<div class="remark">

*Remark*: Another commonly used definition of the matrix $U$ is 

$$
U_{mn} = e^{-ik_m x_n}, \quad 
(U^{-1})_{nm} = \frac{1}{N} e^{ik_m x_n}
$$

Then the DFT formulas become

$$
f(k_m) = \sum_n e^{-i k_m x_n} f(x_n), \quad
f(x_n) = \frac{1}{N} \sum_m e^{i k_m x_n} f(k_m)
$$

which are more convenient for deriving the continuum limit, and will be used below. 

</div><br>

## Fourier Series

The **Fourier series** (**continuous Fourier transform in finite space**) is obtained from DFT by taking the continuum limit

$$
(L = Na \ \text{is fixed}) \quad \text{and} \quad (a \to 0)
$$

- The site position $x_n = na$ becomes a *continuous* variable $x$. 
- The continuous function $f(x)$ inherits periodicity $f(x) = f(x+L)$ from the discrete sequence ($f_n = f_{n+N}$)
- The momentum $k_m = 2\pi m/L$ *remains discrete*, but now $m$ takes value from all $\mathbb{Z}$.

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

<div class="remark">

*Remark*: This rescaling is analog of the relation between *probability distributions* of discrete and continuous random variables. For discrete variables, we talk about the probability $P(x)$ that $x$ takes a certain value; but for continuous variables, we can only describe the probability $p(x) dx$ that $x$ is in the range $(x, x+dx)$ (where $p(x)$ is the probability density).

</div><br>

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

### Unitarity Conditions for Fourier Series

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

## Continuous Fourier Transform

The **continuous Fourier transform (in infinite space)** is obtained from the Fourier series by taking the limit 

$$ L \to \infty $$ 

(i.e. from DFT by taking a *two-step* limit of *first* sending $a \to 0$, *then* $N \to \infty$). Now both $x, k$ will become continuous labels. Define the increment in $x, k$:

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

<div class="remark">

*Remark*: An alternative, more symmetric definition is

$$
f(x) = \int_{-\infty}^{\infty} \frac{dk}{\sqrt{2\pi}} f(k) e^{ikx}, \quad 
f(k) = \int_{-\infty}^{\infty} \frac{dx}{\sqrt{2\pi}} \, f(x) e^{-ikx}
$$

</div><br>

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

## Relation to Quantum Mechanics

In quantum mechanics, the position-space wave function of the momentum eigenstate $\ket{k}$ is (not normalized)

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
