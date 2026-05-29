const prompt = require("prompt-sync")();

let questionA = [

    "expand energy, enjoy groups",
    "interpret literally",
    "logical, thinking, questioning",
    "organized, orderly",
    "more outgoing, think out loud",

    "practical, realistic",
    "candid, straight forward, frank",
    "plan schedule",
    "seek many task",
    "standard, usual, conventional",
    
    "firm, tend to criticize",
    "regulated, structured",
    "external, communicative",
    "focus on here-and-now",
    "tough-minded, just",

    "preparation, plan ahead",
    "active, initiate",
    "facts, things, what is",
    "matter of fact",
    "control, govern"
  ];

let questionB = [

    "conserve energy, enjoy one-on-one",
    "look for meaning and posibilities",
    "empathetic, feeling, accommodating",
    "flexible, adaptable",
    "more reserved, think to yourself",

    "imaginative, innovative",
    "tactful, kind, encouraging",
    "unplanned, spontaneous",
    "seek private, solitary activities",
    "different, novel, unique",

    "gentle, tend to appriciate",
    "easy-going, live and let live",
    "internal, retcent",
    "look to the future, big picture",
    "tender-hearted, merciful",

    "go with the flow",
    "reflective, deliberate",
    "ideas, dreams, what could be",
    "sensitive, people-oriented",
    "latitude, freedom",
 ];

let e = 0;
let i = 0;

let s = 0;
let n = 0;

let t = 0;
let f = 0;

let j = 0;
let p = 0;

let responses = [];

let name = prompt("what is your name ?");

for(let count = 0; count < 20; count++) {
    console.log("\nQuestion " + (count + 1));
    console.log("A " + questionA[count]);
    console.log("B " + questionB[count]);

    let answer = prompt("Chose A or B: ");
    answer = answer.toUpperCase();

    while (answer !== "A" && answer !== "B"){

        console.log("Expected A or B as Response");
        console.log("I know this is an error, please retry again");

        answer = prompt("Choose A or B");
        answer = answer.toUpperCase();
   }
    responses.push(answer);

    if(count === 0 || count === 4 || count === 8 || count === 12 || count === 16){
        if (answer === "A") {
            e = e + 1; 
        }
        else {
        i = i + 1;
        }
    }
    else if (count === 1 || count === 5 || count === 9 || count === 13 || count === 17){
        if (answer === "A"){
            s = s + 1;
        }
        else {
            n = n + 1;    
        }
    }
    else if (count === 2 || count === 6 || count === 10 || count === 14 || count === 18) {
        if (answer === "A"){
            t = t + 1;    
       } 
       else {
            f = f + 1;
       }
    }
    else if (count === 3 || count === 7 || count === 11 || count === 15 || count === 19){
        if (answer === "A"){
            j = j + 1;    
       } 
       else {
            p = p + 1;
       }
    }    
}

let personality = "";

if (e > i){
    personality = personality + "E";
}
else{
    personality = personality + "I";
}

if (s > n){
    personality = personality + "S";
}
else {
    personality = personality + "N";
}

if (t > f) {
    personality = personality + "T";
}
else {
    personality = personality + "F";
}

if (j < p) {
    personality = personality + "J";
}
else {
    personality = personality + "P";
}

console.log("\nYour Responses");
for(let answer of responses){
    console.log(answer);
}

console.log("\nHello " + name);
console.log("Your personality Type is: " + personality);
console.log("\nPersonality meaning ");

if (personality === "INFP"){
    console.log("INFP people are caring and imaginative.");
}

else if (personality === "INTJ") {
    console.log("INTJ people are strategic and independent.");
}

else if (personality === "ENTJ"){
    console.log("ENTJ People are confident leaders.");
}

else if (personality === "ESFP"){
    console.log("ESFP People are energetic and fun.");
}

else{
    console.log("You have a unique personality.")
}


