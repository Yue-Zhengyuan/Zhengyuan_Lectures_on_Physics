# Heisenberg-like Spin Chain

Now we use Jordan-Wigner transformation to map the Hamiltonian $H^{A/P}$ of **Heisenberg-like models** to fermion Hamiltonian $H_F$. 

<div class="result">

**Heisenberg-like spin chain:**

- Local Hamiltonian and $\mathbb{Z}_2$ generator

    $$
    \begin{gather*}
        H_j = J_x S^x_j S^x_{j+1} + J_y S^y_j S^y_{j+1}
        + J_z S^z_j S^z_{j+1} - h S^z_j, \quad
        Z = \textstyle{\prod_{j=1}^N} Z_j
    \end{gather*}
    $$

- ABC boundary term

    $$
    \begin{align*}
        H^A_N &= Z_1 H_N Z_1 \\
        &= - J_x S^x_N S^x_1 - J_y S^y_N S^y_1 
        + J_z S^z_N S^z_1 - h S^z_N
    \end{align*}
    $$

</div><br>

<div class="remark">

*Remark*: Important special cases of Heisenberg-like models

- **(Isotropic) Heisenberg model**: $J_x = J_y = J_z, \ h = 0$
- **Transverse field Ising model**: $J_y = J_z = 0$; critical value $-2J_x = h$
- **XY model**: $J_z = 0$
- **XXZ model**: $J_x = J_y, \ h = 0$

</div><br>

It is convenient to express $H_j$ in terms of $S^\pm$: 

$$
S_j^{\pm} = S_j^x \pm i S_j^y 
\, \Rightarrow \, \left\{
\begin{align*}
    S_j^x &= \frac{1}{2}(S_j^- + S_j^+)
    \\
    S_j^y &= \frac{i}{2}(S_j^- - S_j^+)
\end{align*}
\right.
$$

The first two terms of $H_j$ can then be written as

$$
\begin{align*}
    &\frac{J_x}{4} (S_j^- + S_j^+)(S_{j+1}^- + S_{j+1}^+)
    - \frac{J_y}{4}(S_j^- - S_j^+)(S_{j+1}^- - S_{j+1}^+)
    \\
    &= t(S_j^+ S_{j+1}^- + S_j^- S_{j+1}^+)
    + \Delta (S_j^+ S_{j+1}^+ + S_j^- S_{j+1}^-)
    \\
    &\boxed{
        = t(S_j^+ S_{j+1}^- + h.c.)
        + \Delta (S_j^+ S_{j+1}^+ + h.c.)
    }
    \\[1em]
    &\text{with} \qquad 
    t \equiv \frac{J_x + J_y}{4}, \quad
    \Delta \equiv \frac{J_x - J_y}{4}
\end{align*}
$$

The mapping of $S^z$-terms is the same for all boundary conditions:

$$
S^z_j \to n_j - 1/2
$$

Next we focus on the transformation of the $t,\Delta$-terms, which will be affected by the boundary condition. The following identity will be useful:

$$
F_j F_{j+1} 
= \prod_{l=1}^{j-1} (-1)^{n_l} \prod_{l'=1}^{j} (-1)^{n_{l'}}
= (-1)^{n_j}
$$

## Non-Boundary Terms

- "Spin Hopping" $t$-Term

    $$
    \begin{align*}
        S_j^+ S_{j+1}^-
        &= c_j^\dagger F_j c_{j+1} F_{j+1}
        = c_j^\dagger c_{j+1} F_j F_{j+1}
        \\
        &= c_j^\dagger c_{j+1} (-1)^{n_j}
        \\
        &= c_j^\dagger c_{j+1} \quad
        (\text{$\ne 0$ only when input $n_j = 0$})
    \end{align*}
    $$

- "Spin Pairing" $\Delta$-Term

    $$
    \begin{align*}
        S_j^+ S_{j+1}^+
        &= c_j^\dagger F_j c_{j+1}^\dagger F_{j+1}
        = c_j^\dagger c_{j+1}^\dagger F_j F_{j+1}
        \\
        &= c_j^\dagger c_{j+1}^\dagger (-1)^{n_j} 
        = c_j^\dagger c_{j+1}^\dagger
    \end{align*}
    $$

    The last equality follows from the same argument as for the previous term. This term is related to the **$p$-wave superconductivity**.

<div class="result">

**Non-boundary term of fermion theory:** ($j = 1,...,N-1$)

$$
\begin{align*}
    (H_F)_j &= t(c_j^\dagger c_{j+1} + h.c.)
    + \Delta (c_j^\dagger c_{j+1}^\dagger + h.c.) 
    \\ &\quad
    + J_z (n_j - \tfrac{1}{2}) (n_{j+1} - \tfrac{1}{2})
    - h (n_j - \tfrac{1}{2})
\end{align*} \quad 
$$

</div><br>

## The Boundary Term $H_N$

Since the spin chain contains only nearest neighbor interaction, the only boundary term is $H_N$:

