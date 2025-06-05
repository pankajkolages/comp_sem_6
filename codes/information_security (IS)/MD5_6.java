import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.Scanner;

public class MD5_6 {

    // Shift amounts for each of the 64 rounds (from MD5 spec)
    private static final int[] rotateAmounts = {
            7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
            5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
            4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
            6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
    };

    // Constants derived from sine values (filled in static block)
    private static final int[] constants = new int[64];

    // Initial values of MD5 hash (IV - initialization vector)
    private static final int[] initValues = {
            0x67452301, // A
            0xefcdab89, // B
            0x98badcfe, // C
            0x10325476  // D
    };

    // Fill the constants array using the sine function (MD5 spec)
    static {
        for (int i = 0; i < 64; i++) {
            constants[i] = (int) ((long) (Math.abs(Math.sin(i + 1)) * (1L << 32)) & 0xFFFFFFFFL);
        }
    }

    // Left rotation of x by 'amount' bits (circular shift)
    private static int leftRotate(int x, int amount) {
        return (x << amount) | (x >>> (32 - amount));
    }

    // Main MD5 function that takes byte array input and returns MD5 digest
    public static byte[] md5(byte[] message) {
        int originalLength = message.length;
        long originalLengthBits = (long) originalLength * 8;

        // Calculate new padded length (multiple of 64 bytes)
        int newLength = ((originalLength + 8) / 64 + 1) * 64;
        byte[] paddedMessage = new byte[newLength];

        // Copy original message to padded message
        System.arraycopy(message, 0, paddedMessage, 0, originalLength);

        // Append '1' bit (in byte form as 0x80)
        paddedMessage[originalLength] = (byte) 0x80;

        // Append 64-bit little-endian representation of original message length (in bits)
        for (int i = 0; i < 8; i++) {
            paddedMessage[newLength - 8 + i] = (byte) (originalLengthBits >>> (8 * i));
        }

        // Initialize hash buffer values (A, B, C, D)
        int[] hashPieces = initValues.clone();

        // Process message in 512-bit (64-byte) chunks
        for (int chunkOffset = 0; chunkOffset < newLength; chunkOffset += 64) {
            // Break chunk into sixteen 32-bit little-endian words
            int[] words = new int[16];
            for (int i = 0; i < 16; i++) {
                words[i] = ByteBuffer.wrap(paddedMessage, chunkOffset + i * 4, 4)
                        .order(ByteOrder.LITTLE_ENDIAN)
                        .getInt();
            }

            // Initialize a, b, c, d for this chunk
            int a = hashPieces[0], b = hashPieces[1], c = hashPieces[2], d = hashPieces[3];

            // Main MD5 loop (64 operations)
            for (int i = 0; i < 64; i++) {
                int f, g;

                // Round 1
                if (i < 16) {
                    f = (b & c) | (~b & d);
                    g = i;
                }
                // Round 2
                else if (i < 32) {
                    f = (d & b) | (~d & c);
                    g = (5 * i + 1) % 16;
                }
                // Round 3
                else if (i < 48) {
                    f = b ^ c ^ d;
                    g = (3 * i + 5) % 16;
                }
                // Round 4
                else {
                    f = c ^ (b | ~d);
                    g = (7 * i) % 16;
                }

                // Calculate the transformation
                long temp = ((long) a + f + constants[i] + words[g]) & 0xFFFFFFFFL;
                a = d;
                d = c;
                c = b;
                b = (int) ((b + leftRotate((int) temp, rotateAmounts[i])) & 0xFFFFFFFFL);
            }

            // Add this chunk's result to overall hash
            hashPieces[0] = (hashPieces[0] + a) & 0xFFFFFFFF;
            hashPieces[1] = (hashPieces[1] + b) & 0xFFFFFFFF;
            hashPieces[2] = (hashPieces[2] + c) & 0xFFFFFFFF;
            hashPieces[3] = (hashPieces[3] + d) & 0xFFFFFFFF;
        }

        // Convert final hash to byte array (little endian)
        ByteBuffer buffer = ByteBuffer.allocate(16).order(ByteOrder.LITTLE_ENDIAN);
        for (int value : hashPieces) {
            buffer.putInt(value);
        }

        return buffer.array(); // Return 16-byte digest
    }

    // Converts MD5 byte array to hex string
    public static String md5ToHex(byte[] digest) {
        StringBuilder hexString = new StringBuilder();
        for (byte b : digest) {
            hexString.append(String.format("%02x", b & 0xFF));
        }
        return hexString.toString();
    }

    // Main method to read input and compute MD5 hash
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string to hash using MD5: ");
        String input = scanner.nextLine();
        scanner.close();

        // Hash the input
        byte[] hashedBytes = md5(input.getBytes());

        // Convert hash to hex string
        String hashedValue = md5ToHex(hashedBytes);

        // Print final hash
        System.out.println("MD5 hash: " + hashedValue);
    }
}

