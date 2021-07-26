# Transverse Field Ising Model

<div class="result">

**Transverse field Ising model (TFIM):**

- Non-boundary local spin Hamiltonian
    
    $$
    \begin{align*}
        H_j &= J_x S^x_j S^x_{j+1} - h S^z_j \\
        &= J (S_j^+ S_{j+1}^- + S_j^+ S_{j+1}^+ + h.c.)
        - h S^z_j       
    \end{align*} \quad \bigg(
        J \equiv \frac{J_x}{4}
    \bigg)
    $$

- Fermion Hamiltonian
    
    $$
    \begin{align*}
        H_F &= \sum_{j=1}^N \Big[
            J (c_j^\dagger c_{j+1} + c_j^\dagger c_{j+1}^\dagger + h.c.)
            - h (n_j - 1/2)
        \Big]
    \end{align*}
    $$

</div><br>

## Introducing Majorana Fermions

The fermion Hamiltonian can be further simplified in terms of Majorana fermions $a_j, b_j$:

$$
\begin{bmatrix}
    c_j \\ c_j^\dagger
\end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix}
    a_j - i b_j \\ a_i + i b_j
\end{bmatrix}
$$

- For non-boundary terms, the conversion is straightforward:

    $$
    \begin{align*}
        (H_F)_j &= 
        \frac{J}{2} \Big[
            (a_j + ib_j) (a_{j+1} - ib_{j+1})
            + (a_j + ib_j) (a_{j+1} + ib_{j+1})
            \\ &\qquad \ 
            + (a_{j+1} + ib_{j+1}) (a_j - ib_j)
            + (a_{j+1} - ib_{j+1}) (a_j - ib_j)
        \Big] \\ &\quad
        - \frac{h}{2} (a_j + ib_j) (a_j - ib_j)
        + \cancel{\text{const}}
        \\
        &= \frac{J}{2} \Big[
            2\cancel{\{a_j, a_{j+1}\}} 
            - 2i a_{j+1} b_j + 2i b_j a_{j+1}
        \Big] \\ &\quad 
        - \frac{h}{2} \Big[
            \cancel{a_j^2} + \cancel{b_j^2}
            + i(b_j a_j - a_j b_j)
        \Big] 
        \\
        &= - 2iJ a_{j+1} b_j - ih b_j a_j \quad
        (\text{Use} \ \{a_i,b_j\} = 0)
    \end{align*}
    $$

- For the boundary term $(H_F)_N$, we encounter the operator $a_{N+1}$. We now define it as
    
    $$
    \begin{align*}
        &\text{PBC} \ (c_{N+1} = c_1): & a_{N+1} &= a_1 \\
        &\text{ABC} \ (c_{N+1} = -c_1): & a_{N+1} &= -a_1
    \end{align*}
    $$

Finally

$$
H_F = -i \sum_{j=1}^N \Big[
    2J a_{j+1} b_j + h b_j a_j
\Big]
$$

Due to $\{a_i, b_j\} = 0$, we may unify the two types of fermions $a, b$ by regarding them as the same fermion on different sites:

$$
a_j \to a_{2j-1}, \quad b_j \to a_{2j} \qquad(j = 1,...,N)
$$

The boundary conditions correspond to

$$
\begin{align*}
    \text{PBC}\ &(c_{N+1} = c_1): & a_{2N+1} &= a_1 \\
    \text{ABC}\ &(c_{N+1} = -c_1): & a_{2N+1} &= -a_1
\end{align*}
$$

<div class="result">

**TFIM in terms of Majorana fermion:**

$$
H_F = -i \sum_{j=1}^N \Big[
    2J a_{2j+1} a_{2j} + h a_{2j} a_{2j-1}
\Big]
$$

</div><br>

<div class="remark">

*Remark*: Let us assure that the Hamiltonian is still Hermitian in terms of $a$ operators:

$$
(i a_{n+1} a_n)^\dagger = -i a_n^\dagger a_{n+1}^\dagger
= -i a_n a_{n+1} = i a_{n+1} a_n \quad \blacksquare
$$

</div><br>

## Kramers-Wannier Duality


