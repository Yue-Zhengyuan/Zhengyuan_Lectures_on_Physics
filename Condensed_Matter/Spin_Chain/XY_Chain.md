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

</div><br>

From now on we omit the subscript F of the fermion Hamiltonian. In addition, one usually introduced the **anisotropy parameter** $\gamma$, and fix the scale of $H$ by setting

$$
\begin{gather*}
    J_x = 1+\gamma, \quad J_y = 1-\gamma
    \\[0.7em] \Rightarrow
    t = \frac{1}{2}, \quad \Delta = \frac{\gamma}{2}
\end{gather*}
$$

## Boundary Terms in Fermion Hamiltonian



## Hamiltonian in Momentum Space

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
        \\
        &= \frac{t}{N} \sum_j 
        \sum_{k,p} (
            c_k^\dagger e^{-ikja} c_p e^{ip(j+1)a}
            + h.c.
        )
        \\
        &= t \sum_{k,p} \bigg[
            c_k^\dagger c_p e^{ipa} \delta_{k-p}
            + h.c.
        \bigg]
        \\
        &= t \sum_k c_k^\dagger c_k
        (e^{ika} + e^{-ika})
        = 2t \sum_k c_k^\dagger c_k \cos(ka)
    \end{align*}
    $$

- $p$-Wave potential term

    $$
    \begin{align*}
        & \Delta \sum_j (c_j^\dagger c_{j+1}^\dagger + h.c.) 
        \\
        &= \frac{\Delta}{N} \sum_j 
        \sum_{k,p} (
            c_k^\dagger e^{-ikja} c_p^\dagger e^{-ip(j+1)a}
            + h.c.
        )
        \\
        &= \Delta \sum_{k,p} \bigg[
            c_k^\dagger c_p^\dagger e^{-ipa} \delta_{k+p}
            + h.c.
        \bigg]
        \\
        &= \Delta \sum_k (
            c_k^\dagger c_{-k}^\dagger e^{ika}
            + c_{-k} c_k e^{-ika}
        )
    \end{align*}
    $$

    This term can be processed further: by writing $e^{ika} = \cos ka + i \sin ka$ and relabelling $k \to -k$ for some terms, we obtain

    $$
    \begin{align*}
        &\sum_k c_k^\dagger c_{-k}^\dagger (\cos ka + i \sin ka) \\
        &= \frac{1}{2} \sum_k \Big[
            (
                c_k^\dagger c_{-k}^\dagger 
                + c_{-k}^\dagger c_{k}^\dagger
            ) \cos ka + i (
                c_k^\dagger c_{-k}^\dagger 
                - c_{-k}^\dagger c_{k}^\dagger
            ) \sin ka
        \Big] \\
        &= i \sum_k c_k^\dagger c_{-k}^\dagger \sin ka
        + \text{const}
        \\
        &\sum_k c_{-k} c_k e^{-ika} \\
        &= \frac{1}{2} \sum_k \Big[
            (c_{-k} c_k + c_{k} c_{-k}) \cos ka 
            - i (c_{-k} c_k - c_{k} c_{-k}) \sin ka
        \Big] \\
        &= -i \sum_k c_{-k} c_k \sin ka + \text{const}
    \end{align*}
    $$

    where we used anti-commutation of $c$ operators. Therefore

    $$
    \Delta \sum_j (c_j^\dagger c_{j+1}^\dagger + h.c.)
    = i\Delta \sum_k 
    (c_k^\dagger c_{-k}^\dagger - c_{-k} c_k) \sin ka
    $$

- Chemical potential term (omitting the constants)

    $$
    \begin{align*}
        & -h \sum_j n_j
        = -h \sum_j c_j^\dagger c_j
        \\
        &= -\frac{h}{N} \sum_j \sum_{k,p}
        c_k^\dagger e^{-ikja} c_p e^{ipja}
        \\
        &= -h \sum_{k,p} c_k^\dagger c_p \delta_{k-p}
        = -h \sum_k c_k^\dagger c_k 
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

### Bogoliubov-de-Gennes (BdG) Formalism

To diagonalize the Hamiltonian, we put $H$ into matrix form (**Bogoliubov-de-Gennes (BdG) formalism**): first symmetrize $c_k, c_{-k}$ operators (note that $\epsilon_k = \epsilon_{-k}$)

$$
H = \frac{1}{2} \sum_k \Big[
    \epsilon_k (c_k^\dagger c_k + c_{-k}^\dagger c_{-k})
    + 2\Delta (
        c_k^\dagger c_{-k}^\dagger e^{ika}
        + c_{-k} c_k e^{-ika}
    )
\Big]
$$

Then up to some constants (due to commutation of $c$ operators):

$$
\begin{align*}
    H &= \frac{1}{2} \sum_k (c_k^\dagger, c_{-k}) H_\text{BdG}(k) 
    \begin{pmatrix}
        c_k \\ c_{-k}^\dagger
    \end{pmatrix} \\
    H_\text{BdG} &= \begin{pmatrix}
        \epsilon_k & 2\Delta e^{ika} \\
        2\Delta e^{-ika} & -\epsilon_k
    \end{pmatrix} \ \text{or} \ \begin{pmatrix}
        \epsilon_k & 2i\Delta \sin ka \\
        -2i\Delta \sin ka & -\epsilon_k
    \end{pmatrix}
\end{align*}
$$

<div class="remark">

*Remark*: The first expression of $H_\text{BdG}$ can be decomposed using the Pauli matrices:

$$
H_\text{BdG} = (2\Delta \cos ka) \sigma^x 
- (2\Delta \sin ka) \sigma^y + \epsilon_k \sigma^z
$$

The $\sigma^x$ term has no physical contribution:

$$
\begin{align*}
    &\sum_k (c_k^\dagger, c_{-k}) \, \sigma^x \begin{pmatrix}
        c_k \\ c_{-k}^\dagger
    \end{pmatrix} 
    = \sum_k (c_k^\dagger c_{-k}^\dagger + c_{-k} c_k) \\
    &= \frac{1}{2} \sum_k (
        c_k^\dagger c_{-k}^\dagger + c_{-k}^\dagger c_{k}^\dagger 
        + c_{-k} c_k + c_{k} c_{-k}
    ) = \text{const}
\end{align*}
$$

Then we arrive at the second expression of $H_\text{BdG}$.

</div><br>

The matrix $H_\text{BdG}$ is Hermitian, and can be diagonalized by a unitary transformation, which preserve fermion anti-commutation rules:


