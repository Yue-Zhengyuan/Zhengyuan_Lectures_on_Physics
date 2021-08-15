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
    [a] \equiv \{x \in X \mid x \sim a\}
    $$

    - **Representative of an equivalence class**: any element in this class

<div class="result">

*Theorem*: (Equivalence classes are either disjoint or identical)

Given a set $X$ with an equivalence relation $\sim$, it can always be partitioned into *mutually disjoint* equivalence classes. 

</div>

----

*Proof*: We want to prove that for any two classes $[a], [b]$
    
$$
[a] \cap [b] \ne \varnothing \Rightarrow [a] = [b]
$$

which is equivalent to the statement

$$
[a] \ne [b] \Rightarrow [a] \cap [b] = \varnothing
$$

Suppose $c \in [a] \cap [b]$. Using the transitive property

$$
(a \sim c) \land (b \sim c) \Rightarrow a \sim b
$$

Thus any element equivalent to $a$ must be equivalent to $b$, i.e. $[a] \subset [b]$. For the same reason $[b] \subset [a]$. Therefore $[a] = [b]$. $\blacksquare$

----

## Quotient Space

*Definition*: Let $X$ be a topological space.

- **Quotient space**: the set of all equivalence classes in $X$ with $\sim$, denoted by $X / \sim$

