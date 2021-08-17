# Ring and Field

*Definition*:

- **Ring**: a set $R$ (its elements are called **scalars**) with two binary operations satisfying given axioms.

   - **Addition** $+: R \times R \to R$

        For any $a,b,c \in R$:

        $$
        \begin{array}{r|l}
            \text{Commutativity} & a+b = b+a
            \\[6pt] \hline \\[-6pt]
            \text{Associativity} & a+(b+c) = (a+b)+c
            \\[6pt] \hline \\[-6pt]
            \begin{aligned}
                \text{Existence of zero} \\
                \text{(additive identity)}
            \end{aligned} & \exists 0 \in R, \ a + 0 = a
            \\[6pt] \hline \\[-6pt] 
            \begin{aligned}
                \text{Existence of} \\
                \text{additive inverse}
            \end{aligned} & \exists -a \in R, \ a + (-a) = 0
        \end{array}
        $$

    - **Multiplication** $\cdot: R \times R \to R$ 
        
        Related to addition by the *distributive law*; for any $a,b,c \in R$:

        $$
        (a+b)c = ac + bc, \quad
        a(b+c) = ab + ac
        $$

If we impose additional axioms on the multiplication, we obtain special rings:

- **Associative ring**: multiplication is associative

    $$
    a(bc) = a(bc)
    $$

- **Ring with identity**: existence of identity (one, $1$) of multiplication

    $$
    \exists 1 \in R \quad 1 a = a 1 = a
    $$

- **Commutative ring**: multiplication is commutative

    $$
    ab = ba
    $$

- **Division ring**: every $a \ne 0$ has a multiplicative inverse

    $$
    \exists a^{-1} \in R \quad a^{-1}a = aa^{-1} = 1
    $$

- **Field**: a commutative *and* division ring

- **Skew field**: a non-commutative division ring