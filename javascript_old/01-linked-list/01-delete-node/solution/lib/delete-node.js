'use strict';

const deleteNode = (node) => {
    if (node.val == null) {
        return 'the node have no value'
    } else {
        node.val = node.next.val;
        node.next = node.next.next;
    }
};

module.exports = deleteNode;