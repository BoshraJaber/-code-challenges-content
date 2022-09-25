"use strict";
const repeated_word = require("../index");
const {Node} = require("../hashtable");
const findTarget = require("../../../01-two-sum-BST/javascript/index");


let myStr = "ASAC is a department at LTUC. ASAC teaches programming in LTUC.";
let emptyStr = "";
describe("test 01", () => {
  it("return the first word to occur more than once in that provided string.", () => {
    expect(repeated_word(myStr)).toEqual("ASAC");
  });
  it("return error message if the string is empty.", () => {
    expect(repeated_word(emptyStr)).toEqual(
      "PLEASE ADD ANY WORDS TO FIND THE MOST REAPETED WORD"
    );
  });
});
let BST = new Node(7);
    BST.left = new Node(2);
    BST.left.right = new Node(5);
    BST.left.left = new Node(1);
    BST.right = new Node(9);
    BST.right.right = new Node(14);

describe("test 02", () => {
  it("toBeTruthy", () => {
    expect(findTarget(BST, 7)).toBeTruthy();
  });
  it("toBeFalsy", () => {
    expect(findTarget(BST, 4)).toBeFalsy();
  });
});
