"use strict";
const isSameTree = (p, q) => {
  if (!p || !q) return false;
  const queue = [p, q];
  while (queue.length > 0) {
    const [first, second] = [queue.shift(), queue.shift()];
    if (!first && !second) continue;
    if (!first || !second || first.value !== second.value) return false;
    queue.push(first.left, second.left, first.right, second.right);
  }
  return true;
};

module.exports = {
  isSameTree,
};
