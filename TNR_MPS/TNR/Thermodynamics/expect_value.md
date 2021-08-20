# Expectation Value on 2D Network

The expectation value of an operator $\mathcal{O}$ in a state $|\psi\rangle$ is

$$
\langle \mathcal{O} \rangle
= \frac{\langle \psi | \mathcal{O} |\psi \rangle}
{\langle \psi |\psi \rangle}
$$

When the denominator and the numerator can be expressed as a tensor network (by expressing $|\psi\rangle$ as a **tensor product state (TPS)**, and $\mathcal{O}$ as a circuit gate), we can use the TNR method to calculate them. 

- The numerator network is with impurity tensors. In the following, we consider the special case where $\mathcal{O}$ is a two-site gate on nearest neighbors, or a four-site gate on a small square of neighboring sites. Then that the numerator is the following network with an impurity central plaquette:

    ```
          |   |   |   |  
        - B - A - B - A -
          |   |   |   |
        - A - D - C - B -
          |   |   |   |  
        - B - A'- B'- A -
          |   |   |   |
        - A - B - A - B -
          |   |   |   |  
    ```

In the two-site gate case, $A', B' = A, B$ before RG, hence their notation. 

- The denominator is the usual uniform network:
    
    ```
          |   |   |   |  
        - B - A - B - A -
          |   |   |   |
        - A - B - A - B -
          |   |   |   |  
        - B - A - B - A -
          |   |   |   |
        - A - B - A - B -
          |   |   |   |  
    ```

Before RG, the numbers of the 6 types of tensors in the numerator network are:

$$
\begin{align*}
    A + A' + C: &\quad (N_0 - 2) + 1 + 1 \\
    B + B' + D: &\quad (N_0 - 2) + 1 + 1 \\
\end{align*}
$$

It turns out that in each RG step, the DCA'B' impurity center will not affect the flow of the uniform tensors A and B (their flow is the same as the flow in the denominator network):

$$
\begin{align*}
    (A'^{(i)}, B'^{(i)}, C^{(i)}, D^{(i)})
    &\xrightarrow{\text{RG}}
    (A'^{(i+1)}, B'^{(i+1)}, C^{(i+1)}, D^{(i+1)})
    \\
    (A^{(i)}, B^{(i)})
    &\xrightarrow{\text{RG}}
    (A^{(i+1)}, B^{(i+1)})
\end{align*}
$$

The numbers of tensors after the $i$th RG step are

$$
\begin{align*}
    A + A' + C: &\quad (N_i - 2) + 1 + 1 \\
    B + B' + D: &\quad (N_i - 2) + 1 + 1 \\
\end{align*} \quad \text{with} \quad
N_i = \frac{N_{i-1}}{2}
$$

The two RG flows are normalized by the *quartic root* of following two factors (denoted by $g_i$ and $f_i$), respectively:

```
    A'B'CD flow         AB flow

    g^4 =               f^4 = 
        :   :               :   :
        |   |               |   |
    ..- D - C -..       ..- B - A -..
        |   |               |   |
    ..- A'- B'-..       ..- A - B -..
        |   |               |   |
        :   :               :   :
```

The normalized tensors (denoted by script letters) are

$$
\begin{align*}
    (\mathcal{A}'^{(i)}, \mathcal{B}'^{(i)}, 
    \mathcal{C}^{(i)}, \mathcal{D}^{(i)})
    &= \frac{1}{g_i} (A'^{(i)}, B'^{(i)}, C^{(i)}, D^{(i)})
    \\
    (\mathcal{A}^{(i)}, \mathcal{B}^{(i)})
    &= \frac{1}{f_i} (A^{(i)}, B^{(i)})
\end{align*}
$$

Therefore, the flow of the normalized tensors is then

$$
\begin{align*}
    (\mathcal{A}'^{(i)}, \mathcal{B}'^{(i)}, 
    \mathcal{C}^{(i)}, \mathcal{D}^{(i)})
    &\xrightarrow{\text{RG}} g_{i+1}
    (\mathcal{A}'^{(i)}, \mathcal{B}'^{(i)}, 
    \mathcal{C}^{(i)}, \mathcal{D}^{(i)})
    \\
    (\mathcal{A}^{(i)}, \mathcal{B}^{(i)})
    &\xrightarrow{\text{RG}} f_{i+1}
    (\mathcal{A}^{(i)}, \mathcal{B}^{(i)})
