# Vector Spaces

## Vectors and Vector Spaces

*Definition*: Let $F$ be a field.

- **Vector space**: a set $V$ (its elements $v \in V$ are then called **vectors**) with the following two operations satisfying given axioms.
    
    - **Vector addition** $+: V \times V \to V$
        
        For any $u,v,w \in V$:

        $$
        \begin{array}{r|l}
            \text{Commutativity} & u+v=v+u
            \\[6pt] \hline \\[-6pt]
            \text{Associativity} & u+(v+w) = (u+v)+w
            \\[6pt] \hline \\[-6pt]
            \begin{aligned}
                \text{Existence of zero} \\
                \text{(additive identity)}
            \end{aligned} & \exists 0 \in V, \ v + 0 = v
            \\[6pt] \hline \\[-6pt] 
            \begin{aligned}
                \text{Existence of} \\
                \text{additive inverse}
            \end{aligned} & \exists (-a) \in R, \ a + (-a) = 0
        \end{array}
        $$
    
    - **Scalar multiplication** $F \times V \to V$ 

        For any $a,b \in F$ and $u,v \in V$:

        $$
        \begin{array}{r|l}
            \begin{aligned}
                \text{Compatibility with} \\
                \text{field multiplication}
            \end{aligned} & a(bv) = (ab)v
            \\[6pt] \hline \\[-6pt]
            \begin{aligned}
                \text{Identity of scalar} \\
                \text{multiplication}
            \end{aligned} & 1v = v \ (1 \in F)
            \\[6pt] \hline \\[-6pt]
            \begin{aligned}
                \text{Distributivity with} \\
                \text{respect to vector addition}
            \end{aligned} & a(u+v) = au+av
            \\[6pt] \hline \\[-6pt] 
            \begin{aligned}
                \text{Distributivity with} \\
                \text{respect to scalar addition}
            \end{aligned} & (a+b)v = av + bv
        \end{array}
        $$

## Linear Maps

*Definition*: Let $V, W$ be two vector spaces over the field $K$ (common examples are $\mathbb{C}, \mathbb{R}$).

- **Linear maps**: a map $f: V \to W$ satisfying

    $$
    f(a_1 v_1 + a_2 v_2) = a_1 f(v_1) + a_2 f(v_2)
    \quad \forall a_1, a_2 \in K, v_1, v_2 \in V
    $$

    which is a *homomorphism* preserving the algebraic structure (vector addition and scalar multiplication) of the vector space $V$.

- **Isomorphic vector spaces**: two vector spaces $V, W$ between which exists an isomorphism (*bijective* linear map $f: V \to W$)

<div class="result">

*Theorem*: All $n$-dimensional vector spaces are isomorphic to $K^n$.

</div><br>

### Images and Kernels of Linear Maps

*Definition*: Let $f: V \to W$ be a linear map. 

- **Image** of $f$: $\im f = \{f(v) \in W \mid v \in V\}$

- **Kernel** of $f$: $\ker f = \{v \in V \mid f(v) = 0_W\}$

<div class="result">

*Theorem*: (**Relation between $\ker{f}$ and $\im f$**)

Let $f: V \to W$ be a linear map. Then

$$
\dim{V} = \dim{\ker{f}}  + \dim{\im f}
$$

</div><br>

## Dual Vector Space

## Inner Product and Adjoint

*Definition*:

- **Inner product**
- **Adjoint of linear maps**

<div class="result">

*Theorem*: (**Dimension of $\tilde{f}$**)

$$
\dim{\im f} = \dim{\im \tilde{f}}
$$

</div><br>

<div class="result">

*Theorem*: (**Toy index theorem**)

Let $V, W$ be *finite*-dimensional vector spaces, and $f: V\to W$. Then

$$
\dim{\ker{f}} - \dim{\ker{\tilde{f}}} = \dim{V} - \dim{W}
$$

</div><br>

## Tensors

*Definition*: 

- **Tensor of type $(p,q)$**: a multi-linear map from $p$ dual vectors (in $V^*$) and $q$ vectors (in V) to $\mathbb{R}$, i.e.
    
    $$
    T: \bigotimes^p V^* \bigotimes V \to \mathbb{R}
    $$

    *Example*:

    - Dual vectors (from vector to $\mathbb{R}$): type $(0,1)$

    - Vectors (from dual vectors to $\mathbb{R}$): type $(1,0)$

- **Tensor space $\mathcal{T}^p_q$**: The set of all tensors of the same type $(p,q)$ 

- **Tensor product**: Let $\mu \in \mathcal{T}^p_q, \, \nu \in \mathcal{T}^r_s$. The tensor product of $\mu$ and $\nu$ (denoted by $\tau \equiv \mu \otimes \nu$) is an element in $\mathcal{T}^{p+r}_{q+s}$ defined by

    $$
    \begin{align*}
        &\tau(\omega_1,...,\omega_p,\xi_1,...,\xi_r; u_1,...,u_q,v_1,...,v_s) 
        \\ & \quad \equiv 
        \mu(\omega_1,...,\omega_p; u_1,...,u_q)
        \nu(\xi_1,...,\xi_r; v_1,...,v_s)
    \end{align*}
    $$

- **Tensor contraction**
