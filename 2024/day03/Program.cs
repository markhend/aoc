using System.ComponentModel;

var _sampleFilePath = "/home/mhenders/aoc/2024/day01/in.txt";
var lines = File.ReadLines(_sampleFilePath).ToList();

// var stringBuilder = new StringBuilder();
int ans1 = 0, ans2 = 0;
var left = new List<int>();
var right = new List<int>();

foreach (var line in lines)
{
    var tmp = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);
    left.Add(int.Parse(tmp[0]));
    right.Add(int.Parse(tmp[1]));
}

left.Sort();
right.Sort();

for (int i = 0; i < left.Count; i++)
{
    ans1 += Math.Abs(left[i] - right[i]);
}

Console.WriteLine(ans1);

var rightCount = new Dictionary<int, int>();

foreach (var n in right)
{
    if (!rightCount.ContainsKey(n))
    {
        rightCount[n] = 1;
    }
    else
    {
        rightCount[n] += 1;
    }
}

foreach (var n in left)
{
    ans2 += n * (rightCount.TryGetValue(n, out int result) ? result : 0);
}

Console.WriteLine(ans2);