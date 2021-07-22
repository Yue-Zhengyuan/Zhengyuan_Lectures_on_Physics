# Jordan-Wigner Transformation

## Mapping A Single Spin-1/2 to A Single Fermion

The up and down states of a *single* spin-1/2 site can be thought as the occupied and empty states of a *one*-particle (spinless) fermion states:

$$
\begin{align*}
    \text{(Up)} \quad 
    \ket{\uparrow} &\longleftrightarrow \ket{1} = c^\dagger \ket{0}
    &&\text{(Occupied)}
    \\
    \text{(Down)} \quad 
    \ket{\downarrow} &\longleftrightarrow \ket{0}
    &&\text{(Empty)}
\end{align*}
$$

Under these basis vectors, we define the ladder operators for the spin

$$
\begin{align*}
    S^+ &= \begin{bmatrix}
        0 & 1 \\
        0 & 0
    \end{bmatrix}
    = S^x + iS^y
    \\
    S^- &= \begin{bmatrix}
        0 & 0 \\
        1 & 0
    \end{bmatrix}
    = S^x - iS^y
\end{align*}
$$

where $\sigma^a \, (a = x,y,z)$ are Pauli matrices. We then have the following mapping for a single spin:

<div class="result">

**Mapping a single spin to a single fermion:**

$$
\begin{gather*}
    S^+ = c^\dagger, \quad S^- = c \\ \Rightarrow
    S^z = S^+ S^- - 1/2 = c^\dagger c - 1/2
\end{gather*}
$$

</div><br>

Let us verify the (anti-)commutation relations: the spin operators satisfy

$$
\begin{align*}
    [S^a, S^b] &= i \epsilon^{abc} S^c
    \\
    \{S^a, S^b\} &= \delta^{ab} / 2
\end{align*} \qquad (a,b = x,y,z)
$$

Then we can also show that the ladder operators satisfy

$$
\{S^-, S^+\} = 1, \quad
\{S^\pm, S^\pm\} = 0, \quad
[S^+, S^-] = 2S^z
$$

which is the same as the fermion operators:

$$
\begin{gather*}
    \{c, c^\dagger\} = 1, \quad
    \{c, c\} = \{c^\dagger, c^\dagger\} = 0
    \\
    [c^\dagger, c] = 2 c^\dagger c - \{c, c^\dagger\}
    = 2 \left(n - \frac{1}{2} \right)
\end{gather*}
$$

## String (Kink) Operator

Next, let us we try to generalize the above mapping to a 1D spin chain (with $N$ sites). Each site of the chain will correspond to an independent fermion. The naive mapping is

$$
S_j^+, S_j^-, S_j^z \longleftrightarrow 
c_j^\dagger, c_j, n_j - \tfrac{1}{2}
\qquad j = 1,...,N
$$

However, different fermion operators should *anti-commute*, while the spin operators at different sites *commute*:

$$
[S_i^{(\pm)}, S_j^{(\pm)}] = 0 \qquad
\{c_i^{(\dagger)}, c_j^{(\dagger)}\} = 0 \qquad (i \ne j)
$$

The bracket means we are referring to either $c^\dagger$ or $c$, and $S^+$ or $S^-$. One way to overcome this difficulty is to introduce a **string (kink) operator** to the fermion operators:

<div class="result">

**The string operator for fermion:**

$$
F_j \equiv e^{i\phi_j}, \quad 
\phi_j = \pi \sum_{l=1}^{j-1} c_l^\dagger c_l \quad 
(\text{define} \ \phi_1 \equiv 0 \Rightarrow F_1 = 1)
$$

</div><br>

### Properties of the String

- Since $n_l \equiv c_l^\dagger c_l = 0,1$, one can easily see that $F_j = F_j^\dagger = F_j^{-1}$. 

- It is useful to derive an alternative expression for the string $F_j$:

    $$
    \begin{align*}
        F_j &\equiv \exp\bigg[
            i\pi \sum_{l=1}^{j-1} n_l
        \bigg]
        = \prod_{l=1}^N \exp(i\pi n_l) \quad
        (\text{All $n_l$ commute})
        \\
        &= \prod_{l=1}^{j-1} (-1)^{n_l}
        = \prod_{l=1}^{j-1} (1 - 2n_l)
    \end{align*}
    $$

    In the last step we have used the fact that $n_l$ can only be 0, 1 and therefore $(-1)^{n_l} = 1 - 2n_l$. 

- Different string operators commute (since all $n_l$ commute):
    
    $$
    [F_i, F_j] = 0
    $$

