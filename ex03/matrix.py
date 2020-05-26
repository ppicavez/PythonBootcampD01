class Matrix:
    def __init__(self, *data):
        # First case : data is a list of list
        if len(data) == 1:
            if isinstance(data[0], list):
                length = len(data[0][0])
                for i in data[0]:
                    if not isinstance(i, list):
                        print("data must be a list of lists")
                        return
                    if len(i) != length:
                        print(" All the lists in data's lists \
                              must have the same length")
                        return
                self.data = data[0]
                self.shape = (len(self.data), length)
                # self.shape[0] = len(self.data[0])
                # self.shape[1] = length
            # 2nd case : matrix full of 0 : tuple give the shape
            elif isinstance(data[0], tuple):
                if (len(data[0]) != 2):
                    print("A matrix have 2 dimensions ")
                    return
                self.shape = data[0]
                num_list = self.shape[0]
                num_elem = self.shape[1]
                self.data = []
                for i in range(num_list):
                    col = []
                    for j in range(num_elem):
                        col.append(0.0)
                    self.data.append(col)
        # Third case  Data (list of list) + Dimension
        elif len(data) == 2:
            if isinstance(data[0], list) and isinstance(data[1], tuple):
                self.data = data[0]
                self.shape = data[1]
            else:
                print(" Arguments must be a list of lists and a tuple")
                return
        elif len(data) == 0:
            print("Arguments should not be empty")
            return

    def __repr__(self):
        """All useful details for vector implementation"""
        return f"{self.__class__}, {self.__dict__}"

    def __str__(self):
        return f" shape {self.shape}\n matrix {self.data}"

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.shape == other.shape:
                new = Matrix(self.shape)
                num_list = new.shape[0]
                num_elem = new.shape[1]
                new.data = []
                for i in range(num_list):
                    col = []
                    for j in range(num_elem):
                        col.append(self.data[i][j] + other.data[i][j])
                    new.data.append(col)
                return new
            else:
                return "ERROR! impossible to add matrix with different shape"
        else:
            # Only matrix could be added with a matrix
            name = other.__class__.__name__
            return f"ERROR! Cannot add matrix and {name}, only add matrix"

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.shape == other.shape:
                new = Matrix(self.shape)
                num_list = new.shape[0]
                num_elem = new.shape[1]
                new.data = []
                for i in range(num_list):
                    col = []
                    for j in range(num_elem):
                        col.append(self.data[i][j] - other.data[i][j])
                    new.data.append(col)
                return new
            else:
                return "ERROR! impossible to sub matrix with different shape"
        else:
            # Only matrix could be sub with a matrix
            name = other.__class__.__name__
            return f"ERROR! Cannot sub matrix and {name}, only add matrix"

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
        if isinstance(other, int):
            if int(other) != 0 :
                new = Matrix(self.shape)
                num_list = new.shape[0]
                num_elem = new.shape[1]
                new.data = []
                for i in range(num_list):
                    col = []
                    for j in range(num_elem):
                        col.append(self.data[i][j] / int(other))
                    new.data.append(col)
                return new
            else:
                return "ERROR! impossible to div matrix with 0"
        else:
            # Only scalar could be div  a matrix
            name = other.__class__.__name__
            return f"ERROR! Cannot div matrix and {name}"
        
    __rsub__ = __sub__
    __radd__ = __add__
    __rmul__ = __mul__
    __rtruediv__ = __truediv__
