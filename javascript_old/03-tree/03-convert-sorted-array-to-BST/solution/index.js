"use strict";
class Node {
  constructor(value, left = null, right = null) {
    this.value = value === undefined ? 0 : value;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

const arrayToBST = (nums, start = 0, end = nums.length - 1) => {
  let sortedArr = nums.sort()
  if (start <= end) {
    let mid = Math.floor((start + end) / 2);
    let root = new Node(sortedArr[mid]);
    root.left = arrayToBST(sortedArr, start, mid - 1);
    root.right = arrayToBST(sortedArr, mid + 1, end);
    return root;
  }
  return null;
};
// let nums = [-10, -3, 0, 5, 9];
// console.log(sortedArrayToBST(nums));

module.exports = {
  arrayToBST,
};
