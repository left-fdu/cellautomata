## 前言

本研究参考了目前使用较为广泛的几种细胞自动机模型，构建了一个基于二进制逻辑的细胞自动机。实验结果表明，本研究所建立的细胞自动机模型可以很好地模拟单种及两种不同细胞增殖、细胞间抑制和促进增殖等几种细胞群体行为，验证了其微观及宏观规律，有助于深入研究细胞相互作用的宏观意义。

Inspired by several widely used cellular automata models, this paper constructs a cellular automata based on binary logic. The cellular automata can simulate the behavior of various cell groups and quantifies their microscopic and macroscopic behaviors. Our analysis provides cell social behavior, such as proliferation of two different kinds of cells, intercellular inhibition and promotion of proliferation between cells, and successfully demonstrate the value using computer simulation to obtain macroscopic understanding of molecular interactions between cells.

## 参数

**分裂参数**

| 参数名    | 参数意义                                                     |
| --------- | ------------------------------------------------------------ |
| cycle     | 细胞分裂的阈值，指细胞周期。                                 |
| age       | 浮点数，记录细胞的年龄，随模拟次数增长。 当Age> Cycle时，会进入可增殖状态。 |
| growth    | Age在模拟次数方面的增长率，仅取决于所观察的细胞。            |
| incidence | 浮点数，衡量相邻细胞对Age生长速率的影响程度。  取决于相邻的细胞。 |
| reaction  | 浮点数，衡量细胞对相邻细胞增殖率的反应程度。 取决于所观察的细胞和相邻细胞。 |
| migration | 整数,衡量观察细胞的迁移能力。记录细胞周围是否有空位。当细胞进入可增殖状态时，其周围必须有空间安置分裂的新细胞，才会进行分裂。（如果没有足够空间，则必须等到空余空间出现才分裂。） |

**死亡参数**

| 参数名      | 参数意义                                                     |
| ----------- | ------------------------------------------------------------ |
| vitality    | 浮点数，记录细胞的活力，随模拟次数下降。当vitality<0，观察的细胞会凋亡。 |
| reduction   | vitality随模拟次数的下降率，仅取决于所观察细胞。             |
| incidence_d | 浮点数，衡量相邻细胞对vitality下降率的影响程度。取决于相邻的细胞。 |
| reaction_d  | 浮点数，衡量细胞对相邻细胞凋亡率的影响程度。取决于观察到的细胞和相邻细胞。 |

**细胞间相互作用的抑制和促进关系参数**

| 参数名     | 参数意义                                                     |
| ---------- | ------------------------------------------------------------ |
| relation   | 描述细胞间相互对age作用的关系是抑制还是促进,0促进，1抑制。   |
| relation_d | 描述细胞间相互对vitality作用的关系是抑制还是促进,0促进，1抑制。 |

具体规则如下：

每个格子具有坐标[x][y]，代表其位置，以及当前状态（0，1，2），0表示该格子没有细胞存活，1和2表示当前该位置的细胞种类是cell_1还是cell_2。

当细胞年龄随模拟次数增长，成为成熟具有分裂能力的细胞时，判断其周围是否有空的位置，只有相邻位置有状态为空的空间才能分裂。当细胞年龄过大、活力过低就会凋亡。age随模拟次数增加，vitality随模拟次数减少，这两个参数都会受到周围细胞的影响，如果age先达到cycle就准备增殖，如果vitality到0就凋亡。

细胞间的相互影响采用线性模拟。基本公式如下：

age =                                

vitality = V0 -  

incidence = avg (reaction);

incidence_d = avg (reaction_d);

当relation = 0时，growth += incidence;

当relation = 1时，growth -= incidence;

当relation_d = 0时，reduction += incidence_d;

当relation_d = 1时，reduction -= incidence_d.

本研究是基于模拟次数的模拟，不代入实际的时间参数。V0是细胞初始的活力值。t是模拟的次数。incidence是相邻细胞的reaction的平均数，促进和抑制的影响分别计算。incidence_d是相邻细胞reaction_d的平均数。cycle、age、vitality是和模拟次数t同级的参数；growth、incidence、reaction、reduction、incidence_d、reaction_d是和t的倒数同级的参数；migration、relation、relation_d是状态参数，只区分0或1。

## 实验方法

![image-20200224185002346](C:\Users\黄寅殊\AppData\Roaming\Typora\typora-user-images\image-20200224185002346.png)

![image-20200224185018187](C:\Users\黄寅殊\AppData\Roaming\Typora\typora-user-images\image-20200224185018187.png)



------

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