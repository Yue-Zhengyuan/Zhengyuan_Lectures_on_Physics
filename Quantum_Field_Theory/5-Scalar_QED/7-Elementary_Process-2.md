# Elementary Processes of Scalar QED

<font size=5>

**Part 2: Particle Scattering**

</font>

In this part we introduce *multiple scalar fields* into the scalar QED theory. Consider two (uncoupled) complex scalar fields $\phi, \bar{\phi}$ and $\chi, \bar{\chi}$, of masses $m_\phi, m_\chi$ and charges $Q_\phi, Q_\chi$ respectively. The modified Lagrangian is

$$
\mathcal{L} 
= -\frac{1}{4} F_{\mu \nu}^2
+ |D_\mu^{(\phi)} \phi|^2 + |D_\mu^{(\chi)} \chi|^2
- m_\phi^2 |\phi|^2 - m_\chi^2 |\chi|^2
$$

with

$$
D_\mu^{(\phi)} \phi = \partial_\mu \phi - i e Q_\phi A_\mu \phi
\quad
D_\mu^{(\chi)} \chi = \partial_\mu \chi - i e Q_\chi A_\mu \chi
$$

The fields $\phi, \bar{\phi}$ and $\chi, \bar{\chi}$ are analogs of $e^-, e^+$ and $\mu^-, \mu^+$ in the standard QED. Let us call $\phi$ the "electron", and $\chi$ the "muon".

Since there are no terms containing both $\phi$ and $\chi$, there should be no vertices in the Feynman diagrams that involve both $\phi$ and $\chi$ (or their anti-particles). Other Feynman rules that apply to $\phi, \bar{\phi}$ can be immediately applied to $\chi, \bar{\chi}$ as well. 

## "Electron-to-Muon" Scattering

The "simplest" (according to Peskin and Schroeder) of all QED processes is the following scattering

$$
\phi + \bar{\phi} \to \chi + \bar{\chi}
\\[0.6em]
(\text{analog of } e^- e^+ \to \mu^- \mu^+)
$$

To the lowest order, this corresponds to only one diagram (s-channel):

<center>
<img src="images/ee-mumu.png" height="180px">
</center>

The t- and u- channels are not allowed, since there should be no vertices involving both $\phi$ and $\chi$. The corresponding amplitude is

$$
\begin{align*}
    i \mathcal{M}
    &= \color{green} ieQ_\phi (p_1 - p_2)^\mu
    \color{darkcyan} \frac{-i g_{\mu \nu}}{(p_1 + p_2)^2}
    \color{red} ieQ_\chi (p_3 - p_4)^\nu
    \\
    &= ie^2 Q_\phi Q_\chi 
    \frac{(p_1 - p_2)\cdot (p_3 - p_4)}{(p_1 + p_2)^2}
\end{align*}
$$

Next, consider the kinetics in the CM frame (we have implicitly applied 4-momentum conservation):

<center>
<img src="images/ee-mumu-cm.png" height="160px">
</center>

$$
\def \arraystretch{1.5}
\begin{array}{l|l}
    \text{Initial Momentum} & \text{Final Momentum} \\
    \hline
    p_1^\mu = (E,0,0,p) & 
    p_3^\mu = (E, p'\sin\theta, 0, p'\cos\theta)
    \\
    p_2^\mu = (E,0,0,-p) & 
    p_4^\mu = (E, -p'\sin\theta, 0, -p'\cos\theta)
\end{array}
$$

with

