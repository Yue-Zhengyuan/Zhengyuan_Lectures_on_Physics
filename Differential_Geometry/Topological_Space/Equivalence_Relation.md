# Equivalence Relations

*Definition*:

- **Relation**: defined in a set $X$ specifying the relation (in the usual sense) between two elements (say $a, b$) in $X$; denoted $aRb$
    
    *Example*: $X = \mathbb{R}, \ R =\ >$

- **Equivalence relation**: a special kind of relation (denoted by $\sim$) with the following properties

    $$
    \begin{array}{r|l}
        \text{Requirement} & \text{Symbolic Expression}
        \\[3pt] \hline \\[-6pt]
        \text{Reflective} & a \sim a
        \\[3pt]
        \text{Symmetric} & a \sim b \Rightarrow b \sim a
        \\[3pt]
        \text{Transitive} & (a \sim b) \land (b \sim c) \Rightarrow (a \sim c)
    \end{array}
    $$

- **Equivalence class**: set of elements all equivalent to each other; the equivalence class containing element $a \in X$ is denoted by
    
    $$
    [a] \equiv \{x \in X | x \sim a\}
    $$

- **Representative of an equivalence class**: any element in this class

- **Quotient space**: the set of all equivalence classes in $X$ with $\sim$, denoted by $X / \sim$

<div class="result">

*Theorem*: (Equivalence classes are either disjoint or identical)

Given a set $X$ with an equivalence relation $\sim$, it can always be partitioned into *mutually disjoint* equivalence classes. 

</div><br>
