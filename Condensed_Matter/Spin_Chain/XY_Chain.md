# XY Spin Chain

*Reference*:

- Lieb, E., Schultz, T., & Mattis, D. (1961). Two soluble models of an antiferromagnetic chain. Annals of Physics, 16(3), 407-466.
- Parkinson, J. B., & Farnell, D. J. (2010). An introduction to quantum spin systems (Vol. 816). Springer.
- Bernevig, B. A. (2013). Topological insulators and topological superconductors. Princeton university press.

<div class="result">

**XY spin chain:**

- Non-boundary local spin Hamiltonian
    
    $$
    \begin{align*}
        H_j &= J_x S^x_j S^x_{j+1} + J_y S^y_j S^y_{j+1} - h S^z_j \\
        &= t(S_j^+ S_{j+1}^- + h.c.)
        + \Delta (S_j^+ S_{j+1}^+ + h.c.) - h S^z_j
        \\[0.7em] &\text{with} \quad
        t \equiv \frac{J_x + J_y}{4}, \quad
        \Delta \equiv \frac{J_x - J_y}{4}
    \end{align*}
    $$

- Fermion Hamiltonian
    
    $$
    \begin{align*}
        H_F &= \sum_{j=1}^N \Big[
            t(c_j^\dagger c_{j+1} + h.c.)
            + \Delta (c_j^\dagger c_{j+1}^\dagger + h.c.) 
            - h (n_j - \tfrac{1}{2})
        \Big]
    \end{align*}
    $$

    The PBC and ABC of the fermion chain correspond to $c_{N+1} = \pm c_1$, respectively.

</div><br>

From now on we omit the subscript F of the fermion Hamiltonian. In addition, one usually introduce the **anisotropy parameter** $\gamma$, and fix the scale of $H$ by another parameter $J$

$$
\begin{gather*}
    J_x = J(1+\gamma), \quad J_y = J(1-\gamma)
    \\[0.3em] \Rightarrow
    t = \frac{J}{2}, \quad \Delta = \frac{J\gamma}{2}
\end{gather*}
$$

## Momentum Representation

To obtain the energy levels, we shall go to the momentum space:

$$
c_j = \frac{1}{\sqrt{N}} \sum_k c_k e^{ikx_j}, \quad
x_j = ja
$$

We transform the Hamiltonian term by term:

- Tight-binding term

    $$
    \begin{align*}
        & t \sum_j (c_j^\dagger c_{j+1} + h.c.)
        = \frac{t}{N} \sum_j 
        \sum_{k,p} (
            c_k^\dagger e^{-ikja} c_p e^{ip(j+1)a}
            + h.c.
        )
        \\
        &= t \sum_{k,p} \bigg[
            c_k^\dagger c_p e^{ipa} \delta_{k-p}
            + h.c.
        \bigg]
        = t \sum_k c_k^\dagger c_k
        (e^{ika} + e^{-ika})
        \\
        &= \boxed{
            2t \sum_k c_k^\dagger c_k \cos(ka)
        }
    \end{align*}
    $$

- $p$-Wave potential term

    $$
    \begin{align*}
        & \Delta \sum_j (c_j^\dagger c_{j+1}^\dagger + h.c.) 
        = \frac{\Delta}{N} \sum_j 
        \sum_{k,p} (
            c_k^\dagger e^{-ikja} c_p^\dagger e^{-ip(j+1)a}
            + h.c.
        )
        \\
        &= \Delta \sum_{k,p} \bigg[
            c_k^\dagger c_p^\dagger e^{-ipa} \delta_{k+p}
            + h.c.
        \bigg]
        = \boxed{
            \Delta \sum_k (
                c_k^\dagger c_{-k}^\dagger e^{ika}
                + c_{-k} c_k e^{-ika}
            )
        }
    \end{align*}
    $$

- Chemical potential term (omitting the constants)

    $$
    \begin{align*}
        & -h \sum_j n_j
        = -h \sum_j c_j^\dagger c_j
        = -\frac{h}{N} \sum_j \sum_{k,p}
        c_k^\dagger e^{-ikja} c_p e^{ipja}
        \\
        &= -h \sum_{k,p} c_k^\dagger c_p \delta_{k-p}
        = \boxed{
            -h \sum_k c_k^\dagger c_k 
        }
    \end{align*}
    $$

Thus (define $\epsilon_k = 2t\cos(ka) - h$)

$$
H = \sum_k \Big[
    \epsilon_k c_k^\dagger c_k
    + \Delta (
        c_k^\dagger c_{-k}^\dagger e^{ika}
        + c_{-k} c_k e^{-ika}
    )
\Big]
$$

### Bogoliubov-de-Gennes (BdG) Hamiltonian

To diagonalize the Hamiltonian, we define the vector

$$
\Psi_k = (c_k, c_{-k}^\dagger)^\mathsf{T}
\Rightarrow \Psi_k^\dagger = (c_k^\dagger, c_{-k})
$$

and put $H$ into matrix form (**Bogoliubov-de-Gennes (BdG) formalism**): 

