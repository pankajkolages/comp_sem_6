import java.util.Scanner;

public class RSA_4 {

    // Function to compute (base^expo) % mod efficiently (modular exponentiation)
    public static int power(int base, int expo, int mod) {
        int result = 1;
        base = base % mod;
        while (expo > 0) {
            if ((expo % 2) == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            expo = expo >> 1;
        }
        return result;
    }

    // Compute GCD (Greatest Common Divisor)
    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }

    // Check if a number is prime
    public static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    // Find modular inverse of e mod phi
    public static int modInverse(int e, int phi) {
        for (int d = 2; d < phi; d++) {
            if ((e * d) % phi == 1) {
                return d;
            }
        }
        return -1;
    }

    // Main RSA method
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input prime p
        System.out.print("Enter a prime number (p): ");
        int p = sc.nextInt();
        if (!isPrime(p)) {
            System.out.println("p is not a prime number. Exiting.");
            return;
        }

        // Input prime q
        System.out.print("Enter another prime number (q): ");
        int q = sc.nextInt();
        if (!isPrime(q)) {
            System.out.println("q is not a prime number. Exiting.");
            return;
        }

        // Calculate n and phi
        int n = p * q;
        int phi = (p - 1) * (q - 1);

        // Choose e such that gcd(e, phi) = 1
        int e = 2;
        while (e < phi) {
            if (gcd(e, phi) == 1) break;
            e++;
        }

        // Calculate d = modular inverse of e
        int d = modInverse(e, phi);
        if (d == -1) {
            System.out.println("No modular inverse found. Exiting.");
            return;
        }

        // Print keys
        System.out.println("Public Key (e, n): (" + e + ", " + n + ")");
        System.out.println("Private Key (d, n): (" + d + ", " + n + ")");

        // Input message
        System.out.print("Enter a message (as a number) to encrypt: ");
        int message = sc.nextInt();

        // Encrypt
        int cipher = power(message, e, n);
        System.out.println("Encrypted Message: " + cipher);

        // Decrypt
        int decrypted = power(cipher, d, n);
        System.out.println("Decrypted Message: " + decrypted);

        sc.close();
    }
}
