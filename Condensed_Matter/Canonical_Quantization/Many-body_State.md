# Many-Body State for Identical Particles

Consider a system of $N$ particles (not necessarily identical). Suppose each particle has one-body Hilbert space $\mathcal{H}_k$ ($k = 1, ..., N$), and the interaction between the particles does not destroy it. Then the full Hilbert space for the system is

$$
\mathcal{H}(N) = \mathcal{H}_1 \otimes \cdots
\otimes \mathcal{H}_N
$$

If particle 1 is in state $\ket{\psi_1} \in \mathcal{H}_1$, ..., particle $N$ is in state $\ket{\psi_N} \in \mathcal{H}_N$, then the whole system is in the state

$$
\ket{\psi} \equiv \ket{\psi_1,...,\psi_N} 
= \ket{\psi_1} \otimes \cdots \otimes \ket{\psi_N}
$$

<div class="remark">

In the traditional wave function representation, we are in fact taking the inner product of $\ket{\psi}$ with the position eigenstate 

$$
\begin{align*}
    \ket{x} \equiv \ket{x_1,...,x_N} 
    &= \ket{x_1} \otimes \cdots \otimes \ket{x_N}
    \\ &\Downarrow \\
    \psi(x_1,...,x_N)
    & \equiv \braket{x_1,...,x_N}{\psi_1,...,\psi_N}
    \\
    &= \braket{x_1}{\psi_1} \cdots \braket{x_N}{\psi_N}
    \\
    &= \psi_1(x_1) \cdots \psi_N(x_N)
\end{align*}
$$

</div><br>

## Particle Relabelling (Exchange)

If the $N$ particles are identical, we have

$$
\mathcal{H}_1 = \cdots = \mathcal{H}_N \equiv \mathcal{H}
\, \Rightarrow \,
\mathcal{H}(N) = \otimes^N \mathcal{H}
$$

For such a system, relabelling the particles should not change the many-body state except for some additional phase factors. The operation of relabelling is accomplished by 

<div class="result">

**The permutation operator $P_\sigma$:**

$$
P_\sigma \ket{\psi_1,...,\psi_N}
= \ket{\psi_{\sigma(1)}, ..., \psi_{\sigma(N)}}, \quad
\sigma \in S_N
$$

</div><br>

i.e. the names of the particles are changed from $\sigma(1),...,\sigma(N)$ to $1,...,N$. 

<div class="remark">

*Remark*: For the special case when $\sigma$ is just an exchange of two particles $i \ne j$, the permutation operator will simply be denoted by $P_{ij}$:

$$
P_{ij} \ket{...,\psi_i,...,\psi_j,...}
= \ket{...,\psi_j,...,\psi_i,...}
$$

</div><br>

## State Symmetrization

To construct relabelling-independent many-body states, we need 

<div class="result">

**The anti-/symmetrization operators $S_\pm(N)$:**

$$
S_\pm(N) \equiv \frac{1}{N!} 
\sum_{\sigma \in S_N} (\pm 1)^\sigma P_\sigma
$$

</div><br>

The $1/N!$ factor is an average over all permutations, and $(-1)^\sigma$ refers to the parity of the permutation $\sigma$. The particle number is usually omitted when there is no ambiguity. The symmetrized state will be denoted as

$$
\ket{\psi_\pm} \equiv \ket{(\psi_1,...,\psi_N)_\pm}
= S_\pm(N) \ket{\psi_1,...,\psi_N}
$$

- **Boson**: exchanging two particles leaves the state unchanged
    
    $$
    P_{ij} \ket{\psi_+} = \ket{\psi_+}
    $$

- **Fermion**: exchanging two particles produces a minus sign

    $$
    P_{ij} \ket{\psi_-} = -\ket{\psi_-}
    $$

These symmetrized states $\ket{\psi_\pm}$ are in general not normalized. 

### Properties of $S_\pm(N)$

- $P_\sigma S_\pm = S_\pm P_\sigma = (\pm 1)^\sigma S_\pm$

- $S_\pm^\dagger = S_\pm$ (self-adjoint/Hermitian)

- $S_\pm^2 = S_\pm$ (is a projection operator)

### Inner Product of Symmetrized States

Using the property $S_\pm^2 = S_\pm$, we calculate the inner product of two $N$-body symmetrized states

$$
\begin{align*}
    \braket{u_\pm}{v_\pm} 
    &\equiv \amp{u_1,...,u_N}{S_\pm^2}{v_1,...,v_N}
    \\
    &= \amp{u_1,...,u_N}{S_\pm}{v_1,...,v_N}
    \\
    &= \frac{1}{N!} \sum_{\sigma \in S_N} (\pm 1)^\sigma
    \amp{u_1,...,u_N}{P_\sigma}{v_1,...,v_N}
    \\
    &= \frac{1}{N!} \sum_{\sigma \in S_N} (\pm 1)^\sigma
    \braket{u_1,...,u_N}{v_{\sigma(1)},...,v_{\sigma(N)}}
