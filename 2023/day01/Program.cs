using System.Runtime.InteropServices;
using Microsoft.VisualBasic;

var _sampleFilePath = "in.txt";
var lines = File.ReadLines(_sampleFilePath);

// var stringBuilder = new StringBuilder();
var nums = new HashSet<char>("123456789");
var num_strings = new List<string>
{
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
};
char firstNum = 'x';
char lastNum = 'x';
bool found;
int total = 0;
int firstNumIdx = 0;
int lastNumIdx = 0;

foreach (var line in lines)
{
    Console.Write(line + " ");
    found = false;
    int idx = 0;
    foreach (var c in line)
    {
        if (nums.Contains(c))
        {
            if (!found)
            {
                firstNum = lastNum = c;
                firstNumIdx = idx;
                lastNumIdx = idx;
                found = true;
            }
            else
            {
                lastNum = c;
                lastNumIdx = idx;
            }
        }
        idx++;
    }
    var firstWordIdx = FirstWordIdx(line);
    var lastWordIdx = LastWordIdx(line);
    Console.Write($" {firstWordIdx} {lastWordIdx}");

    if (firstWordIdx < firstNumIdx) 
    {
        foreach (var s in num_strings)
        { 
            if (line.IndexOf(s) == firstWordIdx)
            {
                firstNum = WordToNum(s);
            }
        }
    }

    if (lastWordIdx > lastNumIdx)
    {
        foreach (var s in num_strings)
        { 
            if (line.LastIndexOf(s) == lastWordIdx)
            {
                lastNum = WordToNum(s);
            }
        }
    }

    Console.WriteLine($" {firstNum}{lastNum}");
    total += int.Parse($"{firstNum}{lastNum}");
}
Console.WriteLine(total);


int FirstWordIdx(string line)
{
    for (int i = 0; i < line.Length; i++)
    {
        foreach (var s in num_strings)
        {
            if (line.IndexOf(s) == i)
            {
                return i;
            }
        }
    }
    return 50;
}

int LastWordIdx(string line)
{
    var fill = "xxxxxxx";
    var len = line.Length;
    line = string.Concat(line, fill);
    for (int i = len - 1; i >= 0; i--)
    {
        foreach (var s in num_strings)
        {
            if (line.LastIndexOf(s) == i)
            {
                return i;
            }
        }
    }
    return -1;
}

char WordToNum(string s)
{
    switch (s)
    {
        case "one":
            return '1';
        case "two": 
            return '2';
        case "three": 
            return '3';
        case "four": 
            return '4';
        case "five": 
            return '5';
        case "six": 
            return '6';
        case "seven": 
            return '7';
        case "eight": 
            return '8';
        case "nine": 
            return '9';
        default:
            return '0';
    }
}
    