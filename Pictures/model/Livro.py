class Livro:
    __id: int
    __titulo: str
    __genero: str
    __autor: str

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: int):
        self.__titulo = titulo

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: int):
        self.__genero = genero

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor: int):
        self.__autor = autor

    def __str__(self) -> str:
        return str(self.__class__) + ": " + str(self.__dict__)