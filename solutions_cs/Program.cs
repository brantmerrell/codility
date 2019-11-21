using System;

namespace solutions_cs
{
    class Program
    {
        static void Main(string[] args)
        {
            if(args.Length == 0)
            {
                int[] lesson_1_inputs = new int[] {1041, 15, 32};
                foreach(int input in lesson_1_inputs)
                {
                    Console.WriteLine("binary_gap(" + input + "): " + binary_gap(input));
                }
            }
            else
            {
                foreach(String arg in args) {
                    if(Int32.TryParse(arg, out int j))
                    {
                        Console.WriteLine("binary_gap(" + j + "): " + binary_gap(j));
                    }
                    else
                    {
                        Console.WriteLine(arg + "?");
                    }
                }
            }
        }
        public static int binary_gap(int N)
        {
            // convert to binary string
            String bin = Convert.ToString(N, 2);
            // remove trailing/leading zeros; split by 1s
            bin = Regex.Replace(bin,"^0+|0+$","");

            // split by 1s
            String[] binArray = bin.Split("1");

            // convert each binary gap to a character count
            int[] gaps = new int[binArray.Length];
            for(int i = 0; i < binArray.Length; i++) {
                gaps[i] = binArray[i].length();
            }

            // obtain maximum number from character counts
            int result = 0;
            for(int i = 0; i < gaps.Length; i++) {
                if (gaps[i] > result) {
                    result = gaps[i];
                }
            }
            return result;
        }
    }
}
