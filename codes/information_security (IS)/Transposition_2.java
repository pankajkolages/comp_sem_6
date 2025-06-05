import java.util.Scanner;
public class Transposition_2 {

    // Transposition Cipher Encryption Function
    public static String encrypt(String plaintext, int key) {
        // Create a grid (array of strings) for each column
        StringBuilder[] grid = new StringBuilder[key];
        for (int i = 0; i < key; i++) {
            grid[i] = new StringBuilder();
        }

        // Fill the grid column by column
        for (int i = 0; i < plaintext.length(); i++) {
            grid[i % key].append(plaintext.charAt(i));
        }

        // Combine the columns into the ciphertext
        StringBuilder ciphertext = new StringBuilder();
        for (int i = 0; i < key; i++) {
            ciphertext.append(grid[i]);
        }

        return ciphertext.toString();
    }

    // Transposition Cipher Decryption Function
    public static String decrypt(String ciphertext, int key) {
        // Calculate the number of rows and extra characters
        int numRows = ciphertext.length() / key;
        int numExtraChars = ciphertext.length() % key;

        // Create a grid (array of strings) for each column
        StringBuilder[] grid = new StringBuilder[key];
        for (int i = 0; i < key; i++) {
            grid[i] = new StringBuilder();
        }

        // Fill the grid column by column
        int pointer = 0;
        for (int i = 0; i < key; i++) {
            int length = numRows + (i < numExtraChars ? 1 : 0);
            for (int j = 0; j < length; j++) {
                grid[i].append(ciphertext.charAt(pointer++));
            }
        }

        // Reconstruct the original message by reading row by row
        StringBuilder plaintext = new StringBuilder();
        for (int i = 0; i < numRows + (numExtraChars > 0 ? 1 : 0); i++) {
            for (int j = 0; j < key; j++) {
                if (i < grid[j].length()) {
                    plaintext.append(grid[j].charAt(i));
                }
            }
        }

        return plaintext.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Take input for plaintext and key
        System.out.print("Enter the plaintext: ");
        String plaintext = scanner.nextLine();
        System.out.print("Enter the key (integer): ");
        int key = scanner.nextInt();

        // Encrypt the plaintext
        String ciphertext = encrypt(plaintext, key);
        System.out.println("Encrypted Text: " + ciphertext);

        // Decrypt the ciphertext
        String decryptedText = decrypt(ciphertext, key);
        System.out.println("Decrypted Text: " + decryptedText);

        scanner.close();
    }
}

