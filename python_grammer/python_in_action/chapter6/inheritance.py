class Page:
    def __init__(self,num,content):
        self.num=num
        self.content=content
    
    def output(self):
        return f"{self.content}"

class TitlePage(Page):
    def output(self):
        title=super().output()
        return title.upper()


class Length(float):
    def to_cm(self):
        return super().__str__()+"cm"






if __name__=="__main__":
    title=TitlePage(0,"Python Practice BOok")
    print(title.output())



