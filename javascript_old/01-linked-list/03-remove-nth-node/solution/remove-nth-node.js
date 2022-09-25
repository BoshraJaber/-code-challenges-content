'use strict';

const removeNthFromEnd = function(head, n) {

    if (!head.next) return null;
    if (n < 0) return null;
    let prev = head;
    let nthNode = head;
    let dummy = head;
    let counter = 1;

    while (dummy.next) {
        dummy = dummy.next;
        if (counter >= n) {
            prev = nthNode;
            nthNode = prev.next;
        }
        counter++;
    }
    if (prev.next === nthNode.next) {
        head = head.next;
        return head;
    }
    prev.next = nthNode.next
    return head;
};

module.exports = removeNthFromEnd;