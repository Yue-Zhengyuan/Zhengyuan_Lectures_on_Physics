# Transposition of Grassmann Tensors

*Program implementation: `gtensor.transpose`*

Let $p \equiv (a,b,...)$ be a permutation of axes of a tensor $\mathbf{T}(\theta)$. The transposed tensor $\mathbf{T}^\prime$ are related to the old tensor $\mathbf{T}$ by

$$
\mathbf{T}^\prime(\theta)_{i_1 i_2 ...}^{n_1 n_2 ...}
=
\mathbf{T}(\theta)_{i_a i_b ...}^{n_a n_b ...}
$$

i.e.

$$
{(T^\prime)}_{i_1 i_2 ...}^{n_1 n_2 ...}
\theta_1^{n_1} \theta_2^{n_2} \cdots
= T_{i_a i_b ...}^{n_a n_b ...} 
\theta_a^{n_a} \theta_b^{n_b} \cdots
$$

Note that due to the anti-commutativity of Grassmann numbers, the tensor elements $T$ may acquire sign changes:

$$
{(T^\prime)}_{i_1 i_2 ...}^{n_1 n_2 ...}
= (-1)^{P(p|n)} 
T_{i_a i_b ...}^{n_a n_b ...} 
$$

where $P(p|n)$ is the parity of the sub-permutation of nonzero Grassmann indices $\{n\}$. 

In particular, the *full transposition* (reverse of axis order) will be denoted by $\mathbf{T}^\mathsf{T}$:

$$
\begin{align*}
    \mathbf{T}^\mathsf{T}(\theta)_{i_1 ... i_r}^{n_1 ... n_r}
    &= (-1)^{P(p|n)} T_{i_r ... i_1}^{n_r ... n_1} 
    \theta_1^{n_1} ... \theta_r^{n_r}
    \\
    &= (-1)^{P(p|n)} (T^\mathsf{T})_{i_1 ... i_r}^{n_1 ... n_r} 
    \theta_1^{n_1} ... \theta_r^{n_r}
\end{align*}
$$

This is implemented as `GTensor.T`.

<div class="remark">

*Remark*: 

- To improve program efficiency, the $(-1)^P$ signs are stored in the member `_gSign` of the class `GTensor`, which can be absorbed into the `_blocks` using the method `absorb_sign` if needed.

</div><br>