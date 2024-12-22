#include <iostream>
using namespace std;

struct Node {
    long long n;
    Node *next;
};

long long countDigits(long long n) {
    long long count = 0;
    while (n != 0) {
        count++;
        n = n / 10;
    }
    return count;
} 

long long firstNumber(long long break_index, long long value) {
    string str = to_string(value), final_string = "";
    for (long long i = 0; i <= break_index; i++)
        final_string += str[i];
    
    return stoll(final_string);
}

long long secondNumber(long long break_index, long long digits, long long value) {
    string str = to_string(value), final_string = "";
    for (long long i = break_index+1; i < digits; i++)
        final_string += str[i];
    
    return stoll(final_string);
}

void printList(Node *list) {
    while (list != NULL) {
        cout << list->n << " -> ";
        list = list->next;
    }
    cout << "\n\n";
}

long long get_number(long long number) {
    cout << number << '\n';
    Node *cur = new Node;
    cur->next = NULL;
    cur->n = number;
    Node *first = cur;
    long long count = 1, digits;

    for (long long i = 0; i < 25; i++) {
        cur = first;
        while (cur != NULL) {
            if (cur->n == 0) cur->n = 1;
            else if ((digits = countDigits(cur->n)) % 2 == 0) {
                count++;
                long long break_index = digits / 2 - 1;
                long long num1 = firstNumber(break_index, cur->n);
                long long num2 = secondNumber(break_index, digits, cur->n);
                cur->n = num1;
                // insert after cur
                Node *new_node = new Node;
                new_node->n = num2;
                new_node->next = cur->next;
                cur->next = new_node;
                cur = cur->next;
            }
            else cur->n = cur->n * 2024;
            cur = cur->next;
        }
    }
    return count;
}

int main() {
    int nums[] = {20, 82084, 1650, 3, 346355, 363, 7975858, 0};
    int len = 8;
    long long count = 0;

    for (int i = 0; i < len; i++) {
        count += get_number(nums[i]);
    }

    cout << '\n' << count;
    return 0;
}