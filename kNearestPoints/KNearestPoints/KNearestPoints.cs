using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KNearestPoints
{
    class KNearestPoints
    {
        static void Main(string[] args)
        {
            List<int[]> points = new List<int[]>() {
                new int[] { 1, 6 },
                new int[] { -3, -3 },
                new int[] { 4, 2 },
                new int[] { 7, 3 },
                new int[] { -6, 1 },
                new int[] { 2, 3 },
                new int[] { 4, 3 },
                new int[] { -3, 1 },
                new int[] { 3, -2 }
            };
            int k = 4;
            var result = DetermineNearestPoints(points, k);

            Console.WriteLine("The nearest points are: ");
            result.ForEach(x => Console.WriteLine("[{0}]",string.Join(",",x.ToList())));
            Console.ReadLine();
        }

        private static List<int[]> DetermineNearestPoints(List<int[]> points, int k)
        {
            var returnValue = new List<int[]>();
            var pointsWithDistance = new Dictionary<int[], int>();

            DetermineDistanceFromOrigin(points, ref pointsWithDistance);

            for (int i = 0; i < k; i++)
            {
                returnValue.Add(pointsWithDistance.OrderBy(x => x.Value).ElementAt(i).Key);
            }

            return returnValue;
        }

        private static void DetermineDistanceFromOrigin(List<int[]> points, ref Dictionary<int[], int> pointsWithDistance)
        {
            foreach (var item in points)
            {
                pointsWithDistance.Add(item, Convert.ToInt32(Math.Sqrt(Convert.ToDouble(item[0] * item[0] + item[1] * item[1]))));
            }
        }
    }
}
