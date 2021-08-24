# Categories

*Definition*:

- **Category**: a collection $\mathcal{C}$ of 3 following ingredients

    - **Objects** $\obj(\mathcal{C})$: a class of mathematical objects
    
    - **Morphisms (arrows)**: for any $A, B \in \obj(\mathcal{C})$, there is a map $\Hom(A,B)$ corresponding to the *ordered* pair $(A,B)$

        <div class="remark">

        *Remark*: Elements $f \in \Hom(A,B)$ is denoted by $f: A \to B$ or $A \xrightarrow{f} B$, same as the notation for usual functions.

        </div><br>

    - **Compositions** of morphisms: for any $A, B, C \in \mathcal{C}$

        $$
        \begin{align*}
            \Hom(A,B) \times \Hom(B,C) &\to \Hom(A,C)
            \\
            (f,g) & \mapsto g f
        \end{align*}
        $$

    These ingredients satisfy the following axioms:

    - Each morphism $f \in \Hom(A,B)$ has a unique **domain** $A$ and a unique **target** $B$.
    
    - For each $A \in \obj(\mathcal{C})$, there is an **identity morphism** $1_A \in \Hom(A,A)$ such that

        $$
        \forall f \in \Hom(A,B): 
        f 1_A = 1_B f = f
        $$

    - Composition of morphisms is *associative*: 

        $$
        A \xrightarrow{f} B \xrightarrow{g} C \xrightarrow{h} D
        \Rightarrow h(gf) = (hg)f
        $$

- **Isomorphism**: a morphism $f \in \Hom(A,B)$ such that 

    $$
    \exist g \in \Hom(B,A): (gf = 1_A) \land (fg = 1_B)
    $$

    The mapping $g$ is the **inverse** of $f$, which is *unique*.

## Examples of Categories

In the following examples, the composition are always the usual composition of mappings.

<center>

|          Category          |      Objects       |      Morphisms       |
| :------------------------: | :----------------: | :------------------: |
|          **Sets**          |        Sets        |         Maps         |
|         **Groups**         |       Groups       | Group homomorphisms  |
|           **Ab**           |   Abelian groups   | Group homomorphisms  |
|         **Rings**          |       Rings        |  Ring homomorphism   |
| <sub><i>R</i></sub>**Mod** |  Left $R$-modules  |  $R$-homomorphisms   |
|          **Top**           | Topological spaces | Continuous functions |

</center>
