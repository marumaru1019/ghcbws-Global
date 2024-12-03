import java.util.Scanner;

public class TryCopilotChat {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.println("Enter the base salary (in yen):");
    int baseSalary = scanner.nextInt();

    System.out.println("Enter overtime hours (hours):");
    int overtimeHours = scanner.nextInt();

    int salary = calculateSalary(baseSalary, overtimeHours);
    System.out.println("Your salary is" + salary + "yen.");
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