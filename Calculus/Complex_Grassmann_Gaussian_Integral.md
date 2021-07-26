# Grassmann Gaussian Integral

We start from the simplest case: the Gaussian integral with one pair of Grassmann variable and its "conjugate" (they are in fact independent).

<div class="result">

**Complex Grassmann Gaussian integral (one variable-pair):**

- Generating function
    
    $$
    Z(\bar{J}, J)
    = \int d\bar{\psi} \, d\psi  
    \exp (-\bar{\psi}a \psi +\bar{\psi}J +\bar{J}\psi )
    $$

    - $a$ is a *complex* number.
    - $(\psi, \bar{\psi})$, as well as $(J, \bar{J})$ (the **sources**), are independent Grassmann numbers.

- Integration result
    
    $$
    \begin{align*}
        Z(0,0) &= a \\
        \frac{Z(\bar{J}, J) }{Z(0,0)}
        &= \exp (\bar{J} a^{-1}J )
        \equiv \mathcal{Z}(\bar{J}, J)
    \end{align*}
    $$

</div><br>

*Proof*:

Since $\psi^n = 0 \  (n \ge 2)$ for any Grassmann number $\psi$, we can expand the exponential function as

$$
\begin{align*}
    \exp (-\bar{\psi}a \psi +\bar{\psi}J +\bar{J}\psi )
    = 1 - \bar{\psi}a \psi 
    + \bar{\psi}J + \bar{J}\psi 
    + \bar{\psi}J \bar{J}\psi
\end{align*}
$$

Only terms containing both $\psi$ and $\bar{\psi}$ can survive the integration. Therefore

$$
\begin{align*}
    Z(\bar{J}, J)
    &= \int d\bar{\psi} \, d\psi (
        -\bar{\psi}a \psi +\bar{\psi}J  \bar{J}\psi 
    )
    \\
    &= \int d\bar{\psi} \, d\psi 
    (\psi  a \bar{\psi}-\psi  \bar{\psi} J  \bar{J})
    \quad \text{(Integration order matters)}
    \\
    &= a - J \bar{J}
    = a (1 + \bar{J} a^{-1} J)
    \\
    &= a \exp (\bar{J} a^{-1}J )
    \quad \blacksquare
\end{align*}
$$

Now we generalize the result above to the $n$-pair case

<div class="result">

**Complex Grassmann Gaussian integral (multiple variable-pair):**

- Generating Function

    $$
    \begin{align*}
        Z(\bar{J}, J)
        &= \int D\bar{\psi} \, D\psi 
        \exp (
            -\bar{\psi}_i A_{ij} \psi_j
            + \bar{\psi}_i J_i 
            + \bar{J}_j \psi_j
        )
        \\
        &= \int D\bar{\psi} \, D\psi 
        \exp (
            -\bar{\psi} A \psi 
            + \bar{\psi} J + \bar{J} \psi 
        )
        \\
        \text{with} \quad &
        D\bar{\psi} \, D\psi
        = \prod_{k=1}^n \left(d\bar{\psi}_kd\psi_k\right)
    \end{align*}
    $$

    - $A$ is an $n\times n$ *Hermitian* matrix. 
    - $J$ is an $n$-dimensional column vectors of Grassmann numbers (the **source**).
    - When a bar is added on a column vector, it is "conjugated" and transposed to a row vector (similar to the Hermitian conjugation $\dagger$). 

- Integration result

    $$
    \begin{align*}
        Z(0,0) &= \det A
        \\
        \frac{Z(\bar{J}, J)}{Z(0,0)}
        &= \exp(
            \bar{J}_i [A^{-1}]_{ij} J_j
        )
        % = \prod_{i,j=1}^n 
        % (1 + \bar{J}_i [A^{-1}]_{ij} J_j)
        \equiv \mathcal{Z}(\bar{J}, J)
    \end{align*}
    $$
</div><br>

*Proof*:

Since $A$ is Hermitian, we can diagonalize it with a *unitary* matrix $U$ with determinant 1:

$$
\Lambda =U^{\dagger}A U \Rightarrow \left\{
\begin{align*}
     A &=U \Lambda U^{\dagger}
     \\
     A^{-1} &= (U^{\dagger})^{-1} \Lambda^{-1} O^{-1}
     = U \Lambda^{-1} U^{\dagger}
\end{align*}
\right.
$$

Introduce the new variables and sources 

$$
\begin{align*}
    \theta &= U^{\dagger} \psi , &\quad
    \bar{\theta} &= \bar{\psi} U
    \\
    \mathcal{J} &= U^{\dagger}J , &\quad
    \bar{\mathcal{J}} &= \bar{J} U
\end{align*}
$$

Then

$$
\begin{align*}
    Z(\bar{J}, J)
    &= \int D\bar{\psi}\, D\psi 
    \exp (
        -\bar{\psi}A \psi +\bar{\psi}J +\bar{J}\psi 
    ) \\
    &= \int D\bar{\psi}\, D\psi \exp (
        -\bar{\psi}U \Lambda  U^{\dagger} \psi +\bar{\theta}U^{\dagger}J +\bar{J}U \theta
    )
    \\
    &= \int D\bar{\theta} \, D\theta 
    \exp (
        -\bar{\theta}\Lambda  \theta +\bar{\theta}\mathcal{J} +\bar{\mathcal{J}}\theta
    )
    \\
    &= \prod_{k=1}^n \int d\bar{\theta}_k \, d\theta_k 
    \exp (
        -\bar{\theta}_k \Lambda_k \theta_k
        + \bar{\theta}_k \mathcal{J}_k
        + \bar{\mathcal{J}}_k \theta_k
    )
\end{align*}
$$

Now we can apply our previous result on one-variable-pair integral:

$$
\begin{align*}
    Z(\bar{J}, J)
    &= \prod_{k=1}^n \Lambda_k \exp (\bar{\mathcal{J}}_k\Lambda_k^{-1}\mathcal{J}_k)
    \\
    &= (\det A)
    \exp (
        \bar{\mathcal{J}} \Lambda^{-1} \mathcal{J} 
    )
    = (\det A) \exp (
        \bar{J} U \Lambda^{-1} U^{\dagger} J 
    )
    \\
    &= (\det A) \exp (\bar{J} A^{-1} J)
    \quad \blacksquare
\end{align*}
$$

## Wick's Theorem
