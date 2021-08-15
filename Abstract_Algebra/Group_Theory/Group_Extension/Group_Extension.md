# Group Extension

*Definition*: Let $A, B$ be two groups.

- **Group extension:**  A group $G$ related to $A,B$ by a short exact sequence 
    
    $$
    1 \to A \xrightarrow{i} G \xrightarrow{\pi} B \to 1
    $$

- **Equivalent group extensions**: Two group extensions $G, G'$ are **equivalent** if there is a commutative diagram

    $$
    \begin{CD}
        1 @>>> A @>{i}>> G @>{\pi}>> B @>>> 1
        \\
        @. @VV{\text{id}}V @VV{\varphi}V @VV{\text{id}}V @.
        \\
        1 @>>> A @>>{i'}> G' @>>{\pi'}> B @>>> 1
    \end{CD}
    $$

    where $\varphi: G \to G'$ is a group *isomorphism*.

## Properties of Group Extension

1. $i(A)$ is a normal subgroup of $G$.

    *Proof*: By definition of exact sequence, $i(A) = \ker G$

2. $B$ is isomorphic to the quotient group $G/i(A)$.

## Example

Consider the quotient group $\mathbb{Z}/n\mathbb{Z} \ (n \in \mathbb{N})$, representing the cyclic group of order $n$ (up to group isomorphisms):

$$
\mathbb{Z}/n\mathbb{Z} = \{1, g, ..., g^{n-1}\} \qquad
(g^n = 1)
$$

To demonstrate how the group extension is done, we set

$$
\begin{align*}
    A &= \mathbb{Z}/4\mathbb{Z} = \{1, a, a^2, a^3\} 
    & & (a^4 = 1) \\
    B &= \mathbb{Z}/2\mathbb{Z} = \{1, b\}
    & & (b^2 = 1)
\end{align*}
$$

The extension $G$ is not unique. Let us pick an element $g \in G$ which is mapped to $b \in B$. 