$$
H^{P/A}_N = \pm t(S_N^+ S_1^- + h.c.)
\pm \Delta (S_N^+ S_1^+ + h.c.) + J_z S^z_N S^z_1 - h S^z_N
$$

The $h$-term can be transformed ordinarily. We focus on $S_N S_1$-like terms:

$$
\begin{align*}
    S_N^+ S_1^{(\pm)} &= c_N^\dagger F_N c_1^{(\dagger)} \cancel{F_1}
    = c_N^\dagger F_N c_1^{(\dagger)} \\
    S_N^z S_1^z &= (n_N - 1/2)(n_1 - 1/2)
\end{align*}
$$

Introduce the the **fermion number parity** operator

$$
P \equiv (-1)^{n_\text{tot}} = \exp(i\pi n_\text{tot})
\quad \bigg( n_\text{tot} \equiv \sum_{l=1}^N n_l \bigg)
$$

Obviously $P^2 = 1$, so its eigenvalues are $\pm 1$ ($n_\text{tot}$ is even or odd). Then we express $F_N$ in terms of $P$: (using the anti-commutator $\{P, c_j^{(\dagger)}\} = 0$ for all $j$)

$$
\begin{align*}
    F_N &= F_N (-1)^{2n_N} = P (-1)^{n_N} \\ \Rightarrow
    S_N^+ S_1^{(\pm)} &= c_N^\dagger P (-1)^{n_N} c_1^{(\dagger)}
    \\
    &= c_N^\dagger P c_1^{(\dagger)} \qquad 
    (\ne 0 \ \text{only when input} \ n_N = 0)
    \\
    &= - c_N^\dagger c_1^{(\dagger)} P \qquad
\end{align*}
$$

Now we *require* that the boundary term of the fermion theory $(H_F)_N$ has the same form as the non-boundary term:
    
$$
\begin{align*}
    (H_F)_N &= t(c_N^\dagger c_{N+1} + h.c.)
    + \Delta (c_N^\dagger c_{N+1}^\dagger + h.c.) 
    \\ &\quad
    + J_z (n_j - \tfrac{1}{2}) (n_{j+1} - \tfrac{1}{2})
    - h \left(n_N - \tfrac{1}{2} \right)
    \\ &\Downarrow \\
    c_N^\dagger c_{N+1}^{(\dagger)} &\overset{\text{def}}{=}
    \mp c_N^\dagger c_1^{(\dagger)} P
\end{align*}
$$

where the upper/lower sign is for PBC/ABC spin chain. Since the Hamiltonian $H_F$ preserves fermion parity $[H_F,P] = 0$, we can divide the fermion Hilbert space into $P = \pm 1$ sectors. In each sector, we to define $c_{N+1}$ (i.e. choose the boundary condition for the fermion theory) as:

<div class="result">

**Boundary condition of fermion theory:**

$$
\begin{array}{ccc}
    \text{Spin BC} & \begin{gathered}
        \text{Fermion} \\ \text{Parity} \ P
    \end{gathered} & c_{N+1}^{(\dagger)} & \text{Fermion BC}
    \\[4pt] \hline \\[-8pt]
    \text{Periodic} & +1 & -c_1 & \text{Anti-Periodic}
    \\[0.4em]
    & -1 & +c_1 & \text{Periodic}
    \\[4pt] \hline \\[-8pt]
    \text{Anti-Periodic} & +1 & +c_1 & \text{Periodic}
    \\[0.4em]
    & -1 & -c_1 & \text{Anti-Periodic}
\end{array}
$$

</div><br>

With this definition, the number operator $n_{N+1}$ in any sector is 

$$
n_{N+1} = c_{N+1}^\dagger c_{N+1} = (\pm 1)^2 c_1^\dagger c_1 = n_1
$$

which still satisfies PBC. The fermion Hamiltonian for *both* PBC and ABC are therefore the *same*:

<div class="result">

**Hamiltonian of the fermion theory:**

$$
\begin{align*}
    H_F &= \sum_{j=1}^N \Big[
        t(c_j^\dagger c_{j+1} + h.c.)
        + \Delta (c_j^\dagger c_{j+1}^\dagger + h.c.) 
        \\ &\qquad \quad
        + J_z (n_j - \tfrac{1}{2}) (n_{j+1} - \tfrac{1}{2})
        - h (n_j - \tfrac{1}{2})
    \Big]
\end{align*}
$$

</div><br>

<div class="remark">

*Remark*: The boundary conditions for the fermion theory are usually called:

- PBC: **Ramond (R) sector**
- ABC: **Neveu-Schwarz (NS) sector**

</div><br>

This leads to:

<div class="result">

**Relation between spin theory $H^{A/P}$ and fermion theory $H_F$:**

$$
\begin{align*}
    H^P &= \frac{1+P}{2} H_F^{(A)} + \frac{1-P}{2} H_F^{(P)}
    \\
    H^A &= \frac{1-P}{2} H_F^{(A)} + \frac{1+P}{2} H_F^{(P)}
\end{align*}
$$

where $H_F^{(A/P)}$ refers to $H_F$ with ABC/PBC. 

</div><br>
