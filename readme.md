CellDivision.py：逻辑实现
Cell.py：细胞类的定义

CellDivision.py 23行，self.rand()表示随机生成初始化细胞位置
		self.ini()表示自定义初始化细胞位置，初始化操作在ini函数中手动生成

颜色修改：
CellDivision.py 137行
	colorslist = ['gray', 'pink', '#ffffff']：
		参数1：背景颜色
		参数2：细胞1颜色
		参数3：细胞2颜色
		#ffffff为RGB表示