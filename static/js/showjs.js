//HERE BELOW IS THE TOP ACTORS AND BLINKING MEDALS TASK
let episodeCount = document.querySelectorAll('.episodes').length;
console.log(episodeCount);

backgroundColor(episodeCount);


function backgroundColor(count) {
    let backGround = document.querySelector('.background')
    if (count % 2 == 0) {
        backGround.classList.add('background-blue');
    } else {
        backGround.classList.add('background-green');
    }

}

let coinsListener = document.querySelectorAll('.medal');

for (let coin of coinsListener) {
    coin.addEventListener('click', () => {
        coin.classList.add('blink_me');
        setTimeout(() => {
            coin.classList.remove('blink_me')
        }, 3000);
    })
}

//FROM HERE BELOW, THE IMDB STAR RATING TASK

let starListener = document.querySelectorAll('.star-listen');
for (let star of starListener) {
    star.addEventListener('mouseenter', (event) => {
            event.target.classList.add('target')
            let targetElement = event.target.parentNode.children;
            for (let star of targetElement){
                star.classList.add('fa-star-o');
            }
            for (let star of targetElement) {

                if (star.classList.value.includes('target') == true) {
                    star.classList.remove('fa-star-o');
                    star.classList.add('fa-star');
                    break
                } else {
                    star.classList.remove('fa-star-o');
                    star.classList.add('fa-star');
                }

            }

        }
    )
}
for (let star of starListener) {
    star.addEventListener('mouseleave', (event) => {
        let targetElement = event.target.parentNode.children;
        let rating = parseFloat(event.target.parentNode.parentNode.querySelector('.rating').innerHTML);

        rating = Math.round(rating);
        for (let star of targetElement) {
            star.classList.add('fa-star-o');
        }
        event.target.classList.remove('target');
        let i;
        for (i = 0; i < rating - 1; i++) {
            targetElement[i].classList.remove('fa-star-o');
            targetElement[i].classList.add('fa-star');

        }

    })
}
//FROM HERE BELOW IS THE IMDB CARD TASK
let yearCards = document.querySelectorAll('.year-cards');
let avgRating = 0;
let yearCount = 0;
for (let card of yearCards) {
    card.addEventListener('click', (event) => {
        //console.log(event.target.parentNode.childNodes)
        card.classList.add('clicked-card');
        if (event.target.classList.value.includes('year-cards') != true) {
            avgRating += parseFloat(event.target.parentNode.querySelector('#rating').innerHTML);
            yearCount += 1;
        } else {
            avgRating += parseFloat(event.target.querySelector('#rating').innerHTML);
            yearCount += 1;
        }
        let sumRating = document.querySelector('#avg')
        sumRating.innerText = Math.round(avgRating) / yearCount;
    })
}

