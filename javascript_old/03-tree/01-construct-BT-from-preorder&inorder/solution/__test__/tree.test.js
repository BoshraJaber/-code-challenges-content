"use strict";

const { buildTree, Node } = require("../index");
const {
  isSameTree,
} = require("../../../02-breadth-first-traversal/javascript/index");
const {
  arrayToBST,
} = require("../../../03-convert-sorted-array-to-BST/javascript/index");

describe("test 01 ", () => {
  it("buildTree function should successfully return null if Preorder or Inorder Traversal is empty ", () => {
    let preorder = [];
    let inorder = [9, 3, 15, 20, 7];
    let node = new Node(3);
    node.left = new Node(9);
    node.right = new Node(20);
    node.right.right = new Node(7);
    node.right.left = new Node(15);

    expect(buildTree(preorder, inorder)).toBeNull();
  });

  it("buildTree function should successfully Construct Binary Tree from Preorder and Inorder Traversal (multiple elements in the array) ", () => {
    let preorder = [3, 9, 20, 15, 7];
    let inorder = [9, 3, 15, 20, 7];
    let node = new Node(3);
    node.left = new Node(9);
    node.right = new Node(20);
    node.right.right = new Node(7);
    node.right.left = new Node(15);

    expect(buildTree(preorder, inorder)).toEqual(node);
  });

  it("buildTree function should successfully Construct Binary Tree from Preorder and Inorder Traversal (single element in the array)", () => {
    let preorder = [-1];
    let inorder = [-1];
    let node = new Node(-1);
    expect(buildTree(preorder, inorder)).toEqual(node);
  });
});

describe("test 02 ", () => {
  it("isSameTree function should successfully return true if the given two binary trees are the same", () => {
    let firstTree = new Node(2);
    firstTree.left = new Node(7);
    firstTree.right = new Node(5);
    firstTree.right.right = new Node(9);
    firstTree.right.right.left = new Node(4);
    firstTree.left.left = new Node(2);
    firstTree.left.right = new Node(6);
    firstTree.left.right.left = new Node(5);
    firstTree.left.right.right = new Node(11);

    let secondTree = new Node(2);
    secondTree.left = new Node(7);
    secondTree.right = new Node(5);
    secondTree.right.right = new Node(9);
    secondTree.right.right.left = new Node(4);
    secondTree.left.left = new Node(2);
    secondTree.left.right = new Node(6);
    secondTree.left.right.left = new Node(5);
    secondTree.left.right.right = new Node(11);

    expect(isSameTree(firstTree, secondTree)).toBeTruthy();
  });

  it("isSameTree function should successfully return false if the given two binary trees are not the same", () => {
    let firstTree = new Node(2);
    firstTree.left = new Node(7);
    firstTree.right = new Node(5);
    firstTree.right.right = new Node(9);
    firstTree.right.right.left = new Node(4);
    firstTree.left.left = new Node(2);
    firstTree.left.right = new Node(6);
    firstTree.left.right.left = new Node(5);
    firstTree.left.right.right = new Node(11);

    let SecondTree = new Node(2);
    SecondTree.left = new Node(7);
    SecondTree.right = new Node(5);
    SecondTree.right.right = new Node(9);
    SecondTree.right.right.left = new Node(4);
    SecondTree.left.left = new Node(2);
    SecondTree.left.right = new Node(6);
    SecondTree.left.right.left = new Node(5);
    SecondTree.left.right.right = new Node(4);

    expect(isSameTree(firstTree, SecondTree)).toBeFalsy();
  });

  it("isSameTree function should successfully return false if one of the given two binary trees empty", () => {
    let firstTree = new Node();

    let SecondTree = new Node(2);
    SecondTree.left = new Node(7);
    SecondTree.right = new Node(5);
    SecondTree.right.right = new Node(9);
    SecondTree.right.right.left = new Node(4);
    SecondTree.left.left = new Node(2);
    SecondTree.left.right = new Node(6);
    SecondTree.left.right.left = new Node(5);
    SecondTree.left.right.right = new Node(4);

    expect(isSameTree(firstTree, SecondTree)).toBeFalsy();
  });

  it("isSameTree function should successfully return true if the given two binary trees are empty", () => {
    let firstTree = new Node();

    let SecondTree = new Node();

    expect(isSameTree(firstTree, SecondTree)).toBeTruthy();
  });
});

describe("test 03 ", () => {
  it("arrayToBST function should successfully return BST from given sorted array", () => {
    let BST = new Node(0);
    BST.left = new Node(-10);
    BST.left.right = new Node(-3);
    BST.right = new Node(5);
    BST.right.right = new Node(9);

    let nums = [-10, -3, 0, 5, 9];
    expect(arrayToBST(nums, 0, nums.length - 1)).toEqual(BST);
  });

  it("arrayToBST function should successfully return null if the given array is empty", () => {
    let nums = [];
    expect(arrayToBST(nums, 0, nums.length - 1)).toBeNull();
  });

  it("arrayToBST function should successfully return one node if the given array have one elenment", () => {
    let nums = [1];
    let BST = new Node(1);
    expect(arrayToBST(nums, 0, nums.length - 1)).toEqual(BST);
  });
});
