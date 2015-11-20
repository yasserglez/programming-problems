// Interview Question 1.4

import java.util.Queue;
import java.util.LinkedList;

public class ReplaceSpaces {

    public static void replaceSpaces(char[] str, int len) {
        int i = 0;
        Queue<Character> q = new LinkedList<Character>();

        while (i < len || !q.isEmpty()) {
            if (i < len && !q.isEmpty()) q.add(str[i]);
            char c = q.isEmpty() ? str[i] : q.remove();

            if (c == ' ') {
                str[i++] = '%';
                if (i < len) q.add(str[i]);
                str[i++] = '2';
                if (i < len) q.add(str[i]);
                str[i++] = '0';
            } else {
                str[i++] = c;
            }
        }
    }

    public static void main(String[] args) {
        char[] str = "Mr John Smith    ".toCharArray();
        int len = 13;
        replaceSpaces(str, len);
        System.out.println(new String(str));
    }
}
