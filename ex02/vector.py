class Vector:
    """Vector (list of floats), which can perform other operations
    with another vectors and scalars
    """
    def __init__(self, *args):
        error_msg = ("ERROR!\n"
                     "Initialise vector with  :\n"
                     " - 1 int   = size of vector \n"
                     " - 2 ints  =  range of vector   \n "
                     " - list of floats")
        self.values = None
        if len(args) == 1:
            # if 1 argument and it's a int or valid str(int)
            if isinstance(args[0], list):
                # initialising with list
                # skipping empty lists
                if len(args[0]) > 0:
                    self.values = [float(x) for x in args[0]]
                else:
                    print(error_msg)
                    return
            elif isinstance(args[0], int):
                # initialising with single int (range)
                self.values = [float(x) for x in range(int(args[0]))]
            else:
                print(error_msg)
                return
        elif len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[1], int):
                # initialising with 2 ints (range)
                self.values = [float(x) for x in range(args[0], args[1])]
            else:
                print(error_msg)
                return

        self.size = len(self.values)

    def __repr__(self):
        """All useful details for vector implementation"""
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f"vector {self.values}"

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.size == other.size:
                return [a + b for a, b in zip(self.values, other.values)]
            else:
                return "ERROR! impossible to add vectors with different sizes"
        else:
            # Only vector could be added with a vector
            name = other.__class__.__name__
            return f"ERROR! Cannot add vector and {name}, only add vectors"

    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.size == other.size:
                return [a - b for a, b in zip(self.values, other.values)]
            else:
                return "ERROR! impossible to subtract vectors\
                        with different sizes"
        else:
            name = other.__class__.__name__
            return f"ERROR! Cannot subtract vector with {name},\
                only with vectors"

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.size == other.size:
                return sum([a * b for a, b in zip(self.values, other.values)])
            else:
                return "ERROR! impossible to multiply \
                        vectors with different sizes"
        try:
            return [float(other) * x for x in self.values]
        except (TypeError, ValueError):
            name = other.__class__.__name__
            return f"ERROR! impossible to multiply vector \
                     on {name}, only on scalars"

    def __truediv__(self, other):
        try:
            return [x / float(other) for x in self.values]

        except (TypeError, ValueError):
            name = other.__class__.__name__
            return f"ERROR! impossible to divide vector \
                     on {name}, only on scalars"

    __rsub__ = __sub__
    __radd__ = __add__
    __rmul__ = __mul__
    __rtruediv__ = __truediv__
