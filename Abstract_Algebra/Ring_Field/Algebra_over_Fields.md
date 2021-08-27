# Algebra over A Field

*Definition*: Let $F$ be a field. 

- **Algebra over $F$** (**$F$-algebra**): a vector space $V$ with an additional binary operation called the **vector product** $\times: V \times V \to V$.

    For any $x,y,z \in V$ and any $a,b \in F$, the vector product is *bilinear*, i.e. satisfies the following axioms:

    $$
    \begin{array}{c|c}
        \text{Requirement} & \text{Description}
        \\[4pt] \hline \\[-8pt]
        \text{Right distributivity} &
        (x+y) \times z = x\times z + y\times z
        \\[6pt]
        \text{Left distributivity} &
        z \times (x+y) = z\times x + z\times y
        \\[6pt]
        \text{Compatibility with scalars} &
        (ax) \times (by) = (ab) (x \times y)
    \end{array}
    $$
