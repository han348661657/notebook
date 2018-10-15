### 计算Stokes drift 的名词

![图表](https://note.youdao.com/yws/public/resource/7581d8ae6aefd5ae9cb6a2cf5250d5d6/xmlnote/AA094377EDD84ADCA3455028493A3BAC/21767)
- SWAN_STOKES: Stokes drift velocity is computed by SWAN.

- SWAN_STRESS: $\tau_{oc}$ stress is computed by SWAN.
- SWAN_TRANSPORT: Stokes drift transport is computed by SWAN.
- ROMSWN_WSTAR: $\tau_{air}$ is supplied by ROMS
- BREIVIK_PHILLIPS: Stokes profile is computed by Breivik method
- SHALLOW_STK: Stokes profile in shallow water
- SPECTRUM_STK: Stokes drift spectrum

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
#### SWAN PRINTS STOKES PROFILE

![figure2](https://note.youdao.com/yws/public/resource/7581d8ae6aefd5ae9cb6a2cf5250d5d6/xmlnote/ACC4CA2E5B8E46EAB490439999695451/21770)

a. PROF_STOKES1, basic Stokes in charge.

b. PROF_STOKES2, transport formulation in charge.

c. PROF_STOKES3, Breivik's method in charge.

d. PROF_STOKES4, Stokes in shallow water in charge.

---
#### cpp文件中，以下选项只选一个

- SWAN_STOKES

- SWAN_TRANSPORT
- BREIVIK_PHILLIPS
- SHALLOW_STK
- SPECTRUM_STK

**问题**

SWAN_STOKES 和 BULK_STOKES 的区别

### Case - - Holland_stokes

```c
#define ROMS_MODEL
#define SWAN_MODEL
#define MCT_LIB
/* Coupling parameters */
#define    SWAN_STRESS
#undef     BULK_STOKES
#define    SPECTRUM_STK
#undef     SWAN_TRANSPORT
#undef     BREIVIK_PHILLIPS
#define    PROFILE_STK
#define    PROF_STOKES4

```
