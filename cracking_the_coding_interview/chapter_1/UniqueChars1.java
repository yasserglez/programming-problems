// Interview Question 1.1

// Time complexity: O(n)
// Auxiliary space complexity: O(n)

import java.util.Set;
import java.util.HashSet;

public class UniqueChars1 {

    public static boolean uniqueChars1(String str) {
        Set<Character> set = new HashSet<Character>();

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (set.contains(c)) {
                return false;
            }
            set.add(c);
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(uniqueChars1(""));
        System.out.println(uniqueChars1("a"));
        System.out.println(uniqueChars1("aa"));
        System.out.println(uniqueChars1("abc"));
        System.out.println(uniqueChars1("abca"));
        System.out.println(uniqueChars1("abcb"));
        System.out.println(uniqueChars1("abcc"));
    }
}
