# Scaling Dimension Degeneracy

*Review*: Scaling dimension and spin from conformal dimension:

$$
\Delta = h + \bar{h} \qquad
s = h - \bar{h}
$$

## Example 1: Ising Model

Ising model is described by the Ising CFT, which is a minimal model of $m = 3$. Recall that the minimal model central charge and conformal dimension (unitary representation of Virasoro algebra) are given by

$$
\begin{align*}
    c &= 1 - \frac{6}{m(m+1)} 
    \qquad \quad \qquad m = 3,4,...
    \\
    h_{p,q} = \bar{h}_{p,q}
    &= \frac{[(m+1)p - mq]^2 - 1}{4m(m+1)}
    \quad 
    \begin{array}{l}
        1 \le p \le m - 1
        \\
        1 \le q \le m
    \end{array}
\end{align*}
$$
    
Then we obtain a table of all possible $h, \bar{h}$. 

<center>
<img src="ising_cft-h.png" width="150px">
</center>

The scaling dimension vs spin plot is shown below:

<center>
<img src="tfising-scdim-spin.svg" width="400px">
</center>

Let us pick some larger scaling dimensions and see how they are generated using the $L_{-n}, \bar{L}_{-n}$ ladder operators. Let $g$ be the degeneracy (denoted by "deg." in the following tables) of the scaling dimension.

- $\Delta = 0, \, g = 1$
    
    $$
    \def \arraystretch{1.5}
    \begin{array}{c|c|c|c|c|c}
        h & L \text{ on } h & \bar{h} & \bar{L} \text{ on } \bar{h} & s & \text{deg.}
        \\ \hline
        0 & 1 & 0 & 1 & 0 & 1
    \end{array}
    $$

- $\Delta = 1/8, \, g = 1$
    
    $$
    \def \arraystretch{1.5}
    \begin{array}{c|c|c|c|c|c}
        h & L \text{ on } h & \bar{h} & \bar{L} \text{ on } \bar{h} & s & \text{deg.}
        \\ \hline
        1/16 & 1 & 1/16 & 1 & 0 & 1
    \end{array}
    $$

- $\Delta = 1, \, g = 1$
    
    $$
    \def \arraystretch{1.5}
    \begin{array}{c|c|c|c|c|c}
        h & L \text{ on } h & \bar{h} & \bar{L} \text{ on } \bar{h} & s & \text{deg.}
        \\ \hline
        1/2 & 1 & 1/2 & 1 & 0 & 1
    \end{array}
    $$

    Note that since $h = 0$ corresponds to identity operators, it cannot be descended by $L_{-1}, \bar{L}_{-1}$, which corresponds to $z, \bar{z}$ derivatives.

- $\Delta = 1 + 1/8, \, g = 2$
    
    $$
    \def \arraystretch{1.5}
    \begin{array}{c|c|c|c|c|c}
        h & L \text{ on } h & \bar{h} & \bar{L} \text{ on } \bar{h} & s & \text{deg.}
        \\ \hline
        1/16 & L_{-1} & 1/16 & 1 & 1 & 1
        \\
        1/16 & 1 & 1/16 & \bar{L}_{-1} & -1 & 1
    \end{array}
    $$

- $\Delta = 2, \, g = 4$
    
    $$
    \def \arraystretch{1.5}
    \begin{array}{c|c|c|c|c|c}
        h & L \text{ on } h & \bar{h} & \bar{L} \text{ on } \bar{h} & s & \text{deg.}
        \\ \hline
        0 & L_{-2} & 0 & 1 & 2 & 1
        \\
        0 & 1 & 0 & \bar{L}_{-2} & -2 & 1
        \\
        1/2 & L_{-1} & 1/2 & 1 & 1 & 1
        \\
        1/2 & 1 & 1/2 & \bar{L}_{-1} & -1 & 1
    \end{array}
    $$

Finally, let us see a much higher scaling dimension, for which the descendant level is larger than 1 for non-trivial $h, \bar{h}$.

- $\Delta = 4, \, g = 9$

    $$
    \def \arraystretch{1.5}
    \begin{array}{c|c|c|c|c|c}
        h & L \text{ on } h & \bar{h} & \bar{L} \text{ on } \bar{h} & s & \text{deg.}
        \\ \hline
        0 & L_{-4}, L_{-2}^2 & 0 & 1 & 4 & 2
        \\
        0 & 1 & 0 & \bar{L}_{-4}, \bar{L}_{-2}^2 & -4 & 2
        \\
        0 & L_{-2} & 0 & \bar{L}_{-2} & 0 & 1
        \\
        1/2 & L_{-3} & 1/2 & 1 & 3 & 1
        \\
        1/2 & 1 & 1/2 & \bar{L}_{-3} & -3 & 1
        \\
        1/2 & L_{-2} & 1/2 & \bar{L}_{-1} & 1 & 1
        \\
        1/2 & L_{-1} & 1/2 & \bar{L}_{-2} & -1 & 1
    \end{array}
    $$

    Question: Why, for example, the $s=3$ case has degeneracy 1? Why are some of the following choices not allowed?

    $$
    \def \arraystretch{1.5}
    \begin{array}{c|c|c|c|c|c}
        h & L \text{ on } h & \bar{h} & \bar{L} \text{ on } \bar{h} & s & \text{deg.}
        \\ \hline
        1/2 & L_{-3}, L_{-2}L_{-1}, L_{-1}^3 & 1/2 & 1 & 3 & 3 (?)
    \end{array}
    $$

## Example 2: Compactified Boson

The compactified boson CFT has conformal dimensions given by

$$
\begin{align*}
    h_{m,n} &= \left(\frac{m}{R} + \frac{n R}{2}\right)^2
    \\[1em]
    \bar{h}_{m,n} &= \left(\frac{m}{R} - \frac{n R}{2}\right)^2
\end{align*} \qquad
(m,n \in \Z)
$$

The scaling dimensions are

$$
\Delta_{m,n} = \frac{m^2}{R^2} + \frac{n^2 R^2}{4}
$$

All these values are not changes if we make the substitution $R \leftrightarrow 2/R$. 

Now we consider the special case $R = \sqrt{2}$, the self-dual radius. 
