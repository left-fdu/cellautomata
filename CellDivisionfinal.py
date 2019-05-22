from Cell import Cell
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

class CellDivision(object):
    def ini(self):
        """自定义初始化细胞位置"""
        self.cells[15][16] = 1
        self.cells[16][15] = 2
        self.cells[15][15] = 1
        self.cells[16][16] = 2


    def rand(self):
        """随机初始化细胞位置"""
        self.cells[1:-1, 1:-1] = np.random.randint(2, size=(self.cells_width, self.cells_height))


    def __init__(self, cells_shape):
        self.cells = np.zeros(cells_shape)
        self.cells_width = cells_shape[0] - 2
        self.cells_height = cells_shape[1] - 2
        self.ini()  ##self.ini()
        self.timer = 0
        self.cellArray = []
        self.alive_cell_num = [0,0,0,0,0,0];
        for count_x in range(0, self.cells_width + 2):
            self.cellArray.append([]);
            for count_y in range(0, self.cells_height + 2):
                if (self.cells[count_x, count_y]):
                    self.cellArray[count_x].append(Cell(islive=1,type=self.cells[count_x, count_y]))
                    num = int(self.cells[count_x, count_y])
                    self.alive_cell_num[num] += 1
                else:
                    self.cellArray[count_x].append(Cell(islive=0, type=0))


    def die(self):
        """所有的细胞生长1个周期，不计算所有的影响，只剔除死亡的细胞"""
        for count_x in range(0, self.cells_width + 1):
            for count_y in range(0, self.cells_height + 1):
                cell = self.cellArray[count_x][count_y]
                if (cell.islive):
                    """只有活着才生长"""
                    cell.vitality -= cell.reduction
                    cell.age += cell.growth
                    if (cell.vitality < 0):
                        print("（{}，{}）死去".format(count_x, count_y))
                        self.cellArray[count_x][count_y].islive = -1
                        num = int(self.cellArray[count_x][count_y].type)
                        self.alive_cell_num[num] -= 1
                        self.cells[count_x][count_y] = 0
                    print(
                        "（{}，{}），age={}, incidence={}, vitality={}, incidence_d={}, type={}".format(count_x, count_y,
                                                                                           cell.age,
                                                                                           cell.incidence,
                                                                                           cell.vitality,
                                                                                           cell.incidence_d,
                                                                                           cell.type))
                    if ((cell.age / cell.cycle) > cell.iteraction) and (cell.vitality > 0):
                        self.cellArray[count_x][count_y].migration = 1
                else:
                    self.cells[count_x][count_y] = 0


    def division(self):
        """当细胞可以分裂，且周围有空余空间，分裂一个新的细胞,新的细胞从0开始，原位置的细胞继续生长"""
        for count_x in range(1, self.cells_width + 1):
            for count_y in range(1, self.cells_height + 1):
                cell = self.cellArray[count_x][count_y]
                if(cell.islive == -1):
                        cell.islive = 0
                elif self.cellArray[count_x][count_y].migration == 1:
                    tmp = 0
                    enable = int(self.cells[count_x][count_y])
                    
                    if count_x == 1:
                        if count_y == 1:
                            if (self.cellArray[1][2].islive * self.cellArray[2][2].islive * self.cellArray[2][1].islive == 0):
                                while self.cellArray[count_x][count_y].migration == 1:
                                    i = random.randint(0,1) + 1
                                    j = random.randint(0,1) + 1
                                    if (self.cellArray[i][j].islive == 0):
                                        if (self.cellArray[i][j].islive == 0):
                                            print("x={},y={},type={}出生".format(i, j, enable))
                                            cell_n = Cell(islive=1,type=enable)
                                            self.cellArray[i][j] = cell_n
                                            self.cells[i][j] = enable
                                            self.alive_cell_num[enable] += 1
                                            self.cellArray[count_x][count_y].iteraction += 1
                                            self.cellArray[count_x][count_y].migration = 0
                                        
                        elif count_y == self.cells_height:
                            if (self.cellArray[1][self.cells_height-1].islive * self.cellArray[2][self.cells_height-1].islive * self.cellArray[2][self.cells_height].islive == 0):
                                while self.cellArray[count_x][count_y].migration == 1:
                                    i = random.randint(0,1) + 1
                                    j = random.randint(0,1) + self.cells_height - 1
                                    if (self.cellArray[i][j].islive == 0):
                                        print("x={},y={},type={}出生".format(i, j, enable))
                                        cell_n = Cell(islive=1,type=enable)
                                        self.cellArray[i][j] = cell_n
                                        self.cells[i][j] = enable
                                        self.alive_cell_num[enable] += 1
                                        self.cellArray[count_x][count_y].iteraction += 1
                                        self.cellArray[count_x][count_y].migration = 0
                                        
                        else:
                            for i in range(1, 3):
                                for j in range(count_y - 1, count_y + 2):
                                    if (self.cellArray[i][j].islive == 0):
                                        tmp += 1
                            if tmp :
                                while self.cellArray[count_x][count_y].migration == 1:
                                    i = random.randint(0,1) + 1
                                    j = random.randint(0,2) + count_y - 1
                                    if (self.cellArray[i][j].islive == 0):
                                        print("x={},y={},type={}出生".format(i, j, enable))
                                        cell_n = Cell(islive=1,type=enable)
                                        self.cellArray[i][j] = cell_n
                                        self.cells[i][j] = enable
                                        self.alive_cell_num[enable] += 1
                                        self.cellArray[count_x][count_y].iteraction += 1
                                        self.cellArray[count_x][count_y].migration = 0
                    
                    elif count_x == self.cells_width:
                        if count_y == 1:
                            if (self.cellArray[self.cells_width][2].islive * self.cellArray[self.cells_width-1][2].islive * self.cellArray[self.cells_width-1][1].islive == 0):
                                while self.cellArray[count_x][count_y].migration == 1:
                                    i = random.randint(0,1) + self.cells_width -1
                                    j = random.randint(0,1) + 1
                                    if (self.cellArray[i][j].islive == 0):
                                        print("x={},y={},type={}出生".format(i, j, enable))
                                        cell_n = Cell(islive=1,type=enable)
                                        self.cellArray[i][j] = cell_n
                                        self.cells[i][j] = enable
                                        self.alive_cell_num[enable] += 1
                                        self.cellArray[count_x][count_y].iteraction += 1
                                        self.cellArray[count_x][count_y].migration = 0
                                    
                        elif count_y == self.cells_height:
                            if (self.cellArray[self.cells_width][self.cells_height-1].islive * self.cellArray[self.cells_width-1][self.cells_height-1].islive * self.cellArray[self.cells_width-1][self.cells_height].islive == 0):
                                while self.cellArray[count_x][count_y].migration == 1:
                                    i = random.randint(0,1) + self.cells_width - 1
                                    j = random.randint(0,1) + self.cells_height - 1
                                    if (self.cellArray[i][j].islive == 0):
                                        print("x={},y={},type={}出生".format(i, j, enable))
                                        cell_n = Cell(islive=1,type=enable)
                                        self.cellArray[i][j] = cell_n
                                        self.cells[i][j] = enable
                                        self.alive_cell_num[enable] += 1
                                        self.cellArray[count_x][count_y].iteraction += 1
                                        self.cellArray[count_x][count_y].migration = 0
                                    
                        else:
                            for i in range(count_x - 1, count_x + 1):
                                for j in range(count_y - 1, count_y + 2):
                                    if (self.cellArray[i][j].islive == 0):
                                        tmp += 1
                            if tmp :
                                while self.cellArray[count_x][count_y].migration == 1:
                                    i = random.randint(0,1) + count_x - 1
                                    j = random.randint(0,2) + count_y - 1
                                    if (self.cellArray[i][j].islive == 0):
                                        print("x={},y={},type={}出生".format(i, j, enable))
                                        cell_n = Cell(islive=1,type=enable)
                                        self.cellArray[i][j] = cell_n
                                        self.cells[i][j] = enable
                                        self.alive_cell_num[enable] += 1
                                        self.cellArray[count_x][count_y].iteraction += 1
                                        self.cellArray[count_x][count_y].migration = 0

                    elif count_y == 1:
                        for i in range(count_x - 1, count_x + 2):
                            for j in range(1, 3):
                                if (self.cellArray[i][j].islive == 0):
                                        tmp += 1
                            if tmp :
                                while self.cellArray[count_x][count_y].migration == 1:
                                    i = random.randint(0,2) + count_x - 1
                                    j = random.randint(0,1) + 1
                                    if (self.cellArray[i][j].islive == 0):
                                        print("x={},y={},type={}出生".format(i, j, enable))
                                        cell_n = Cell(islive=1,type=enable)
                                        self.cellArray[i][j] = cell_n
                                        self.cells[i][j] = enable
                                        self.alive_cell_num[enable] += 1
                                        self.cellArray[count_x][count_y].iteraction += 1
                                        self.cellArray[count_x][count_y].migration = 0
                    
                    elif count_y == self.cells_height:
                        for i in range(count_x - 1, count_x + 2):
                            for j in range(count_y - 1, count_y + 1):
                                if (self.cellArray[i][j].islive == 0):
                                    tmp += 1
                            if tmp :
                                while self.cellArray[count_x][count_y].migration == 1:
                                    i = random.randint(0,2) + count_x - 1
                                    j = random.randint(0,1) + count_y - 1
                                    if (self.cellArray[i][j].islive == 0):
                                        print("x={},y={},type={}出生".format(i, j, enable))
                                        cell_n = Cell(islive=1,type=enable)
                                        self.cellArray[i][j] = cell_n
                                        self.cells[i][j] = enable
                                        self.alive_cell_num[enable] += 1
                                        self.cellArray[count_x][count_y].iteraction += 1
                                        self.cellArray[count_x][count_y].migration = 0
                    
                    else:
                        for i in range(count_x - 1, count_x + 2):
                            for j in range(count_y - 1, count_y + 2):
                                if (self.cellArray[i][j].islive == 0):
                                    tmp += 1
                        if tmp :
                            while self.cellArray[count_x][count_y].migration == 1:
                                i = random.randint(0,2) + count_x - 1
                                j = random.randint(0,2) + count_y - 1
                                if (self.cellArray[i][j].islive == 0):
                                    print("x={},y={},type={}出生".format(i, j, enable))
                                    cell_n = Cell(islive=1,type=enable)
                                    self.cellArray[i][j] = cell_n
                                    self.cells[i][j] = enable
                                    self.alive_cell_num[enable] += 1
                                    self.cellArray[count_x][count_y].iteraction += 1
                                    self.cellArray[count_x][count_y].migration = 0

                        
    def caculate(self, count_x, count_y):
        sum_1 = 0;
        sum_2 = 0;
        sum_d_1 = 0;
        sum_d_2 = 0;
        incidence_1 = 0;
        incidence_2 = 0
        incidence_d_1 = 0;
        incidence_d_2 = 0;
        for i in range(count_x - 1, count_x + 2):
            for j in range(count_y - 1, count_y + 2):
                if (self.cells[i][j] and (i != count_x or j != count_y) and (self.cellArray[i][j].type != self.cellArray[count_x][count_y].type)):
                    if (self.cellArray[count_x][count_y].relation == 0):
                        sum_1 += 1
                        incidence_1 += self.cellArray[i][j].reaction
                    elif (self.cellArray[count_x][count_y].relation):
                        sum_2 += 1
                        incidence_2 += self.cellArray[i][j].reaction
                    if (self.cellArray[count_x][count_y].relation_d == 0):
                        sum_d_1 += 1
                        incidence_d_1 += self.cellArray[i][j].reaction_d
                    elif (self.cellArray[count_x][count_y].relation_d):
                        sum_d_2 += 1
                        incidence_d_2 += self.cellArray[i][j].reaction_d
        if (sum_1):
            self.cellArray[count_x][count_y].growth += incidence_1/sum_1
        if (sum_2):
            self.cellArray[count_x][count_y].growth -= incidence_2/sum_2
        if (sum_d_1):
            self.cellArray[count_x][count_y].reduction += incidence_d_1/sum_d_1
        if (sum_d_2):
            self.cellArray[count_x][count_y].reduction -= incidence_d_2/sum_d_2


    def effect(self):
        """计算相邻细胞的影响因素"""
        for count_x in range(1, self.cells_width + 1):
            for count_y in range(1, self.cells_height + 1):
                cell = self.cellArray[count_x][count_y]
                if (self.cells[count_x, count_y]):
                    self.caculate(count_x=count_x, count_y=count_y)


    def update_state(self):
        self.die()
        self.division()
        self.effect()
        self.timer += 1


    def update_and_plot(self, n_iter):

        plt.ion()
        self.effect()
        colorslist = ['gray', 'pink', '#ffffff']
        cmaps = mpl.colors.LinearSegmentedColormap.from_list('mylist', colorslist, N=800)
        for _ in range(n_iter):
            plt.title('Iter :{}, alive cells1:{}, alive cells2:{}'.format(self.timer, self.alive_cell_num[1], self.alive_cell_num[2]))
            buf = self.cells[1:self.cells_width + 1, 1:self.cells_height + 1]
            plt.savefig(str(format(self.timer))+'.png')
            plt.imshow(buf, cmap=cmaps)
            self.update_state()
            plt.pause(0.2)
            with open('14-1.txt','a') as f:
                f.write("{}\n".format(self.alive_cell_num[1]))
            with open('14-2.txt','a') as g:
                g.write("{}\n".format(self.alive_cell_num[2]))
            print("----------------{}--------------------------".format(self.timer))
            print("alive cells1:{}, alive cells2:{}".format(self.alive_cell_num[1], self.alive_cell_num[2]))
        plt.ioff()



if __name__ == '__main__':
    cell = CellDivision(cells_shape=(34, 34));
    cell.update_and_plot(30)
##print(Cell().__dict__);
