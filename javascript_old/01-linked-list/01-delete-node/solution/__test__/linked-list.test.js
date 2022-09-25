"use strict";

const LinkedList = require("../linked-list/linked-list");
const Node = require("../linked-list/node");
const deleteNode = require("../lib/delete-node");
const findMiddle = require("../../../02-find-middle-node/javascript/find-middle");
const removeNthFromEnd = require("../../../03-remove-nth-node/javascript/remove-nth-node");

let ll = new LinkedList();
let node1 = new Node(15);
let node2 = new Node(2);
let node3 = new Node(21);
let node4 = new Node(175);

node1.next = node2;
node2.next = node3;
node3.next = node4;
ll.append(node1);

describe("test 01 ", () => {
  it("deleteNode function should delete node", () => {
    deleteNode(node2);
    expect(ll.toString()).toEqual("15 -> 21 -> 175 -> null");
  });
});
describe("test 02 ", () => {
  test("findMiddle function should return the middle node of the linked list that have odd length", () => {
    let ll2 = new LinkedList();
    let node55 = new Node(175);
    let node11 = new Node(15);
    let node22 = new Node(2);
    let node33 = new Node(21);
    let node44 = new Node(175);

    node55.next = node11;
    node11.next = node22;
    node22.next = node33;
    node33.next = node44;
    ll2.append(node55);
    expect(findMiddle(node55).val).toEqual(2);
  });
  test("findMiddle function should return the middle node of the linked list that have even length", () => {
    let ll = new LinkedList();
    let node1 = new Node(15);
    let node2 = new Node(2);
    let node3 = new Node(21);
    let node4 = new Node(175);

    node1.next = node2;
    node2.next = node3;
    node3.next = node4;
    ll.append(node1);
    expect(findMiddle(node1).val).toEqual(21);
  });
  test("findMiddle function should return the head if the linked list have just one node", () => {
    let ll2 = new LinkedList();
    let node11 = new Node(15);
    ll2.append(node11);
    expect(findMiddle(node11).val).toEqual(15);
  });
});
describe("test 03 ", () => {
  test("removeNthFromEnd function should delete the nth node from the end of the linked list", () => {
    let ll2 = new LinkedList();
    node1.next = node2;
    node2.next = node3;
    node3.next = node4;
    ll2.append(node1);
    console.log(ll2.toString());
    removeNthFromEnd(node1, 0);
    expect(ll2.toString()).toEqual("15 -> 21 -> 21 -> null");
  });
  test("removeNthFromEnd function should delete the nth node from the end of the linked list", () => {
    let ll2 = new LinkedList();
    node1.next = node2;
    node2.next = node3;
    node3.next = node4;
    ll2.append(node1);
    removeNthFromEnd(node1, 2);
    expect(ll2.toString()).toEqual("15 -> 21 -> 175 -> null");
  });
  test("removeNthFromEnd function should return the the Linked list without deleting anything if n greater than the length of the linked-list", () => {
    let ll2 = new LinkedList();
    node1.next = node2;
    node2.next = node3;
    node3.next = node4;
    ll2.append(node1);
    removeNthFromEnd(node1, 10);
    expect(ll2.toString()).toEqual("15 -> 21 -> 21 -> 175 -> null");
  });
  test("removeNthFromEnd function should return the null if  the linked-list just have the head", () => {
    let ll2 = new LinkedList();
    let node11 = new Node(15);
    ll2.append(node11);

    expect(removeNthFromEnd(node11, 0)).toEqual(null);
  });
  test("removeNthFromEnd function should return the null if n less than 0", () => {
    let ll2 = new LinkedList();
    let node11 = new Node(15);
    ll2.append(node11);
    expect(removeNthFromEnd(node11, -2)).toEqual(null);
  });
});
