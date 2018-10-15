## COAWST 修改版
https://www.researchgate.net/project/Updating-the-COAWST-WRF-ROMS-SWAN-CICE5-world
<center>
<img src="https://www.researchgate.net/profile/Guoqiang_Liu5/project/Updating-the-COAWST-WRF-ROMS-SWAN-CICE5-world/attachment/5adcc1c7b53d2f63c3c75b19/AS:618263725756423@1524416967769/image/holland_stokes.tif" width=50% height=30% />

Figure 1 四种不同的stokes参数化方法得到的飓风条件下stokes drift 剖面，单色波参数法在近表面产生高估，在deep Stokes drift产生低估

<img src="https://www.researchgate.net/profile/Guoqiang_Liu5/project/Updating-the-COAWST-WRF-ROMS-SWAN-CICE5-world/attachment/5adcc1c84cde260d15da472a/AS:618263729950722@1524416968122/image/Figure.1.tif" width=100% height=90% />

Figure 2  COAWST修改示意图

</center>

---

### 1. 将斯托克斯漂从SWAN移植到ROMS

$Langrange = Euler + Stokes$

斯托克斯漂：$u_{SD}\equiv \overline{\xi \cdot \Delta u}$

$u$是线性波波速，$\xi$是相应的线性位移，$\partial\xi/\partial t=u$。

 传统上，海浪和海洋已经被单独建模，每个都受到大气通量的强迫而没有反馈到大气边界层或波与海洋表面边界层（OSBL）之间的通量交换。这不对的，因为海洋模型不能计算表面波。应该修改运动方程，湍流动能（TKE）预算和其他守恒方程，以解释表面波的影响。原则上，这需要计算完整的二维波谱，因为斯托克斯在给定垂直水平上的漂移需要Kenyon[26] 在（2.4）的积分。对于大多数模型系统来说，这对计算要求太高且不切实际，尽管Webb & Fox-Kemper [75]通过偶合WAVEWATCH-III模型[采用全二维波谱97 ]在the Community Earth System Model社区地球系统模型[98]这样做过。取而代之的是，简化波场（单色波）经常被使用的[99 - 104]。

但是利用单色波表示也存在问题：宽频谱的Stokes drift 的垂直剪切速率要强于单色波的。此外由于宽频谱包含更长的波，宽频谱的Stokes drift在深处要强于单色波，穿透更深。虽然在宽带风力波谱下存在更接近斯托克斯漂移剖面的近似剖面[ 106 ]，但很明显，为了在风浪和涌浪混合条件下充分模拟斯托克斯剖面，完整的两个维波谱必须通过波浪模型来表示（见[ 107 - 112]用于第三代波浪模型的示例和描述）。这只能通过将波浪模型与海洋模型耦合来实现。

随着斯托克斯漂移进入波动平均动量方程，以及示踪平流方程和TKE方程，很明显必须估计其对欧拉海洋模型中循环和水文的重要性。McWilliams & Restrepo [128]使用风力气候学来评估通过添加科里奥利 - 斯托克斯和涡旋力以及斯托克斯漂移到示踪平流方程对大气环流的影响。这些作者发现，在热带地区，影响确实非常显着，波浪效应高达风力驱动的埃克曼运输的40％。
> van den Bremer, T. S. and Ø. Breivik (2018). "Stokes drift."  376(2111).
#### 1.1 Stokes drift in the momentum and tracer advection equations
<font color=#0099F size=5>Craik–Leibovich动量方程：</font>
$$
\partial_tu + u \cdot \Delta u + 2\Omega \times u_{SD} + \Delta(\pi +u \cdot u_{SD}) = u_{SD} \times (\Delta \times u) + \nu \Delta^2u
$$

- Coriolis-Stokes力： $2\Omega \times u_{SD}$

- Craik–Leibovich 涡旋力：$u_{SD} \times (\Delta \times u)$, 这一项在近岸非常的重要，对于全球海洋的Langmuir湍流也非常重要。
- 压力校正：$\Delta(\pi +u \cdot u_{SD})$

<font color=#0099F size=5>扩散方程：</font>

$$
\frac{Dc}{Dt}+SGS=-u_{SD} \cdot \Delta c \\
其中SGS表示sub-grid~ scale~ effects。
$$
- 引入Stokes平流项，以便欧拉海洋模型适当地考虑未解决的波浪效应。

#### 1.2 朗缪尔湍流

CL提出了两种不稳定机制来解释朗缪尔环流的生成机制：

CL1: 斯托克斯在横风方向漂移的周期性，如果 $u_{SD}$ 在恒风方向变化不稳定，由vortex force引起的直接驱动不稳定，不能够被平衡，因此产生旋转。

CL2：由斯托克斯漂移的垂直剪切引起的，由于平均表面流场进入水平面的可能很小的扰动，倾斜垂直涡度。这已被称为CL2不稳定机制。这里，不需要相干波结构，只有欧拉电流中的水平剪切。只有CL2被认为在开阔的海洋中具有重要意义，因为没有任何迹象表明斯托克斯在广阔的风 - 海频谱下漂移会在横风方向上表现出所需的周期性。

