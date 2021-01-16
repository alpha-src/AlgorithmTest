"use strict";

//javascript classes
/*
    -introduced in ES6
    -prototype-based inheritance
*/

//1. class declaration
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    speak() {
        console.log(`${this.name} hi`);
    }
}

const mark = new Person("sihyun", 23);
console.log(mark);

// 2. getter, setter

class User {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    get age() {
        return this._age;
    }

    set age(value) {
        if (value < 0) throw Error("age can't be negative");
        this._age = value;
    }
}

// 3. fields (public, private)

class Experiment {
    constructor() {
        this.publicField = 2;
    }
}

const experiment = new Experiment();
console.log(experiment.publicField);

// 4. instanceOf
console.log(experiment instanceof Experiment);
