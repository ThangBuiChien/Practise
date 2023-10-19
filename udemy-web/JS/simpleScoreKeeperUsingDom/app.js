

const point1 = document.querySelector("#p1Points");
const point2 = document.querySelector("#p2Points");
const btnPlayer1 = document.querySelector("#btnPlayer1");
const btnPlayer2 = document.querySelector("#btnPlayer2");
const btnReset1 = document.querySelector("#btnReset");
const maxPoint = document.querySelector("#maxPoint");

let p1Score = 0;
let p2Score = 0;

btnPlayer1.addEventListener("click", function () {
    if (p1Score == maxPoint.value) {
        point1.style.color = "red";
    }
    else {
        p1Score += 1;
        point1.textContent = p1Score;
    }

});

btnPlayer2.addEventListener("click", () => {
    p2Score += 1;
    point2.innerText = p2Score;


});

btnReset1.addEventListener("click", () => {

    p1Score = 0;
    p2Score = 0;
    point1.textContent = p1Score;
    point2.textContent = p1Score;

})



