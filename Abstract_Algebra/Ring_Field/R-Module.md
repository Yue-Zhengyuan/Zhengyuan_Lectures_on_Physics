# *R*-Modules

Modules over rings are generalizations of vector spaces on fields.

*Definition*: Let $R$ be a ring.

- **Left $R$-module**: an *Abelian group* $M$ with the following two binary operations satisfying given axioms.

    - The usual group binary operation $+: M \times M \to M$ (written in additive notation)

    - (*New*) **Scalar multiplication** $\cdot: R \times M \to M$

        For any $a,b \in R$ and $u,v \in M$

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

- **Right $R$-module**: the scalar multiplication will performed on the right. 