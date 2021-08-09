# Creation and Annihilation Operators

The number of particles can be variable. Then all occupation number basis states span the **Fock space**:

$$
\mathcal{F} \equiv \ket{0} \oplus \mathcal{H}(1)
\oplus \cdots \mathcal{H}(N) \oplus \cdots
$$

where $\ket{0}$ is the vacuum (no-particle) state. We can go back and forth between spaces of different number of particles using the **creation/annihilation operators**. 

The **creation operator**, which creates a particle at state $\ket{u}$, is defined as (note that $\ket{u},\ket{u_1},...\ket{u_N}$ below need *not* be one-body basis states)

<div class="result">

**Creation operator on an $N$-body state:**

$$
a_{\ket{u}}^\dagger \ket{(u_1,...,u_N)_\pm}
= \sqrt{N+1} \ket{(u, u_1,...,u_N)_\pm}
$$

</div><br>

<div class="remark">

*Remark*: Note that by convention, we put the new particle at the first slot of the symmetrized $(N+1)$-body state. This choice has no effect on boson systems, but matters for fermions.

</div><br>

The **annihilation operator** is defined as the Hermitian conjugate of the creation operator. We then immediately get its action on bras (using $S_\pm(N) = S^\dagger_\pm(N)$): 

$$
\bra{(u_1,...,u_N)_\pm} a_{\ket{u}}
= \sqrt{N+1} \bra{(u, u_1,...,u_N)_\pm}
$$

It must remove one particle from the symmetrized state. To find its action on kets, we calculate the following amplitude:

$$
\begin{align*}
    &\amp{(v_1,...,v_{N-1})_\pm}{a_{\ket{u}}}{(u_1,...,u_N)_\pm}
    \\
    &= \sqrt{N} \braket{(u,v_1,...,v_{N-1})_\pm}{(u_1,...,u_N)_\pm}
    \\
    &= \frac{\sqrt{N}}{N!} D_\pm \begin{bmatrix}
        \braket{u}{u_1} & \cdots & \braket{u}{u_N} \\
        \braket{v_1}{u_1} & \cdots & \braket{v_1}{u_N} \\
        \vdots & & \vdots \\
        \braket{v_{N-1}}{u_1} & \cdots & \braket{v_{N-1}}{u_N}
    \end{bmatrix}
\end{align*}
$$

We expand $D_\pm$ with respect to the first row:

$$
\begin{align*}
    &= \frac{\sqrt{N}}{N!} \sum_{j=1}^N
    (\pm 1)^{j+1} \braket{u}{u_j} 
    D_\pm \{\braket{v_i}{u_k}\}_{k\ne j}
    \\
    &= \frac{1}{\sqrt{N}} \sum_{j=1}^N
    (\pm 1)^{j+1} \braket{u}{u_j}
    \braket{(v_1,...,v_{N-1})_\pm}{(u_1,...,\cancel{u_j},...,u_N)_\pm}
\end{align*}
$$

Since $\bra{(v_1,...,v_{N-1})_\pm}$ is an *arbitrary* state in the Hilbert space of the system of $N-1$ identical particles, we conclude that

<div class="result">

**Annihilation operator on an $N$-body state:**

$$
\begin{align*}
    &a_{\ket{u}} S_\pm(N) \ket{u_1,...,u_N}
    \\ &\quad
    = \frac{1}{\sqrt{N}} \sum_{j=1}^N (\pm 1)^{j+1}
    \braket{u}{u_j} S_\pm(N-1) 
    \ket{u_1,...,\cancel{u_j},...,u_N}
\end{align*}
$$

</div><br>

## Building Many-Body State from Vacuum

A creation operator acting on vacuum ($N = 0$) produces:

$$
a_{\ket{u}}^\dagger \ket{0} = \ket{u}
$$

Then, by repeating this procedure, we obtain

<div class="result">

**Building the symmetrized state from vacuum:**

$$
\ket{(u_1,...,u_N)_\pm}
= \frac{1}{\sqrt{N!}} a^\dagger_{\ket{u_1}}
\cdots a^\dagger_{\ket{u_N}} \ket{0}
$$

</div><br>

## Commutation Relations

The creation and annihilation operators satisfy the following commutation relations:

<div class="result">

**Commutation relations for $a, a^\dagger$:** 

For any two one-particle states $\ket{u}, \ket{v}$

$$
\begin{align*}
    [a_{\ket{u}}, a_{\ket{v}}]_\pm
    &= [a^\dagger_{\ket{u}}, a^\dagger_{\ket{v}}]_\pm = 0
    \\
    [a_{\ket{u}}, a^\dagger_{\ket{v}}]_\pm 
    &= \braket{u}{v}
\end{align*}
$$

The + sign (anti-commutator) is for fermions. 

</div>

----

*Proof*:

----

<div class="remark">

*Remark*: If we use a set of orthonormal basis $\{\ket{r}\}$, we have the following "**canonical**" commutation relations:

