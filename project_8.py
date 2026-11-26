
import numpy as np


class DataAnalytics:
    """Interactive NumPy Analyzer using Object-Oriented Programming."""

    project_name = "NumPy Analyzer"

    def __init__(self, array=None):
        self.__array = array
        self.__history = []

    def get_array(self):
        return self.__array

    def set_array(self, array):
        self.__array = array
        self.__history.append("Array updated")

    def __validate_array(self):
        if self.__array is None:
            print("Please create an array first!")
            return False
        return True

    def __get_elements(self, count):
        while True:
            try:
                values = list(map(float, input(
                    f"Enter {count} elements separated by spaces: "
                ).split()))

                if len(values) != count:
                    print(f"Please enter exactly {count} elements.")
                    continue

                if all(v.is_integer() for v in values):
                    values = [int(v) for v in values]

                return values

            except ValueError:
                print("Invalid input! Enter numeric values only.")

    def __parse_range(self, prompt):
        while True:
            try:
                value = input(prompt).strip()

                if ":" in value:
                    start, end = value.split(":")
                    return int(start), int(end)

                print("Use start:end format. Example: 0:2")

            except ValueError:
                print("Invalid range! Try again.")

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

    def create_array(self):
        print("\nSelect Array Type:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                n = int(input("Enter number of elements: "))

                if n <= 0:
                    print("Size must be positive.")
                    return

                elements = self.__get_elements(n)
                self.__array = np.array(elements)

            elif choice == "2":
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))

                if not self.is_valid_shape((rows, cols)):
                    print("Invalid array dimensions.")
                    return

                elements = self.__get_elements(rows * cols)
                self.__array = np.array(elements).reshape(rows, cols)

            elif choice == "3":
                depth = int(input("Enter depth: "))
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))

                if not self.is_valid_shape((depth, rows, cols)):
                    print("Invalid array dimensions.")
                    return

                elements = self.__get_elements(depth * rows * cols)
                self.__array = np.array(elements).reshape(
                    depth, rows, cols
                )

            else:
                print("Invalid choice!")
                return

            print("\nArray created successfully:")
            print(self.__array)
            self.__history.append("Array created")

            self.indexing_slicing_menu()

        except ValueError:
            print("Please enter valid numbers.")

    def indexing_slicing_menu(self):
        while True:
            print("\n1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.do_indexing()
            elif choice == "2":
                self.do_slicing()
            elif choice == "3":
                break
            else:
                print("Invalid choice!")

    def do_indexing(self):
        if not self.__validate_array():
            return

        print("\nCurrent Array:")
        print(self.__array)

        try:
            if self.__array.ndim == 1:
                index = int(input("Enter index: "))
                print("Element:", self.__array[index])

            elif self.__array.ndim == 2:
                row = int(input("Enter row index: "))
                col = int(input("Enter column index: "))
                print("Element:", self.__array[row, col])

            else:
                depth = int(input("Enter depth index: "))
                row = int(input("Enter row index: "))
                col = int(input("Enter column index: "))
                print("Element:", self.__array[depth, row, col])

        except (ValueError, IndexError):
            print("Invalid index!")

    def do_slicing(self):
        if not self.__validate_array():
            return

        print("\nCurrent Array:")
        print(self.__array)

        try:
            if self.__array.ndim == 1:
                start, end = self.__parse_range(
                    "Enter range (start:end): "
                )
                result = self.__array[start:end]

            elif self.__array.ndim == 2:
                rs, re = self.__parse_range("Enter row range: ")
                cs, ce = self.__parse_range("Enter column range: ")
                result = self.__array[rs:re, cs:ce]

            else:
                ds, de = self.__parse_range("Enter depth range: ")
                rs, re = self.__parse_range("Enter row range: ")
                cs, ce = self.__parse_range("Enter column range: ")
                result = self.__array[ds:de, rs:re, cs:ce]

            print("\nSliced Array:")
            print(result)

        except ValueError:
            print("Invalid slicing range!")

    def get_second_array(self):
        if not self.__validate_array():
            return None

        elements = self.__get_elements(self.__array.size)

        second = np.array(elements).reshape(self.__array.shape)

        print("\nOriginal Array:")
        print(self.__array)

        print("\nSecond Array:")
        print(second)

        return second

    def math_operations(self):
        if not self.__validate_array():
            return

        print("\nMathematical Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3", "4", "5", "6"]:
            second = self.get_second_array()

            if second is None:
                return

            try:
                if choice == "1":
                    result = self.__array + second

                elif choice == "2":
                    result = self.__array - second

                elif choice == "3":
                    result = self.__array * second

                elif choice == "4":
                    if np.any(second == 0):
                        print("Division by zero is not allowed!")
                        return
                    result = self.__array / second

                elif choice == "5":
                    result = np.dot(self.__array, second)

                elif choice == "6":
                    if self.__array.ndim != 2:
                        print("Matrix multiplication requires 2D arrays!")
                        return
                    result = np.matmul(self.__array, second)

                print("\nResult:")
                print(result)

                self.__history.append("Mathematical operation performed")

            except ValueError as e:
                print("Operation failed:", e)

        else:
            print("Invalid choice!")

    def combine_split(self):
        if not self.__validate_array():
            return

        print("\n1. Combine Arrays")
        print("2. Split Array")

        choice = input("Enter your choice: ")

        if choice == "1":
            second = self.get_second_array()

            if second is None:
                return

            print("\n1. Vertical Stack")
            print("2. Horizontal Stack")
            print("3. Concatenate")

            option = input("Enter your choice: ")

            try:
                if option == "1":
                    result = np.vstack((self.__array, second))

                elif option == "2":
                    result = np.hstack((self.__array, second))

                elif option == "3":
                    result = np.concatenate(
                        (self.__array, second), axis=0
                    )

                else:
                    print("Invalid choice!")
                    return

                print("\nCombined Array:")
                print(result)

            except ValueError as e:
                print("Combination failed:", e)

        elif choice == "2":
            try:
                parts = int(input("Enter number of parts: "))

                if parts <= 0:
                    print("Number of parts must be positive.")
                    return

                result = np.array_split(self.__array, parts)

                for i, part in enumerate(result, 1):
                    print(f"\nPart {i}:")
                    print(part)

            except ValueError:
                print("Invalid number!")

        else:
            print("Invalid choice!")

    def search_sort_filter(self):
        if not self.__validate_array():
            return

        print("\n1. Search")
        print("2. Sort")
        print("3. Filter")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                value = float(input("Enter value to search: "))
                indices = np.where(self.__array == value)

                print("\nOriginal Array:")
                print(self.__array)

                if len(indices[0]) == 0:
                    print("Value not found!")
                else:
                    print("Found at indices:", indices)
                    print("Total occurrences:", len(indices[0]))

            except ValueError:
                print("Invalid value!")

        elif choice == "2":
            print("\n1. Ascending")
            print("2. Descending")

            order = input("Enter your choice: ")

            sorted_arr = np.sort(self.__array, axis=-1)

            if order == "2":
                sorted_arr = np.flip(sorted_arr, axis=-1)
            elif order != "1":
                print("Invalid choice!")
                return

            print("\nSorted Array:")
            print(sorted_arr)

        elif choice == "3":
            print("\n1. Greater Than")
            print("2. Less Than")
            print("3. Equal To")
            print("4. Even Numbers")
            print("5. Odd Numbers")

            option = input("Enter your choice: ")

            if option in ["1", "2", "3"]:
                try:
                    value = float(input("Enter comparison value: "))

                    if option == "1":
                        result = self.__array[self.__array > value]

                    elif option == "2":
                        result = self.__array[self.__array < value]

                    else:
                        result = self.__array[self.__array == value]

                    print("\nFiltered Values:")
                    print(result)

                except ValueError:
                    print("Invalid value!")

            elif option == "4":
                print(self.__array[self.__array % 2 == 0])

            elif option == "5":
                print(self.__array[self.__array % 2 != 0])

            else:
                print("Invalid choice!")

        else:
            print("Invalid choice!")

    def aggregates_statistics(self):
        if not self.__validate_array():
            return

        print("\nStatistical Operations:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum and Maximum")
        print("7. Percentiles")
        print("8. Correlation Coefficient")

        choice = input("Enter your choice: ")

        print("\nOriginal Array:")
        print(self.__array)

        if choice == "1":
            print("Sum:", np.sum(self.__array))

        elif choice == "2":
            print("Mean:", np.mean(self.__array))

        elif choice == "3":
            print("Median:", np.median(self.__array))

        elif choice == "4":
            print("Standard Deviation:", np.std(self.__array))

        elif choice == "5":
            print("Variance:", np.var(self.__array))

        elif choice == "6":
            print("Minimum:", np.min(self.__array))
            print("Maximum:", np.max(self.__array))

        elif choice == "7":
            try:
                p = float(input("Enter percentile (0-100): "))

                if not 0 <= p <= 100:
                    print("Percentile must be between 0 and 100.")
                    return

                print(f"{p}th Percentile:",
                      np.percentile(self.__array, p))
                print("25th Percentile:",
                      np.percentile(self.__array, 25))
                print("50th Percentile:",
                      np.percentile(self.__array, 50))
                print("75th Percentile:",
                      np.percentile(self.__array, 75))

            except ValueError:
                print("Invalid percentile!")

        elif choice == "8":
            second = self.get_second_array()

            if second is None:
                return

            try:
                corr = np.corrcoef(
                    self.__array.flatten(),
                    second.flatten()
                )

                print("\nCorrelation Matrix:")
                print(corr)
                print("Correlation Coefficient:", corr[0, 1])

            except (ValueError, FloatingPointError) as e:
                print("Correlation failed:", e)

        else:
            print("Invalid choice!")


def main():
    analyzer = DataAnalytics()

    DataAnalytics.show_welcome()

    while True:
        print("\n" + "=" * 55)
        print("              MAIN MENU")
        print("=" * 55)

        print("1. Create a NumPy Array")
        print("2. Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Aggregates and Statistics")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

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
            print("\nThank you for using NumPy Analyzer!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1 and 6.")


if __name__ == "__main__":
    main()
```
