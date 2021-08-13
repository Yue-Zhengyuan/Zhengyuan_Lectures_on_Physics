# Bogoliubov Transformation

<font size=5>

**Part 2: Momentum Space Formulation**

</font>

One may think that simply regarding subscripts $i,j$ in the real space formalism as momentum labels, we can directly obtain the Bogoliubov transformation in momentum space. However in practice, the transformation procedure is different to make use of the translation symmetry of the system. For notation simplicity, only 1D systems will be discussed below. 

Starting from the real space Hamiltonian

$$
H = \frac{1}{2} \sum_{i,j} (c_i^\dagger, c_i)
\begin{bmatrix}
    A_{ij} & B_{ij} \\ B^\dagger_{ij} & -A_{ij}^\mathsf{T}
\end{bmatrix} \begin{bmatrix}
    c_j \\ c_j^\dagger
\end{bmatrix} + \frac{1}{2} \operatorname{Tr} A
$$

We separate the subscript of $c_j$ to two parts: 

$$
c_j \to c_R^j \quad \left\{\begin{aligned}
    & R: \text{Lattice (unit cell) position}
    \\
    & j: \text{Other labels (spin, sub-lattice, etc)}
\end{aligned} \right.
$$

The Fourier transform of the fermion operators is

$$
c^j_R = \frac{1}{\sqrt{N}} \sum_k c^j_k e^{ik(R+x_j)}
$$

where $x_j$ is some position vectors within one unit cell. Then the bilinear part of $H$ is transformed to (note that creation operators $c^\dagger$ are transformed with momentum $-k$, in order to give the same exponential factor as $c$):

$$
\begin{align*}
    & \frac{1}{2} \sum_{\begin{subarray}{c}
        i,j \\ R,R'
    \end{subarray}}
    (c^{i\dagger}_R, c^i_R)
    \begin{bmatrix}
        A^{ij}_{RR'} & B^{ij}_{RR'} 
        \\ (B^\dagger)^{ij}_{RR'} & -(A^\mathsf{T})^{ij}_{RR'}
    \end{bmatrix} \begin{bmatrix}
        c^j_{R'} \\ c^{j\dagger}_{R'}
    \end{bmatrix}
    \\
    &= \frac{1}{2N} \sum_{k,k'}
    \sum_{\begin{subarray}{c}
        i,j \\ R,R'
    \end{subarray}} 
    (c^{i\dagger}_k, c^i_{-k})
    \begin{bmatrix}
        A^{ij}_{RR'} & B^{ij}_{RR'} 
        \\ (B^\dagger)^{ij}_{RR'} & -(A^\mathsf{T})^{ij}_{RR'}
    \end{bmatrix} \begin{bmatrix}
        c^j_{k'} \\ c^{j\dagger}_{-k'}
    \end{bmatrix} 
    e^{i[-k(R+x_i) + k'(R'+x_j)]}
    \\
    &= \frac{1}{2} \sum_{k,k'} \sum_{i,j} 
    (c^{i\dagger}_k, c^i_{-k})
    \begin{bmatrix}
        A^{ij}_{kk'} & B^{ij}_{kk'} 
        \\ (B^\dagger)^{ij}_{kk'} & -(A^\mathsf{T})^{ij}_{kk'}
    \end{bmatrix} \begin{bmatrix}
        c^j_{k'} \\ c^{j\dagger}_{-k'}
    \end{bmatrix} 
\end{align*}
$$

Here we define the Fourier transform $M^{ij}_{kk'}$ of any matrix $M^{ij}_{RR'}$ as

$$
M^{ij}_{kk'}
= \frac{1}{N} \sum_{R,R'} M^{ij}_{RR'} 
e^{i[-k(R+x_i) + k'(R'+x_j)]}
$$

The transformed $M^\mathsf{T}, M^\dagger$ are


Let $D$ be the dimension of degrees of freedom other than the lattice position (i.e. the indices $i,j$). Define the vector

$$
\Psi_k \equiv (
    c_k^1, ..., c_k^D,
    c_{-k}^{1\dagger}, ..., c_{-k}^{D\dagger}
)^\mathsf{T}, \quad
$$

In matrix notation,

<div class="result">

**BdG Hamiltonian in momentum space:**

$$
\begin{align*}
    H &= \frac{1}{2} \sum_{k,k'} \Psi^\dagger_k 
    H^\text{BdG}_{kk'} \Psi_{k'} 
    + \frac{1}{2} \operatorname{Tr} A
    \\
    H^\text{BdG}_{kk'}
    &= \begin{bmatrix}
        A_{kk'} & B_{kk'} \\ (B^\dagger)_{kk'} & -(A^\mathsf{T})_{kk'}
    \end{bmatrix} \in \C^{2D \times 2D}
\end{align*}
$$

</div><br>

### Properties of $A_{kk'}, B_{kk'}$

In the original real-space formulation, $A$ is Hermitian and $B$ is anti-symmetric:

$$
A = A^\dagger, \quad B = -B^\mathsf{T}
$$

Then

$$
\begin{align*}
    (A^\mathsf{T})^{ij}_{-k,-k'}
    &= \frac{1}{N} \sum_{R,R'} (A^\mathsf{T})^{ij}_{RR'} 
    e^{i[k(R+x_i) - k'(R'+x_j)]} \\
    &= \frac{1}{N} \sum_{R,R'} (A^*)^{ij}_{RR'} 
    e^{i[k(R+x_i) - k'(R'+x_j)]} \\
    &= (A^{ij}_{kk'})^*
\end{align*}
$$

## Translation Invariance

The momentum space formalism is usually used for systems with **translation symmetry**, which implies that: 

- Nonzero elements in matrices $A^{ij}, B^{ij}$ are at diagonal lines.
- Elements on each diagonal line are equal.

Mathematically (setting lattice constant $a = 1$)

$$
\begin{aligned}
    A^{ij}_{0,d} = A^{ij}_{1,d+1} = \cdots 
    = A^{ij}_{N-1,N-1+d} \equiv A^{ij}_d
    \\
    B^{ij}_{0,d} = B^{ij}_{1,d+1} = \cdots 
    = B^{ij}_{N-1,N-1+d} \equiv B^{ij}_d
\end{aligned} \quad (d = 0,...,N-1)
$$

where $d$ is the vector connecting two interacting fermions (for most physical systems $d$ will be small). The subscripts are labelled module $N$, with PBC/ABC imposed on terms crossing the boundary (thus cancelling the $\pm$ sign in $c_{n+N} = \pm c_n$); for example

$$
A^{ij}_{N-2, N+5} \equiv \pm A^{ij}_{N-2,5}
$$

This will lead to momentum conservation:

$$
\begin{align*}
    A^{ij}_{kk'}
    &= \frac{1}{N} \sum_d \sum_{R} \Big[
        A^{ij}_{R,R+d} e^{i[-k(R+x_i) + k'(R+d+x_j)]}
        \\ &\qquad \qquad \qquad
        + A^{ij}_{R+d,R} e^{i[-k(R+d+x_i) + k'(R+x_j)]}
    \Big]
    \\
    &= \frac{1}{N} \sum_d \sum_{R} 
    A^{ij}_d e^{i[(-k+k')R]} e^{i[-kx_i+k'x_j]} 
    [e^{ik'd} + e^{-ikd}]
    \\
    &= 2\delta_{k-k'} e^{ik(-x_i+x_j)} 
    \sum_d A^{ij}_d \cos kd
    \\
    B^{ij}_{kk'}
    &= \frac{1}{N} \sum_d \sum_{R} \Big[
        B^{ij}_{R,R+d} e^{i[-k(R+x_i) + k'(R+d+x_j)]}
        \\ &\qquad \qquad \qquad
        + B^{ij}_{R+d,R} e^{i[-k(R+d+x_i) + k'(R+x_j)]}
    \Big]
    \\
    &= \frac{1}{N} \sum_d \sum_{R} 
    B^{ij}_d e^{i[(-k+k')R]} e^{i[-kx_i+k'x_j]} 
    [e^{ik'd} - e^{-ikd}]
    \\
    &= 2i \delta_{k-k'} e^{ik(-x_i+x_j)} 
    \sum_d B^{ij}_d \sin kd
\end{align*}
$$

## Diagonalization of $H^\text{BdG}_{k}$

## Example: XY Spin Chain

After Bogoliubov transformation, the spinless fermion Hamiltonian corresponding to the 1D XY spin chain is (with zero external field)

$$
H_F = \sum_{R=1}^N \Big[
    t(c_R^\dagger c_{R+1} + h.c.)
    + \Delta (c_R^\dagger c_{R+1}^\dagger + h.c.) 
\Big]
\quad (c_{N} = \pm c_0)
$$

which obviously has translation symmetry. Here we set the lattice constant $a = 1$ (or equivalently, measure momentum $k$ in units of $1/a$). The nonzero elements of real space matrices $A, B$ are nearest neighbor ($d = 1$) terms

$$
\begin{aligned}
    A_{R,R+1} &= A_{R+1,R} = t \\
    B_{R,R+1} &= -B_{R+1,R} = \Delta
\end{aligned} \quad (R=0,...,N-1)
$$

Again, the indices are module $N$ (e.g. $A_{N-1,N} = \pm A_{N-1,0}$). The Fourier transformed matrices $A_{kk'}, B_{kk'}$ are (in this example the original subscripts refer to position only; thus all $x_j = 0$, and $A_{kk'}, B_{kk'}$ are both a single number)

$$
\begin{align*}
    A_{kk'}
    &= 2\delta_{k-k'} t \cos k
    \\
    B_{kk'} 
    &\equiv 2i \delta_{k-k'} \sum_d \Delta \sin k
\end{align*}
$$

Thus the momentum space BdG Hamiltonian is (restoring the lattice constant $a$)

$$
\begin{align*}
    H^\text{BdG}_{kk'}
    &= \begin{bmatrix}
        A_{kk'} & B_{kk'} \\ (B^\dagger)_{kk'} & -(A^\mathsf{T})_{kk'}
    \end{bmatrix} \\
    &= \begin{bmatrix}
        2t \cos ka & 2i\Delta \sin ka \\
        -2i\Delta \sin ka & -2t \cos ka
    \end{bmatrix} \delta_{k-k'}
\end{align*}
$$