$$
\begin{align*}
    [a_r, a_{r'}]_\pm
    &= [a^\dagger_{r}, a^\dagger_{r'}]_\pm = 0
    \\
    [a_{r}, a^\dagger_{r'}]_\pm 
    &= \braket{r}{r'} = \delta_{rr'}
\end{align*}
$$

</div><br>

## Action on the Fock Basis

If we use the Fock basis, with the one-particle orthonormal basis states $\{\ket{r}\}$, then:

- For boson:

    $$
    \begin{align*}
        b_r^\dagger \sqrt{\frac{... N_r! ...}{N!}}
        \ket{...,N_r,...} 
        &= \sqrt{N+1} \sqrt{\frac{... (N_r+1)! ...}{(N+1)!}}
        \ket{...,N_r+1,...} 
        \\ \Rightarrow \quad
        b_r^\dagger \ket{...,N_r,...} 
        &= \sqrt{N_r + 1} \ket{...,N_r+1,...}
    \end{align*} 
    $$

- For fermion:


## Change of Basis

From the definition of $a_{\ket{u}}^\dagger$, and the action of $a_{\ket{u}}$, one can easily obtain

<div class="result">

**Linear (anti-linear) property of creation (annihilation) operator:**

$$
\begin{align*}
    a^\dagger_{\alpha \ket{u} + \beta \ket{v}}
    &= \alpha a^\dagger_{\ket{u}} + \beta a^\dagger_{\ket{v}}
    \\
    a_{\alpha \ket{u} + \beta \ket{v}}
    &= \alpha^* a_{\ket{u}} + \beta^* a_{\ket{v}}
\end{align*}
$$

</div><br>

Based on these property, we can determine how the $a, a^\dagger$ operators transform as we change the basis vectors: suppose two sets of basis vectors (not necessarily orthonormal) $\{\ket{u}\}, \{\ket{v}\}$ are related by the linear transformation $\mathcal{D}$

$$
\ket{v} = \sum_u \ket{u} \mathcal{D}_{uv}
$$

The operators $a^{(\dagger)}_{\ket{v}}$ is related to the old $a^{(\dagger)}_{\ket{u}}$ by

$$
a^\dagger_{\ket{v}} = \sum_u a^\dagger_{\ket{u}} \mathcal{D}_{uv},
\quad
a_{\ket{v}} = \sum_u a_{\ket{u}} \mathcal{D}^*_{uv}
$$

----

*Verifying the commutation rules:* From the general result, we expect that

$$
\boxed{
    [a_{\ket{v}}, a_{\ket{v'}}]_\pm = 0, \quad
    [a_{\ket{v}}, a^\dagger_{\ket{v'}}]_\pm = \braket{u}{v}
}
$$

Indeed, 

$$
\begin{align*}
    [a_{\ket{v}}, a_{\ket{v'}}]_\pm
    &= \sum_{u,u'} [
        a_{\ket{u}} \mathcal{D}^*_{uv}, 
        a_{\ket{u'}} \mathcal{D}^*_{u'v'}
    ]_\pm \\
    &= \sum_{u,u'} 
    [a_{\ket{u}}, a_{\ket{u'}}]_\pm 
    \mathcal{D}^*_{uv} \mathcal{D}^*_{u'v'}
    = 0
    \\
    [a_{\ket{v}}, a^\dagger_{\ket{v'}}]_\pm
    &= \sum_{u,u'} [
        a_{\ket{u}} \mathcal{D}^*_{uv}, 
        a^\dagger_{\ket{u'}} \mathcal{D}_{u'v'}
    ]_\pm \\
    &= \sum_{u,u'} 
    [a_{\ket{u}}, a^\dagger_{\ket{u'}}]_\pm 
    \mathcal{D}^*_{uv} \mathcal{D}_{u'v'}
    \\
    &= \sum_{u,u'} \braket{u}{u'}
    \mathcal{D}^*_{uv} \mathcal{D}_{u'v'}
    \\
    &= \sum_u \bra{u} \mathcal{D}^*_{uv}
    \sum_{u'} \ket{u'} \mathcal{D}_{u'v'}
    = \braket{v}{v'}
    &\blacksquare
\end{align*}
$$

----

### Canonical Transformation

Suppose we start with an orthonormal basis $\{\ket{r}\}$, and transform to another orthonormal basis $\{\ket{s}\}$. Such transformations preserves the canonical commutation rules, and are called **canonical transformations**.

If both $\{\ket{r}\}, \{\ket{s}\}$ are sets of orthonormal basis, we have the following constraint on the transformation $\mathcal{D}$:

$$
\begin{align*}
    \ket{s} &= \sum_r \ket{r} \mathcal{D}_{rs}
    \\[-8pt] &\Downarrow \\
    \braket{s}{s'}
    &= \sum_{r,r'} \underbrace{\braket{r}{r'}}_{\delta_{rr'}}
    \mathcal{D}^*_{rs} \mathcal{D}_{r's'} 
    \\
    &= \sum_{r} \mathcal{D}^*_{rs} \mathcal{D}_{rs'} 
    = \sum_{r} (\mathcal{D}^\dagger)_{sr} \mathcal{D}_{rs'}
    \\
    &= (\mathcal{D}^\dagger \mathcal{D})_{ss'}
    \overset{!}{=} \delta_{ss'}
    \Rightarrow \boxed{
        \mathcal{D}\ \text{is unitary}
    }
\end{align*}
$$

### Special Cases

- Going to the (continuous) *position eigenstates*. The creation and annihilation operators in the position basis are called the **field operators**:

    $$
    \begin{align*}
        \phi(x) &= \sum_r \braket{x}{r} a_r
        = \sum_r \phi_r(x) a_r
        \\
        \phi^\dagger(x) &= \sum_r a_r^\dagger \braket{r}{x} 
        = \sum_r \phi_r^*(x) a_r^\dagger
    \end{align*}
    $$

- Fourier transform (unitary)

    The creation/annihilation operators on a $N$-site lattice (site positions are labelled by $R$) can be Fourier transformed to

    $$
    a^\dagger_k = \frac{1}{\sqrt{N}} \sum_R a^\dagger_R e^{+ikR}
    , \quad
    a_k = \frac{1}{\sqrt{N}} \sum_R a_R e^{-ikR}
    $$

    Corresponding the *unitary* matrix

    $$
    \mathcal{D}_{Rk} = \frac{1}{\sqrt{N}} e^{ikR}
    $$

    Thus Fourier transform is a canonical transformation. 