- (Anti-)commutation relations with fermion operators

    $$
    \begin{align*}
        [F_j, c_m^{(\dagger)}] &= 0 \qquad j \le m \\
        \{F_j, c_m^{(\dagger)}\} &= 0 \qquad j > m
    \end{align*}
    $$

    ----

    *Proof*: We first observe the following commutation relations between $e^{i\pi n_l}$ and $c_m^{(\dagger)}$:
    
    $$
    \begin{array}{ll}
        l \ne m: \quad & [n_l, c_m^{(\dagger)}] = 0 \Rightarrow
        [e^{i\pi n_l}, c_m^{(\dagger)}] = 0
        \\[0.7em]
        l = m: \quad & 
        \begin{align*}
            \{e^{i\pi n_m}, c_m\}
            &= e^{i\pi n_m} c_m + c_m e^{i\pi n_m} \\
            &= e^{i\pi (1-1)} c_m + c_m e^{i\pi 1} = 0
            \\
            \{e^{i\pi n_m}, c_m^\dagger\}
            &= e^{i\pi n_m} c_m^\dagger + c_m^\dagger e^{i\pi n_m} \\
            &= e^{i\pi (0+1)} c_m + c_m e^{i\pi 0} = 0
        \end{align*}
    \end{array}
    $$

    - When $j \le m$, $e^{i\pi n_m}$ is not in $F_j$. Each term in $F_j$ commutes with $e^{i\pi n_m}$. Therefore
        
        $$ [F_j, c_m^{(\dagger)}] = 0 $$

    - When $j > m$, $e^{i\pi n_m}$ is in $F_j$. Then

        $$
        \{F_j, c_m^{(\dagger)}\}
        = e^{i\pi n_1} \cdots \cancel{e^{i\pi n_m}} 
        \cdots e^{i\pi n_{j-1}} \{e^{i\pi n_m} c_m^{(\dagger)}\}
        = 0 \quad \blacksquare
        $$

    ----

## Jordan-Wigner Transformation

With the string operator, the complete mapping from spin to (complex) fermion is

<div class="result">

**The Jordan-Wigner transformation:**

$$
\begin{gather*}
    S_j^+ = c_j^\dagger F_j = F_j c_j^\dagger, \quad 
    S_j^- = c_j F_j = F_j c_j
    \\[0.5em] \Rightarrow
    S^z_j = S^+_j S^-_j - 1/2 = c_j^\dagger c_j - 1/2
\end{gather*} \qquad (j = 1,...,N)
$$

</div><br>

<center>
<img src="images/spin-fermion.png" width="450px" alt="string operator">
</center>

<div class="remark">

*Remark*: In terms of spin operators, we have
    
- Expression of $F_j$
    
    $$
    F_j = \prod_{l=1}^{j-1} (1 - 2n_l)
    = \prod_{l=1}^{j-1} (-2S^z_l)
    = \prod_{l=1}^{j-1} (-Z_l)
    $$

- Commutation relations with spin operators

    $$
    \begin{align*}
        [F_j, S_m^{a}] &= 0 \qquad j \le m \\
        \{F_j, S_m^{a}\} &= 0 \qquad j > m
    \end{align*} \qquad (a = +,-,x,y)
    $$

</div>

----

*Proof of the commutation relations*:

- When $j \le m$, the string $F_j$ contains no operators of site $m$. Thus $[F_j, S^a_m] = 0$ 

- When $j > m$, $S^z_m$ is in $F_j$. Then

    $$
    \{F_j, S^a_m\} = (-2)^{j-1} 
    S^z_1 \cdots \cancel{S^z_m} \cdots S^z_{j-1} 
    \underbrace{\{S^z_m, S^a_m\}}_{=0} = 0
    \quad \blacksquare
    $$

----

We are now prepared to check that the introduction of the string operator indeed gives us the correct commutation relations of fermions:

$$
\{c_i, c_j\} = \{c_i^\dagger, c_j^\dagger\} = 0, \quad
\{c_i, c_j^\dagger\} = \delta_{ij}
$$

----

*Proof*: Without loss of generality, we can assume $i < j$. Then

$$
\begin{align*}
    \{c_i, c_j^{(\dagger)}\} &= \{S^-_i F_i, S^\pm_j F_j\}
    = S^-_i (F_i S^\pm_j) F_j + S^\pm_j (F_j S^-_i) F_i \\
    &= S^-_i (S^\pm_j F_i) F_j + S^\pm_j (-S^-_i F_j) F_i \\
    &= S^-_i S^\pm_j F_i F_j - S^-_i S^\pm_j F_i F_j = 0
    \\~\\
    \{c_i, c_i^\dagger\} &= \{S^-_i F_i, S^+_i F_i\}
    = S^-_i F_i S^+_i F_i + S^+_i F_i S^-_i F_i \\
    &= \underbrace{\{S^-_i, S^+_i\}}_{=1} (F_i)^2 = 1 
    & \blacksquare
\end{align*}
$$

----

## Majorana Fermion

The complex fermion $c_j$ can be rearranged into **Majorana fermions** $a_j, b_j$, whose corresponding operators are *Hermitian*:

$$
\begin{bmatrix}
    c_j \\ c_j^\dagger
