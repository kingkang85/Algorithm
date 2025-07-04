package Programmers.Stack;

import java.util.*;

// Lv2. 올바른 괄호
public class Parentheses {
    static boolean parentheses(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (c == ')') {
                if (stack.isEmpty() || stack.pop() != '(') {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args) {
        System.out.println(parentheses("(())()"));
    }
}
