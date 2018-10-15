### pyroms安装

* [markdown-toc](###1.安装环境)

---
官网：https://github.com/ESMG/pyroms

[Mac os 安装流程](https://houstonthereisaproblem.blogspot.tw/2011/12/installation-of-pyroms-into-mac-os-1072.html)


---
### 1. 安装环境
 * numpy 自带
 * scipy 自带
 * matplotlib 自带
 * [basemap from matplotlib](https://jaist.dl.sourceforge.net/project/matplotlib/matplotlib-toolkits/basemap-1.0.7/basemap-1.0.7.tar.gz)
 * [netcdf4](https://pypi.python.org/pypi/netCDF4/1.3.1)
 * liblpsolve55
 * [natgrid](http://github.com/matplotlib/natgrid) for at least one of the examples.
> 利用阿里镜像安装
```sh
pip3 install scipy matplotlib netcdf4  -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
```
#### 1.1 netcdf4 for python 安装
```sh
pip install netCDF4-1.3.1-cp36-cp36m-manylinux1_x86_64.

# 声明已安装的netcdf4 for fortran
export PATH=/data/soft/netcdf4.4/intel/bin:$PATH
```
#### 1.2 basemap 安装

##### 2018.9最新安装，亲测可行:
```shell
conda install basemap
```
如果安装过程出现权限问题：
```shell
# ubuntu conda 更新、下载模块包权限问题 'Permission denied'
sudo chown -R henry:henry /home/henry/anaconda3
```
安装完成后，如果出现以下错误：
```shell
pyproj_datadir = os.environ['PROJ_LIB']
epsgf = open(os.path.join(pyproj_datadir,'epsg'))
KeyError: 'PROJ_LIB'
```
解决方法：
查找包含epsg文件的路径，并在环境中声明
```shell
export PROJ_LIB=/home/henry/anaconda3/pkgs/proj4-5.1.0-h470a237_2/share/proj
```
---
>这些是Python的地图工具，在示例目录（用户注意）中使用etopo2。

官网：https://matplotlib.org/basemap/users/installing.html

**1.安装 [proj](http://proj4.org/download.html#linux)**

> PROJ是一种标准的UNIX过滤器功能，可将地理的经度和纬度坐标转换为笛卡尔坐标
 （反之亦然），它是一个CAPI，供软件开发人员将坐标转换包含在其自己的软件中。

**<font color=#00969 size=4>ubuntu安装 pyproj  -2018.9.9</font>**
```python
conda install pyproj
```

**2. 安装geos**
>GEOS（几何引擎 - 开源）是Java拓扑套件（JTS）的C ++端口。
因此，它的目标是在C ++中包含JTS的完整功能。 这包括所有用于SQL空间谓词函
数和空间运算符的OpenGIS Simple特性，以及特定的JTS增强拓扑函数。
```shell
# 解压basemap安装包
cd geos-3.3.3
export GEOS_DIR=<where you want the libs and headers to go>
# A reasonable choice on a Unix-like system is /usr/local, or
# if you don't have permission to write there, your home directory.
./configure --prefix=$GEOS_DIR
make
make install
```
3. 安装basemap

```shell
# 进入basemap目录
python setup.py install
```

4. 检查安装是否成功
```python
from mpl_toolkits.basemap import Basemap
# cd to the examples directory
python run_all.py
```


#### 1.3 liblpsolve55 安装

#### 最新更新，亲测可行2018.8.16：
1. 下载安装包
- [lp_solve_5.5.2.0_source.tar.gz](http://sourceforge.net/projects/lpsolve/files/lpsolve/5.5.2.0/lp_solve_5.5.2.0_source.tar.gz/download)

- [lp_solve_python_3x-master.zip](https://github.com/chandu-atina/lp_solve_python_3x)

2. 解压 lp_solve_5.5.2.0_source.tar.gz，得到lp_solve_5.5文件夹， 并执行以下命令
```shell
 $ cd lp_solve_5.5/lpsolve55
 $ sh ccc (on linux)
 $ sh ccc.osx (on Mac)
```
3. 解压lp_solve_python_3x.zip, 生成lp_solve_python_3x-master文件夹，将文件夹下的extra文件夹复制到lp_solve_5.5文件夹下
,并执行以下命令
```shell
cd extra/Python/
python setup.py install

# 安装信息
Writing /data/home/henry/anaconda3/lib/python3.6/site-packages/lpsolve55-5.5.0.9-py3.6.egg-info


```
4. 将生成的liblpsolve55.so 拷贝到 /data/home/henry/anaconda3/lib/
```shell
cd  lpsolve55/bin/ux64/
cp liblpsolve55.so /data/home/henry/anaconda3/lib/
```
5. 测试
```python
import lp_solve
```

---

[参考教程](https://stackoverflow.com/questions/48765299/how-to-install-lpsolve-for-python-3-6)

**ubuntu安装:**

> conda install -c snorfalorpagus lpsolve

> export PYTHONPATH=/home/henry/anaconda3/lib:$PYTHONPATH

1. 下载安装包
- [lpsolve55-5.5.0.9.linux-x86_64.tar.gz](http://sourceforge.net/projects/lpsolve/files/lpsolve/5.5.2.0/lp_solve_5.5.2.0_source.tar.gz/download)

- [lp_solve_python_3x](https://github.com/chandu-atina/lp_solve_python_3x)


2. 解压 lpsolve55-5.5.0.9.linux-x86_64.tar.gz， 并执行以下命令
```
 $ cd lp_solve_5.5/lpsolve55
 $ sh ccc (on linux)
 $ sh ccc.osx (on Mac)
```
> 如果出现以下问题
```shell
In file included from ../lp_SOS.c:3:0:
../shared/commonlib.h:88:24: error: expected identifier or ‘(’ before numeric constant
   #define FALSE        0
```
> 参考[ubuntu下lpsolve55安装解决方案](https://stackoverflow.com/questions/44772590/compile-and-build-lp-solve-from-source-code-ubuntu)
3. 解压lp_solve_python_3x.zip, extra/Python folder into lp_solve_5.5,并执行以下命令

```sh
cd lp_solve_5.5/extra/Python/
python setup.py install
```
4. 声明变量：

```sh
# /data/home/henry/download/pyroms/lp_solve_5.5/lpsolve55/bin/ux64
# /path/to/liblpsolve55.so
 export LD_LIBRARY_PATH=/home/henry/download/lp_solve_5.5/lpsolve55/bin/ux64:$LD_LIBRARY_PATH
```
5. 检查是否安装成功

```python
import lp_solve
```
#### 1.4 natgrid 安装
```python
python setup.py install
```
---
### 2.安装pyroms

#### 2.1 pyroms_toolbox
```shell
cd pyroms_toolbox
python setup.py build --fcompiler=gnu95
python setup.py install --prefix=/path
```
#### 2.2 bathy_smoother

```sh
cd bathy_smoother
python setup.py build --fcompiler=gnu95
python setup.py install --prefix=/path
from bathy_smoother import *
# 如果出现以下错误
lpsolve55.so not found.
Linear programming method will not be available.
# 则说明 liblpsolve55未正确安装或者安装好后没有做环境声明
```
#### 2.3 pyroms
2.3.1 自动安装

在install_pyroms.sh中添加环境变量：
```shell
export PATH=/data/soft/netcdf4.4/gnu/bin:$PATH
export NF_CONFIG=/data/soft/netcdf4.4/gnu/bin/nf-config

export LIBDIR=/data/soft/netcdf4.4/gnu/lib:/data/soft/hdf5/gnu/lib
export LDFLAGS="-L$LIBDIR -shared"
```
并指定安装路径
运行安装脚本即可自动安装

2.3.2 手动安装

具体步骤可参考：
https://houstonthereisaproblem.blogspot.tw/2011/12/installation-of-pyroms-into-mac-os-1072.html

其中编译SCRIP最容易出错，可参考
https://bbs.archlinuxcn.org/viewtopic.php?id=2409

- [SCRIP官方](http://oceans11.lanl.gov/trac/SCRIP)安装

make

make f2py

如果出现一下错误,而scrip.so已经顺利安装：
```shell
/usr/bin/ld: cannot find -lhdf5
collect2: ld returned 1 exit status
/usr/bin/ld: cannot find -lhdf5
collect2: ld returned 1 exit status
```
或者
```sh
make: *** [scrip.so] Error 1
/bin/cp: cannot stat ‘./scrip.so’: No such file or directory
make: *** [install] Error 1
cp: missing destination file operand after ‘scrip.so’
```
修改makefile
```sh
export LIBDIR=/data/soft/netcdf4.4/gnu/lib:/data/soft/hdf5/gnu/lib
export LDFLAGS="-L$LIBDIR -shared"
NC_CONFIG = /data/soft/netcdf4.4/intel/bin/nf-config
# F2PY_LIB = -L${LIBDIR}  -lnetcdf -lnetcdff -lhdf5 -lhdf5_hl
F2PY_LIB = -L${LIBDIR} -L/data/soft/hdf5/gnu/lib/libhdf5.so -L/data/soft/hdf5/gnu/lib/libhdf5_hl.so -lnetcdf -lnetcdff

```
将生成的scrip.cpython-36m-x86_64-linux-gnu.so拷贝到pyroms安装地址：

```shell
cp scrip.cpython-36m-x86_64-linux-gnu.so /data/home/henry/anaconda3/lib/python3.6/site-packages/pyroms
```


### 3.声明pyroms环境
在安装好pyroms后，可能会出现以下错误：

#### 错误1：
找不到netcdftime模块
```shell
conda install netcdftime
```

#### 错误2：


```python
>>> import pyroms
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/data/home/henry/anaconda3/lib/python3.6/site-packages/pyroms/__init__.py", line 19, in <module>
    from . import tools
  File "/data/home/henry/anaconda3/lib/python3.6/site-packages/pyroms/tools.py", line 4, in <module>
    import _iso
ModuleNotFoundError: No module named '_iso'
```
但是在路径：`/data/home/henry/anaconda3/lib/python3.6/site-packages/pyroms`下包含`_iso.cpython-36m-x86_64-linux-gnu.so`，说明pyroms没有添加到python搜索路径中

添加python搜索路径：

在site-packages添加一个路径文件，如mypkpath.pth，必须以.pth为后缀，写上你要加入的模块文件所在的目录名称

```sh
cd /data/home/henry/anaconda3/lib/python3.6/site-packages
# 创建mypkpath.pth，并添加
./pyroms
./pyroms_toolbox
./bathy_smoother
```
#### 错误3：
```python
import pyroms
scrip.so not found. Remapping function will not be available
```
检查错误来源，发现如下错误

```python
import scrip
ImportError: libnetcdff.so.6: cannot open shared object file: No such file or directory
```
因此需要声明libnetcdff.so.6：
```sh
export  LD_LIBRARY_PATH=/usr/local/netcdf4.6.1/lib/:$LD_LIBRARY_PATH
```
亲测，可完美解决scrip.so缺失问题

#### 错误4：
运行Yellow sea 例子出错
```python
 run the Yellow Sea examples
 hgrd = pyroms.grid.Gridgen(lonp, latp, beta, (Mm+3, Lm+3), proj=map)
 AttributeError: dlsym(0x7ff244190130, gridgen_generategrid2): symbol not found
Exception AttributeError: 'dlsym(0x7ff244190130, gridnodes_destroy): symbol not found' in <bound method Gridgen.__del__ of <pyroms.hgrid.Gridgen object at 0x10fbd9f90>> ignored
```
错误原因：
libgridgen.so没有安装成功，`libgridgen.so ` file that was built is missing the generategrid2 function

**解决方案：**

重新安装pyroms/external文件夹下的工具（包括`libgridgen.so`），参考pystall.py脚本, ubuntu最好安装在/usr/local路径下。也可参考本文件夹下的 <font color=#00969 size=4>pyroms-gridgen安装.md</font> 和<font color=#00969 size=4>运行yellow sea例子出错.md</font>
