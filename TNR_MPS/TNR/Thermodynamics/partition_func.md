# Calculation of Partition Function

The tensor network represents the partition function as the full conTract of tensors $T_A$ and $T_B$, formally denoted as

$$
Z = \operatorname{Tr} (T_A T_B)^N
$$

where $N$ is the number of $T_A$ (or $T_B$) contained in the tensor network. Here we are considering a tensor network on a bipartite square lattice.

RG tensor flow from step $i$ to $i+1$ (where $i = 0,1,2,...$):

$$
(T_A^{(i)}, T_B^{(i)})
\xrightarrow{\text{RG}}
(T_A^{(i+1)}, T_B^{(i+1)})
$$

RG does not change the partition function, therefore

$$
Z = \operatorname{Tr} (T_A^{(i)} T_B^{(i)})^{N_i}
= \operatorname{Tr} (T_A^{(i+1)} T_B^{(i+1)})^{N_{i+1}}
$$

However, to avoid the tensor elements becoming too large, we need to normalize the tensors after each RG step using some appropriate number $f_i$, which is usually chosen as the *absolute value* of the *quartic root* of the full Trace of the $2\times 2$ Transfer matrix consTructed from $T_A^{(i)}$ and $T_B^{(i)}$ (trace is denoted by `..` below):

```
        :   :
        |   |     
    ..- B - A -..
        |   |
    ..- A - B -..
        |   |
        :   :
```

The normalized tensors are denoted by

$$
(\mathcal{T}_A^{(i)}, \mathcal{T}_B^{(i)})
=\frac{1}{f_i} (T_A^{(i)}, T_B^{(i)})
$$

Therefore, the RG flow of the normalized tensor should be

$$
(\mathcal{T}_A^{(i)}, \mathcal{T}_B^{(i)})
\xrightarrow{\text{RG}} 
f_{i+1} (\mathcal{T}_A^{(i+1)}, \mathcal{T}_B^{(i+1)})
$$

Let us then write the partition function in terms of the normalized tensors.

$$
\begin{align*}
    Z &= \operatorname{Tr} (T_A^{(0)} T_B^{(0)})^{N_0}
    \\
    &= f_0^{2N_0} 
    \operatorname{Tr} (\mathcal{T}_A^{(0)} \mathcal{T}_B^{(0)})^{N_0}
    \\
    &= f_0^{2N_0}
    \operatorname{Tr} (f_1 \mathcal{T}_A^{(1)} f_1 \mathcal{T}_B^{(1)})^{N_1}
    \\
    &= f_0^{2N_0} f_1^{2N_1}
    \operatorname{Tr} (\mathcal{T}_A^{(1)} \mathcal{T}_B^{(1)})^{N_1}
    \\
    & \cdots \quad \text{(after } a \text{ RG steps)}
    \\
    &= f_0^{2N_0} f_1^{2N_1} \cdots f_a^{2N_a}
    \operatorname{Tr} (\mathcal{T}_A^{(a)} \mathcal{T}_B^{(a)})^{N_a}
\end{align*}
$$

Take the logarithm:

$$
\ln Z = \sum_{i=0}^a 2N_i \ln f_i
+ \ln \operatorname{Tr} (\mathcal{T}_A^{(a)} \mathcal{T}_B^{(a)})^{N_a}
$$

Usually the *density* of the free energy $F = -T \ln Z$ (per particle) is more important. 

- For 2D classical models, the system size is equal to the tensor number. Thus the free energy density is

    $$
    - \frac{1}{2N_0} \frac{1}{\beta} \ln Z
    = -\sum_{i=0}^a \frac{N_i}{\beta N_0} \ln f_i
    - \frac{1}{2 \beta N_0}\ln \operatorname{Tr} (\mathcal{T}_A^{(a)} \mathcal{T}_B^{(a)})^{N_a}
    $$

    But $N_0$ is supposed to be a large number, so the second term can be neglected. On the square lattice, the RG step gives

    $$
    N_{i+1} = \frac{N_i}{2} 
    \, \Rightarrow \,
    N_i = \frac{N_0}{2^i}
    $$

    Thus we finally obtain

    <div class="result">

    **Free Energy Density (2D Classical Models)**

    $$
    - \frac{1}{2N_0} \frac{1}{\beta} \ln Z 
    = -\frac{1}{\beta} \sum_{i=0}^a \frac{1}{2^i} \ln f_i
    $$

    </div><br>

- For (1+1)D quantum models, the system size is *twice* (due to construction of tensors from Trotter gates) of the *square root* of the tensor number. Suppose that in the initial network, each row of tensors represents reciprocal temperature $\beta$. Then for the whole network
    
    $$
    \frac{1}{T} = \sqrt{2N_0}\beta
    $$

    Thus the free energy density is

    <div class="result">

    **Free Energy Density (1+1D Quantum Models)**

    $$
    \begin{align*}
        - \frac{1}{2\sqrt{2N_0}} T \ln Z
        &= - \frac{1}{4N_0 \beta} \ln Z
        \\
        &= -\frac{1}{\beta} \sum_{i=0}^a \frac{1}{2^{i+1}} \ln f_i
    \end{align*}
    $$

    </div><br>
    
    which is similar to the classical case. 
    