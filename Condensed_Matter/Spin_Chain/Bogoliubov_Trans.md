# Bogoliubov Transformation

*Reference*:

- S. Suzuki et al., *Quantum Ising Phases and Transitions in Transverse Ising Models* (Appendix 2.A)
- M. Stone, *Review of BCS-Bogoliubov Formalism* ([link](http://people.physics.illinois.edu/stone/magnus_berry.pdf))

## Bilinear Fermion Hamiltonian

The general bilinear fermion Hamiltonian (**Bogoliubov-de-Gennes Hamiltonian**) has the form

$$
H_\text{BdG} = \frac{1}{2} \sum_{i,j} \Big[
    c_i^\dagger A_{ij} c_j + c_i^\dagger B_{ij} c_j^\dagger 
    + h.c.
\Big]
$$

The indices can have various meanings:

- For a 1D chain of $N$ sites of spinless fermion:
    - In real space, we usually choose $i,j = 1,...,N$. 
    - In momentum space, $i, j$ are momentum labels, but not necessarily in ascending/descending order. Usually they count $k, -k$ in pairs. 
- These indices may also include the spin, sub-lattice, etc. of the particle. 

Writing the h.c. terms explicitly, we obtain

$$
\begin{align*}
    H_\text{BdG} &= \frac{1}{2} \sum_{i,j} \Big[
        c_i^\dagger A_{ij} c_j 
        + c_j^\dagger A^\dagger_{ji} c_i
        + c_i^\dagger B_{ij} c_j^\dagger 
        + c_j B^\dagger_{ji} c_i
    \Big] \\
    &= \sum_{i,j} \Big[
        c_i^\dagger H_{ij} c_j 
        + \frac{1}{2} c_i^\dagger B_{ij} c_j^\dagger 
        + \frac{1}{2} c_i B^\dagger_{ij} c_j
    \Big]
\end{align*}
$$

Here the matrices $H \equiv (A + A^\dagger)/2$ and $B$ have the following notable properties: 

- $H$ is *Hermitian* ($H = H^\dagger$) by definition. 
- $B$ can always be made *anti-symmetric* ($B = -B^\mathsf{T}$) due to anti-commutativity of fermion operators.

----

*Proof for anti-symmetry of $B$*: Any matrix can be expressed as a sum of a symmetric matrix $S$ and an anti-symmetric matrix $A$:

$$
S_{ij} = \frac{B_{ij}+B_{ji}}{2}, \quad 
A_{ij} = \frac{B_{ij}-B_{ji}}{2}
$$

Then the bilinear terms in $H_\text{BdG}$ in terms of $S, A$ are

$$
\begin{align*}
    c_i^\dagger (S_{ij}+A_{ij}) c_j^\dagger 
    &= \frac{1}{2} \Big[
        c_i^\dagger S_{ij} c_j^\dagger 
        + c_j^\dagger S_{ji} c_i^\dagger 
        + c_i^\dagger A_{ij} c_j^\dagger 
        + c_j^\dagger A_{ji} c_i^\dagger 
    \Big] \\
    &= \frac{1}{2} \Big[
        c_i^\dagger S_{ij} c_j^\dagger 
        - c_i^\dagger S_{ij} c_j^\dagger 
        + c_i^\dagger A_{ij} c_j^\dagger 
        - c_i^\dagger (-A_{ij}) c_j^\dagger 
    \Big] \\
    &= c_i^\dagger A_{ij} c_j^\dagger 
\end{align*}
$$

and similarly for its Hermitian conjugate. Only the anti-symmetric part contributes to $H_\text{BdG}$. $\blacksquare$

----

We then write $H_\text{BdG}$ in matrix form: 

$$
\begin{align*}
    c_i^\dagger H_{ij} c_j 
    &= \frac{1}{2} \Big[
        H_{ij} c_i^\dagger c_j 
        + H_{ij} (\delta_{ij} - c_j c_i^\dagger)
    \Big] \\
    &= \frac{1}{2} \Big[
        c_i^\dagger H_{ij} c_j 
        - c_i H_{ij}^\mathsf{T} c_j^\dagger
        + H_{ij} \delta_{ij}
    \Big] 
    \\ &\Downarrow \\
    H_\text{BdG} 
    &= \frac{1}{2} \sum_{i,j} \Big[
        c_i^\dagger H_{ij} c_j 
        - c_i H_{ij}^\mathsf{T} c_j^\dagger
        + c_i^\dagger B_{ij} c_j^\dagger 
        + c_i B^\dagger_{ij} c_j
        + H_{ij} \delta_{ij}
    \Big]
    \\
    &= \frac{1}{2} \sum_{ij} (c_i^\dagger, c_i)
    \begin{pmatrix}
        H_{ij} & B_{ij} \\ B^\dagger_{ij} & -H_{ij}^\mathsf{T}
    \end{pmatrix} \begin{pmatrix}
        c_j \\ c_j^\dagger
    \end{pmatrix} + \frac{1}{2} \operatorname{Tr} H
    \\
    &= \frac{1}{2} \Psi^\dagger
    \begin{pmatrix}
        H & B \\ B^\dagger & -H^\mathsf{T}
    \end{pmatrix} \Psi + \frac{1}{2} \operatorname{Tr} H
\end{align*}
$$

where we defined the vector

$$
\Psi = (c_1,...,c_N,c_1^\dagger,...,c_N^\dagger)^\mathsf{T}
$$

Later the symbol $H_\text{BdG}$ may refer only to the $2N \times 2N$ matrix

$$
H_\text{BdG} = \begin{pmatrix}
    H & B \\ B^\dagger & -H^\mathsf{T}
\end{pmatrix}
$$

## Diagonalization: Bogoliubov Transformation

To diagonalize $H_\text{BdG}$, we need its eigenvalues and eigenvectors:

$$
\begin{pmatrix}
    H & B \\ B^\dagger & -H^\mathsf{T}
\end{pmatrix} \begin{pmatrix}
    u_\alpha \\ v_\alpha
\end{pmatrix} = E_\alpha \begin{pmatrix}
    u_\alpha \\ v_\alpha
\end{pmatrix}
$$

- $\alpha = 1,...,2N$ labels the eigenvalues and eigenvectors of $H_\text{BdG}$.
- $u_\alpha, v_\alpha$ are $N$-dimensional vectors.
- Since $H_\text{BdG}$ is Hermitian:
    - All eigenvalues $E_\alpha$ are real.
    - All eigenvectors are orthogonal, i.e. $H_\text{BdG}$ can be diagonalized by a unitary matrix.

But due to the special structure of $H_\text{BdG}$, not all eigenvalues are unrelated: taking the complex conjugate of the above eigen-equation, we obtain

$$
\begin{align*}
    \begin{pmatrix}
        H^* & B^* \\ B^\mathsf{T} & -H^\dagger
    \end{pmatrix} \begin{pmatrix}
        u^*_\alpha \\ v^*_\alpha
    \end{pmatrix} &= E_\alpha \begin{pmatrix}
        u^*_\alpha \\ v^*_\alpha
    \end{pmatrix} 
    \\ &\Downarrow \\
    \begin{pmatrix}
        H^\mathsf{T} & -B^\dagger \\ -B & -H
    \end{pmatrix} \begin{pmatrix}
        u^*_\alpha \\ v^*_\alpha
    \end{pmatrix} &= E_\alpha \begin{pmatrix}
        u^*_\alpha \\ v^*_\alpha
    \end{pmatrix}
    \\ &\Downarrow \\
    \begin{pmatrix}
        -H & -B \\ -B^\dagger & H^\mathsf{T}
    \end{pmatrix} \begin{pmatrix}
        v^*_\alpha \\ u^*_\alpha
    \end{pmatrix} &= E_\alpha \begin{pmatrix}
        v^*_\alpha \\ u^*_\alpha
    \end{pmatrix}
\end{align*}
$$

In the second step we used

$$
\begin{array}{ccc}
    H = H^\dagger &\Rightarrow & H^* = H^\mathsf{T} 
    \\[0.3em]
    B = -B^\mathsf{T} &\Rightarrow & B^* = -B^\dagger
\end{array}
$$

This means that

<div class="result">
<center>

If $(u, v)^\mathsf{T}$ is an eigenvector of $H_\text{BdG}$ with eigenvalue $E$, <br> then $(v^*, u^*)^\mathsf{T}$ is also an eigenvector with eigenvalue $-E$.

</center>
</div><br>

To proceed, we make an important assumption:

<div class="result">
<center>

**All eigenvalues of $H_\text{BdG}$ are nonzero.**

</center>
</div><br>

Let $E_1,...,E_N$ be the positive eigenvalues of $H_\text{BdG}$. Then the eigen-decomposition (called **Bogoliubov transformation** in this context) of $H_\text{BdG}$ is given by:

$$
\begin{align*}
    U^{\dagger} H_\text{BdG} U 
    &= \operatorname{diag}(E_1,...,E_N,-E_1,...,-E_N)
    \\
    U &= \begin{pmatrix}
        u_1 & \cdots & u_N & v^*_1 & \cdots & v^*_N
        \\
        v_1 & \cdots & v_N & u^*_1 & \cdots & u^*_N
    \end{pmatrix}
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

*Remark*: Usually the $2N \times 2N$ matrix $H_\text{BdG}$ is already *block-diagonal* (e.g. in momentum representation). Then we can diagonalize each block separately.

</div><br>

### Bogoliubov Quasi-Particles

We define a new set of operators $a_\alpha, a_\alpha^\dagger$ related to the old $c_j, c_j^\dagger$ by the matrix $U$:

$$
\Phi = (a_1,...,a_N,a_1^\dagger,...,a_N^\dagger)^\mathsf{T}
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

Since $U$ is unitary, the new operators still satisfy the fermion anti-commutation rules. Now the BdG Hamiltonian can be diagonalized as

$$
\begin{align*}
    H_\text{BdG}
    &= \frac{1}{2} \Phi^\dagger U^\dagger
    \begin{pmatrix}
        H & B \\ B^\dagger & -H^\mathsf{T}
    \end{pmatrix} U \Phi 
    + \frac{1}{2} \operatorname{Tr} H
    \\
    &= \frac{1}{2} \sum_\alpha E_\alpha 
    (a_\alpha^\dagger a_\alpha - a_\alpha a_\alpha^\dagger)
    + \frac{1}{2} \operatorname{Tr} H
    \\
    &= \sum_\alpha E_\alpha a_\alpha^\dagger a_\alpha
    - \frac{1}{2} \sum_\alpha E_\alpha
    + \frac{1}{2} \sum_j \epsilon_j
\end{align*}
$$

where $\epsilon_j \ (j=1,...,N)$ are eigenvalues of $H$.

### BCS State


