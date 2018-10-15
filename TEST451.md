## TEST451计算$C_d$
### 1. WWWIII模式手册
> Tolman, H. L. (2014). User manual and system documentation of WAVEWATCH III  version 4.18

<font color=#0099 size=5>WWWIII模式中的$S_{in}$ and $S_{ds}$</font>

Switch | Origination| Provided| Cd
--- |---|---    |---
ST1 | WAM cycle 3  |Snyder et al 1981 <br> Komen et al 1984| $u_*=u_{10}\sqrt{(0.8+0.065u_{10}10^{-3})}$
ST2 | WWWIII    | Tolman and Chalikov 1996| $\lambda_a=\frac{2\pi}{k\mid(\theta-\theta_w\mid}$   $\lambda$ :波长 <br> $C_r=10^{-3}(0.021+\frac{10.4}{R^{1.23}+1.85})$<br> $C_\lambda=C_r(\frac{u_a}{u_\lambda})^2$
ST3 | WAM cycle 4 (ECWAM)| Janssen 2004 $S_{in}$ <br> Ardhuin et al 2009a $S_{ds}$ 考虑涌浪| 如下子标题
ST4 | WWWIII| Ardhuin et al. 2010 <br>$S_{in}$ 减小高频和高风速下风能输入| reduction of $u_*$ is implemented in <br> order to allow  a balance with <br> a saturation-based dissipation. <br> This is done by reducing the <br> wind input for  high frequencies and  high winds.


#### ST3 - Janssen 2004 提出的Cd计算方法：
<center>
<img src="https://note.youdao.com/yws/public/resource/4f66fd58de9eb2118f8590f4d083028a/xmlnote/C9A3DA76F72243768A935BFEA008050C/21176" width=70% height=70% />
<img src="https://note.youdao.com/yws/public/resource/4f66fd58de9eb2118f8590f4d083028a/xmlnote/199B0CAB07A24641BD6893DD91256419/21178" width=70% height=70% />
</center>

where $\tau = u_*^2$
, and $z_u$ is the height at which the wind is specified. These two
equations provide an implicit functional dependence of $u_*$ on $U_{10}$ and $\tau_w/\tau$.
This relationship is tabulated (Janssen, 1991; Bidlot et al., 2007).

<center>
<img src="https://note.youdao.com/yws/public/resource/4f66fd58de9eb2118f8590f4d083028a/xmlnote/02C20B1101AF4D3C8BC744FF38D2AD2B/21257" width=70% height=70% />

Table 2.4: Parameter values for WAM4, BJA and the 2012 update in the
ECWAM model.
</center>

#### ST4 - TEST451在 Janssen2004 基础上做的改进：
This parameterization uses a positive part of the wind input that is taken
from WAM cycle 4, with an ad hoc reduction of $u_*$ is implemented in order
to allow a balance with a saturation-based dissipation. This correction also
reduces the drag coefficient at high winds. This is done by reducing the
wind input for high frequencies and high winds. For this, $u_*$ in eq. (2.90) is
replaced by $u'_*(k)$ defined for each frequency as


<center>
<img src="https://note.youdao.com/yws/public/resource/4f66fd58de9eb2118f8590f4d083028a/xmlnote/DEFF2D3362474B08B8B50E2D21A5D207/21187" width=70% height=70% />

</center>

where the sheltering coefficient $|s_u|\sim 1$ can be used to tune the stresses at high winds, which would be largely overestimated for $|s_u|= 0$. For $|s_u|>0$ this sheltering is also applied within the diagnostic tail in eq. (2.95),
which requires the estimation of a 3-dimensional look-up table for the high
frequency stress, the third parameter being the energy level of the tail.


<center>
<img src="https://note.youdao.com/yws/public/resource/4f66fd58de9eb2118f8590f4d083028a/xmlnote/434DE57B503547C38E900FAA43AEB47D/21253" width=80% height=70% />

</center>


---
### 2. Rascle 2013

Rascle, N. and F. Ardhuin (2013). "A global wave parameter database for geophysical applications. Part 2: Model validation with improved source term parameterization." Ocean Modelling 70: 174-188.
<center>
<img src="https://note.youdao.com/yws/public/resource/4f66fd58de9eb2118f8590f4d083028a/xmlnote/3C1BF5FC37574753B7AB769A892E9221/21096" width=70% height=70% />


Figure 2 拖曳系数

</center>


<font color=#0099ff size=4>Figure2a and 2b</font>拖曳系数计算：
$$
C_d=\frac{u^{*2}}{u_{10}^2}
$$

已知这种阻力系数随着风速而增加，但是也被认为取决于波浪年龄，陡峭的年轻波的值更大（参见Drennan等人（2005）对专用现场实验的回顾）。 其他实验未必报告如此强烈的依赖性（Edson等，2007），但这可能是由于风速与此类数据集中的波浪年龄的固有相关性。 定量计算如<font color=#0099ff size=4>Figure2c</font>所示，其中我们使用Drennan等人的经验公式。 （2005年，他们的方程（4）），

$$
C_d=(\frac{1}{k}log\frac{10}{z_{0}})^{-2}
$$
$$
\frac{z_0}{H_s}=3.35(\frac{u^*}{C_p})^{3.4}
$$


相比之下，BJA参数化产生了$C_D$的合理依赖性（图12b），而新参数化TEST451看起来几乎独立于波浪年龄（图12a）。 这显然是由于风输入参数化的唯一变化，即引入遮蔽效应，其降低了较短波浪分量的表观应力。 显然需要进一步的工作来改进和验证新参数化中的气 - 波动量交换，特别是因为波浪支撑的应力可能是不现实的。 进一步的工作可能会调查如何减少避难期限.这可能需要增加耗散以保持光谱尾部的正确平衡。 由于摩擦速度 $u^*$ 不仅仅是波模型的诊断参数，而是进入风力发电项的参数，因此还预期增加特定于年轻波的 $u^*$ 可以帮助减少短取的低波高偏差。
