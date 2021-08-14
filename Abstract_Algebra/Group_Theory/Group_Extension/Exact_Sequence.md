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
    \im f_n = \ker f_{n+1}
    $$

    <div class="remark">

    *Remark*: The notation $G_n \xrightarrow{f_{n+1}} G_{n+1}$ only means $f_{n+1}(G_n) \subset G_{n+1}$; they are in general *not* equal.

    </div><br>

- **Short exact sequence**: an exact sequence of the form
    
    $$
    1 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0
    \quad (\im f = \ker g)
    $$

    where $1$ is the trivial group containing only one element. In this case:

    - $f$ is a **monomorphism (单同态映射)**, 
    - $g$ is an **epimorphism (满同态映射)**.

## Examples

$$
1 \to H \to G \to G/H \to 1
$$
