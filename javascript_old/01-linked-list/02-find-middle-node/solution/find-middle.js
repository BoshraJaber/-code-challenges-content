'use strict';

const findMiddle = (head) => {
    if (!head.next) {
        return head;
    }
    let oneJump = head;
    let twoJump = oneJump;
    while (twoJump && twoJump.next) {
        oneJump = oneJump.next;
        twoJump = twoJump.next.next;
    }
    return oneJump;
}

module.exports = findMiddle;