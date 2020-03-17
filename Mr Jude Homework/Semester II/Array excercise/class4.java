import java.util.Scanner;

public class class4 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Input an odd number: ");
        int n = input.nextInt();
        if (n % 2 == 0) {
            System.out.println("Error. Try inputting an odd number");
            System.exit(0);
        }
        int square[][] = new int[n + 2][n + 2];
        int i = 1, j = (n / 2) + 1;
        for (int m = 1; m <= Math.pow(n, 2); m++) {
            square[i][j] = m;
            if (i - 1 < 1) {
                i = n;
            } else {
                i = i - 1;
            }
            if (j + 1 > n) {
                j = 1;
            } else {
                j = j + 1;
            }
            if (square[i][j] != 0) {
                i = i + 1;
                j = j - 1;
                if (i > n) {
                    i = 1;
                }
                if (j < 1) {
                    j = n;
                }
                i++;
            }
        }
        for (int k = 1; k <= n; k++) {
            for (int l = 1; l <= n; l++) {
                System.out.print("|" + square[k][l] + "");
            }
            System.out.println("|");
        }
    }
}