\end{align*}
$$

Then the un-normalized expectation value is then

$$
\begin{align*}
    \langle \psi |\mathcal{O}| \psi \rangle 
    &= \operatorname{Tr} [(A^{(0)})^{N_0-2} (B^{(0)})^{N_0-2}
    A'^{(0)} B'^{(0)} C^{(0)} D^{(0)}]
    \\
    &= f_0^{2N_0} \left(\frac{g_0}{f_0}\right)^4 
    \\ & \quad \times
    \operatorname{Tr}[
        (\mathcal{A}^{(0)})^{N_0-2} (\mathcal{B}^{(0)})^{N_0-2}
        \mathcal{A}'^{(0)} \mathcal{B}'^{(0)} 
        \mathcal{C}^{(0)} \mathcal{D}^{(0)}
    ]
    \\
    &= f_0^{2N_0} f_1^{2N_1} \left(\frac{g_0 g_1}{f_0 f_1}\right)^4 
    \\ & \quad \times
    \operatorname{Tr}[
        (\mathcal{A}^{(1)})^{N_1-2} (\mathcal{B}^{(1)})^{N_1-2}
        \mathcal{A}'^{(1)} \mathcal{B}'^{(1)} 
        \mathcal{C}^{(1)} \mathcal{D}^{(1)}
    ]
    \\ &= \cdots
\end{align*}
$$

Finally we will reach the $a$th RG step, where $N_a = 2$, i.e. the network is reduced to the four tensors A', B', C, D. Then

$$
\begin{align*}
    \langle \psi |\mathcal{O}| \psi \rangle 
    &= f_0^{2N_0} \cdots f_a^{2N_a} 
    \left(\frac{g_0 \cdots g_a}{f_0 \cdots f_a}\right)^4 
    \\ & \quad \times
    \underbrace{
        \operatorname{Tr}[
            \mathcal{A}'^{(a)} \mathcal{B}'^{(a)} 
            \mathcal{C}^{(a)} \mathcal{D}^{(a)}
        ]
    }_{\text{normalized to 1}}
    \\ 
    &= f_0^{2N_0} \cdots f_a^{2N_a} 
    \left(\frac{g_0 \cdots g_a}{f_0 \cdots f_a}\right)^4 
\end{align*}
$$

The series of $f_i$ factors in the front can be eliminated by the denominator:

$$
\begin{align*}
    \langle \psi|\psi \rangle 
    &= \operatorname{Tr} (A^{(0)} B^{(0)})^{N_0}
    \\
    &= f_0^{2N_0} 
    \operatorname{Tr} (\mathcal{A}^{(0)} \mathcal{B}^{(0)})^{N_0}
    \\
    &= f_0^{2N_0}
    \operatorname{Tr} (f_1 \mathcal{A}^{(1)} f_1 \mathcal{B}^{(1)})^{N_1}
    \\
    &= f_0^{2N_0} f_1^{2N_1}
    \operatorname{Tr} (\mathcal{A}^{(1)} \mathcal{B}^{(1)})^{N_1}
    \\
    & \cdots \quad \text{(after } a \text{ RG steps)}
    \\
    &= f_0^{2N_0} \cdots f_a^{2N_a}
    \underbrace{
        \operatorname{Tr} 
        (\mathcal{A}^{(a)} \mathcal{B}^{(a)})^{N_a}
    }_{\text{normalized to 1}}
    \\
    &= f_0^{2N_0} \cdots f_a^{2N_a}
\end{align*}
$$

Finally, we obtain

<div class="result">

**Expectation Value on 2D Tensor Product State**

$$
\frac{\langle \psi | \mathcal{O} |\psi \rangle}
{\langle \psi |\psi \rangle}
= \left(\frac{g_0 \cdots g_a}{f_0 \cdots f_a}\right)^4 
$$

</div><br>

<div class="remark">

*Remark*: From this expression we see that the ratio $g_a / f_a$ must converge to 1 if the TNR algorithm works correctly. 

</div><br>