\end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix}
    a_j - i b_j \\ a_i + i b_j
\end{bmatrix}
\Rightarrow 
\begin{bmatrix}
    a_j \\ b_j
\end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix}
    c_j + c_j^\dagger \\
    i (c_j - c_j^\dagger)
\end{bmatrix}    
$$

$a, b$ operators have the following anti-commutation relations: 

$$
\{a_i, a_j\} = \{b_i, b_j\} = \delta_{ij}, \quad
\{a_i, b_j\} = 0
$$

----

*Proof*:

$$
\begin{align*}
    \{a_i, a_j\} &= \frac{1}{2} \{c_i+c_i^\dagger, c_j+c_j^\dagger\}
    \\ &= \frac{1}{2} \Big[
        \{c_i, c_j\} + \{c_i, c_j^\dagger\} 
        + \{c_i^\dagger, c_j\} + \{c_i^\dagger, c_j^\dagger\}
    \Big]
    \\ &= \frac{1}{2} (0 + \delta_{ij} + \delta_{ij} + 0)
    = \delta_{ij}
    \\~\\
    \{b_i, b_j\} &= \frac{-1}{2} \{c_i-c_i^\dagger, c_j-c_j^\dagger\}
    \\ &= \frac{-1}{2} \Big[
        \{c_i, c_j\} - \{c_i, c_j^\dagger\} 
        - \{c_i^\dagger, c_j\} + \{c_i^\dagger, c_j^\dagger\}
    \Big]
    \\ &= \frac{-1}{2} (0 - \delta_{ij} - \delta_{ij} + 0)
    = \delta_{ij}
    \\~\\
    \{a_i, b_j\} &\propto \{c_i + c_i^\dagger, c_j - c_j^\dagger\}
    \\ &= \{c_i, c_j\} - \{c_i, c_j^\dagger\}
    + \{c_i^\dagger, c_j\} - \{c_i^\dagger, c_j^\dagger\} 
    \\ &= 0 - \delta_{ij} + \delta_{ij} - 0 = 0
    \qquad \blacksquare
\end{align*}
$$

----

Next we determine the mapping from spin to Majorana fermions. 

$$
\begin{align*}
    c_j &= S_j^- F_j = (S^x_j - iS^y_j) F_j
    \overset{!}{=} \frac{1}{\sqrt{2}}(a_j - ib_j)
    \\
    c_j^\dagger &= S_j^+ F_j = (S^x_j + iS^y_j) F_j
    \overset{!}{=} \frac{1}{\sqrt{2}}(a_j + ib_j)
\end{align*}
$$

Comparing with the definition of $a_j, b_j$, we obtain (remember that $F_j$ is Hermitian)

<div class="result">

**Jordan-Wigner transformation to Majorana fermions:**

$$
a_j = \sqrt{2} S^x_j F_j, \quad
b_j = \sqrt{2} S^y_j F_j \qquad
\bigg[ F_j = \prod_{l=1}^{j-1} (-Z_l) \bigg]
$$

</div><br>

Let us verify the anti-commutation relations of $a, b$ again using the spin representation. 

----

*Proof*: Assume $i < j$ without loss of generality.

$$
\begin{align*}
    \{a_i, a_j\} &= 2 \{S^x_i F_i, S^x_j F_j\} 
    = 2 [
        S^x_i F_i S^x_j F_j + S^x_j F_j S^x_i F_i
    ] \\
    &= 2 [
        S^x_i S^x_j F_i F_j + S^x_j (-S^x_i F_j) F_i
    ] \\
    &= 2 [
        S^x_i S^x_j F_i F_j - S^x_i S^x_j F_i F_j
    ] = 0 
    \\
    \{a_i, a_i\} &= 2 a_i^2
    = 4 S^x_i F_i S^x_i F_i = 4 (S^x_i)^2 (F_i)^2 = 1
\end{align*}
$$

The relation $\{b_i, b_j\} = \delta_{ij}$ can be proved analogously. Finally

$$
\begin{align*}
    \{a_i, b_j\} &= 2 \{S^x_i F_i, S^y_j F_j\}
    = 2 [
        S^x_i F_i S^y_j F_j + S^y_j F_j S^x_i F_i
    ] \\
    &= 2 [
        S^x_i S^y_j F_i F_j + S^y_j (-S^x_i F_j) F_i
    ] \\
    &= 2 [
        S^x_i S^y_j F_i F_j - S^x_i S^y_j F_i F_j
    ] = 0 
    \\
    \{a_i, b_i\} &= 2 \{S^x_i F_i, S^y_i F_i\} 
    = 2 [
        S^x_i F_i S^y_i F_i + S^y_i F_i S^x_i F_i
    ] \\
    &= 4 \underbrace{\{S^x_i, S^y_i\}}_{=0} (F_i)^2 = 0
    & \blacksquare
\end{align*}
$$

----
