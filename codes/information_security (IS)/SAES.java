import java.util.Scanner;
public class SAES {
    // S-Box for substitution
    private static final int[] SBOX = {
        0x9, 0x4, 0xA, 0xB, 0xD, 0x1, 0x8, 0x5,
        0x6, 0x2, 0x0, 0x3, 0xC, 0xE, 0xF, 0x7
    };

    // Function to apply S-Box substitution
    private static int substituteNibbles(int state) {
        return (SBOX[(state >> 4) & 0x0F] << 4) | SBOX[state & 0x0F];
    }

    // Function to shift rows (swap nibbles)
    private static int shiftRows(int state) {
        return ((state & 0xF0) >> 4) | ((state & 0x0F) << 4);
    }

    // Function to XOR with key
    private static int addRoundKey(int state, int key) {
        return state ^ key;
    }

    // Improved Key Expansion (ensuring distinct round keys)
    private static int[] keyExpansion(int key) {
        int w0 = (key >> 8) & 0xFF;
        int w1 = key & 0xFF;
        int rcon = 0x80; // Example round constant for SAES

        // Generate w2 by applying S-Box to w1 and XOR with w0 and rcon
        int w2 = w0 ^ (SBOX[w1 >> 4] << 4) ^ SBOX[w1 & 0x0F] ^ rcon;
        int w3 = w2 ^ w1; // w3 is derived from w2

        return new int[]{(w0 << 8) | w1, (w2 << 8) | w3};
    }

    // SAES Encryption Function for a single character
    public static int saesEncrypt(int plaintext, int key) {
        // Generate round keys
        int[] roundKeys = keyExpansion(key);

        // Initial Add Round Key
        int state = addRoundKey(plaintext & 0xFF, roundKeys[0] & 0xFF);

        // Round 1: Substitute, Shift Rows, Add Round Key
        state = substituteNibbles(state);
        state = shiftRows(state);
        state = addRoundKey(state, roundKeys[1] & 0xFF);

        return state & 0xFF;
    }

    // Function to encrypt a string using SAES
    public static String encryptString(String input, int key) {
        StringBuilder encryptedText = new StringBuilder();
        for (char c : input.toCharArray()) {
            int charValue = c & 0xFF; // Convert character to 8-bit ASCII
            int encryptedChar = saesEncrypt(charValue, key);
            encryptedText.append(encryptedChar).append(" ");
        }
        return encryptedText.toString().trim();
    }

    // Main function to get user input and perform encryption
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Take string input
        System.out.print("Enter a string to encrypt: ");
        String plaintext = scanner.nextLine();

        // Take decimal input for key
        System.out.print("Enter key (decimal): ");
        int key = scanner.nextInt();

        // Encrypt the string
        String ciphertext = encryptString(plaintext, key);

        // Display results
        System.out.println("\n=== SAES Encryption Output ===");
        System.out.println("Plaintext: " + plaintext);
        System.out.println("Key (Decimal): " + key);
        System.out.println("Ciphertext: " + ciphertext);

        scanner.close();
    }
}
