# *R*-Modules

Modules over rings are generalizations of vector spaces on fields.

*Definition*: Let $R$ be a ring with multiplication identity $1$.

- **Left $R$-module**: an *Abelian group* $M$ (written additively) with an additional operation called the **scalar multiplication** 
    
    $$
    \_ \cdot \_: R \times M \to M
    $$

- **Axioms for scalar multiplication**: for any $a,b \in R$ and $u,v \in M$

    $$
    \begin{array}{r|l}
        \text{Requirement} & \text{Description}
        \\[4pt] \hline \\[-8pt]
        \text{Ring-multip. compatibility} & 
        a \cdot (b\cdot v) = (ab) \cdot v
        \\[6pt]
        \text{Identity of ring} & 
        1_R \cdot v = v
        \\[6pt]
        \text{Distributivity over vectors} & 
        a \cdot (u+v) = a\cdot u + a\cdot v
        \\[6pt]
        \text{Distributivity over scalars} & 
        (a+b) \cdot v = a\cdot v + b\cdot v
    \end{array}
    $$

- **Right $R$-module**: the scalar multiplication will performed on the right. 