$$
E = \sqrt{p^2 + m_\phi^2} = \sqrt{p'^2 + m_\chi^2}
$$ 

Using the kinetics, we can express the amplitude $\mathcal{M}$ as

$$
\begin{align*}
    i\mathcal{M}
    &= ie^2 Q_\phi Q_\chi 
    \frac{(p_1 - p_2)\cdot (p_3 - p_4)}{(p_1 + p_2)^2}
    \\
    &= ie^2 Q_\phi Q_\chi 
    \frac{-2pp'\cos\theta}{E^2}
\end{align*}
$$

From known results of $2\to 2$ scattering in CM frame:

$$
\begin{align*}
    \left( \frac{d\sigma}{d\Omega} \right)_\text{CM}
    &= \frac{1}{64 \pi^2 E_\text{CM}^2} 
    \frac{p_f}{p_i}
    |\mathcal{M}_{fi}|^2
    \\
    &= \frac{1}{64\pi^2 (2E)^2} \frac{p'}{p} (e^4 Q_\phi^2 Q_\chi^2) \frac{4p^2 p'^2 \cos^2\theta}{E^4}
    \\
    &= \frac{\alpha^2 Q_\phi^2 Q_\chi^2}{4} 
    \frac{p p'^3}{E^6} \cos^2\theta
\end{align*}
$$

## Variants of Electron-Muon Scattering

### Electron and Muon

$$
\phi + \chi \to \phi + \chi
\\[0.6em]
(\text{analog of } e^- \mu^- \to e^- \mu^-)
$$

This corresponds to the following diagram (t-channel)

<center>
<img src="images/emu-emu-t.png" height="200px">
</center>

$$
\begin{align*}
    i \mathcal{M}
    &= \color{green} ieQ_\phi (p_1 + p_3)^\mu
    \color{darkcyan} \frac{-i g_{\mu \nu}}{(p_3 - p_1)^2}
    \color{red} ieQ_\chi (p_2 + p_4)^\nu
    \\
    &= ie^2 Q_\phi Q_\chi 
    \frac{(p_1 + p_3)\cdot (p_2 + p_4)}{(p_3 - p_1)^2}
\end{align*}
$$

The s- and u- channel diagrams are not allowed, again because there should be no vertices involving both $\phi$ and $\chi$. Using on-shell conditions, we have

$$
(p_3 - p_1)^2 = 2(m_\phi^2 + p_1\cdot p_3)
$$

<div class="remark">

*Remark*: This amplitude can be obtained from $\phi \bar{\phi} \to \chi \bar{\chi}$ using **cross symmetry**, i.e. the replacement

$$
p_1 \to p_1, \quad p_2 \to -p_3, \quad
p_3 \to p_4, \quad p_4 \to -p_2
$$

</div><br>

Next, consider the kinetics in CM frame:

<center>
<img src="images/emu-emu-cm.png" height="160px">
</center>

$$
\def \arraystretch{1.5}
\begin{array}{l|l}
    \text{Initial Momentum} & \text{Final Momentum} \\
    \hline
    p_1^\mu = (E,0,0,p) & 
    p_3^\mu = (E, p\sin\theta, 0, p\cos\theta)
    \\
    p_2^\mu = (E',0,0,-p) & 
    p_4^\mu = (E', -p\sin\theta, 0, -p\cos\theta)
\end{array}
$$

with

$$
E = \sqrt{p^2 + m_\phi^2}, \quad E' = \sqrt{p'^2 + m_\chi^2}
$$ 

Then the amplitude $\mathcal{M}$ can be expressed as

$$
\begin{align*}
    i \mathcal{M}
    &= ie^2 Q_\phi Q_\chi 
    \frac{(p_1 + p_3)\cdot (p_2 + p_4)}{(p_3 - p_1)^2}
    \\
    &= -ie^2 Q_\phi Q_\chi 
    \frac{p^2(1 + \cos^2\theta) + 2EE'}{p^2(1-\cos\theta)}
\end{align*}
$$ 

From known results of $2\to 2$ scattering in CM frame:

$$
\begin{align*}
    \left( \frac{d\sigma}{d\Omega} \right)_\text{CM}
    &= \frac{1}{64 \pi^2 E_\text{CM}^2} 
    \frac{p_f}{p_i}
    |\mathcal{M}_{fi}|^2
    \\
    &= \frac{1}{64\pi^2 (E + E')^2} (e^4 Q_\phi^2 Q_\chi^2) 
    \left(
        \frac{p^2(1 + \cos^2\theta) + 2EE'}{p^2(1-\cos\theta)}
    \right)^2
    \\
    &= \frac{\alpha^2 Q_\phi^2 Q_\chi^2}{4} 
    \left(
        \frac{p^2(1 + \cos^2\theta) + 2EE'}{p^2(E+E')(1-\cos\theta)}
    \right)^2
\end{align*}
$$

### Electron and Anti-Muon

$$
\phi + \bar{\chi} \to \phi + \bar{\chi}
\\[0.6em]
(\text{analog of } e^- \mu^+ \to e^- \mu^+)
$$

This corresponds to the following diagram (t-channel)

<center>
<img src="images/emubar-emubar-t.png" height="200px">
</center>

$$
\begin{align*}
    i \mathcal{M}
    &= \color{green} ieQ_\phi (p_1 + p_3)^\mu
    \color{darkcyan} \frac{-i g_{\mu \nu}}{(p_3 - p_1)^2}
    \color{red} (-i)eQ_\chi (p_2 + p_4)^\nu
    \\
    &= -ie^2 Q_\phi Q_\chi 
    \frac{(p_1 + p_3)\cdot (p_2 + p_4)}{(p_3 - p_1)^2}
\end{align*}
$$

We merely get an extra minus sign for $\mathcal{M}$ since we are dealing with the anti-particle now. So the result of the differential cross section will be the same as electron-muon scattering derived above. 

## Electron-Electron (Mott) Scattering

This is the scattering

$$
\phi + \phi \to \phi + \phi
\\[0.6em]
(\text{analog of } e^- e^- \to e^- e^-)
$$