$$
H = \frac{1}{2} \sum_k \Psi_k^\dagger H^\text{BdG}_k \Psi_k
+ (\text{Possible constant})
$$

The $1/2$ factor will be explained later. To read off the matrix $H_\text{BdG}$ from $H$, we *should first symmetrize for momenta $k, -k$*: 

- The already-diagonalized term becomes (note that $\epsilon_k = \epsilon_{-k}$)

    $$
    \sum_k \epsilon_k c_k^\dagger c_k
    = \frac{1}{2} \sum_k \epsilon_k 
    (c_k^\dagger c_k + c_{-k}^\dagger c_{-k})
    $$

- The fermion pairing term becomes

    $$
    \begin{align*}
        &\Delta \sum_k (
            c_k^\dagger c_{-k}^\dagger e^{ika}
            + c_{-k} c_k e^{-ika}
        ) \\ 
        &= \frac{\Delta}{2} \sum_k \Big[
            (
                c_k^\dagger c_{-k}^\dagger e^{ika}
                + c_{-k} c_k e^{-ika}
            ) + (
                c_{-k}^\dagger c_{k}^\dagger e^{-ika}
                + c_{k} c_{-k} e^{+ika}
            )
        \Big] \\
        &= \frac{\Delta}{2} \sum_k \Big[
            c_k^\dagger c_{-k}^\dagger 
            (e^{ika} - e^{-ika}) 
            + c_{k} c_{-k} (e^{ika} - e^{-ika})
        \Big] \\
        &= i\Delta \sin ka (c_k^\dagger c_{-k}^\dagger + c_{k} c_{-k})
    \end{align*}
    $$

    <div class="remark">

    *Remark*: In this calculation, if the factors $e^{ika}$ were absent (corresponding to $k$-independent (**s-wave**) pairing potential), we would obtain
    
    $$
    \sum_k c_{-k} c_k
    = \frac{1}{2} \sum_k (c_{-k} c_k + c_k c_{-k}) = 0
    $$

    and similarly the $\sum_k c^\dagger_{k} c^\dagger_{-k} = 0$.
    Therefore the spinless fermion model does not support s-wave superconductivity.

    </div><br>

Thus the symmetrized Hamiltonian we should use is

$$
\begin{align*}
    H &= \frac{1}{2} \sum_k \Big[
        \epsilon_k (c_k^\dagger c_k + c_{-k}^\dagger c_{-k})
        + 2i\Delta (c_k^\dagger c_{-k}^\dagger - c_{-k} c_k) \sin ka
    \Big] \\
    &= \frac{1}{2} \sum_k \Big[
        \epsilon_k (c_k^\dagger c_k - c_{-k} c_{-k}^\dagger)
        + 2i\Delta (c_k^\dagger c_{-k}^\dagger - c_{-k} c_k) \sin ka
    \Big] + \frac{1}{2} \sum_k \epsilon_k
\end{align*}
$$

Thus the bilinear part is given by the matrix

$$
H^\text{BdG}_k = \begin{pmatrix}
    \epsilon_k & 2i\Delta \sin ka \\
    -2i\Delta \sin ka & -\epsilon_k
\end{pmatrix}
$$

The matrix $H_\text{BdG}$ is Hermitian, and can be diagonalized by a unitary matrix $U$:

$$
U_k^{\dagger} H^\text{BdG}_k U_k
= \Lambda_k \equiv \begin{pmatrix}
    E_k & \\ & -E_k
\end{pmatrix}
$$

<div class="result">

**Eigenvalues of BdG Hamiltonian:**

$$
\pm E_k = \pm \sqrt{\epsilon_k^2 + (2\Delta \sin ka)^2}, \quad
\epsilon_k = 2t\cos(ka) - h
$$

In terms of parameters $J,\gamma$:

$$
\pm E_k = \pm \sqrt{\epsilon_k^2 + (J\gamma \sin ka)^2}, \quad
\epsilon_k = J\cos(ka) - h
$$

</div><br>

### Finding the Unitary Matrix $U_k$

The special form of $H^\text{BdG}_k$ impose additional constraints on the unitary matrix $U_k$. Consider a general matrix 

$$
A = \begin{pmatrix}
    a & ib \\ -ib & -a
\end{pmatrix} \qquad (a, b \in \R)
$$

In $H^\text{BdG}_k$, we have $a = \epsilon_k, \ b = 2\Delta\sin ka$. 

If $(u,v)^\mathsf{T} \ (u,v\in \mathbb{C})$ is an eigenvector with eigenvalue $E \in \R$:

$$
\begin{align*}
    \begin{pmatrix}
        a & ib \\ -ib & -a
    \end{pmatrix} \begin{pmatrix}
        u \\ v
    \end{pmatrix} &= E \begin{pmatrix}
        u \\ v
    \end{pmatrix}
    \\ &\Downarrow \\
    \underbrace{\begin{pmatrix}
        -a & -ib \\ ib & a
    \end{pmatrix}}_{-A} \begin{pmatrix}
        v \\ u
    \end{pmatrix} &= E \begin{pmatrix}
        v \\ u
    \end{pmatrix}
