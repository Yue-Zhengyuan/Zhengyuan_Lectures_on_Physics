# Group Extension

*Definition*:

- **Exact sequence**: a sequence of groups and group homomorphisms between them
    
    $$
    G_0 \xrightarrow{f_1} G_1 
    \xrightarrow{f_2} G_2
    \xrightarrow{f_3} \cdots
    \xrightarrow{f_n} G_n
    $$

    which satisfy the requirement

    $$
    \im f_k = \ker f_{k+1}
    $$

    which means that only the group $G_k$ (image of $f_k$) is mapped by $f_{k+1}$ to the identity of group $G_{k+1}$.

- **Short exact sequence**: an exact sequence of the form
    
    $$
    1 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0
    \quad (\im f = \ker g)
    $$

    where $1$ is the trivial group containing only one element. In this case:

    - $f$ is a **monomorphism (单同态映射)**, 
    - $g$ is an **epimorphism (满同态映射)**.

- **Group extension:** Let $Q, N$ be two groups. Then $G$ is an **extension** of $Q$ by $N$ if there is a short exact sequence 
    
    $$
    1 \to N \xrightarrow{i} G \xrightarrow{\pi} Q \to 1
    $$

    Later we prove that $G$ is also a group.

    - **Equivalent group extensions**: Two group extensions $G, G'$ are **equivalent** if there is a commutative diagram

        $$
        \begin{CD}
            1 @>>> N @>{i}>> G @>{\pi}>> Q @>>> 1
            \\
            @. @VV{\text{id}}V @VV{\varphi}V @VV{\text{id}}V @.
            \\
            1 @>>> N @>>{i'}> G' @>>{\pi'}> Q @>>> 1
        \end{CD}
        $$

        where $\varphi: G \to G'$ is a group *isomorphism*.

## Properties of Group Extension

- The extension $G$ is a group.

- $i(N)$ is a normal subgroup of $G$.

    *Proof*: By definition of exact sequence, $i(N) = \ker G$

- $Q$ is isomorphic to the quotient group $G/i(N)$.

