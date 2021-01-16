"use strict";

// 1. function declaration
// function name(param1, param2) {body ... return;}
// one function === one thing
//naming : doSomthing, command, verb
// ** function is object in JS**

function printHello() {
    console.log("Hello");
}

printHello();

function changeName(obj) {
    obj.name = "Mark";
}

const Person = { name: "Chang" };
changeName(Person);

console.log(Person.name);

// default params

function showMsg(message, from = "unknown") {
    console.log(`${message} from ${from}`);
}

showMsg("Hey", "Mark");

//Rest params

function printAll(...args) {
    //for (const arg of args)
    args.forEach((arg) => console.log(arg));
}

printAll("cung", "cungs1", "cusnt2");

// Local Scope
let globalMsg = "global";

function printMsg() {
    let msg = "hello";
    console.log(msg);
    console.log(globalMsg);
}

printMsg();

// First-class function
// function are treated like any other variables
// can be assigned as a value to variable
// can be passed as an argument to other functions
// can be returned by another function


// function Expression
// a function declaration can be called earlier than it is defined 
// a function expression is created when the execution reaches it.

const print = function() { //anonymous function
    console.log('print');
}

print();

// ** CALLBACK function using function expression

const printYes = function () {
    console.log('Yes');
}

const printNo = function() {
    console.log('NO');
}

function randomQuiz(answer, printYes, printNo) {
    if(answer === "ANS") {
        printYes();
        return;
    }

    printNo();
}

randomQuiz("ANs", printYes, printNo);

// Arrow function
// always anonymous

const simplePrint = () => {
    console.log("simple print");
    console.log("simpole print2");
};

simplePrint();

//IIFE
// Immediately Invoked Function Expressed

(function hello() {
    console.log("IIFE");
})();