TKE方程：
$$ \frac{De}{Dt}=\nu_{m}S^2-\nu_hN^2+\nu_mS\cdot\frac{\partial \bf{v}_s}{\partial z} - \frac{\partial}{\partial z}(\overline{w'e})-\frac{1}{\rho_w}\frac{\partial}{\partial z}(\overline{w'p'}) - \epsilon $$

这里$e$表示单位质量湍动能，$w'e'$ 和 $w'p'$ 是湍流出传输和压力校正项。剪切生成项 ${\bf{S}}\cdot {\bf{S}}=S^2=(\partial\overline{u}/\partial z)^2$，浮力生成项$N^2=-(g/\rho_w)d\rho_w/dz$。$\nu _{h,m}$ 是湍流扩散系数， $\epsilon$ 代表TKE耗散。$\nu_mS\cdot{\partial \bf{v}_s}/{\partial z}$ 代表朗缪尔湍流生成项，**注意**，该项包含Stokes drift 剪切，这个量随深度急剧下降，显然朗缪尔产生项的任何参数化都严重依赖于斯托克斯漂移速度剖面的形式。

---
#### 1.3 Stokes drift velocity profiles 参数化
<center>
<img src="https://www.researchgate.net/profile/Guoqiang_Liu5/project/Updating-the-COAWST-WRF-ROMS-SWAN-CICE5-world/attachment/591701621042bf5867e52997/AS:493537453776896@1494679906126/image/Stokes_profiles.png" width=70% height=70% />

Figure 3  不同的stokes 参数化方案得到的剖面图

</center>
cpp文件中，以下选项必须选一个

- SWAN_STOKES

- SWAN_TRANSPORT
- BREIVIK_PHILLIPS
- SHALLOW_STK
- SPECTRUM_STK


```c
#define SWAN_STOKES      !based on the surface wave bulk parameters

#define SWAN_TRANSPORT   !based on Breivik et al., 2014 JPO

#define BREIVIK_PHILIPS  !based on the Philips spectrum, see Breivik et al., 2016

#define STOKES_SPECTRUM  !based on the surface wave Stokes drift spectrum
```
<center>
<img src="https://ars.els-cdn.com/content/image/1-s2.0-S1463500316000159-gr1_lrg.jpg" width=1000% height=50% />

Figure 3  不同的stokes 参数化方案得到的剖面图

</center>

##### 1. 谱积分方法
$$
{\bf{v}_s}(z)=\frac{2}{g}\int_{0}^{2\pi}\int_0^\infty\omega^3{\bf{\hat{k}}}e^{2kz}E(\omega,\theta)d\omega d\theta
$$

$\theta$是波浪传播方向，$\omega$是圆频率，$\bf{\hat{k}}$ 是波浪传播方向上的单位矢量。

##### 2. 单色波参数法

根据Kenyon 1969 提出的深海频散关系 $\omega^2=gk$ ，谱积分表达式可以通过波数谱在任意深度的表达式进一步推导出斯托克斯漂速度：
$$
v_s(z)=\frac{2}{g}\int_{0}^{\infty}\omega^3F(\omega)e^{2kz}d\omega
$$
其中
$$
F(\omega)\equiv\int_0^{2\pi}E(\omega,\theta)d\theta
$$

因此，斯托克斯漂与the third spectral moment ($\omega^3$)呈比例，这里定义$m_n=\int_0^\infty\omega^nF(\omega)d\omega$，表层斯托克斯漂速度表示为：
$$
v_0=2m_3/g
$$
**单色波剖面**即为
$$
v_m=v_0e^{2k_mz}
$$
$k_m$平均波数。

##### 3. 指数参数法 (Breivik et al.2014)

$$
v_e=v_0\frac{e^{2k_ez}}{{1-Ck_ez}}
$$
$C=8$是最优的，$k_e$逆深度尺度。

**指数法**要好于**单色波法**，均方根误差能减少60%，被用于欧洲集合预报系统，见Janssen et al. 2013 and Breivik et al.2015。

##### 4. Philips方法 (Breivik et al. 2016)
$$
v_{Phil}(z)=2\alpha g\int_{\omega_p}^\infty \omega^{-2}e^{2\omega^2z/g}d\omega
$$
基于深海频散关系 $\omega^2=gh$, 对于Phillips波谱， $v_{phil}$ 可写为：
$$
v_{phil}(z)=\frac{2\alpha g}{\omega_p}[e^{2k_pz}-\sqrt{-2\pi k_pz}erfc (\sqrt{-2k_pz})]
$$
$erfc$ 是余差函数，$k_p=\omega_p^2/g$是峰值波数。因此，表层斯托克斯漂速度表示为
$$
v_0\equiv v_{Phil}(z=0)=\frac{2\alpha g}{\omega_p}
$$
只对 $\omega_p$以上频率进行积分，并经过技巧性的计算和近似，可以得到**Philips stokes profile近似**：
$$
v_s(z)\approx v_0[e^{2k_pz}-\beta \sqrt{-2k_p\pi z}erfc(\sqrt{-2k_p z})]
$$
可以得到斯托克斯输运：
$$
V=\frac{v_0}{2k_p}(1-2\beta/3)
$$
对于波浪模式，斯托克斯漂和斯托克斯输运是已知的，因此逆深度尺度 $\overline{k}$ 表层斯托克斯漂速度表示为
$$
\overline{k}=\frac{v_0}{2V}(1-2\beta /3)
$$
相比于指数法，Philips法更能匹配斯托克斯剖面，特别是对接近表面的shear表达。


---

### 2. 从SWAN计算风应力

用于将波浪引起的应力传递到ROMS的新CPP选项
- SWAN_STRESS

用于传输斯托克斯漂移曲线的新CPP选项：
- SWAN_STOKES

- SWAN_TRANSPORT
- BREIVIK_PHILLIPS
- SHALLOW_STK（3D斯托克斯漂移）
