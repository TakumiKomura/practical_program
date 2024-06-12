// GPA 河村拓実 コウムラタクミ 2023/10/13

import java.util.ArrayList;
import java.util.Scanner;
public class GPA {
    public static void main(String[] args) {
        ArrayList<GradePoint> gradePoints = new ArrayList<GradePoint>();
        Scanner sc = new Scanner(System.in);

        boolean isArrive = true;
        while(isArrive)
        {
            System.out.print("単位数: ");
            int credit = sc.nextInt();

            System.out.print("成績  : ");
            int grade = sc.nextInt();

            System.out.print("科目数: ");
            int numSubject = sc.nextInt();

            gradePoints.add(new GradePoint(grade, credit, numSubject));

            System.out.print("入力続行-> 1 ,計算開始-> 0 : ");
            if (sc.nextInt() == 0) {
                isArrive = false;
            }
            System.out.println("");
        }
        sc.close();

        double gpa = calcGPA(gradePoints);

        System.out.println("GPA : "+gpa);
    }
    
    public static double calcGPA(ArrayList<GradePoint> gradePoints)
    {
        int totalDenominator = 0;
        int totalNumerator = 0;
        for (GradePoint gradePoint : gradePoints) {
            totalDenominator += gradePoint.denominator();
            totalNumerator += gradePoint.numerator();
        }

        return (double) totalNumerator / totalDenominator;
    }
}