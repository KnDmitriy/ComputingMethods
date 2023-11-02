using System.Collections.Generic;
using System.Linq;
using System;
using System.Text;

public class A
{
    public static double L(double x_find, List<(double x, double y)> f, int n)
    {
        double summand;
        double res = 0;
        for (int i = 0; i < n; ++i)
        {
            summand = f[i].y;
            for (int j = 0; j < n; ++j)
            {
                if (j != i)
                {
                    summand *= (x_find - f[j].x) / (f[i].x - f[j].x);
                }
            }
            res += summand;
        }
        return res;
    }
    public static double N(double x_find, List<(double x, double y)> f, double[][] pp)
    {
        double res = 0;
        double item = 1;
        for(int i = 0; i < f.Count; ++i)
        {
            item = pp[0][i];
            for(int j = 0; j < i; ++j)
            {
                item *= x_find - f[j].x; //item *= (x - x_j)
            }
            res += item;
        }
        return res;
    }
    public static double[][] PP(List<(double x, double y)> f, int n)
    {
        double[][] pp = new double[n][];
        for (int i = n, j = 0; i >= 1 && j < n; --i, ++j)
        {
            pp[j] = new double[i];
        }
        for (int j = 0; j < n; ++j)
        {
            pp[j][0] = f[j].y;
        }
        int counter = n - 1;
        for (int j = 1; j < n; ++j)
        {
            for (int i = 0; i < counter; ++i)
            {
                pp[i][j] = (pp[i + 1][j - 1] - pp[i][j - 1]) / (f[i + j].x - f[i].x);
            }
            --counter;
        }
        //for (int poryadok_minus_1 = 1; poryadok_minus_1 < n; ++poryadok_minus_1)
        //{
        //    for (int k = 0; k < n; ++k)
        //    {
        //        pp[k][poryadok_minus_1] = (pp[k + 1][poryadok_minus_1 - 1] - pp[k][poryadok_minus_1 - 1]) / (f[k + 1].x - f[k].x);
        //    }
        //}    
        return pp;
    }
    public static double[,] inputA(int n)
    {
        double[,] a = new double[n, n];
        return a;
    }
    //public static double[] MG(double[,] a, double[][] b)
    //{
    //    return
    //}
    //public static double[][] SLAU_Newton(List<(double x, double y)> f, int n, int h)
    //{
    //    double[][] slau = new double[n][];
    //    for (int i = n, j = 0; i >= 1 && j < n; --i, ++j)
    //    {
    //        slau[j] = new double[i];
    //    }
    //}

    public static void Main()
    {
        

        int n = 4;

        Console.Write("Введите количество дискретных значений, задающих функцию: ");
        //n = Convert.ToInt32(Console.ReadLine());
        List<(double x, double y)> f = new List<(double x, double y)>()
            {(1, 1), (2, 8), (3, 27), (4, 64)};
        /*  
          for (int i = 0; i < n; ++i)
          {
              double x, y;
              Console.Write($"Введите x_{i}:");
              x = Convert.ToDouble(Console.ReadLine());
              Console.Write($"Введите f_{i}:");
              y = Convert.ToDouble(Console.ReadLine());
              f.Add((x, y));
              Console.WriteLine();
          }*/
        //f.Sort();
        List<(double x, double y)> result_table = new List<(double x, double y)>();
        Console.WriteLine();
        for (int i = 0; i < n; ++i)
        {
            Console.WriteLine($"x_{i} = {f[i].x}");
            Console.WriteLine($"f_{0} = {f[i].y}");
            Console.WriteLine();
        }
        //double[,] table = new double[n + 1, n + 1];
        for (double i = 1; i <= 4; i += 0.5)
        {
            Console.WriteLine($"L({i}) = {L(i, f, n)}");

        }
        double[][] PP1 = PP(f, n);
        int counter = n;
        for (int j = 0; j < n; ++j)
        {
            for (int i = 0; i < counter; ++i)
            {
                Console.Write($"{PP1[j][i]}    ");
            }
            --counter;
            Console.WriteLine();
        }
        for (double i = 1; i <= 4; i += 0.5)
        {
            Console.WriteLine($"N({i}) = {N(i, f, PP1)}");

        }
        Console.ReadKey();
    }

}