\end{align*}
$$

In matrix notation:

<div class="result">

**Inner product of symmetrized states:**

$$
\braket{u_\pm}{v_\pm} = \frac{1}{N!} D_\pm \begin{bmatrix}
    \braket{u_1}{v_1} & \cdots & \braket{u_1}{v_N} \\
    \vdots & & \vdots \\
    \braket{u_N}{v_1} & \cdots & \braket{u_N}{v_N}
\end{bmatrix}
$$

where $D_+$ is the matrix *permanent*, and $D_-$ is the matrix *determinant*. 

</div><br>

<div class="remark">

*Remark*: When $\bra{u_\pm}$ is the symmetrized position state $\bra{x_\pm}$, we recover the symmetrized wave function $v_\pm(x)$ of the state $\ket{v_\pm}$. 

</div><br>

## The Occupation Number (Fock) Basis

It is usually to choose a set of orthonormal basis $\{\ket{r}\} \, (r = 1,2,...)$ for the one-body Hilbert space $\mathcal{H}$. The one-particle wave function of the $r$th state is denoted as

$$
\phi_r(x) = \braket{x}{r} \qquad
r = 1,2,...
$$

Let us denote the basis state occupied by particle $i$ as $\ket{r_i}$. Then the product states

$$
\ket{r_1,...,r_N} \equiv 
\ket{r_1} \otimes \cdots \otimes \ket{r_N}
\quad
(\ket{r_i} \in \{\ket{r}\} ; \, i = 1,...,N)
$$

naturally form an orthonormal basis for the $N$-body Hilbert space $\mathcal{H}(N)$.

For a system of identical particles, only the anti-/symmetrized states are allowed. These states form a *subspace* $\mathcal{H}(N)_\pm$ of the original Hilbert space $\mathcal{H}(N)$. 

The symmetrized subspace can be described by another set of basis, called the **occupation number basis**. If the system has $N_r$ particles in state $\ket{r} \, (r = 1,2,...)$, then the corresponding basis state (for bosons or fermions, respectively) is

$$
\begin{align*}
    \ket{N_1,N_2,...} &\equiv \text{const} \times 
    S_\pm(N) \ket{r_1,...,r_N}
    \\
    &= \text{const} \times \ket{(r_1,...,r_N)_\pm}
\end{align*}
$$

In this definition, we conventionally set $r_1 \le \cdots \le r_N$. Obviously, $N_1 + N_2 + \cdots = N$, and

$$
\begin{align*}
    \text{Bosons: } &\quad 0 \le N_r \le N \\
    \text{Fermions: } &\quad 0 \le N_r \le 1
\end{align*}
$$

By definition, two Fock basis states $\ket{N_1,N_2,...}$ and $\ket{N'_1, N'_2,...}$ are orthogonal if $N_r \ne N'_r$ for any $r$. To make the Fock basis *orthonormal*, we will determine the constant (normalization factor) below.

### Normalization of the Fock Basis

Calculate the inner product:

$$
\begin{align*}
    &\braket{N_1,N_2,...}{N_1,N_2,...}
    \\
    &= \frac{\text{const}^2}{N!}
    \sum_{\sigma \in S_N} (\pm 1)^\sigma
    \braket{r_1}{r_{\sigma(1)}} \cdots
    \braket{r_N}{r_{\sigma(N)}}
\end{align*}
$$

The the orthonormal condition for the states $\ket{r}$ means that $\braket{r_i}{r_{\sigma(i)}} = 1$ only when the particles $i$ and $\sigma(i)$ are in the same state; otherwise it is 0. In other words, the permutations that have nonzero contribution to the state norm can only shuffle particles in the same state. The number of such commutations is then $N_1! \times N_2! \times \cdots$. Then for bosons, we have

$$
\frac{\text{const}^2}{N!}
N_1! N_2! \cdots \overset{!}{=} 1
$$

For fermions, things are even simpler. Since each state can at most have one particle, only the identity permutation contributes. Then

$$
\frac{\text{const}^2}{N!} \overset{!}{=} 1
$$

Since $N_r = 0,1$ for fermions (then $N_r!$ is always 1), we can combine the two cases and simply write

<div class="result">

**The Fock (occupation number) basis:**

$$
\ket{N_1,N_2,...} \equiv 
\sqrt{\frac{N!}{N_1! N_2! \cdots}}
\ket{(r_1,...,r_N)_\pm}
$$

</div><br>
