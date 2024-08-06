import java.util.Scanner;

public class TryCopilotChat {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.println("基本給を入力してください（円）：");
    int baseSalary = scanner.nextInt();

    System.out.println("残業時間を入力してください（時間）：");
    int overtimeHours = scanner.nextInt();

    int salary = calculateSalary(baseSalary, overtimeHours);
    System.out.println("あなたの給与は" + salary + "円です。");
  }

  public static int calculateSalary(int baseSalary, int overtimeHours) {
    final int OVERTIME_RATE = baseSalary * 1.25;
    int overtimePay = OVERTIME_RATE * overtimeHours;
    int salary = baseSalary + overtimePay;
    final double DEDUCTION_RATE = 0.2;
    int deduction = (int) (salary * DEDUCTION_RATE);
    int netSalary = salary - deduction;
    return netSalary;
  }
}