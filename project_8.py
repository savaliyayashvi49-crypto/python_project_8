import numpy as np


class DataAnalytics:
    """All NumPy functionalities ne encapsulate kare che."""

    # Class-level variable
    project_name = "NumPy Analyzer"

    def __init__(self, array=None):
        # Constructor - array ne initialize kare che
        self.__array = array  # Private attribute (Encapsulation)
        self.__history = []

    # ---------- Encapsulation: Getter / Setter ----------
    def get_array(self):
        return self.__array

    def set_array(self, array):
        self.__array = array
        self.__history.append("Array updated")

    # ---------- Private Methods (internal computation) ----------
    def __validate_array(self):
        if self.__array is None:
            print("Pela array banavo! Main Menu > Option 1")
            return False
        return True

    def __get_elements(self, count):
        """User pase thi 'count' jetla elements levana"""
        while True:
            try:
                data = input(f"Enter {count} elements for the array separated by space: ")
                values = list(map(float, data.strip().split()))
                if len(values) != count:
                    print(f"Barabar {count} elements nakho! Fari try karo.")
                    continue
                # Jo badha int hoy to int ma convert karo - output photo jevo dekhase
                if all(v.is_integer() for v in values):
                    values = [int(v) for v in values]
                return values
            except ValueError:
                print("Khali numbers nakho!")

    def __parse_range(self, prompt):
        """'0:2' jevu input ne (start, end) ma convert kare"""
        while True:
            try:
                s = input(prompt).strip()
                if ":" in s:
                    a, b = s.split(":")
                    return int(a), int(b)
                else:
                    print("Format: start:end  Ex: 0:2")
            except ValueError:
                print("Sacha numbers nakho!")

    # ---------- ClassMethod & StaticMethod ----------
    @classmethod
    def get_project_name(cls):
        return cls.project_name

    @staticmethod
    def show_welcome():
        print("Welcome to the NumPy Analyzer!")
        print("=" * 55)

    @staticmethod
    def is_valid_shape(shape):
        return len(shape) > 0 and all(x > 0 for x in shape)

    # ================= 1. ARRAY CREATION =================
    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        ch = input("Enter your choice: ")

        try:
            if ch == "1":
                n = int(input("Enter the number of elements: "))
                elements = self.__get_elements(n)
                self.__array = np.array(elements)
            elif ch == "2":
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                total = rows * cols
                elements = self.__get_elements(total)
                self.__array = np.array(elements).reshape(rows, cols)
            elif ch == "3":
                d = int(input("Enter depth: "))
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                total = d * rows * cols
                elements = self.__get_elements(total)
                self.__array = np.array(elements).reshape(d, rows, cols)
            else:
                print("Khoto choice!")
                return
            print("\nArray created successfully:")
            print(self.__array)
            # Creation pachi Indexing / Slicing option - photo mujab
            self.indexing_slicing_menu()
        except ValueError:
            print("Sacha number nakho!")

    def indexing_slicing_menu(self):
        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            ch = input("Enter your choice: ")
            if ch == "1":
                self.do_indexing()
            elif ch == "2":
                self.do_slicing()
            elif ch == "3":
                break
            else:
                print("Khoto choice!")

    def do_indexing(self):
        if not self.__validate_array():
            return
        print(f"\nCurrent Array:\n{self.__array}")
        try:
            if self.__array.ndim == 1:
                idx = int(input("Enter index (0 thi start): "))
                print(f"Element at index {idx}: {self.__array[idx]}")
            elif self.__array.ndim == 2:
                r = int(input("Enter row index: "))
                c = int(input("Enter column index: "))
                print(f"Element at [{r}][{c}]: {self.__array[r, c]}")
            else:
                d = int(input("Enter depth index: "))
                r = int(input("Enter row index: "))
                c = int(input("Enter column index: "))
                print(f"Element at [{d}][{r}][{c}]: {self.__array[d, r, c]}")
        except (ValueError, IndexError):
            print("Khoto index!")

    def do_slicing(self):
        if not self.__validate_array():
            return
        print(f"\nCurrent Array:\n{self.__array}")
        try:
            if self.__array.ndim == 1:
                s, e = self.__parse_range("Enter the range (start:end): ")
                print(f"\nSliced Array:\n{self.__array[s:e]}")
            elif self.__array.ndim == 2:
                rs, re = self.__parse_range("Enter the row range (start:end): ")
                cs, ce = self.__parse_range("Enter the column range (start:end): ")
                print(f"\nSliced Array:\n{self.__array[rs:re, cs:ce]}")
            else:
                ds, de = self.__parse_range("Enter depth range (start:end): ")
                rs, re = self.__parse_range("Enter the row range (start:end): ")
                cs, ce = self.__parse_range("Enter the column range (start:end): ")
                print(f"\nSliced Array:\n{self.__array[ds:de, rs:re, cs:ce]}")
        except ValueError:
            print("Sachi range nakho!")

    def get_second_array(self):
        """Same shape no bijo array levano - Math / Combine mate"""
        if not self.__validate_array():
            return None
        total = self.__array.size
        elements = self.__get_elements(total)
        second = np.array(elements).reshape(self.__array.shape)
        print(f"\nOriginal Array:\n{self.__array}")
        print(f"\nSecond Array:\n{second}")
        return second

    # ================= 2. MATHEMATICAL OPERATIONS =================
    def math_operations(self):
        if not self.__validate_array():
            return
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")
        ch = input("Enter your choice: ")

        if ch in ["1", "2", "3", "4"]:
            second = self.get_second_array()
            if second is None:
                return
            if ch == "1":
                result, name = self.__array + second, "Addition"
            elif ch == "2":
                result, name = self.__array - second, "Subtraction"
            elif ch == "3":
                result, name = self.__array * second, "Multiplication"
            else:
                if np.any(second == 0):
                    print("Second array ma 0 che, Division na thai!")
                    return
                result, name = self.__array / second, "Division"
            print(f"\nResult of {name}:\n{result}")

        elif ch == "5":
            second = self.get_second_array()
            if second is None:
                return
            try:
                print(f"\nDot Product:\n{np.dot(self.__array, second)}")
            except ValueError as e:
                print(f"Dot Product na thai: {e}")

        elif ch == "6":
            if self.__array.ndim != 2:
                print("Matrix Multiplication mate 2D array joiye!")
                return
            second = self.get_second_array()
            if second is None:
                return
            try:
                print(f"\nMatrix Multiplication Result:\n{np.matmul(self.__array, second)}")
            except ValueError as e:
                print(f"Matrix Multiplication na thai: {e}")
        else:
            print("Khoto choice!")

    # ================= 3. COMBINE / SPLIT =================
    def combine_split(self):
        if not self.__validate_array():
            return
        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        ch = input("Enter your choice: ")

        if ch == "1":
            second = self.get_second_array()
            if second is None:
                return
            print("\nChoose combine type:")
            print("1. Vertical Stack (vstack)")
            print("2. Horizontal Stack (hstack)")
            print("3. Concatenate")
            t = input("Enter your choice: ")
            try:
                if t == "1":
                    result = np.vstack((self.__array, second))
                    print(f"\nCombined Array (Vertical Stack):\n{result}")
                elif t == "2":
                    result = np.hstack((self.__array, second))
                    print(f"\nCombined Array (Horizontal Stack):\n{result}")
                elif t == "3":
                    result = np.concatenate((self.__array, second), axis=0)
                    print(f"\nCombined Array (Concatenate):\n{result}")
                else:
                    print("Khoto choice!")
            except ValueError as e:
                print(f"Combine na thai: {e}")

        elif ch == "2":
            try:
                parts = int(input("Enter number of parts to split into: "))
                result = np.array_split(self.__array, parts)
                print(f"\nSplit Arrays into {parts} parts:")
                for i, part in enumerate(result, 1):
                    print(f"Part {i}:\n{part}")
            except ValueError:
                print("Sacho number nakho!")
        else:
            print("Khoto choice!")

    # ================= 4. SEARCH, SORT, FILTER =================
    def search_sort_filter(self):
        if not self.__validate_array():
            return
        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        ch = input("Enter your choice: ")

        if ch == "1":
            try:
                val = float(input("Enter value to search: "))
                if val.is_integer():
                    val = int(val)
                indices = np.where(self.__array == val)
                print(f"\nOriginal Array:\n{self.__array}")
                if len(indices[0]) == 0:
                    print(f"Value {val} array ma malyo nahi!")
                else:
                    print(f"Value {val} found at indices: {indices}")
                    print(f"Count: {len(indices[0])}")
            except ValueError:
                print("Sacho number nakho!")

        elif ch == "2":
            print(f"\nOriginal Array:\n{self.__array}")
            print("\nSort order:")
            print("1. Ascending")
            print("2. Descending")
            o = input("Enter your choice: ")
            # Photo mujab row-wise sort
            sorted_arr = np.sort(self.__array, axis=-1)
            if o == "2":
                sorted_arr = sorted_arr[:, ::-1] if sorted_arr.ndim >= 2 else sorted_arr[::-1]
            print(f"\nSorted Array:\n{sorted_arr}")
            print("(Sorting applied row-wise.)")

        elif ch == "3":
            print("\nFilter condition:")
            print("1. Greater than ( > )")
            print("2. Less than ( < )")
            print("3. Equal to ( == )")
            print("4. Even numbers")
            print("5. Odd numbers")
            f = input("Enter your choice: ")
            if f in ["1", "2", "3"]:
                try:
                    val = float(input("Enter value for comparison: "))
                    if f == "1":
                        result = self.__array[self.__array > val]
                        print(f"\nValues greater than {val}:\n{result}")
                    elif f == "2":
                        result = self.__array[self.__array < val]
                        print(f"\nValues less than {val}:\n{result}")
                    else:
                        result = self.__array[self.__array == val]
                        print(f"\nValues equal to {val}:\n{result}")
                except ValueError:
                    print("Sacho number nakho!")
            elif f == "4":
                print(f"\nEven numbers:\n{self.__array[self.__array % 2 == 0]}")
            elif f == "5":
                print(f"\nOdd numbers:\n{self.__array[self.__array % 2 == 1]}")
            else:
                print("Khoto choice!")
        else:
            print("Khoto choice!")

    # ================= 5. AGGREGATES & STATISTICS =================
    def aggregates_statistics(self):
        if not self.__validate_array():
            return
        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum and Maximum")
        print("7. Percentiles")
        print("8. Correlation Coefficients")
        ch = input("Enter your choice: ")

        print(f"\nOriginal Array:\n{self.__array}")

        if ch == "1":
            print(f"\nSum of Array: {np.sum(self.__array)}")
        elif ch == "2":
            print(f"\nMean of Array: {np.mean(self.__array)}")
        elif ch == "3":
            print(f"\nMedian of Array: {np.median(self.__array)}")
        elif ch == "4":
            print(f"\nStandard Deviation of Array: {np.std(self.__array)}")
        elif ch == "5":
            print(f"\nVariance of Array: {np.var(self.__array)}")
        elif ch == "6":
            print(f"\nMinimum Value: {np.min(self.__array)}")
            print(f"Maximum Value: {np.max(self.__array)}")
        elif ch == "7":
            try:
                p = float(input("Enter percentile (0-100): "))
                print(f"\n{p}th Percentile: {np.percentile(self.__array, p)}")
                print(f"25th Percentile: {np.percentile(self.__array, 25)}")
                print(f"50th Percentile (Median): {np.percentile(self.__array, 50)}")
                print(f"75th Percentile: {np.percentile(self.__array, 75)}")
            except ValueError:
                print("Sacho number nakho!")
        elif ch == "8":
            second = self.get_second_array()
            if second is None:
                return
            try:
                corr = np.corrcoef(self.__array.flatten(), second.flatten())
                print(f"\nCorrelation Coefficient:\n{corr}")
                print(f"Correlation between arrays: {corr[0, 1]:.4f}")
            except Exception as e:
                print(f"Correlation na thai: {e}")
        else:
            print("Khoto choice!")


# ================= MAIN MENU / UI =================
def main():
    analyzer = DataAnalytics()
    DataAnalytics.show_welcome()

    while True:
        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            analyzer.create_array()
        elif choice == "2":
            analyzer.math_operations()
        elif choice == "3":
            analyzer.combine_split()
        elif choice == "4":
            analyzer.search_sort_filter()
        elif choice == "5":
            analyzer.aggregates_statistics()
        elif choice == "6":
            print("\nThank you for using the NumPy Analyzer!")
            print("Goodbye!")
            break
        else:
            print("Khoto choice! 1 thi 6 vachhe nakho.")


if __name__ == "__main__":
    main()
