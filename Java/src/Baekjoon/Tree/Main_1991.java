package Baekjoon.Tree;

import java.io.*;
import java.util.*;

public class Main_1991 {
    static class Node {
        char data;
        Node left;
        Node right;

        Node(char data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    static StringBuilder preorder = new StringBuilder();
    static StringBuilder inorder = new StringBuilder();
    static StringBuilder postorder = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Node[] nodes = new Node[26];
        for (int i = 0; i < 26; i++) {
            nodes[i] = new Node((char)('A' + i));
        }

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            char parent = st.nextToken().charAt(0);
            char leftChild = st.nextToken().charAt(0);
            char rightChild = st.nextToken().charAt(0);

            if (leftChild != '.') {
                nodes[parent - 'A'].left = nodes[leftChild - 'A'];
            }

            if (rightChild != '.') {
                nodes[parent - 'A'].right = nodes[rightChild - 'A'];
            }
        }

        Node root = nodes[0];

        preorderTraversal(root);
        inorderTraversal(root);
        postorderTraversal(root);

        System.out.println(preorder);
        System.out.println(inorder);
        System.out.println(postorder);
    }

    static void preorderTraversal(Node node) {
        if (node == null) return;

        preorder.append(node.data);
        preorderTraversal(node.left);
        preorderTraversal(node.right);
    }

    static void inorderTraversal(Node node) {
        if (node == null) return;

        inorderTraversal(node.left);
        inorder.append(node.data);
        inorderTraversal(node.right);
    }

    static void postorderTraversal(Node node) {
        if (node == null) return;

        postorderTraversal(node.left);
        postorderTraversal(node.right);
        postorder.append(node.data);
    }
}
