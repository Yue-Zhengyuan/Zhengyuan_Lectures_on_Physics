# Bogoliubov Transformation

*Reference*:

- S. Suzuki et al., *Quantum Ising Phases and Transitions in Transverse Ising Models* (Appendix 2.A)
- M. Stone, *Review of BCS-Bogoliubov Formalism* ([link](http://people.physics.illinois.edu/stone/magnus_berry.pdf))

## Bilinear Fermion Hamiltonian

A general bilinear fermion Hamiltonian has the form

$$
H = \frac{1}{2} \sum_{i,j} \Big[
    c_i^\dagger A_{ij} c_j + c_i^\dagger B_{ij} c_j^\dagger 
    + h.c.
\Big]
$$

Here these indices refer to the lattice position; they may also include the spin, sub-lattice, etc. of the particle. Writing the h.c. terms explicitly, we obtain

$$
\begin{align*}
    H &= \frac{1}{2} \sum_{i,j} \Big[
        c_i^\dagger A_{ij} c_j 
        + c_j^\dagger A^\dagger_{ji} c_i
        + c_i^\dagger B_{ij} c_j^\dagger 
        + c_j B^\dagger_{ji} c_i
    \Big] \\
    &= \sum_{i,j} \Big[
        c_i^\dagger A_{ij} c_j 
        + \frac{1}{2} c_i^\dagger B_{ij} c_j^\dagger 
        + \frac{1}{2} c_i B^\dagger_{ij} c_j
    \Big]
\end{align*}
$$

Here we redefined $(A + A^\dagger)/2 \to A$ and $B$ have the following notable properties: 

- $A$ is *Hermitian* ($A = A^\dagger$) by definition. 
- $B$ can always be made *anti-symmetric* ($B = -B^\mathsf{T}$) due to anti-commutativity of fermion operators.

----

*Proof for anti-symmetry of $B$*: Any matrix can be expressed as a sum of a symmetric matrix $\mathcal{S}$ and an anti-symmetric matrix $\mathcal{A}$:

$$
\mathcal{S}_{ij} = \frac{B_{ij}+B_{ji}}{2}, \quad 
\mathcal{A}_{ij} = \frac{B_{ij}-B_{ji}}{2}
$$

Then the bilinear terms in $H$ in terms of $S, A$ are

$$
\begin{align*}
    c_i^\dagger (\mathcal{S}_{ij}+\mathcal{A}_{ij}) c_j^\dagger 
    &= \frac{1}{2} \Big[
        c_i^\dagger \mathcal{S}_{ij} c_j^\dagger 
        + c_j^\dagger \mathcal{S}_{ji} c_i^\dagger 
        + c_i^\dagger \mathcal{A}_{ij} c_j^\dagger 
        + c_j^\dagger \mathcal{A}_{ji} c_i^\dagger 
    \Big] \\
    &= \frac{1}{2} \Big[
        c_i^\dagger \mathcal{S}_{ij} c_j^\dagger 
        - c_i^\dagger \mathcal{S}_{ij} c_j^\dagger 
        + c_i^\dagger \mathcal{A}_{ij} c_j^\dagger 
        - c_i^\dagger (-\mathcal{A}_{ij}) c_j^\dagger 
    \Big] \\
    &= c_i^\dagger \mathcal{A}_{ij} c_j^\dagger 
\end{align*}
$$

and similarly for its Hermitian conjugate. $\blacksquare$

----

We then write $A$ in matrix form: 

$$
\begin{align*}
    c_i^\dagger A_{ij} c_j 
    &= \frac{1}{2} \Big[
        A_{ij} c_i^\dagger c_j 
        + A_{ij} (\delta_{ij} - c_j c_i^\dagger)
    \Big] \\
    &= \frac{1}{2} \Big[
        c_i^\dagger A_{ij} c_j 
        - c_i A_{ij}^\mathsf{T} c_j^\dagger
        + A_{ij} \delta_{ij}
    \Big] 
    \\ &\Downarrow \\
    H 
    &= \frac{1}{2} \sum_{i,j} \Big[
        c_i^\dagger A_{ij} c_j 
        - c_i A_{ij}^\mathsf{T} c_j^\dagger
        + c_i^\dagger B_{ij} c_j^\dagger 
        + c_i B^\dagger_{ij} c_j
        + A_{ij} \delta_{ij}
    \Big]
    \\
    &= \frac{1}{2} \sum_{ij} (c_i^\dagger, c_i)
    \begin{bmatrix}
        A_{ij} & B_{ij} \\ B^\dagger_{ij} & -A_{ij}^\mathsf{T}
    \end{bmatrix} \begin{bmatrix}
        c_j \\ c_j^\dagger
    \end{bmatrix} + \frac{1}{2} \operatorname{Tr} A
\end{align*}
$$

To simplify the notation further, we assemble the big vector

$$
\Psi \equiv (c_1,c_2,...,c_1^\dagger,c_2^\dagger...)^\mathsf{T}
\Rightarrow
\left\{ \begin{aligned}
    & H = \frac{1}{2} \Psi^\dagger
    H^\text{BdG} \Psi + \frac{1}{2} \operatorname{Tr} A
    \\
    & H^\text{BdG} \equiv \begin{bmatrix}
        A & B \\ B^\dagger & -A^\mathsf{T}
    \end{bmatrix}
\end{aligned} \right.
$$

The $2N \times 2N$ matrix $H^\text{BdG}$ is called the **Bogoliubov-de-Gennes (BdG) Hamiltonian**.

## Bogoliubov Transformation

To diagonalize $H^\text{BdG}$, we need its eigenvalues and eigenvectors:

$$
\begin{bmatrix}
    A & B \\ B^\dagger & -A^\mathsf{T}
\end{bmatrix} \begin{bmatrix}
    u_\alpha \\ v_\alpha
\end{bmatrix} = E_\alpha \begin{bmatrix}
    u_\alpha \\ v_\alpha
\end{bmatrix}
$$

- $\alpha = 1,...,2N$ labels the eigenvalues and eigenvectors of $H$.
- $u_\alpha, v_\alpha$ are $N$-dimensional vectors.
- Since $H^\text{BdG}$ is Hermitian:
    - All eigenvalues $E_\alpha$ are real.
    - All eigenvectors are orthogonal, i.e. $H^\text{BdG}$ can be diagonalized by a unitary matrix.

But due to the special structure of $H^\text{BdG}$, not all eigenvalues are unrelated: taking the complex conjugate and swapping $u_\alpha, v_\alpha$, we obtain

$$
\begin{align*}
    \begin{bmatrix}
        A^* & B^* \\ B^\mathsf{T} & -A^\dagger
    \end{bmatrix} \begin{bmatrix}
        u^*_\alpha \\ v^*_\alpha
    \end{bmatrix} &= E_\alpha \begin{bmatrix}
        u^*_\alpha \\ v^*_\alpha
    \end{bmatrix} 
    \\ &\Downarrow \\
    \begin{bmatrix}
        A^\mathsf{T} & -B^\dagger \\ -B & -A
    \end{bmatrix} \begin{bmatrix}
        u^*_\alpha \\ v^*_\alpha
    \end{bmatrix} &= E_\alpha \begin{bmatrix}
        u^*_\alpha \\ v^*_\alpha
    \end{bmatrix}
    \\ &\Downarrow \\
    \begin{bmatrix}
        -A & -B \\ -B^\dagger & A^\mathsf{T}
    \end{bmatrix} \begin{bmatrix}
        v^*_\alpha \\ u^*_\alpha
    \end{bmatrix} &= E_\alpha \begin{bmatrix}
        v^*_\alpha \\ u^*_\alpha
    \end{bmatrix}
\end{align*}
$$

In obtaining the second line, we used

$$
\begin{array}{ccc}
    A = A^\dagger &\Rightarrow & A^* = A^\mathsf{T} 
    \\[0.3em]
    B = -B^\mathsf{T} &\Rightarrow & B^* = -B^\dagger
\end{array}
$$

This means that

<div class="result">
<center>

If $(u, v)^\mathsf{T}$ is an eigenvector of $H^\text{BdG}$ with eigenvalue $E$, <br> then $(v^*, u^*)^\mathsf{T}$ is also an eigenvector with eigenvalue $-E$.

</center>
</div><br>

To proceed, we make an important assumption:

<div class="result">
<center>

**All eigenvalues of $H^\text{BdG}$ are nonzero.**

</center>
</div><br>

Let $E_1,...,E_N$ be the positive eigenvalues of $H^\text{BdG}$. Then the eigen-decomposition (called **Bogoliubov transformation** in this context) of $H$ is given by:

$$
\begin{align*}
    U^{\dagger} H^\text{BdG} U 
    &= \operatorname{diag}(E_1,...,E_N,-E_1,...,-E_N)
    \\
    U &= \begin{bmatrix}
        u_1 & \cdots & u_N & v^*_1 & \cdots & v^*_N
        \\
        v_1 & \cdots & v_N & u^*_1 & \cdots & u^*_N
    \end{bmatrix}
\end{align*}
$$

The transformation matrix $U$ is *unitary*, which imposes the following constraints on $u_\alpha, v_\alpha$:

$$
\begin{align*}
    u^*_\alpha u_\beta + v^*_\alpha v_\beta 
    &= \delta_{\alpha \beta} \\
    v_\alpha u_\beta + u_\alpha v_\beta &= 0
\end{align*}
$$

<div class="remark">

*Remark*: Usually the $2N \times 2N$ matrix $H$ is already *block-diagonal* (e.g. in momentum representation). Then we can diagonalize each block separately.

</div><br>

### Bogoliubov Quasi-Particles

We define a new set of operators $a_\alpha, a_\alpha^\dagger$ related to the old $c_j, c_j^\dagger$ by the matrix $U$:

$$
\Phi \equiv (a_1,a_2,...,a_1^\dagger,a_2^\dagger...)^\mathsf{T}
\Rightarrow \Psi = U \Phi
$$

For each component:

<div class="result">

**Bogoliubov quasi-particles $a_\alpha, a_\alpha^\dagger$:**

$$
\begin{align*}
    c_j = \sum_\alpha (u_{j\alpha} a_\alpha + v^*_{j\alpha} a_\alpha^\dagger)
    \\
    c_j^\dagger = \sum_\alpha (v_{j\alpha} a_\alpha + u^*_{j\alpha} a_\alpha^\dagger)
\end{align*}
$$

</div><br>

Since $U$ is unitary, the new operators still satisfy the fermion anti-commutation rules. Now the fermion Hamiltonian can be diagonalized as

$$
\begin{align*}
    H
    &= \frac{1}{2} \Phi^\dagger U^\dagger
    H^\text{BdG} U \Phi 
    + \frac{1}{2} \operatorname{Tr} A
    \\
    &= \frac{1}{2} \sum_\alpha E_\alpha 
    (a_\alpha^\dagger a_\alpha - a_\alpha a_\alpha^\dagger)
    + \frac{1}{2} \operatorname{Tr} A
    \\
    &= \sum_\alpha E_\alpha a_\alpha^\dagger a_\alpha
    - \frac{1}{2} \sum_\alpha E_\alpha
    + \frac{1}{2} \sum_j \epsilon_j
\end{align*}
$$

where $\epsilon_j \ (j=1,...,N)$ are eigenvalues of $A$.

## Bogoliubov Transformation in Momentum Space

One may think that simply regarding subscripts $i,j$ as momentum labels, we can directly obtain the Bogoliubov transformation in momentum space. However in practice, the transformation procedure is a little bit different to make use of the translation symmetry of the system. 

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

where $x_j$ is some relative position within one unit cell. Then the bilinear part of $H$ is transformed to

$$
\begin{align*}
    & \frac{1}{2} \sum_{i,j} \sum_{R,R'} 
    (c^{i\dagger}_R, c^i_R)
    \mathcal{H}^{ij}_{RR'} \begin{bmatrix}
        c^j_{R'} \\ c^{j\dagger}_{R'}
    \end{bmatrix}
    \\
    &= \frac{1}{2N} \sum_{R,R'} \sum_{k,k'}
    (c^{i\dagger}_k, c^i_{-k})
    \mathcal{H}^{ij}_{RR'} \begin{bmatrix}
        c^j_{k'} \\ c^{j\dagger}_{-k'}
    \end{bmatrix} 
    e^{i[-k(R+x_i) + k'(R'+x_j)]}
\end{align*}
$$

Now we define the $2\times 2$ matrix $\mathcal{H}$ in momentum space as

$$
\mathcal{H}^{ij}_{kk'}
\equiv \frac{1}{N} \sum_{R,R'} \mathcal{H}^{ij}_{RR'} 
e^{i[-k(R+x_i) + k'(R'+x_j)]}
$$

and we construct the big vector

$$
\Psi_k \equiv (
    c_k^1, c_k^2,..., 
    c_{-k}^{1\dagger}, c_{-k}^{2\dagger}, ...
)^\mathsf{T}
$$

Then

$$
\begin{align*}
    H &= \frac{1}{2} \sum_{k,k'} \Psi^\dagger_k 
    H^\text{BdG}_{kk'} \Psi_{k'} 
    + \frac{1}{2} \operatorname{Tr} A
\end{align*}
$$

The BdG Hamiltonian in momentum space is thus given by

$$
\begin{align*}
    H^\text{BdG}_{kk'}
    &= \begin{bmatrix}
        A_{kk'} & B_{kk'} \\ B^\dagger_{kk'} & -A^\mathsf{T}_{kk'}
    \end{bmatrix}
\end{align*}
$$

Here the matrices $A_{kk'}, B_{kk'}$ are defined similarly to $\mathcal{H}_{kk'}$:

$$
\begin{align*}
    A^{ij}_{kk'}
    &\equiv \frac{1}{N} \sum_{R,R'} A^{ij}_{RR'} 
    e^{i[-k(R+x_i) + k'(R'+x_j)]}
    \\
    B^{ij}_{kk'}
    &\equiv \frac{1}{N} \sum_{R,R'} B^{ij}_{RR'} 
    e^{i[-k(R+x_i) + k'(R'+x_j)]}
\end{align*}
$$

In the original real-space formulation, $A$ is Hermitian and $B$ is anti-symmetric:

$$
\begin{align*}
    A^{ij}_{RR'} = (A^\dagger)^{ij}_{RR'}, \quad
    B^{ij}_{RR'} = -(B^\mathsf{T})^{ij}_{RR'}
\end{align*}
$$
