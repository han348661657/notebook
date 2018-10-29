# netcdf_c读取nc文件

## [官网教程](https://www.unidata.ucar.edu/software/netcdf/docs/reading_unknown.html)

- nc_open(路径，模式，int *ncid)
  >模式包含：0 or NC_NOWRITE; NC_WRITE
  >
  >ncid: 指向要存储返回的netCDF ID的位置的指针
- nc_inq（int ncid, int *ndimsp int *nvarsp, int *nattsp,int *unlimdimidp）查找维数，变量和全局属性的数量，以及无限制的dimid。
  >ncid: NetCDF或组ID，来自先前对nc_open（），nc_create（），nc_def_grp（）的调用，或相关的查询函数，如nc_inq_ncid（）。\
  >ndimsp: 指向为此netCDF数据集定义的返回维数的位置的指针。如果为NULL则忽略。\
  >nvarsp： 指向为此netCDF数据集定义的返回变量数的位置的指针。如果为NULL则忽略。\
  >nattsp：指向为此netCDF数据集定义的返回数量的全局属性的位置的指针。如果为NULL则忽略。\
  >unlimdimidp：指向无限维度的返回ID的位置的指针，如果此netCDF数据集有一个。如果未定义无限长度维度，则返回-1。如果为NULL则忽略。如果存在多个无限维度（仅可用于netCDF-4文件），则仅返回指向第一个文件的指针，以实现向后兼容性。如果你想要它们全部，请使用nc_inq_unlimids（）。
- nc_inq_att（）查找属性名称，类型和长度。
- nc_inq_dim（）查找维名称和长度。
- nc_inq_var（）查找变量名称，类型，num维度，dim ID和num属性。
- nc_inq_dimid（）从名称中查找维度ID。
- nc_inq_varid（）从名称中查找变量ID。
- nc_inq_format（）查找文件格式：经典或64位偏移
- nc_inq_libvers（）查找netCDF库版本。

---

## 读取实例

```C++
// 待读取nc文件
#define NC_NAME "E:\L1B\data\CFO_OPER_SWI_L1B____F_20160823T000000_20160823T014500_NXD.nc"
#define FILE_NAME1 "simple_xy.nc"

#define NDIMS 2
#define NX 6
#define NY 12
```

```C++
int ncid, varid;
int data_in[NX][NY];
/* Loop indexes, and error handling. */
int x, y, retval;
/* Open the file. NC_NOWRITE tells netCDF we want read-only access
* to the file.*/
system("pause");
if ((retval = nc_open(FILE_NAME1, NC_NOWRITE, &ncid)))
	ERR(retval);
/* Get the varid of the data variable, based on its name. */
if ((retval = nc_inq_varid(ncid, "data", &varid)))
	ERR(retval);
/* Read the data. */
if ((retval = nc_get_var_int(ncid, varid, &data_in[0][0])))
	ERR(retval);
/* Check the data. */
for (x = 0; x < NX; x++)
	for (y = 0; y < NY; y++)
		if (data_in[x][y] != x * NY + y)
			return ERRCODE;
/* Close the file, freeing all resources. */
if ((retval = nc_close(ncid)))
	ERR(retval);
```