"use strict";
class Node {
  constructor(value, left = null, right = null) {
    this.value = value === undefined ? 0 : value;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

const buildTree = (preorder, inorder) => {
  if (!preorder.length || !inorder.length) return null;
  let root = new Node(preorder[0]);
  let rootIndexInorder = inorder.indexOf(preorder[0]);
  root.left = buildTree(
    preorder.slice(1, rootIndexInorder + 1),
    inorder.slice(0, rootIndexInorder)
  );
  root.right = buildTree(
    preorder.slice(rootIndexInorder + 1),
    inorder.slice(rootIndexInorder + 1)
  );
  return root;
};

// preorder = [3, 9, 20, 15, 7];
// inorder = [9, 3, 15, 20, 7];
// console.log(buildTree(preorder, inorder));
module.exports = {
  buildTree,
  Node,
};
