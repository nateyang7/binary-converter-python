class Calculator:
    """
    Classe représentant une simple calculatrice sur les entiers

    Attributes:
        __x (int): Premier entier
        __y (int): Second entier
    """

    def __init__(self, x: int=0, y: int=0) -> None:
        """
        Initialise une calculatrice

        Args:
            x (int): Un entier qui initialise l'attribut __x
            y (int): Un entier qui initialise l'attribut __y
        """
        self.__x: int = x
        self.__y: int = y

    def get_x(self) -> int:
        """ Getter de l'attribut __x de la calculatrice """
        return self.__x

    def set_x(self, new_x: int) -> None:
        """ Setter de l'attribut __x par un autre entier """
        self.__x = new_x

    def get_y(self) -> int:
        """ Getter de l'attribut __y de la calculatrice """
        return self.__y

    def set_y(self, new_y: int) -> none:
        """ Setter de l'attribut __y de la calculatrice """
        self.__y = new_y

    def add(self) -> int:
        """ Renvoie la somme de __x et __y """
        return self.__x + self.__y

    def subtract(self) -> int:
        """ Renvoie la différence de __x et __y """
        return self.__x - self.__y

    def multiply(self) -> int:
        """ Renvoie le produit de __x et __y """
        return self.__x * self.__y

