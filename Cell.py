class Cell():
    """class cell
    cycle       细胞分裂的阈值，指细胞周期。
    age	        浮点数，记录细胞的年龄，随时间增长。 当age>Cycle时，可能会发生分裂。
    growth		age在时间方面的增长率，仅取决于观察到的细胞。
    incidence	浮点数，衡量相邻细胞对age生长速率的影响程度。 取决于相邻的细胞。
    reaction	浮点数，衡量细胞对相邻细胞增殖率的反应程度。 取决于观察到的细胞和相邻细胞。
    migration	整数,衡量观察细胞的迁移能力。记录细胞周围是否有空位，如果有才能分裂。migration表示当age> Cycle时，观察到的细胞如何为分裂留出空间。（如果空间失败，则单元格必须等到可访问空间出现。）

    vitality	浮点数，记录细胞的年龄，随时间下降。当Vitality<0，观察的细胞会凋亡。
    reduction	vitality随时间的下降率，仅取决于观察到的细胞。
    incidence_d	浮点数，衡量相邻细胞对vitality下降率的影响程度。取决于相邻的细胞。
    reaction_d	浮点数，衡量细胞对相邻细胞增值率的影响程度。取决于观察到的细胞和相邻细胞。
    相互作用
    relation	描述细胞间相互对age作用的关系是抑制还是促进,0促进，1抑制。
    relation_d  描述细胞间相互对vitality作用的关系是抑制还是促进,0促进，1抑制。
    """

    def __init__(self, cycle=6, iteraction=0, age=0.0, growth=2.0, incidence=0, reaction=0, migration=0, vitality=9.0,
                 reduction=1.0, incidence_d=0, reaction_d=0, relation=0, islive=0, relation_d=0, type=1):
        """init a cell"""
        self.cycle = cycle
        self.age = age
        self.growth = growth
        self.incidence = incidence
        self.migration = migration
        self.vitality = vitality
        self.reaction = reaction
        self.reduction = reduction
        self.incidence_d = incidence_d
        self.reaction_d = reaction_d
        self.islive = islive
        self.iteraction = iteraction

        self.type = type
        if(type == 1):
            self.reaction = 0
            self.reaction_d = 0.8
            self.relation = 0
            self.relation_d = 0
        elif(type == 2):
            ##self.cycle = 1
            ##self.growth = 1.0
            ##self.vitality = 50.0
            self.reaction = 0
            self.reaction_d = 0
            self.relation = 0
            self.relation_d = 1
