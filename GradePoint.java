// GradePoint 河村拓実 コウムラタクミ 2023/10/13
// GPA計算用クラス
public class GradePoint {
    private int grade; // 成績
    private int credit; // 単位
    private int numSubject; // 科目数

    GradePoint(int grade, int credit, int numSubject)
    {
        if (grade < 1 || grade > 4) {
            throw new IllegalArgumentException("不正な成績です");
        }
        this.grade = grade;
        this.credit = credit;
        this.numSubject = numSubject;
    }

    public int denominator()
    {
        return credit * numSubject;
    }

    public int numerator()
    {
        return grade * credit * numSubject;
    }
}
