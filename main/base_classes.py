class Direction():
    # Класс направления внутри вуза
    def __init__(self, name:str, q_place:str, ref:str) -> None:
        self.name = name
        self.q_place = q_place
        self.ref = ref
        pass
    
    def get_inf(self) -> dict:
        return {"name": self.name, "q_place": self.q_place, "ref": self.ref}


class Student():
    # Класс отдельного поступающего, со снилсом вместо id
    def __init__(self, id:int, sum_ege_score:int) -> None:
        self.id = id
        self.sum_ege_score = sum_ege_score
        pass
    
    def add_to_table(self, college:str, direction:Direction, self_progress:int, priority:int, diplom:bool, place) -> None:
        pass
        
