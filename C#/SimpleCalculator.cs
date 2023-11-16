using System;

Console.WriteLine("Welcome to Simple Calculator!\n");

Console.Write("Enter number one: ");

string inputNumber1 = Console.ReadLine();
float number1 = float.Parse(inputNumber1);

Console.Write("Enter number two: ");

string inputNumber2 = Console.ReadLine();
float number2 = float.Parse(inputNumber2);

Console.Write("Enter operator (*,/,+,-): ");

string operatorr = Console.ReadLine();
    

if (operatorr == "*")
{
    float result = number1 * number2;
    Console.WriteLine("Your output is: " + result);
}
else if (operatorr == "/")
{
    float result = number1 / number2;
    Console.WriteLine("Your output is: " + result);
}
else if (operatorr == "+")
{
    float result = number1 + number2;
    Console.WriteLine("Your output is: " + result);
}
else if (operatorr == "-")
{
    float result = number1 - number2;
    Console.WriteLine("Your output is: " + result);
}
else
{
    Console.WriteLine("Invalid operator");
}