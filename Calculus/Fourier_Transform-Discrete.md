# Fourier Transform

To motivate the discrete Fourier transform, consider an infinite 1D chain of evenly separated sites. The distance between two nearest neighbors is $a$. The $n$th site is at the position

$$
x_n = na \quad (n \in \mathbb{Z})
$$

The we apply a function $f(x): \R \to \C$ on the sites of the chain, and obtain a sequence of function values:

$$
f_n \equiv f(x_n)
$$

The function may represent some physical quantities of the site, such as mass, displacement, field strength, etc. 

## Boundary Conditions

As usually the case in practice, one can impose the **periodic/anti-periodic boundary condition (PBC/ABC)**: assume that:

$$
f(x + L) = \pm f(x), \quad L = Na \quad (N \in \mathbb{N}_+)
$$

Then all useful information is included in any interval containing $N$ consecutive sites, since the sequence $\{f(x_n)\}$ repeats itself every $N$ sites (with alternating signs for ABC):

$$
f_{n+N} = \pm f_n \quad \text{or} \quad
f(x_{n+N}) = \pm f(x_n)
$$

<div class="remark">

*Remark*: The ABC with period $L$ can be regarded as a special case of PBC with period $2L$, but of course there are redundant information in this doubled interval.

</div><br>

## Site Labelling Conventions

The sites within one period can be labelled by any $N$ consecutive integers. Two common choices are:

- The *natural* convention: labelling by natural numbers
    
    $$
    n \in [0, N) \cap \mathbb{Z} 
    = \{0, 1, ..., N-1\}
    $$

- The *symmetric* convention: labels are symmetrized around the origin

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

For notational convenience, below we use the natural convention unless otherwise stated.

## Exponential Functions as Basis Vectors

The $N$ values $\{f(x_n)\}$ within one period into a column vector in the vector space $\mathbb{C}^N$:

$$
f = [f(x_0), ..., f(x_{N-1})]^\mathsf{T} \in \mathbb{C}^N
$$

Then $f(x_n)$ can be regarded as the component of $f$ along the standard basis vectors $e_n$ $(n=1,...,N)$

$$
f = \sum_n f(x_n) e_n
$$

The **discrete Fourier transform** of $\{f(x_n)\}$ is the component of the vector $f$ under a *new set of orthonormal basis vectors* $\{u_m\}$, labelled by **momenta** $k_m$:

$$
f = \sum_m f(k_m) u_m, \quad
u_m^\dagger u_{m'} = \delta_{mm'}
$$

<div class="remark">

*Remark*: The momentum label $m$ is usually in the symmetric convention

$$
m \in \left[-\frac{N}{2}, \frac{N}{2} \right) \cap \mathbb{Z} 
$$

</div><br>

How to choose the new basis vectors $u_m$? This is done from the group theory point of view. The 1D lattice is invariant under translations by an integer number of sites; the group of translation is a

$$
T \cong \mathbb{Z}/N\mathbb{Z} \equiv \mathbb{Z}_N
$$

- Periodic boundary condition

    The 1D lattice is invariant





To summarize:

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
    k_m = \frac{2m\pi}{L}
    $$


</div><br>

## Unitarity of Transformation $U$

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

In term of $k_m, x_n$, these unitarity conditions can be written as

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

## Periodicity in Momentum Space

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

## Inverse Transform

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

## Another Convention

Another commonly used definition of the matrix $U$ is 

$$
U_{mn} = e^{-ik_m x_n}, \quad 
(U^{-1})_{nm} = \frac{1}{N} e^{ik_m x_n}
$$

Then the DFT formulas become

$$
f(k_m) = \sum_n e^{-i k_m x_n} f(x_n), \quad
f(x_n) = \frac{1}{N} \sum_m e^{i k_m x_n} f(k_m)
$$
