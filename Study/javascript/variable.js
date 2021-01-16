'use strict';

let globalName= 'global';

{
    let name = 'mark';
    console.log(name);

    name = 'hello';
    console.log(name);
}

console.log(globalName);

// 3. Constants

const max = 10;


// 4. variable types
// first class function

const count = 17;
const size = 19.1;
console.log(`value : ${count}, type: ${typeof count}`);
console.log(`value : ${size}, type: ${typeof size}`);

// Symbol

const symbol1 = Symbol('id');
const symbol2 = Symbol('id');

const gSymbol1 = Symbol.for('do');
const gSymbol2 = Symbol.for('do');

console.log(gSymbol1 === gSymbol2);
console.log(gSymbol1.description);

// Dynamic typing **

