# Exact Sequence

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
    \im f_j = \ker f_{j+1} \quad (j = 1,...,n)
    $$

    <div class="remark">

    *Remark*: The notation $G_n \xrightarrow{f_{n+1}} G_{n+1}$ only means $f_{n+1}(G_n) \le G_{n+1}$; they are *not* guaranteed to be equal.

    </div><br>

## Examples

Below $1$ refers to the trivial group containing only the identity. 

- In the following 3-group exact sequence
    
    $$
    1 \xrightarrow{f_1} A \xrightarrow{f_2} B
    \ \Rightarrow \ \im f_1 = \ker f_2
    $$

    However, since $f_1$ is a map from the trivial group, $\im f_1$ contains only one element:

    $$
    \im f_1 = \{f_1(1)\} = \{1_A\} \overset{!}{=} \ker f_2
    $$

    which implies that $f_2$ is a *monomorphism (injective)*.

- In the following 3-group exact sequence
    
    $$
    B \xrightarrow{f_3} C \xrightarrow{f_4} 1
    \ \Rightarrow \ \im f_3 = \ker f_4
    $$

    However, since the only image of $f_4$ is the identity, the entire group $C$ is in $\ker f_4$, which implies that $\im f_3 = C$ is a *epimorphism (surjective)*.

- **Short exact sequence**: a 5-group exact sequence of the form
    
    $$
    1 \to A \xrightarrow{f} B \xrightarrow{g} C \to 1
    \quad (\im f = \ker g)
    $$

    From previous two examples, $f$ is *injective*, and $g$ is *surjective*.