\end{align*}
$$

then $(v,u)^\mathsf{T}$ is also an eigenvector with eigenvalue $-E$ (this explains why the energy eigenvalues come in pairs). 

When $E \ne 0$ (which is the case for $H^\text{BdG}_k$), we have then found all eigenvectors of it; the matrix $U$ diagonalizing $A$ is therefore

$$
U = \begin{pmatrix}
    u & v \\ v & u
\end{pmatrix}
$$

Unitarity of $U$ further imposes 3 constrains

$$
|u^2| + |v^2| = 1, \quad
u^* v + v^* u = 0
$$

The second equation contains two constrains (real and imaginary parts). Therefore, there is only 1 free real parameter in $U$. Without loss of generality, assume $u$ is *real and positive* (since eigenvectors are determined up to a normalization factor). The second equation then implies

$$
u(v + v^*) = 0 \ \Rightarrow \ 
(u = 0) \ \text{or} \ (\text{$v$ is purely imaginary})
$$

The case $u = 0$ (and therefore $|v| = 1$) requires $b = 0$, so we do not consider it. Therefore, we can re-parametrize $u, v$ as

$$
u = \cos \theta, \quad v = i\sin \theta \quad (\theta \in \R)
$$

The matrix $U_k$ for $H^\text{BdG}_k$ then has the form (we pick out the $i$ factor from $v$, so that both $u, v$ are real)

$$
U_k = \begin{pmatrix}
    u_k & iv_k \\
    iv_k & u_k
\end{pmatrix}, \quad
\begin{cases}
    u_k = \cos \theta_k \\
    v_k = \sin \theta_k
\end{cases} \quad (\theta_k \in \R)
$$

In addition, we can determine the relation between $U_k$ and $U_{-k}$:

$$
H^\text{BdG}_{-k} = (H^{\text{BdG}}_k)^*
\Rightarrow U_{-k} = U_k^*
\Rightarrow \begin{cases}
    u_{-k} = u_k \\
    v_{-k} = -v_k
\end{cases}
$$

### Quasi-Particles

We then define a new set of operators (**Bogoliubov quasi-particles**) as

<div class="result">

**Bogoliubov quasi-particles $a_k, a_k^\dagger$ (fermions):**

$$
\begin{pmatrix}
    c_k \\ c_{-k}^\dagger
\end{pmatrix} = U_k \begin{pmatrix}
    a_k \\ a_{-k}^\dagger
\end{pmatrix} = \begin{pmatrix}
    u_k a_k + iv_k a_{-k}^\dagger \\
    iv_k a_k + u_k a_{-k}^\dagger
\end{pmatrix}
$$

</div><br>

Since $U_k$ is unitary, $a_k, a_k^\dagger$ also satisfy the fermion anti-commutation rules. Thus these new particles are still fermions.

<div class="remark">

*Remark*: Let us check the self-consistency of this transformation. From the first line 

$$
\begin{align*}
    c_{-k}^\dagger 
    &= u_{-k} a_{-k}^\dagger - i v_{-k} a_k \\
    &= u_{k} a_{-k}^\dagger + i v_{k} a_k
\end{align*}
$$

which agrees with the second line. 

</div><br>

The diagonalized Hamiltonian is (note that $E_k = E(-k)$) 

$$
\begin{align*}
    H &= \frac{1}{2} \sum_k \Psi_k^\dagger H^\text{BdG}_k \Psi_k
    + \frac{1}{2} \sum_k \epsilon_k
    \\
    &= \frac{1}{2} \sum_k (a_k^\dagger, a_{-k})
    U^\dagger H^\text{BdG}_k U \begin{pmatrix}
        a_k \\ a_{-k}^\dagger
    \end{pmatrix} 
    + \frac{1}{2} \sum_k \epsilon_k \\
    &= \frac{1}{2} \sum_k (a_k^\dagger, a_{-k})
    \begin{pmatrix}
        E_k & \\ & -E_k
    \end{pmatrix} \begin{pmatrix}
        a_k \\ a_{-k}^\dagger
    \end{pmatrix} + \frac{1}{2} \sum_k \epsilon_k
    \\
    &= \frac{1}{2} \sum_k E_k (
        a_k^\dagger a_k
        - a_{-k} a_{-k}^\dagger
    ) + \frac{1}{2} \sum_k \epsilon_k
    \\
    &= \frac{1}{2} \sum_k E_k (
        a_k^\dagger a_k
        + a_{-k}^\dagger a_{-k} 
    ) - \frac{1}{2} \sum_k (E_k - \epsilon_k)
    \\
    &= \sum_k E_k a_k^\dagger a_k
    + \frac{1}{2} \sum_k (\epsilon_k - E_k)
\end{align*}
$$

Now we see the reason of introducing the $1/2$ factor; it makes the eigenvalues $E_k$ of $H_\text{BdG}$ directly equal to the quasi-particle energy. 

