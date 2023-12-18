class Shop:
    jeans_count = 10
    def __init__(self,  color):
        self.color = color
         
class Jeans(Shop):
    def __init__(self, height, weight, color):
        super().__init__( color)
        self.height = height
        self.weight = weight
        self.jeans_count -= 1
    
    @property
    def check(self):
        if self.height >= 165 and self.height <= 175:
            if self.weight >= 44 and self.weight <= 46:
                print(f'Вам может подойти размер (S)')
            
        if self.height >= 170 and self.height <= 180:
                if self.weight >= 46 and self.weight <= 48:
                     print(f'Вам может подойти размер (M)')
        
        if self.height >= 175 and self.height <= 185:
                if self.weight >= 48 and self.weight <= 50:
                     print(f'Вам может подойти размер (L)')
        
        if self.height >= 175 and self.height <= 185:
                if self.weight >= 50 and self.weight <= 52:
                    print(f'Вам может подойти размер (XL)')
                else:
                    print('K сожалению таких размеров нету в наличии')



j = Jeans(180, 52, 'black')
v = Jeans(180, 52, 'black')
print(j.jeans_count)
print(v.jeans_count)  