# Conformal Invariance

The subject **conformal field theory** studies (classical or quantum) theories that are invariant under **conformal transformations** (angle-preserving maps), which are defined as:

<div class="result">

*(Reference: [Physics Stack Exchange](https://physics.stackexchange.com/q/469205/222821))*

A **conformal transformation** of the coordinates is an *invertible* coordinate-change mapping $x \mapsto x'$ which scales the metric *locally*:

$$
g'_{\mu \nu}(x')
= \Lambda(x) g_{\mu \nu}(x)
$$

All conformal transformations with the usual mapping composition form a group, called the **conformal group**. 

</div><br>

<div class="remark">

*Remark*: 

- *(Reference: [Physics Stack Exchange](https://physics.stackexchange.com/q/38138/222821), arXiv 1702.07079)*

    There is a concept very similar to conformal transformation, called the **Weyl transformation**. Its effect on the metric is also
        
    $$
    g'_{\mu \nu}(x) = \Lambda(x) g_{\mu \nu}(x)
    $$

    but it *actively* modify the metric, and is *in general not* a coordinate transformation. We can also say that a conformal transformation is a *coordinate transformation* which has the same effect on the metric as a Weyl transformation.

- In $d = 1$, the metric tensor reduces to a single number. Then the requirement above is satisfied by any smooth change of coordinates. Thus we shall consider only $d \ge 2$.

</div><br>

In particular, CFT in **two dimensional** spaces is special and important:
    
- It can be defined in a rather abstract way via *operator algebras* and their representation theory without knowing the Lagrangian action (*bootstrap approach*)

- The algebra of infinitesimal conformal transformations in 2D is *infinite dimensional* and therefore highly constraining. (e.g. we can determine the general form of 2-point and 3-point *correlation functions* without knowing the details of the system)

    *Digression*: An **algebra** $A$ over a field $K$ is a *vector space* equipped with a bilinear product $[\_,\_]: A\times A \to A$ (e.g. the Lie bracket). Its **dimension** is the number of infinitesimal transformation generators. These generators will be later known as $L_n \, (n \in \Z)$

Important examples (or applications) of CFT include:

- Free massless boson field
- Continuum description at a second-order phase transition for 2D statistical models (fixed points of renormalization group flow)
- String theory

## Infinitesimal Conformal Transformation

Let us see what constraints will be imposed on the infinitesimal transformations:

$$
x^{\mu}\to x'^{\mu}=x^{\mu}+\epsilon^{\mu}(x)
$$

The scaling $\Lambda(x)$ will be later determined from $\epsilon(x)$. Under a general coordinate transformation, the metric transforms as

$$
g_{\mu \nu}^{\prime}(x')
= 
\frac{\partial x^{\rho}}{\partial x'^{\mu}}
\frac{\partial x^{\sigma}}{\partial x'^{\nu}}
g_{\rho \sigma}(x)
$$

For current purposes, we always assume that we are originally in *flat* space $\R^{p,q}$, i.e.

$$
g_{\mu \nu}(x) = \eta_{\mu \nu}
= \operatorname{diag}(
    \underbrace{1, \,\cdots, 1}_{p}, 
    \underbrace{-1, \,\cdots, -1}_{q}
)
$$

Then one can show that

<div class="result">

**Requirement on infinitesimal conformal transformations $\epsilon(x)$ <br> (Conformal Killing equations)**

$$
\begin{gathered}
    \partial_{\mu} \epsilon_{\nu}(x)
    + \partial_{\nu} \epsilon_{\mu}(x)
    = f(x) \eta_{\mu \nu}
    \\[0.6em]
    f(x) \equiv 1 - \Lambda(x) = \frac{2}{d} (\partial \cdot \epsilon) (x)
\end{gathered}
$$

</div><br>

*Proof*: Consider the infinitesimal transformation

$$
x^{\mu}\to x'^{\mu}=x^{\mu}+\epsilon^{\mu}(x)
$$

The metric transforms according to the law

$$
g_{\mu \nu}^{\prime}\left(x'\right)
= 
\frac{\partial x^{\rho}}{\partial x'^{\mu}}
\frac{\partial x^{\sigma}}{\partial x'^{\nu}}
g_{\rho \sigma}(x)
$$

Here the partial derivatives are

$$
\frac{\partial x^{\rho}}{\partial x'^{\mu}}
= \frac{\partial}{\partial x'^{\mu}}[
    x'^{\rho} 
    - \epsilon^{\rho}(x(x'))
]
= 
\delta_{\mu}^{\rho}
- \frac{\partial x^{\alpha}}{\partial x'^{\mu}}
\frac{\partial \epsilon^{\rho}}{\partial x^{\alpha}}
$$

But we know that $\partial x^{\alpha}/\partial x'^{\mu} = \delta_{\mu}^{\alpha} + O(\epsilon)$, then up to first order in $\epsilon$

$$
\frac{\partial x^{\rho}}{\partial x'^{\mu}}
= \delta_{\mu}^{\rho}
- \frac{\partial \epsilon^{\rho}(x)}{\partial x^{\mu}}
+ O(\epsilon^2)
$$

Then

$$
\begin{align*}
    g_{\mu \nu}^{\prime}\left(x'\right)
    &\simeq \left(
        \delta_{\mu}^{\rho}
        - \frac{\partial \epsilon^{\rho}(x)}{\partial x^{\mu}}
    \right) \left(
        \delta_{\nu}^{\sigma}
        - \frac{\partial \epsilon^{\sigma}(x)}{\partial x^{\nu}}
    \right) g_{\rho \sigma}(x)
    \\
    &\simeq (
        \delta_{\mu}^{\rho}\delta_{\nu}^{\sigma}
        - \delta_{\mu}^{\rho} \partial_{\nu} \epsilon^{\sigma}(x)
        - \delta_{\nu}^{\sigma} \partial_{\mu} \epsilon^{\rho}(x)
    ) g_{\rho \sigma}(x)
    \\
    &= g_{\mu \nu}(x)
    - g_{\mu \sigma}(x) \partial_{\nu} \epsilon^{\sigma}(x)
    - g_{\rho \nu}(x) \partial_{\mu} \epsilon^{\rho}(x)
\end{align*}
$$

For current purposes, we always assume that we are originally in *flat* (Euclidean) spacetime, i.e.

$$
g_{\mu \nu}(x) = \eta_{\mu \nu}
= \text{diag}(1,...,1)
$$

Then

$$
g_{\mu \nu}^{\prime}\left(x'\right)
= \eta_{\mu \nu}
- \partial_{\nu}\epsilon_{\mu}(x)
- \partial_{\mu}\epsilon_{\nu}(x)
$$

Then we get the requirement on the transformation

$$
\partial_{\mu} \epsilon_{\nu}(x)
+ \partial_{\nu} \epsilon_{\mu}(x)
= f(x) \eta_{\mu \nu}
$$

By taking trace of both sides, we can determine the factor $f(x)$:

$$
f(x) = \frac{2}{d} \partial_{\rho} \epsilon^{\rho}(x)
\tag*{$\blacksquare$}
$$

<div class="remark">

*Remark*: Some useful corollaries follow.

$$
\begin{align*}
    2 \partial_\mu \partial_{\nu} \epsilon_{\rho}
    &= \eta_{\rho \mu} \partial_\nu f
    + \eta_{\nu \rho} \partial_\mu f
    - \eta_{\mu \nu} \partial_\rho f
    &\quad (1)
    \\[0.5em]
    2 \partial^2 \epsilon_\mu 
    &= (2 - d) \partial_\mu f
    &\quad (2)
    \\[0.5em]
    (d - 1) \partial^2 f &= 0
    \qquad (d \ne 2)
    &\quad (3)
\end{align*}
$$

From (2) (3) we see that the case $d = 2$ will be different from the others. Thus we shall discuss $d = 2$ and $d \ge 3$ separately. 

</div><br>

*Proof*: 

1. Take derivative of the general requirement and permute indices

    $$
    \begin{align*}
        -: &\quad 
        \partial_\rho \partial_{\mu} \epsilon_{\nu}(x)
        + \partial_\rho \partial_{\nu} \epsilon_{\mu}(x)
        = \partial_\rho [f(x) \eta_{\mu \nu}]
        \\
        +: &\quad 
        \partial_\mu \partial_{\nu} \epsilon_{\rho}(x)
        + \partial_\mu \partial_{\rho} \epsilon_{\nu}(x)
        = \partial_\mu [f(x) \eta_{\rho \nu}]
        \\
        +: &\quad 
        \partial_\nu \partial_{\rho} \epsilon_{\mu}(x)
        + \partial_\nu \partial_{\mu} \epsilon_{\rho}(x)
        = \partial_\nu [f(x) \eta_{\rho \mu}]
    \end{align*}
    $$

    Add these together (with sign described above)

    $$
    \tag{1}
    2 \partial_\mu \partial_{\nu} \epsilon_{\rho}
    = \eta_{\rho \mu} \partial_\nu f
    + \eta_{\nu \rho} \partial_\mu f
    - \eta_{\mu \nu} \partial_\rho f
    $$

2. Contract Corollary 1 with $\eta^{\mu \nu}$

    $$
    \tag{2}
    2 \partial^2 \epsilon_\mu 
    = (2 - d) \partial_\mu f
    $$

    From this equation we see that the case $d = 2$ will be different from the others.

3. Take $\partial^2$ on the general requirement:

    $$
    \eta_{\mu \nu} \partial^2 f
    = \partial^2 (
        \partial_{\mu} \epsilon_{\nu}
        + \partial_{\nu} \epsilon_{\mu}
    )
    $$
    
    Take $\partial_\nu$ on Corollary 2:
    
    $$
    \begin{align*}
        (2 - d) \partial_\nu \partial_\mu f
        &= 2 \partial_\nu \partial^2 \epsilon_\mu 
        = 2 \partial^2 \partial_\nu  \epsilon_\mu 
        &\quad (\text{i})
        \\
        (2 - d) \partial_\mu \partial_\nu f
        &= 2 \partial^2 \partial_\mu \epsilon_\nu 
        \quad (\text{Exchange } \mu, \nu)
        &\quad (\text{ii})
    \end{align*}
    $$

    Then we add half of (i) and half of (ii) to obtain

    $$
    \begin{align*}
        (2 - d) \partial_\mu \partial_\nu f
        &= \partial^2 (
            \partial_{\mu} \epsilon_{\nu}
            + \partial_{\nu} \epsilon_{\mu}
        ) \\
        &= \eta_{\mu \nu} \partial^2 f
    \end{align*}
    $$

    <div class="remark">

    *Remark*: This step makes sense only when $d \ne 2$; otherwise we can take any combination of the two equations.

    </div><br>

    Contract with $\eta^{\mu \nu}$:

    $$
    (2-d) \partial^2 f = d \partial^2 f
    $$

    or simply

    $$
    \tag{3}
    (d - 1) \partial^2 f = 0 \qquad (d \ne 2)
    $$
