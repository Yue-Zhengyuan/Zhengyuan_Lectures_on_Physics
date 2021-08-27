# Fundamental Groups

## Paths and Loops

*Definition*:

- **Path**: a *continuous* map from the interval $I = [0,1]$ to a topological space $X$
    
    $$ \alpha: I \to X $$

    - **Loop at point $x_0$**: a *closed path* whose initial point and end point are both at $x_0$, i.e. $\alpha(0) = \alpha(1) = x_0$ 
    
    - **Constant path**: a path only at a constant point

        $$
        c_x: I \to X \quad c_x(s) = x \in X, \forall s \in I
        $$
    
- **Product of two paths**: if the end point of path $\alpha$ is the *same* as the initial point of another path $\beta$
 
    $$ \alpha(1) = \beta(0) $$
    
    then we define the **product** of $\alpha$ and $\beta$ as the "connection" of them, which is also a path; mathematically
    
    $$
    (\alpha * \beta)(s) \equiv
    \begin{cases}
        \alpha(2s)  & 0 \le s \le 1/2 \\
        \beta(2s-1) & 1/2 < s \le 1
    \end{cases}
    $$

- **Inverse path**: the inverse path of path $\alpha$ is 

    $$
    \alpha^{-1}(s) \equiv \alpha(1-s), \quad s \in I
    $$

    The initial and the end points are swapped, and the path direction is reversed. 

## Homotopy

*Definition*:

- **Homotopy (同伦)**: the *continuous* map $F: I \times I \to X$ which deform the two loops to each other. Concretely, 

    $$
    \begin{align*}
        \forall s \in I: &\quad 
        F(s,0) = \alpha(s), F(s, 1) = \beta(s) \\
        \forall t \in I: &\quad 
        F(0,t) = F(1,t) = x_0
    \end{align*}
    $$

    The first parameter $s$ controls the deformation:
        
    - $s = 0$: the loop is $\alpha$
    - $s = 1$: the loop is $\beta$

    The second parameter $t$ specify the position on the deformed loop. During the deformation, the initial and end points are fixed. 

- **Homotopic loops (同伦环路)**: Two loops $\alpha, \beta$ at the *same point* $x_0$ are **homotopic** if they can be *continuously deformed to each other* by a map $F$ described above.

<div class="result">

*Theorem*: The homotopic relation is an *equivalence relation*.  

</div><br>

<div class="remark">
    
*Remark*: 

- For this reason, "$\alpha$ is homotopic to $\beta$" is denoted by $\alpha \sim \beta$. 
- Intuitively, if $\alpha$ can be continuously deformed to $\beta$, and $\beta$ can be further continuously deformed to $\gamma$, then $\alpha$ can certainly be continuously deformed to $\gamma$. 

</div><br>

## Fundamental Groups

The above theorem motivates the following definitions.

*Definition*:

- **Homotopy class $[\alpha]$**: the equivalence class consisting of loops homotopic to $\alpha$

- **Fundamental group (the first homotopy group) $\pi_1(X,x)$**: the *group* of homotopy classes of loops at point $x$ in the topological space $X$
    
    **Group structure**:

    - Product: $[\alpha] * [\beta] \equiv [\alpha * \beta]$
    - Identity: $[c_x]$
    - Inverse: $[\alpha]^{-1}$ = $[\alpha^{-1}]$
