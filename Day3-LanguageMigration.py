#Notes
# When migrating from C# to Python:
# No static keyword in the same way (Python functions are standalone)
# No explicit type declarations (int, string, etc.)
# No Console.Write
# No LINQ methods like .Sum() or .Max()
# No Enum.GetName
# Python uses built-in functions like sum(), max()
# Simpler loops and string handling

# C# = Python:
#static int = def function():
#string = str
#numbers.Sum() = sum(numbers)
#numbers.Max() = max(numbers)
#foreach = for item is iterable
#Console.Write = print()
#Enum.GetName() = list index

# 1. Square

# C#
#public static int Square(int number)
#{
#    return number * number;
#}

# Python
def square(number):
    return number * number


# 2. Concatenate Strings

# C#
#public static string ConcatenateStrings(string str1, string str2)
#{
#    return str1 + str2;
#}

# Python
def concatenate_strings(str1, str2):
    return str1 + str2

# 3. Count Vowels

# C#
#public static int CountVowels(string input)
#{
#    string vowels = "aeiouAEIOU";
#    int count = 0;

#    foreach (char character in input)
#    {
#        if (vowels.Contains(character))
#        {
#            count++;
#        }
#    }
#
#    return count;
#}

# Python
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for character in input_string:
        if character in vowels:
            count += 1
    return count


# 4. Sum Array

# C#
#public static int SumArray(int[] numbers)
#{
#    return numbers.Sum();
#}

# Python
def sum_array(numbers):
    return sum(numbers)


# 5. Print Multiples

# C#
#public static void PrintMultiples(int n)
#{
#    for (int i = 1; i <= 5; i++)
#    {
#        Console.Write(n * i + " ");
#    }
#    Console.WriteLine();
#}

# Pyhton
def print_multiples(n):
    for i in range(1, 6):
        print(n * i, end=" ")
    print()


# 6. Get Day Of Week

# C#
#public static string GetDayOfWeek(int day)
#{
#    return Enum.GetName(typeof(DayOfWeek), day);
#}

# Python
def get_day_of_week(day):
    days = [
        "Sunday", "Monday", "Tuesday", 
        "Wednesday", "Thursday", "Friday", "Saturday"
    ]
    if 0 <= day < len(days):
        return days[day]
    return None


# 7. Find Max

# C#
#public static int FindMax(int[] numbers)
#{
#    return numbers.Max();
#}

# Python
def find_max(numbers):
    return max(numbers)


# 8. Celsius To Fahrenheit

# C#
#public static double CelsiusToFahrenheit(double celsius)
#{
#    return (celsius * 9 / 5) + 32;
#}
 
#Python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# 9. Is Prime

# C#
#public static bool IsPrime(int number)
#{
#    if (number < 2) return false;
#    for (int i = 2; i <= Math.Sqrt(number); i++)
#    {
#        if (number % i == 0) return false;
#    }
#    return true;
#}

# Python
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# 10. Reverse Words

# C#
#public static string ReverseWords(string sentence)
#{
#    string[] words = sentence.Split(' ');
#    Array.Reverse(words);
#    return string.Join(' ', words);
#}

#Python
def reverse_words(sentence):
    words = sentence.split(" ")
    words.reverse()
    return " ".join(words)

# Running each code to ensure it works correctly
def tests():
    print("Testing square:", square(4) == 16)
    print("Testing concatenate_strings:", concatenate_strings("Hello", "World") == "HelloWorld")
    print("Testing count_vowels:", count_vowels("Hello") == 2)
    print("Testing sum_array:", sum_array([1, 2, 3, 4]) == 10)
    
    print("Testing print_multiples (should print 5 10 15 20 25):")
    print_multiples(5)
    
    print("Testing get_day_of_week:", get_day_of_week(1) == "Monday")
    print("Testing find_max:", find_max([3, 7, 2, 9]) == 9)
    print("Testing celsius_to_fahrenheit:", celsius_to_fahrenheit(0) == 32)
    print("Testing is_prime:", is_prime(7) == True and is_prime(8) == False)
    print("Testing reverse_words:", reverse_words("Hello World") == "World Hello")


tests()